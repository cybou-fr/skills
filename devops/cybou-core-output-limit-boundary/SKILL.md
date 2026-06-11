---
name: cybou-core-output-limit-boundary
description: 'Implement and review output capture boundary: stdout/stderr byte limits, timeout status, truncation metadata,
  redaction and evidence capture.'
---

# Runtime Output Limit Boundary

Bounds stdout/stderr before model exposure. Captures truncation status, redaction status and evidence metadata.

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
