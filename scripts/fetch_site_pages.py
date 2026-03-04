#!/usr/bin/env python3
"""
Fetch top-level OECS pages from https://oecs.mit.edu, extract thematic
collections and article lists, and write iframe URL + thematic_collections data.
Repeatable: overwrites data/iframe_semantic_network.json and data/thematic_collections.json.
"""
import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://oecs.mit.edu"
TIMEOUT = 30
THEMES_PATH = "/themes"
ARTICLES_LIST_PATH = "/open-encyclopedia-of-cognitive-science"


def resolve_root() -> Path:
    return Path(__file__).resolve().parents[1]


def fetch_html(session: requests.Session, path: str) -> Optional[str]:
    url = BASE_URL + path if path.startswith("/") else BASE_URL + "/" + path
    try:
        r = session.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        print(f"Warning: failed to fetch {url}: {e}")
        return None


def extract_iframe_src(html: str) -> Optional[str]:
    if not html:
        return None
    soup = BeautifulSoup(html, "lxml")
    iframe = soup.find("iframe", src=True)
    if iframe:
        return iframe.get("src") or None
    return None


def extract_theme_links(html: str) -> List[Tuple[str, str]]:
    """Return list of (slug, title) for thematic collection links on /themes page."""
    if not html:
        return []
    soup = BeautifulSoup(html, "lxml")
    links: List[Tuple[str, str]] = []
    for a in soup.find_all("a", href=True):
        href = a.get("href", "").strip()
        if not href.startswith("/") or href == "/":
            continue
        # Theme URLs are like /language, /ai-and-cognitive-modeling (no /pub/, not /legal, etc.)
        if href.startswith("/pub/") or href.startswith("/legal") or href.startswith("/rss"):
            continue
        if "/" in href[1:]:
            continue
        slug = href.lstrip("/")
        title = (a.get_text() or "").strip()
        if slug and title and slug not in ("themes", "editors", "about", "faq", "search", "open-encyclopedia-of-cognitive-science"):
            links.append((slug, title))
    # Dedupe by slug
    seen: set = set()
    out: List[Tuple[str, str]] = []
    for s, t in links:
        if s not in seen:
            seen.add(s)
            out.append((s, t))
    return out


def extract_article_titles_from_theme_page(html: str) -> List[str]:
    """
    Extract article titles from a thematic collection page.
    Page structure: h2 theme title, then h3 for each article with optional "also, X" and "by Author".
    We take the h3 text and strip "also, ..." and "by ..." to get the canonical title.
    """
    if not html:
        return []
    soup = BeautifulSoup(html, "lxml")
    titles: List[str] = []
    for h3 in soup.find_all(["h3"]):
        text = (h3.get_text() or "").strip()
        if not text:
            continue
        # Remove "also, Something" and "by Author Name" (often on following nodes or same block)
        # Try to get just the main title: first line or part before "also," or "by"
        lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
        main = lines[0] if lines else text
        if main.lower().startswith("by "):
            continue
        if " also, " in main:
            main = main.split(" also, ")[0].strip()
        if " by " in main and main.count(" by ") == 1:
            # "Title by Author" possible for short titles
            parts = main.rsplit(" by ", 1)
            if len(parts) == 2 and len(parts[1]) > 3 and not parts[1].startswith("("):
                main = parts[0].strip()
        titles.append(main)
    return titles


def load_title_to_slug(root: Path) -> Dict[str, str]:
    """Build title -> slug from metadata/current_articles.csv (and optionally articles/index.json)."""
    title_to_slug: Dict[str, str] = {}
    csv_path = root / "metadata" / "current_articles.csv"
    if csv_path.exists():
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = (row.get("title") or "").strip()
                slug = (row.get("slug") or "").strip()
                if title and slug and title not in title_to_slug:
                    title_to_slug[title] = slug
    index_path = root / "articles" / "index.json"
    if index_path.exists():
        data = json.loads(index_path.read_text(encoding="utf-8"))
        for art in data.get("articles") or []:
            title = (art.get("title") or "").strip()
            slug = (art.get("slug") or "").strip()
            if title and slug and title not in title_to_slug:
                title_to_slug[title] = slug
    return title_to_slug


def normalize_title_for_match(t: str) -> str:
    """Normalize title for matching (strip, collapse spaces)."""
    return re.sub(r"\s+", " ", (t or "").strip())


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch OECS site pages and extract iframe + thematic collections.")
    parser.add_argument("--output-html", action="store_true", help="Save fetched HTML under scripts/output/site_pages/")
    args = parser.parse_args()

    root = resolve_root()
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)
    metadata_dir = root / "metadata"
    metadata_dir.mkdir(exist_ok=True)
    if args.output_html:
        out_html_dir = root / "scripts" / "output" / "site_pages"
        out_html_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "OECS-static-fetcher/1.0"})

    # 1) Home – extract iframe
    home_html = fetch_html(session, "/")
    iframe_url: Optional[str] = None
    if home_html:
        iframe_url = extract_iframe_src(home_html)
        if args.output_html:
            (out_html_dir / "home.html").write_text(home_html, encoding="utf-8")
    iframe_data = {"url": iframe_url or ""}
    (data_dir / "iframe_semantic_network.json").write_text(
        json.dumps(iframe_data, indent=2), encoding="utf-8"
    )
    print(f"Iframe URL written to data/iframe_semantic_network.json: {iframe_url or '(empty)'}")

    # 2) Themes index – list of theme slugs/titles
    themes_html = fetch_html(session, THEMES_PATH)
    theme_links = extract_theme_links(themes_html or "")
    if args.output_html and themes_html:
        (out_html_dir / "themes.html").write_text(themes_html, encoding="utf-8")

    # 3) Title -> slug for resolving article titles
    title_to_slug = load_title_to_slug(root)

    # 4) Each theme page – article titles -> slugs
    thematic_collections: List[Dict[str, Any]] = []
    for slug, title in theme_links:
        path = "/" + slug
        html = fetch_html(session, path)
        if args.output_html and html:
            safe = slug.replace("/", "_")
            (out_html_dir / f"theme_{safe}.html").write_text(html, encoding="utf-8")
        raw_titles = extract_article_titles_from_theme_page(html or "")
        article_slugs_set: set = set()
        for t in raw_titles:
            nt = normalize_title_for_match(t)
            if nt in title_to_slug:
                article_slugs_set.add(title_to_slug[nt])
            else:
                for k, s in title_to_slug.items():
                    if normalize_title_for_match(k) == nt:
                        article_slugs_set.add(s)
                        break
        thematic_collections.append({
            "slug": slug,
            "title": title,
            "article_slugs": sorted(article_slugs_set),
        })
        print(f"Theme {slug}: {len(article_slugs_set)} articles")

    (data_dir / "thematic_collections.json").write_text(
        json.dumps(thematic_collections, indent=2), encoding="utf-8"
    )
    (metadata_dir / "thematic_collections.json").write_text(
        json.dumps(thematic_collections, indent=2), encoding="utf-8"
    )
    print(f"Wrote data/thematic_collections.json and metadata/thematic_collections.json ({len(thematic_collections)} themes)")

    # Write Hugo content for each thematic collection (except search)
    content_tc = root / "content" / "thematic-collections"
    content_tc.mkdir(parents=True, exist_ok=True)
    for tc in thematic_collections:
        if tc.get("slug") == "search":
            continue
        slug = tc["slug"]
        title = tc["title"]
        slugs_list = tc.get("article_slugs") or []
        fm = {"title": title, "article_slugs": slugs_list}
        import yaml
        fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        md_path = content_tc / f"{slug}.md"
        md_path.write_text("---\n" + fm_str.strip() + "\n---\n\n", encoding="utf-8")
    print(f"Wrote {len([t for t in thematic_collections if t.get('slug') != 'search'])} thematic collection pages to content/thematic-collections/")

    # 5) Fetch editors, about, faq; save HTML (if --output-html) and convert to Markdown for Hugo
    try:
        from markdownify import markdownify as md
    except ImportError:
        md = None
    for name, path in [("editors", "/editors"), ("about", "/about"), ("faq", "/faq")]:
        html = fetch_html(session, path)
        if args.output_html and html:
            (out_html_dir / f"{name}.html").write_text(html, encoding="utf-8")
        if html and md:
            # Extract main content: try multiple selectors used by PubPub/OECS
            soup = BeautifulSoup(html, "lxml")
            for tag in soup.find_all(["header", "nav"]):
                tag.decompose()
            main = (
                soup.find("main")
                or soup.find("article")
                or soup.find(attrs={"role": "main"})
                or soup.find("div", class_=re.compile(r"content|main|body|pub", re.I))
                or soup.find("div", id=re.compile(r"content|main|body", re.I))
            )
            if main:
                body_html = str(main)
            else:
                body_html = str(soup.find("body") or soup)
            markdown_body = md(body_html, heading_style="ATX", strip=["script", "style", "nav"]).strip()
            content_dir = root / "content" / name
            content_dir.mkdir(parents=True, exist_ok=True)
            titles = {"editors": "Editors", "about": "About", "faq": "FAQ"}
            fm = f"---\ntitle: \"{titles[name]}\"\n---\n\n"
            (content_dir / "_index.md").write_text(fm + markdown_body, encoding="utf-8")
            print(f"Wrote content/{name}/_index.md")
        elif html and not md:
            print(f"Tip: install markdownify (pip install markdownify) to auto-update content/{name}/_index.md")


if __name__ == "__main__":
    main()
