from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List
import subprocess, os, time

from .redaction import redact

SAFE_ALLOWLIST = {
    ("cargo", "check"),
    ("cargo", "test"),
    ("cargo", "fmt"),
    ("cargo", "clippy"),
    ("cargo", "metadata"),
    ("cargo", "tree"),
    ("cargo", "doc"),
    ("git", "status"),
    ("git", "diff"),
    ("git", "log"),
    ("git", "show"),
    ("git", "branch"),
    ("shell", "pwd"),
    ("shell", "ls"),
}

def _bounded_output(text: str, max_bytes: int) -> tuple[str, bool]:
    data = text.encode("utf-8", errors="replace")
    if max_bytes <= 0:
        return "", bool(data)
    if len(data) <= max_bytes:
        return text, False
    return data[:max_bytes].decode("utf-8", errors="replace"), True

def command_is_allowlisted(action) -> bool:
    return (action.tool, action.operation) in SAFE_ALLOWLIST

class ToolExecutionBoundary:
    def __init__(self, workdir: str | Path):
        self.workdir = Path(workdir)

    def execute(self, action, policy_decision, sandbox_name: str, sandbox: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
        result = {
            "command": action.raw_input,
            "tool": action.tool,
            "operation": action.operation,
            "sandbox_profile": sandbox_name,
            "policy_decision": policy_decision.decision,
            "would_execute": False,
            "executed": False,
            "exit_code": None,
            "timed_out": False,
            "stdout": "",
            "stderr": "",
            "output_truncated": False,
            "redaction_applied": False,
            "blocked_reason": None,
        }

        if sandbox.get("execution") in ["deny", None] or policy_decision.decision in ["deny", "deny_by_default", "refuse_or_escalate"]:
            result["blocked_reason"] = "blocked_by_policy_or_sandbox"
            return result

        if policy_decision.approval_required:
            result["blocked_reason"] = "approval_required"
            return result

        if sandbox.get("execution") == "simulate_only_in_prototype":
            result["would_execute"] = True
            result["blocked_reason"] = "prototype_simulate_only_for_approved_high_risk"
            return result

        if not command_is_allowlisted(action):
            result["blocked_reason"] = "not_in_execution_allowlist"
            return result

        result["would_execute"] = True
        if dry_run:
            result["stdout"] = f"DRY RUN: {action.raw_input}"
            return result

        max_seconds = int(sandbox.get("max_seconds") or 10)
        max_output = int(sandbox.get("max_output_bytes") or 65536)
        start = time.time()
        try:
            proc = subprocess.run(
                action.raw_input,
                cwd=str(self.workdir),
                shell=True,
                text=True,
                capture_output=True,
                timeout=max_seconds,
                env={k: os.environ[k] for k in ["PATH", "HOME", "USER", "LANG", "LC_ALL"] if k in os.environ},
            )
            result["executed"] = True
            result["exit_code"] = proc.returncode
            stdout, trunc1 = _bounded_output(proc.stdout, max_output)
            stderr, trunc2 = _bounded_output(proc.stderr, max_output)
            stdout, red1 = redact(stdout)
            stderr, red2 = redact(stderr)
            result["stdout"] = stdout
            result["stderr"] = stderr
            result["output_truncated"] = trunc1 or trunc2
            result["redaction_applied"] = red1 or red2
        except subprocess.TimeoutExpired as exc:
            result["timed_out"] = True
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            if isinstance(stdout, bytes): stdout = stdout.decode("utf-8", errors="replace")
            if isinstance(stderr, bytes): stderr = stderr.decode("utf-8", errors="replace")
            result["stdout"], _ = _bounded_output(stdout, max_output)
            result["stderr"], _ = _bounded_output(stderr, max_output)
        return result
