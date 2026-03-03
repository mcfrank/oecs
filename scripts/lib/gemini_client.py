import json
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from google import genai


@dataclass
class GeminiConfig:
    api_key: str
    model: str


def initialize_gemini(config: GeminiConfig) -> genai.Client:
    return genai.Client(api_key=config.api_key)


def extract_json_from_text(text: str) -> Optional[Any]:
    if not text:
        return None
    match = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def generate_crosslinks(
    client: genai.Client,
    model: str,
    prompt: str,
) -> Tuple[List[Dict[str, Any]], str, str]:
    last_error: Optional[Exception] = None
    for attempt in range(1, 4):
        try:
            response = client.models.generate_content(model=model, contents=prompt)
            raw_text = response.text or ""
            response_debug = repr(response)
            break
        except Exception as exc:
            last_error = exc
            if attempt == 3:
                raise
            time.sleep(2 * attempt)
    else:
        raise last_error or RuntimeError("Gemini request failed")
    data = extract_json_from_text(raw_text)
    if isinstance(data, dict) and "links" in data:
        data = data["links"]
    if isinstance(data, list):
        return data, raw_text, response_debug
    return [], raw_text, response_debug
