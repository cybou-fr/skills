from __future__ import annotations
import re
from runtime_prototype.models import NormalizedAction
from .common import split_command, detect_environment, has_sensitive_hint, unique

def normalize_shell(raw: str) -> NormalizedAction:
    tokens = split_command(raw)
    low = raw.lower()
    env = detect_environment(raw, tokens)
    effects = []

    if re.search(r"(curl|wget).*\|\s*(sh|bash|zsh)", low):
        return NormalizedAction("shell", "pipe_to_shell", raw, {"tokens": tokens, "pipe_to_shell": True}, environment=env, side_effects=["code_execution", "network_or_pipe"], sensitive_data_possible=True)

    if tokens and tokens[0] in ["bash", "sh", "zsh"] and "-c" in tokens:
        idx = tokens.index("-c")
        wrapped = tokens[idx + 1] if idx + 1 < len(tokens) else ""
        wrapped_low = wrapped.lower()
        if any(x in wrapped_low for x in ["rm -rf", "delete", "destroy", "drop database"]):
            effects.append("destructive")
        if any(x in wrapped_low for x in ["rm", "mv", "cp", "chmod", "chown", "terraform apply", "terraform destroy"]):
            effects.append("write")
        return NormalizedAction("shell", "shell_wrapper", raw, {"tokens": tokens, "wrapper": tokens[0], "wrapped": wrapped}, environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw))

    op = tokens[0] if tokens else "unknown"
    if "rm -rf" in low or op in ["rm", "unlink", "shred"]:
        effects += ["destructive", "write"]
    if any(x in low for x in [">", ">>", "chmod", "chown", "mv ", "cp ", "install "]):
        effects.append("write")
    if "|" in raw:
        effects.append("pipe")
    return NormalizedAction("shell", op, raw, {"tokens": tokens}, environment=env, side_effects=unique(effects), sensitive_data_possible=has_sensitive_hint(raw))
