import argparse
import csv
import json
from pathlib import Path
from typing import Dict, List

from lib.text_utils import extract_links_from_doc, extract_links_from_html


def resolve_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_articles(articles_dir: Path) -> List[Dict[str, str]]:
    articles: List[Dict[str, str]] = []
    for path in articles_dir.glob("*.json"):
        if path.name == "index.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        data["__file"] = path.name
        articles.append(data)
    return articles


def write_current_articles_csv(output_path: Path, articles: List[Dict[str, str]]) -> None:
    fieldnames = ["id", "slug", "title", "url", "published_at", "file"]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            writer.writerow(
                {
                    "id": article.get("id"),
                    "slug": article.get("slug"),
                    "title": article.get("title"),
                    "url": article.get("url"),
                    "published_at": article.get("published_at"),
                    "file": article.get("__file"),
                }
            )


def write_current_crosslinks_csv(
    output_path: Path,
    articles: List[Dict[str, str]],
    known_slugs: List[str],
) -> None:
    fieldnames = [
        "source_id",
        "source_slug",
        "source_article",
        "target_slug",
        "target_url",
        "anchor_text",
        "full_crosslink_text",
        "context_snippet",
        "href",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            html = article.get("html") or ""
            raw_text = article.get("raw_text")
            if html:
                links = extract_links_from_html(html, known_slugs)
            elif isinstance(raw_text, dict):
                links = extract_links_from_doc(raw_text, known_slugs)
            else:
                links = []
            for link in links:
                writer.writerow(
                    {
                        "source_id": article.get("id"),
                        "source_slug": article.get("slug"),
                        "source_article": article.get("title"),
                        "target_slug": link.get("target_slug"),
                        "target_url": f"https://oecs.mit.edu/pub/{link.get('target_slug')}",
                        "anchor_text": link.get("anchor_text"),
                        "full_crosslink_text": link.get("full_crosslink_text"),
                        "context_snippet": link.get("context_snippet"),
                        "href": link.get("href"),
                    }
                )


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract current OECS crosslinks.")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of articles.")
    args = parser.parse_args()

    root = resolve_root()
    articles_dir = root / "articles"
    metadata_dir = root / "metadata"
    metadata_dir.mkdir(exist_ok=True, parents=True)

    articles = load_articles(articles_dir)
    if args.limit is not None:
        articles = articles[: args.limit]

    known_slugs = [article.get("slug") for article in articles if article.get("slug")]
    write_current_articles_csv(metadata_dir / "current_articles.csv", articles)
    write_current_crosslinks_csv(
        metadata_dir / "current_crosslinks.csv", articles, known_slugs
    )


if __name__ == "__main__":
    main()
