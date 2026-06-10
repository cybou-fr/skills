from __future__ import annotations
import re
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

WRITE = {"insert", "update", "delete", "drop", "truncate", "alter", "create", "grant", "revoke"}

def normalize_database(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    low = raw.strip().lower()
    m = re.match(r"^\s*([a-zA-Z]+)", raw)
    op = m.group(1).lower() if m else (tokens[0] if tokens else "unknown")
    effects = []
    if op in WRITE:
        effects.append("write")
    if op in ["drop", "truncate", "delete"]:
        effects.append("destructive")
    if "migration" in low or "migrate" in low:
        effects.append("schema_migration")
    return NormalizedAction("database", op, raw, {"tokens": tokens, "sql_operation": op}, target="database", environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw) or op == "select")
