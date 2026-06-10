---
name: runtime-network-boundary
description: 'Implement and review network boundary for tool execution: offline default, host allowlist, method limits and
  pipe-to-shell denial.'
---

# Runtime Network Boundary

Network is denied by default except explicitly scoped `http_fetch` operations. Pipe-to-shell remains denied.

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
