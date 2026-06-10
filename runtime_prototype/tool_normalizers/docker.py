from __future__ import annotations
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

WRITE = {"run", "exec", "rm", "rmi", "stop", "restart", "kill", "build", "push", "pull", "compose"}

def normalize_docker(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    env = detect_environment(raw, tokens)
    op = tokens[1] if len(tokens) > 1 and tokens[0] == "docker" else (tokens[0] if tokens else "unknown")
    effects = []
    if op in WRITE:
        effects.append("write")
    if op in ["rm", "rmi", "kill"] or ("compose" in tokens and "down" in tokens):
        effects.append("destructive")
    if "--privileged" in tokens:
        effects.append("privileged_container")
    if any("/var/run/docker.sock" in t for t in tokens):
        effects.append("docker_socket_mount")
    target = next((t for t in reversed(tokens) if not t.startswith("-")), None)
    return NormalizedAction("docker", op, raw, {"tokens": tokens}, target=target, environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw))
