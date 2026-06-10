from __future__ import annotations
from .common import split_command
from .shell import normalize_shell
from .cargo import normalize_cargo
from .kubectl import normalize_kubectl
from .terraform import normalize_terraform
from .docker import normalize_docker
from .git import normalize_git
from .database import normalize_database
from .http_fetch import normalize_http_fetch

def normalize(raw: str, tool_hint: str | None = None):
    raw = raw.strip()
    tokens = split_command(raw)
    low = raw.lower()
    tool = tool_hint
    if not tool:
        first = tokens[0] if tokens else "unknown"
        if first == "cargo": tool = "cargo"
        elif first == "kubectl": tool = "kubectl"
        elif first in ["terraform", "tofu"]: tool = "terraform"
        elif first == "docker": tool = "docker"
        elif first == "git": tool = "git"
        elif first in ["curl", "wget"] or low.startswith("http://") or low.startswith("https://"): tool = "http_fetch"
        elif first in ["psql", "mysql", "sqlite3"] or low.startswith(("select", "insert", "update", "delete", "drop", "truncate", "alter", "create")): tool = "database"
        elif "log" in low or "logs" in low: tool = "log_reader"
        else: tool = "shell"
    if tool == "cargo": return normalize_cargo(raw)
    if tool == "kubectl": return normalize_kubectl(raw)
    if tool == "terraform": return normalize_terraform(raw)
    if tool == "docker": return normalize_docker(raw)
    if tool == "git": return normalize_git(raw)
    if tool == "database": return normalize_database(raw)
    if tool == "http_fetch": return normalize_http_fetch(raw)
    if tool == "log_reader":
        a = normalize_shell(raw)
        a.tool = "log_reader"
        a.operation = tokens[0] if tokens else "read"
        return a
    return normalize_shell(raw)
