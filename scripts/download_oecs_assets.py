#!/usr/bin/env python3
"""
Download OECS graphical assets from the live site: hero background, hero logo,
nav logo, and thematic collection images. Saves to static/images/ and updates
data/thematic_collections.json with image paths.

Run from repo root (e.g. python scripts/download_oecs_assets.py).
Requires: requests, beautifulsoup4, lxml.
"""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://oecs.mit.edu"
TIMEOUT = 60


def resolve_root() -> Path:
    return Path(__file__).resolve().parents[1]


def fetch_html(session: requests.Session, path: str = "/") -> str | None:
    url = BASE_URL + path if path.startswith("/") else BASE_URL + "/" + path
    try:
        r = session.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        print(f"Warning: failed to fetch {url}: {e}")
        return None


def extract_initial_data(html: str) -> dict | None:
    """Parse script#initial-data data-json from OECS home page."""
    if not html:
        return None
    soup = BeautifulSoup(html, "lxml")
    script = soup.find("script", id="initial-data", type="text/plain", attrs={"data-json": True})
    if not script or not script.get("data-json"):
        return None
    raw = script["data-json"]
    # data-json is HTML-entity encoded (e.g. &quot; for ")
    raw = raw.replace("&quot;", '"').replace("&amp;", "&").replace("&#39;", "'")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def download_file(session: requests.Session, url: str, dest: Path) -> bool:
    """Download URL to dest; return True on success."""
    try:
        r = session.get(url, timeout=TIMEOUT, stream=True)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True
    except (requests.RequestException, OSError) as e:
        print(f"Warning: failed to download {url}: {e}")
        return False


def extension_from_url(url: str) -> str:
    path = urlparse(url).path.lower()
    if ".png" in path:
        return "png"
    if ".jpg" in path or ".jpeg" in path:
        return "jpg"
    return "png"


def main() -> None:
    root = resolve_root()
    static_images = root / "static" / "images"
    static_images.mkdir(parents=True, exist_ok=True)
    (static_images / "themes").mkdir(exist_ok=True)
    data_dir = root / "data"

    session = requests.Session()
    session.headers.update({"User-Agent": "OECS-Static-Asset-Downloader/1.0"})

    print("Fetching OECS home page for asset URLs...")
    html = fetch_html(session, "/")
    if not html:
        print("Could not fetch home page. Aborting.")
        return

    data = extract_initial_data(html)
    if not data:
        print("Could not parse initial-data JSON from home page. Aborting.")
        return

    community = data.get("communityData") or {}
    collections = community.get("collections") or []

    # 1) Hero background
    hero_bg = community.get("heroBackgroundImage")
    if hero_bg:
        if download_file(session, hero_bg, static_images / "hero-bg.png"):
            print("Downloaded hero-bg.png")
    else:
        print("No heroBackgroundImage in community data.")

    # 2) Hero logo (large logo on home)
    hero_logo = community.get("heroLogo")
    if hero_logo:
        if download_file(session, hero_logo, static_images / "hero-logo.png"):
            print("Downloaded hero-logo.png")
    else:
        print("No heroLogo in community data.")

    # 3) Nav/header logo (small)
    header_logo = community.get("headerLogo")
    if header_logo:
        if download_file(session, header_logo, static_images / "logo.png"):
            print("Downloaded logo.png")
    else:
        print("No headerLogo in community data.")

    # 4) Thematic collection avatars (only tag collections, exclude the book collection)
    slug_to_image: dict[str, str] = {}
    for coll in collections:
        if coll.get("kind") != "tag":
            continue
        slug = (coll.get("slug") or "").strip()
        if slug in ("", "open-encyclopedia-of-cognitive-science", "search"):
            continue
        avatar = coll.get("avatar")
        if not avatar:
            continue
        ext = extension_from_url(avatar)
        filename = f"{slug}.{ext}"
        dest = static_images / "themes" / filename
        if download_file(session, avatar, dest):
            # Path relative to site root for use with relURL in layouts
            slug_to_image[slug] = f"images/themes/{filename}"
            print(f"Downloaded theme image: {filename}")

    # 5) Update data/thematic_collections.json with image paths
    tc_path = data_dir / "thematic_collections.json"
    if tc_path.exists() and slug_to_image:
        tc = json.loads(tc_path.read_text(encoding="utf-8"))
        for item in tc:
            s = item.get("slug")
            if s and s in slug_to_image:
                item["image"] = slug_to_image[s]  # e.g. images/themes/technology.png
        tc_path.write_text(json.dumps(tc, indent=2), encoding="utf-8")
        print(f"Updated {tc_path} with image paths.")

    # 6) Write theme_images.json for layouts that prefer a simple slug -> path map
    theme_images_path = data_dir / "theme_images.json"
    theme_images_path.write_text(json.dumps(slug_to_image, indent=2), encoding="utf-8")
    print(f"Wrote {theme_images_path}.")

    print("Done.")


if __name__ == "__main__":
    main()
