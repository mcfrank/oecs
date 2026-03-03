import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

from lib.pubpub_client import (
    PubPubConfig,
    fetch_pub,
    fetch_pub_text,
    list_collection_pubs,
    load_config,
    login,
)
from lib.text_utils import clean_html_to_text, doc_to_text

import os
import requests


def resolve_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_pubpub_config(config: Dict[str, Any]) -> PubPubConfig:
    pubpub = config["pubpub"]
    return PubPubConfig(
        base_url=pubpub["base_url"],
        email=pubpub["email"],
        collection_id=pubpub["collection_id"],
        community_id=pubpub["community_id"],
        limit=pubpub.get("limit", 1000),
        offset=pubpub.get("offset", 0),
    )


def extract_html_from_text_payload(payload: Dict[str, Any]) -> Optional[str]:
    for key in ("html", "text", "content", "body"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return None


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch OECS PubPub articles.")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of pubs fetched.")
    parser.add_argument(
        "--article",
        type=str,
        default=None,
        help="Fetch a single article by pub ID.",
    )
    args = parser.parse_args()

    root = resolve_root()
    load_dotenv(root / ".secrets")
    config_path = root / "config.json"
    config = load_config(str(config_path))
    pubpub_config = build_pubpub_config(config)

    password = os.getenv("OECS_PASSWORD")
    if not password:
        raise RuntimeError("Missing OECS_PASSWORD in environment.")

    articles_dir = root / "articles"
    articles_dir.mkdir(exist_ok=True, parents=True)

    session = requests.Session()
    login(session, pubpub_config, password)

    if args.article:
        pubs = [{"id": args.article}]
    else:
        pubs = list_collection_pubs(session, pubpub_config)

    if args.limit is not None:
        pubs = pubs[: args.limit]

    index: List[Dict[str, Any]] = []
    for pub in pubs:
        pub_id = pub.get("id") or pub.get("pubId") or pub.get("pub_id")
        if not pub_id:
            continue
        pub_data = fetch_pub(session, pubpub_config, pub_id)
        text_data = fetch_pub_text(session, pubpub_config, pub_id)
        html = extract_html_from_text_payload(text_data) or ""
        slug = pub_data.get("slug")
        title = pub_data.get("title")
        published_at = pub_data.get("publishedAt") or pub_data.get("published_at")
        url = f"https://oecs.mit.edu/pub/{slug}" if slug else None

        plain_text = clean_html_to_text(html) if html else ""
        if not plain_text and isinstance(text_data, dict):
            plain_text = doc_to_text(text_data)
        record = {
            "id": pub_id,
            "slug": slug,
            "title": title,
            "url": url,
            "published_at": published_at,
            "html": html,
            "plain_text": plain_text,
            "raw_pub": pub_data,
            "raw_text": text_data,
        }
        filename = f"{slug or pub_id}.json"
        save_json(articles_dir / filename, record)
        index.append(
            {
                "id": pub_id,
                "slug": slug,
                "title": title,
                "url": url,
                "published_at": published_at,
                "file": filename,
            }
        )

    save_json(articles_dir / "index.json", {"count": len(index), "articles": index})


if __name__ == "__main__":
    main()
