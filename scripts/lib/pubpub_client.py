import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

from Crypto.Hash import keccak
import requests


@dataclass
class PubPubConfig:
    base_url: str
    email: str
    collection_id: str
    community_id: str
    limit: int = 1000
    offset: int = 0


def load_config(config_path: str) -> Dict[str, Any]:
    with open(config_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def request_json(
    session: requests.Session,
    method: str,
    base_url: str,
    endpoint: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
) -> Any:
    url = f"{normalize_base_url(base_url)}/{endpoint.lstrip('/')}"
    debug = os.getenv("OECS_DEBUG") == "1"
    safe_body = None
    if json_body is not None:
        safe_body = dict(json_body)
        if "password" in safe_body:
            safe_body["password"] = "***REDACTED***"
    response = session.request(
        method,
        url,
        json=json_body,
        params=params,
        headers={"Accept": "application/json"},
        timeout=60,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError:
        if debug:
            print("PubPub request failed")
            print("Method:", method)
            print("URL:", url)
            print("Params:", params)
            print("JSON body:", safe_body)
            print("Status:", response.status_code)
            print("Response:", response.text)
        raise
    return response.json()


def login(session: requests.Session, config: PubPubConfig, password: str) -> None:
    keccak_hash = keccak.new(digest_bits=512)
    keccak_hash.update(password.encode("utf-8"))
    hashed_password = keccak_hash.hexdigest()
    request_json(
        session,
        "POST",
        config.base_url,
        "login",
        json_body={"email": config.email, "password": hashed_password},
    )


def extract_pubs_from_collection_response(data: Any) -> Tuple[List[Dict[str, Any]], Optional[int]]:
    if isinstance(data, list):
        return data, None
    if isinstance(data, dict):
        for key in ("pubs", "results", "data"):
            if key in data and isinstance(data[key], list):
                total = data.get("total")
                return data[key], total
        if all(isinstance(value, dict) for value in data.values()):
            return list(data.values()), None
    raise ValueError("Unexpected response format from collectionPubs")


def list_collection_pubs(
    session: requests.Session,
    config: PubPubConfig,
) -> List[Dict[str, Any]]:
    all_pubs: List[Dict[str, Any]] = []
    offset = config.offset
    while True:
        params = {
            "collectionId": config.collection_id,
            "communityId": config.community_id,
            "limit": config.limit,
            "offset": offset,
        }
        data = request_json(session, "GET", config.base_url, "collectionPubs", params=params)
        pubs, total = extract_pubs_from_collection_response(data)
        if not pubs:
            break
        all_pubs.extend(pubs)
        if total is not None and len(all_pubs) >= total:
            break
        if len(pubs) < config.limit:
            break
        offset += config.limit
    return all_pubs


def fetch_pub(session: requests.Session, config: PubPubConfig, pub_id: str) -> Dict[str, Any]:
    return request_json(session, "GET", config.base_url, f"pubs/{pub_id}")


def fetch_pub_text(session: requests.Session, config: PubPubConfig, pub_id: str) -> Dict[str, Any]:
    return request_json(session, "GET", config.base_url, f"pubs/{pub_id}/text")


def put_pub_text(
    session: requests.Session,
    config: PubPubConfig,
    pub_id: str,
    doc: Dict[str, Any],
    *,
    publish_release: bool = False,
    method: str = "replace",
) -> Dict[str, Any]:
    payload = {
        "doc": doc,
        "publishRelease": publish_release,
        "method": method,
        "clientID": "api",
    }
    return request_json(session, "PUT", config.base_url, f"pubs/{pub_id}/text", json_body=payload)
