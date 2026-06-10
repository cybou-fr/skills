from __future__ import annotations
import shlex

SENSITIVE_WORDS = ["secret", "token", "password", "credential", "cookie", "api key", "apikey", "bearer", "session"]

def split_command(raw: str) -> list[str]:
    try:
        return shlex.split(raw)
    except ValueError:
        return raw.split()

def detect_environment(raw: str, tokens: list[str] | None = None) -> str:
    low = raw.lower()
    if any(x in low for x in ["prod", "production", "namespace prod", "-n prod", "--namespace prod", "--context prod", "context=prod"]):
        return "production"
    if "staging" in low or "stage" in low:
        return "staging"
    if "dev" in low or "local" in low:
        return "development"
    return "unknown"

def has_sensitive_hint(raw: str) -> bool:
    low = raw.lower()
    return any(w in low for w in SENSITIVE_WORDS)

def unique(items: list[str]) -> list[str]:
    return sorted(set([x for x in items if x]))
