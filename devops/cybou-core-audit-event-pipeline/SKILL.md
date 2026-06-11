---
name: cybou-core-audit-event-pipeline
description: Implement audit event pipeline for task, skill selection, normalized action, policy decision, approval, tool
  call and redaction events.
---

# Runtime Audit Event Pipeline

Every allowed, blocked or approval-required action must emit an audit event without leaking secrets.

## Runtime enforcement rule

Skills may recommend. Runtime decides. Tool Router enforces.

Runtime flow:

```text
raw request -> NormalizedAction -> PolicyDecision -> approval/scope check -> audit -> execution only if allowed -> redaction
```

## Required output

End with:
- runtime component;
- normalized action impact;
- policy decision impact;
- tests required;
- audit/redaction impact;
- approval required, if any.
