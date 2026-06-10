from __future__ import annotations
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

WRITE = {"apply", "destroy", "import", "state", "force-unlock", "taint", "untaint"}

def _flag_value(tokens, prefix):
    for i,t in enumerate(tokens):
        if t == prefix and i+1 < len(tokens): return tokens[i+1]
        if t.startswith(prefix+"="): return t.split("=",1)[1]
    return None

def normalize_terraform(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    op = "unknown"
    for t in tokens[1:]:
        if not t.startswith("-"):
            op = t
            break
    chdir = _flag_value(tokens, "-chdir")
    effects = []
    if op in WRITE:
        effects.append("write")
    if op == "destroy":
        effects.append("destructive")
    if "-auto-approve" in tokens:
        effects.append("auto_approve")
    if op == "state":
        effects.append("state_mutation")
    return NormalizedAction("terraform", op, raw, {"tokens": tokens, "chdir": chdir, "auto_approve": "-auto-approve" in tokens}, target=chdir or "terraform_workspace", environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw))
