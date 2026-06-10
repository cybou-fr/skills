from __future__ import annotations
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

WRITE = {"apply", "delete", "patch", "edit", "scale", "exec", "rollout", "create", "replace", "cordon", "drain", "taint", "label", "annotate"}

def _flag_value(tokens, names):
    for i,t in enumerate(tokens):
        for n in names:
            if t == n and i+1 < len(tokens): return tokens[i+1]
            if t.startswith(n+"="): return t.split("=",1)[1]
    return None

def normalize_kubectl(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    verb = tokens[1] if len(tokens) > 1 and tokens[0] == "kubectl" else (tokens[0] if tokens else "unknown")
    resource = tokens[2] if len(tokens) > 2 else None
    name = tokens[3] if len(tokens) > 3 and not tokens[3].startswith("-") else None
    namespace = _flag_value(tokens, ["-n", "--namespace"])
    context = _flag_value(tokens, ["--context"])
    if (namespace and namespace.lower() in ["prod", "production"]) or (context and "prod" in context.lower()):
        env = "production"
    effects = []
    if verb in WRITE:
        effects.append("write")
    if verb == "delete" or (verb == "rollout" and "restart" in tokens):
        effects.append("destructive")
    if verb == "exec":
        effects.append("remote_execution")
    if "--dry-run=client" in tokens or "--dry-run=server" in tokens:
        effects = [e for e in effects if e != "write"]
    return NormalizedAction("kubectl", verb, raw, {"tokens": tokens, "resource": resource, "name": name, "namespace": namespace, "context": context}, target=resource, environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw) or verb == "logs")
