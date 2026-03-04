#!/usr/bin/env python3
"""
Download OECS graphical assets from the live site: hero background, hero logo,
nav logo, and thematic collection images. Saves to static/images/ and updates
data/thematic_collections.json with image paths.

Run from repo root (e.g. python scripts/download_oecs_assets.py).
Requires: requests, beautifulsoup4, lxml.
"""
import base64
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse, urlunparse, unquote

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


def normalize_asset_url(url: str) -> str:
    """Normalize asset URL: replace Unicode spaces with ASCII space so server accepts the request."""
    parsed = urlparse(url)
    path = parsed.path
    # Replace narrow no-break space (U+202F) and non-breaking space (U+00A0) with ASCII space.
    path = path.replace("\u202f", " ").replace("\u00a0", " ")
    # If the JSON contained mojibake (UTF-8 bytes for U+202F read as Latin-1), fix that too.
    path = path.replace("\xe2\x80\xaf", " ")
    return urlunparse((parsed.scheme, parsed.netloc, path, parsed.params, parsed.query, parsed.fragment))


def download_file(session: requests.Session, url: str, dest: Path) -> bool:
    """Download URL to dest; return True on success."""
    url = normalize_asset_url(url)
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


def build_resize_v3_url(assets_url: str) -> str | None:
    """Build resize-v3.pubpub.org URL from an assets.pubpub.org URL (used when direct CDN returns 404)."""
    parsed = urlparse(assets_url)
    if "pubpub.org" not in (parsed.netloc or ""):
        return None
    path = (parsed.path or "").strip()
    if not path or not path.startswith("/"):
        return None
    key = unquote(path[1:])  # no leading slash, percent-encoding decoded
    # Fix mojibake: UTF-8 bytes for U+202F (narrow no-break) sometimes appear as three code points
    key = key.replace("\u00e2\u0080\u00af", "\u202f")
    payload = {
        "bucket": "assets.pubpub.org",
        "key": key,
        "edits": {"resize": {"width": 600, "fit": "inside", "withoutEnlargement": True}},
    }
    try:
        # Compact JSON (no space after ':') and UTF-8 in key so base64 matches live site
        json_str = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
        b64 = base64.b64encode(json_str.encode("utf-8")).decode("ascii")
        return f"https://resize-v3.pubpub.org/{b64}"
    except Exception:
        return None


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
    failed_slugs: list[str] = []
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
            slug_to_image[slug] = f"images/themes/{filename}"
            print(f"Downloaded theme image: {filename}")
        else:
            # Fallback: try resize-v3.pubpub.org (direct CDN often 404s for these keys)
            resize_url = build_resize_v3_url(avatar)
            if resize_url and download_file(session, resize_url, dest):
                slug_to_image[slug] = f"images/themes/{filename}"
                print(f"Downloaded theme image via resize: {filename}")
            else:
                failed_slugs.append(slug)

    # 4b) Placeholder for themes whose avatar URL returned 404 (e.g. CDN filenames with spaces)
    placeholder_sources = [
        ("ai-and-cognitive-modeling", "technology.png"),
        ("social-cognition", "cognition.jpg"),
    ]
    for slug, copy_from_name in placeholder_sources:
        if slug not in slug_to_image and slug in failed_slugs:
            src = static_images / "themes" / copy_from_name
            ext = Path(copy_from_name).suffix
            dest = static_images / "themes" / f"{slug}{ext}"
            if src.exists():
                shutil.copy2(src, dest)
                slug_to_image[slug] = f"images/themes/{dest.name}"
                print(f"Using placeholder for {slug} (copied from {copy_from_name})")

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
