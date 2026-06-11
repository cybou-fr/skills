---
name: cybou-core-filesystem-boundary
description: 'Implement and review filesystem boundary for tool execution: cwd scope, path allowlist, write restrictions,
  temp dirs and denied sensitive paths.'
---

# Runtime Filesystem Boundary

Restricts execution to allowed working directories and denies sensitive filesystem roots by default.

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
