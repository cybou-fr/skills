---
name: runtime-tool-execution-boundary
description: Implement and review central tool execution boundary with dry-run by default, timeout, output byte caps, cwd allowlist, environment allowlist and redaction hooks.
---

# Runtime Tool Execution Boundary

Central execution wrapper for approved low-risk prototype commands. It is dry-run by default and blocks high-risk commands unless explicitly allowed with approval and sandbox profile.

## Runtime enforcement rule

This skill belongs to sandbox and tool execution boundary.

No tool may execute directly from assistant text. Every execution must pass through normalization, policy evaluation, approval validation if needed, sandbox profile selection, timeout/output limits, redaction and audit/evidence capture.

## Required output

End with:

- sandbox profile;
- allowed filesystem roots;
- network mode;
- timeout/output limits;
- policy decision;
- execution mode;
- audit/evidence impact;
- tests required.
