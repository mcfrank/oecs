import re
from typing import Any, Dict, Iterable, List, Optional, Tuple

from bs4 import BeautifulSoup


PUB_SLUG_PATTERN = re.compile(r"/pubs?/([^/?#]+)")
SEE_PATTERN = re.compile(r"\[see\s+([^\]]+)\]", re.IGNORECASE)


def clean_html_to_text(html: str) -> str:
    soup = BeautifulSoup(html or "", "lxml")
    text = soup.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", text).strip()


def extract_slug_from_href(href: str) -> Optional[str]:
    if not href:
        return None
    match = PUB_SLUG_PATTERN.search(href)
    if match:
        return match.group(1)
    return None


def build_context_snippet(text: str, max_len: int = 240) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def extract_links_from_html(html: str, known_slugs: Iterable[str]) -> List[Dict[str, str]]:
    slug_set = set(known_slugs)
    soup = BeautifulSoup(html or "", "lxml")
    links: List[Dict[str, str]] = []
    for anchor in soup.find_all("a"):
        href = anchor.get("href") or ""
        anchor_text = anchor.get_text(" ", strip=True)
        slug = extract_slug_from_href(href)
        if not (slug and slug in slug_set):
            continue
        parent_text = anchor.parent.get_text(" ", strip=True) if anchor.parent else anchor_text
        matches = list(SEE_PATTERN.finditer(parent_text))
        if not matches:
            continue
        full_crosslink_text = None
        if anchor_text:
            anchor_lower = anchor_text.lower()
            for match in matches:
                if anchor_lower in match.group(0).lower():
                    full_crosslink_text = match.group(0)
                    break
        if not full_crosslink_text:
            continue
        links.append(
            {
                "target_slug": slug,
                "href": href,
                "anchor_text": anchor_text,
                "full_crosslink_text": full_crosslink_text,
                "context_snippet": build_context_snippet(parent_text),
            }
        )
    return links


def iter_block_nodes(node: Any) -> Iterable[Dict[str, Any]]:
    if isinstance(node, dict):
        node_type = node.get("type")
        if node_type in {"paragraph", "heading", "list_item", "listItem", "blockquote"}:
            yield node
        for child in node.get("content", []) or []:
            yield from iter_block_nodes(child)
    elif isinstance(node, list):
        for child in node:
            yield from iter_block_nodes(child)


def extract_segments(node: Any) -> List[Tuple[str, Optional[str]]]:
    segments: List[Tuple[str, Optional[str]]] = []
    if isinstance(node, dict):
        node_type = node.get("type")
        if node_type == "text":
            text = node.get("text", "")
            href = None
            for mark in node.get("marks", []) or []:
                if mark.get("type") == "link":
                    href = (mark.get("attrs") or {}).get("href")
                    break
            segments.append((text, href))
        elif node_type == "hard_break":
            segments.append(("\n", None))
        for child in node.get("content", []) or []:
            segments.extend(extract_segments(child))
    elif isinstance(node, list):
        for child in node:
            segments.extend(extract_segments(child))
    return segments


def merge_segments(segments: List[Tuple[str, Optional[str]]]) -> List[Tuple[str, Optional[str]]]:
    merged: List[Tuple[str, Optional[str]]] = []
    for text, href in segments:
        if not text:
            continue
        if merged and merged[-1][1] == href:
            prev_text, _ = merged[-1]
            merged[-1] = (prev_text + text, href)
        else:
            merged.append((text, href))
    return merged


def extract_links_from_doc(doc: Dict[str, Any], known_slugs: Iterable[str]) -> List[Dict[str, str]]:
    slug_set = set(known_slugs)
    links: List[Dict[str, str]] = []
    for block in iter_block_nodes(doc):
        segments = merge_segments(extract_segments(block.get("content", []) or []))
        full_text = "".join(text for text, _ in segments)
        matches = list(SEE_PATTERN.finditer(full_text))
        if not matches:
            continue
        for text, href in segments:
            if not href:
                continue
            slug = extract_slug_from_href(href)
            if not (slug and slug in slug_set):
                continue
            full_crosslink_text = None
            anchor_lower = text.lower() if text else ""
            for match in matches:
                if anchor_lower and anchor_lower in match.group(0).lower():
                    full_crosslink_text = match.group(0)
                    break
            if not full_crosslink_text:
                continue
            links.append(
                {
                    "target_slug": slug,
                    "href": href,
                    "anchor_text": text,
                    "full_crosslink_text": full_crosslink_text,
                    "context_snippet": build_context_snippet(full_text),
                }
            )
    return links


def doc_to_text(doc: Dict[str, Any]) -> str:
    segments = merge_segments(extract_segments(doc))
    full_text = "".join(text for text, _ in segments)
    return re.sub(r"\s+", " ", full_text).strip()
