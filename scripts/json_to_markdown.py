#!/usr/bin/env python3
"""
Convert article JSON (ProseMirror or HTML) to Hugo Markdown under content/articles/<slug>.md.
Internal links to /pub/{slug} are rewritten to /articles/{slug}. Repeatable (overwrites).
Downloads figure images from article JSON into static/images/articles/<slug>/ and emits
figure captions and figure references (e.g. "Figure 1", "Figure 2A").
"""
import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse

import requests
from markdownify import markdownify as md

# Import from lib for link rewriting
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lib.text_utils import extract_slug_from_href

FIGURE_DOWNLOAD_TIMEOUT = 60

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


def _collect_image_blocks(node: Any, out: List[Dict[str, Any]]) -> None:
    """Append image block nodes (with attrs.id, attrs.url, attrs.caption) in doc order."""
    if isinstance(node, dict):
        if node.get("type") == "image":
            attrs = node.get("attrs") or {}
            if attrs.get("id") and (attrs.get("url") or attrs.get("src")):
                out.append(node)
        for c in node.get("content") or []:
            _collect_image_blocks(c, out)
    elif isinstance(node, list):
        for c in node:
            _collect_image_blocks(c, out)


def _count_reference_targets(node: Any, counts: Dict[str, int]) -> None:
    """Increment counts[targetId] for each reference node with attrs.targetId."""
    if isinstance(node, dict):
        if node.get("type") == "reference":
            tid = (node.get("attrs") or {}).get("targetId")
            if tid:
                counts[tid] = counts.get(tid, 0) + 1
        for c in node.get("content") or []:
            _count_reference_targets(c, counts)
    elif isinstance(node, list):
        for c in node:
            _count_reference_targets(c, counts)


def _extension_from_url(url: str) -> str:
    path = urlparse(url).path.lower()
    if ".png" in path:
        return "png"
    if ".jpg" in path or ".jpeg" in path:
        return "jpg"
    if ".gif" in path:
        return "gif"
    if ".webp" in path:
        return "webp"
    return "png"


def _download_figure(session: requests.Session, url: str, dest: Path) -> bool:
    """Download url to dest; try resize-v3 fallback on 404. Return True on success."""
    try:
        r = session.get(url, timeout=FIGURE_DOWNLOAD_TIMEOUT, stream=True)
        if r.status_code == 404 and "assets.pubpub.org" in url:
            # Resize-v3 fallback (same logic as download_oecs_assets)
            try:
                from download_oecs_assets import build_resize_v3_url
                fallback = build_resize_v3_url(url)
                if fallback:
                    r = session.get(fallback, timeout=FIGURE_DOWNLOAD_TIMEOUT, stream=True)
            except ImportError:
                pass
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True
    except (requests.RequestException, OSError) as e:
        print(f"Warning: failed to download figure {url}: {e}")
        return False


def download_article_figures(
    root: Path,
    slug: str,
    image_blocks: List[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    """
    Download figure images for an article. Returns figure_info: id -> {num, path, caption_md}.
    path is absolute from site root for markdown (e.g. /images/articles/xdqgwrkq/figure_1.png).
    """
    figure_info: Dict[str, Dict[str, Any]] = {}
    if not image_blocks:
        return figure_info
    static_base = root / "static" / "images" / "articles" / slug
    static_base.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.setdefault("User-Agent", "OECS-Static-Article-Figures/1.0")
    for i, block in enumerate(image_blocks, 1):
        attrs = block.get("attrs") or {}
        node_id = attrs.get("id")
        url = attrs.get("url") or attrs.get("src") or ""
        caption_html = (attrs.get("caption") or "").strip()
        if not node_id or not url:
            continue
        ext = _extension_from_url(url)
        filename = f"figure_{i}.{ext}"
        dest = static_base / filename
        if _download_figure(session, url, dest):
            # Path without leading slash so Hugo relURL can prepend baseURL path (e.g. when baseURL has subpath)
            rel_path = f"images/articles/{slug}/{filename}"
            caption_md = html_to_markdown(caption_html) if caption_html else ""
            figure_info[node_id] = {"num": i, "path": rel_path, "caption_md": caption_md}
    return figure_info


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


def render_inline(
    node: Dict[str, Any],
    known_slugs: Set[str],
    buf: List[str],
    context: Optional[Dict[str, Any]] = None,
) -> None:
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
    elif t == "reference" and context:
        # Figure reference: "Figure N" (single or two refs) or "Figure NA", "Figure NB", ...
        attrs = node.get("attrs") or {}
        target_id = attrs.get("targetId")
        figure_info = context.get("figure_info") or {}
        ref_counts = context.get("ref_counts") or {}
        ref_index = context.get("ref_index")
        if target_id and ref_index is not None and target_id in figure_info:
            info = figure_info[target_id]
            num = info.get("num", 0)
            count = ref_counts.get(target_id, 0)
            idx = ref_index.setdefault(target_id, 0)
            if count <= 2:
                label = f"Figure {num}"
            else:
                label = f"Figure {num}{chr(ord('A') + idx)}"
            ref_index[target_id] = idx + 1
            buf.append(label)
    elif t and "content" in node:
        for c in node.get("content") or []:
            render_inline(c, known_slugs, buf, context)


def block_to_md(
    node: Dict[str, Any],
    known_slugs: Set[str],
    indent: str = "",
    context: Optional[Dict[str, Any]] = None,
) -> str:
    t = node.get("type")
    content = node.get("content") or []

    if t == "paragraph":
        buf: List[str] = []
        for c in content:
            render_inline(c, known_slugs, buf, context)
        return indent + "".join(buf).strip()

    if t == "heading":
        level = (node.get("attrs") or {}).get("level", 1)
        buf = []
        for c in content:
            render_inline(c, known_slugs, buf, context)
        return indent + "#" * level + " " + "".join(buf).strip()

    if t == "blockquote":
        lines = []
        for c in content:
            line = block_to_md(c, known_slugs, context=context)
            if line:
                lines.append("> " + line)
        return "\n".join(lines)

    if t == "bullet_list":
        lines = []
        for c in content:
            if c.get("type") == "list_item":
                lines.append(block_to_md_list_item(c, known_slugs, "-", context))
        return "\n".join(lines)

    if t == "ordered_list":
        lines = []
        for i, c in enumerate(content, 1):
            if c.get("type") == "list_item":
                lines.append(block_to_md_list_item(c, known_slugs, f"{i}.", context))
        return "\n".join(lines)

    if t == "list_item":
        return block_to_md_list_item(node, known_slugs, "-", context)

    if t == "image":
        attrs = node.get("attrs") or {}
        node_id = attrs.get("id")
        figure_info = (context or {}).get("figure_info") or {}
        if node_id and node_id in figure_info:
            info = figure_info[node_id]
            path = info.get("path") or ""
            num = info.get("num", 0)
            caption_md = (info.get("caption_md") or "").strip()
            alt = attrs.get("altText") or attrs.get("alt") or ""
            if caption_md:
                return f"![{alt}]({path})\n\n**Figure {num}.** {caption_md}"
            return f"![{alt}]({path})"
        # Legacy: no figure_info (e.g. re-run without download)
        src = attrs.get("url") or attrs.get("src") or ""
        alt = attrs.get("altText") or attrs.get("alt") or ""
        return f"![{alt}]({src})"

    # Default: recurse
    parts = []
    for c in content:
        if isinstance(c, dict):
            parts.append(block_to_md(c, known_slugs, indent, context))
    return "\n".join(p for p in parts if p)


def block_to_md_list_item(
    node: Dict[str, Any],
    known_slugs: Set[str],
    prefix: str,
    context: Optional[Dict[str, Any]] = None,
) -> str:
    content = node.get("content") or []
    parts = []
    for c in content:
        if isinstance(c, dict):
            part = block_to_md(c, known_slugs, context=context)
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


def doc_to_markdown(
    doc: Dict[str, Any],
    known_slugs: Set[str],
    figure_info: Optional[Dict[str, Dict[str, Any]]] = None,
    ref_counts: Optional[Dict[str, int]] = None,
) -> str:
    context = None
    if figure_info is not None and ref_counts is not None:
        context = {"figure_info": figure_info, "ref_counts": ref_counts, "ref_index": {}}
    blocks = []
    for node in doc.get("content") or []:
        if isinstance(node, dict):
            line = block_to_md(node, known_slugs, context=context)
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
        figure_info: Dict[str, Dict[str, Any]] = {}
        ref_counts: Dict[str, int] = {}
        if raw_text and isinstance(raw_text, dict) and raw_text.get("type") == "doc":
            image_blocks: List[Dict[str, Any]] = []
            _collect_image_blocks(raw_text, image_blocks)
            _count_reference_targets(raw_text, ref_counts)
            if image_blocks:
                figure_info = download_article_figures(root, slug, image_blocks)
            body = doc_to_markdown(raw_text, known_slugs, figure_info=figure_info, ref_counts=ref_counts)
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
