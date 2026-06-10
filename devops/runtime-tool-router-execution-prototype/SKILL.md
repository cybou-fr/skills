---
name: runtime-tool-router-execution-prototype
description: Implement tool router execution prototype that connects normalizer, policy, approval, sandbox, executor, audit
  store and evidence store.
---

# Runtime Tool Router Execution Prototype

Implements full flow from command to simulated/controlled execution record.

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
