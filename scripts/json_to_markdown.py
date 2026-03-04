#!/usr/bin/env python3
"""
Convert article JSON (ProseMirror or HTML) to Hugo Markdown under content/articles/<slug>.md.
Internal links to /pub/{slug} are rewritten to /articles/{slug}. Repeatable (overwrites).
"""
import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from markdownify import markdownify as md

# Import from lib for link rewriting
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lib.text_utils import extract_slug_from_href

OECS_PUB_PATTERN = re.compile(r"https?://(?:www\.)?oecs\.mit\.edu/pub/([^/?#]+)")


def resolve_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_known_slugs(root: Path) -> Set[str]:
    slugs: set = set()
    index_path = root / "articles" / "index.json"
    if index_path.exists():
        data = json.loads(index_path.read_text(encoding="utf-8"))
        for a in data.get("articles") or []:
            s = (a.get("slug") or "").strip()
            if s:
                slugs.add(s)
    for p in (root / "articles").glob("*.json"):
        if p.name == "index.json":
            continue
        slugs.add(p.stem)
    return slugs


def rewrite_internal_url(href: Optional[str], known_slugs: Set[str]) -> str:
    if not href:
        return ""
    slug = extract_slug_from_href(href)
    if slug and slug in known_slugs:
        return f"/articles/{slug}"
    # Full OECS URL
    m = OECS_PUB_PATTERN.match(href.strip())
    if m and m.group(1) in known_slugs:
        return f"/articles/{m.group(1)}"
    return href


def get_text_marks(node: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for mark in node.get("marks") or []:
        t = mark.get("type")
        if t == "link":
            out["link"] = (mark.get("attrs") or {}).get("href")
        elif t == "em":
            out["em"] = True
        elif t == "strong":
            out["strong"] = True
    return out


def render_inline(node: Dict[str, Any], known_slugs: Set[str], buf: List[str]) -> None:
    t = node.get("type")
    if t == "text":
        text = node.get("text", "")
        marks = get_text_marks(node)
        href = marks.get("link")
        if href:
            url = rewrite_internal_url(href, known_slugs)
            buf.append(f"[{text.strip()}]({url})")
        elif marks.get("strong") and marks.get("em"):
            buf.append(f"***{text}***")
        elif marks.get("strong"):
            buf.append(f"**{text}**")
        elif marks.get("em"):
            buf.append(f"*{text}*")
        else:
            buf.append(text)
    elif t == "hard_break":
        buf.append("\n")
    elif t == "citation":
        label = (node.get("attrs") or {}).get("customLabel") or ""
        buf.append(label)  # no extra parens; prose already has ( ) around citation
    elif t and "content" in node:
        for c in node.get("content") or []:
            render_inline(c, known_slugs, buf)


def block_to_md(node: Dict[str, Any], known_slugs: Set[str], indent: str = "") -> str:
    t = node.get("type")
    content = node.get("content") or []

    if t == "paragraph":
        buf: List[str] = []
        for c in content:
            render_inline(c, known_slugs, buf)
        return indent + "".join(buf).strip()

    if t == "heading":
        level = (node.get("attrs") or {}).get("level", 1)
        buf = []
        for c in content:
            render_inline(c, known_slugs, buf)
        return indent + "#" * level + " " + "".join(buf).strip()

    if t == "blockquote":
        lines = []
        for c in content:
            line = block_to_md(c, known_slugs)
            if line:
                lines.append("> " + line)
        return "\n".join(lines)

    if t == "bullet_list":
        lines = []
        for c in content:
            if c.get("type") == "list_item":
                lines.append(block_to_md_list_item(c, known_slugs, "-"))
        return "\n".join(lines)

    if t == "ordered_list":
        lines = []
        for i, c in enumerate(content, 1):
            if c.get("type") == "list_item":
                lines.append(block_to_md_list_item(c, known_slugs, f"{i}."))
        return "\n".join(lines)

    if t == "list_item":
        return block_to_md_list_item(node, known_slugs, "-")

    if t == "image":
        attrs = node.get("attrs") or {}
        src = attrs.get("src") or ""
        alt = attrs.get("alt") or ""
        return f"![{alt}]({src})"

    # Default: recurse
    parts = []
    for c in content:
        if isinstance(c, dict):
            parts.append(block_to_md(c, known_slugs, indent))
    return "\n".join(p for p in parts if p)


def block_to_md_list_item(node: Dict[str, Any], known_slugs: Set[str], prefix: str) -> str:
    content = node.get("content") or []
    parts = []
    for c in content:
        if isinstance(c, dict):
            part = block_to_md(c, known_slugs)
            if part:
                parts.append(part)
    inner = "\n".join(parts)
    if "\n" in inner:
        lines = inner.split("\n")
        return prefix + " " + lines[0] + "\n" + "\n".join("  " + ln for ln in lines[1:])
    return prefix + " " + inner


def _collect_citations(node: Any, out: List[Tuple[str, str]]) -> None:
    """Recursively collect (customLabel, unstructuredValue) from citation nodes, order of first appearance."""
    if isinstance(node, dict):
        if node.get("type") == "citation":
            attrs = node.get("attrs") or {}
            uv = (attrs.get("unstructuredValue") or "").strip()
            label = (attrs.get("customLabel") or "").strip()
            if uv:
                out.append((label, uv))
        for c in node.get("content") or []:
            _collect_citations(c, out)
    elif isinstance(node, list):
        for c in node:
            _collect_citations(c, out)


def collect_citation_references(doc: Dict[str, Any]) -> List[str]:
    """Return list of unique unstructuredValue HTML strings in doc order (deduped by value)."""
    raw: List[Tuple[str, str]] = []
    _collect_citations(doc, raw)
    seen: set = set()
    unique: List[str] = []
    for _label, uv in raw:
        if uv and uv not in seen:
            seen.add(uv)
            unique.append(uv)
    return unique


def doc_to_markdown(doc: Dict[str, Any], known_slugs: Set[str]) -> str:
    blocks = []
    for node in doc.get("content") or []:
        if isinstance(node, dict):
            line = block_to_md(node, known_slugs)
            if line:
                blocks.append(line)
    body = "\n\n".join(blocks)
    # Remove stray space after markdown link in "[see ...]" so "[see [Ref](url) ]" and "[see [A](url) ; [B](url)]" render without extra space
    body = re.sub(r"\]\(([^)]+)\)\s+(\])", r"](\1)\2", body)
    body = re.sub(r"\]\(([^)]+)\)\s+(;)", r"](\1)\2", body)
    # Append References section from citation unstructuredValue (like OECS expandable section)
    refs_html = collect_citation_references(doc)
    if refs_html:
        refs_md = []
        for i, html in enumerate(refs_html, 1):
            refs_md.append(html_to_markdown(html))
        body = body + "\n\n# References\n\n" + "\n\n".join(refs_md)
    return body


def html_to_markdown(html: str) -> str:
    return md(html or "", heading_style="ATX", strip=["script", "style"]).strip()


def _attribution_name(att: Dict[str, Any]) -> Optional[str]:
    name = att.get("name") or (att.get("user") or {}).get("fullName")
    return (name or "").strip() or None


def extract_authors(raw_pub: Optional[Dict]) -> List[str]:
    authors = []
    for att in (raw_pub or {}).get("attributions") or []:
        if att.get("isAuthor"):
            name = _attribution_name(att)
            if name:
                authors.append(name)
    return authors


def extract_section_editors(raw_pub: Optional[Dict]) -> List[str]:
    out = []
    for att in (raw_pub or {}).get("attributions") or []:
        roles = att.get("roles") or []
        if any(r and "Section Editor" in str(r) for r in roles):
            name = _attribution_name(att)
            if name and name not in out:
                out.append(name)
    return out


def extract_editors_in_chief(raw_pub: Optional[Dict]) -> List[str]:
    out = []
    for att in (raw_pub or {}).get("attributions") or []:
        roles = att.get("roles") or []
        if any(r and "Editor-in-Chief" in str(r) for r in roles):
            name = _attribution_name(att)
            if name and name not in out:
                out.append(name)
    return out


def iso_date_from(created: Optional[str], published: Optional[str]) -> str:
    s = published or created or ""
    if not s:
        return ""
    # Keep only date part if ISO datetime
    if "T" in s:
        s = s.split("T")[0]
    return s


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert article JSON to Hugo Markdown.")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of articles.")
    parser.add_argument("--articles-json", action="store_true", help="Also write data/articles.json.")
    args = parser.parse_args()

    root = resolve_root()
    articles_dir = root / "articles"
    content_articles = root / "content" / "articles"
    content_articles.mkdir(parents=True, exist_ok=True)
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)

    known_slugs = load_known_slugs(root)
    paths = sorted(p for p in articles_dir.glob("*.json") if p.name != "index.json")
    if args.limit:
        paths = paths[: args.limit]

    index_data = []
    for path in paths:
        slug = path.stem
        data = json.loads(path.read_text(encoding="utf-8"))
        title = (data.get("title") or slug).strip()
        raw_pub = data.get("raw_pub") or {}
        raw_text = data.get("raw_text")
        html = data.get("html") or ""

        body = ""
        if raw_text and isinstance(raw_text, dict) and raw_text.get("type") == "doc":
            body = doc_to_markdown(raw_text, known_slugs)
        elif html:
            body = html_to_markdown(html)
        if not body.strip():
            body = "(No content.)"

        created = raw_pub.get("createdAt")
        published = data.get("published_at") or raw_pub.get("customPublishedAt")
        date = iso_date_from(created, published)
        doi = raw_pub.get("doi") or ""
        authors = extract_authors(raw_pub)
        section_editors = extract_section_editors(raw_pub)
        editors_in_chief = extract_editors_in_chief(raw_pub)
        subtitle = (raw_pub.get("description") or "").strip() or None

        fm: Dict[str, Any] = {"title": title, "slug": slug}
        if date:
            fm["date"] = date
        if doi:
            fm["doi"] = doi
        if authors:
            fm["authors"] = authors
        if subtitle:
            fm["subtitle"] = subtitle
        if section_editors:
            fm["section_editors"] = section_editors
        if editors_in_chief:
            fm["editors_in_chief"] = editors_in_chief

        # YAML front matter (simple dump)
        import yaml
        try:
            fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        except Exception:
            fm_str = yaml.dump(fm, allow_unicode=True, sort_keys=False)
        md_content = "---\n" + fm_str.strip() + "\n---\n\n" + body

        out_path = content_articles / f"{slug}.md"
        out_path.write_text(md_content, encoding="utf-8")

        if args.articles_json:
            index_data.append({"slug": slug, "title": title, "date": date or ""})

    if args.articles_json and index_data:
        (data_dir / "articles.json").write_text(
            json.dumps({"articles": index_data}, indent=2), encoding="utf-8"
        )
        print(f"Wrote data/articles.json ({len(index_data)} entries)")

    print(f"Wrote {len(paths)} articles to content/articles/")


if __name__ == "__main__":
    main()
