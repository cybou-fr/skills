---
name: runtime-sandbox-regression-suite
description: Create regression tests for sandbox profile selection, dry-run behavior, timeout, output cap, denied network
  pipe, blocked destructive actions and allowed read-only commands.
---

# Runtime Sandbox Regression Suite

Tests sandbox and execution boundary semantics independently and in full router flow.

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
