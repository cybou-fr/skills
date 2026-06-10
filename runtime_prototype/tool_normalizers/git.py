from __future__ import annotations
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

WRITE = {"commit", "push", "reset", "clean", "rebase", "merge", "checkout", "switch", "tag"}

def normalize_git(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    op = tokens[1] if len(tokens) > 1 and tokens[0] == "git" else (tokens[0] if tokens else "unknown")
    effects = []
    if op in WRITE:
        effects.append("write")
    if op == "push" and any(t in ["--force", "-f", "--force-with-lease"] for t in tokens):
        effects.append("history_rewrite")
    if op == "reset" and "--hard" in tokens:
        effects.append("destructive")
    if op == "clean" and any(t.startswith("-f") for t in tokens):
        effects.append("destructive")
    target = tokens[-1] if len(tokens) > 2 and not tokens[-1].startswith("-") else None
    return NormalizedAction("git", op, raw, {"tokens": tokens}, target=target, environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw))
