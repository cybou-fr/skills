from __future__ import annotations
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

READ_ONLY = {"check", "test", "fmt", "clippy", "metadata", "tree", "audit", "deny", "doc", "bench"}
WRITE = {"publish", "install", "update", "add", "remove", "package"}

def normalize_cargo(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    op = tokens[1] if len(tokens) > 1 and tokens[0] == "cargo" else (tokens[0] if tokens else "unknown")
    effects = []
    if op in WRITE:
        effects.append("write")
    if op == "publish":
        effects.append("external_publish")
    if op in ["install", "update", "add", "remove"]:
        effects.append("supply_chain_change")
    features = []
    for i, t in enumerate(tokens):
        if t in ["--features", "-F"] and i + 1 < len(tokens):
            features.append(tokens[i + 1])
        elif t in ["--all-features", "--no-default-features"]:
            features.append(t)
    channel = next((t[1:] for t in tokens if t.startswith("+")), None)
    return NormalizedAction("cargo", op, raw, {"tokens": tokens, "features": features, "channel": channel, "read_only_known": op in READ_ONLY}, target="cargo_workspace", environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw))
