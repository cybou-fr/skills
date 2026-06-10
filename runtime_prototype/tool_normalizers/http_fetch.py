from __future__ import annotations
from urllib.parse import urlparse
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

def normalize_http_fetch(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    method = "GET"
    url = None
    output_file = None
    effects = []
    for i,t in enumerate(tokens):
        if t in ["-X", "--request"] and i+1 < len(tokens):
            method = tokens[i+1].upper()
        if t.startswith("http://") or t.startswith("https://"):
            url = t
        if t in ["-o", "--output"] and i+1 < len(tokens):
            output_file = tokens[i+1]
            effects.append("write")
    if "|" in raw:
        effects.append("pipe")
    if method not in ["GET", "HEAD", "OPTIONS"]:
        effects.append("write")
    host = urlparse(url).netloc if url else None
    return NormalizedAction("http_fetch", method.lower(), raw, {"tokens": tokens, "url": url, "host": host, "output_file": output_file}, target=host, environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw) or any(t.lower() in ["-h", "--header", "-d", "--data"] for t in tokens))
