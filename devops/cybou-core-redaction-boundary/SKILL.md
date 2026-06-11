---
name: cybou-core-redaction-boundary
description: Implement runtime redaction boundary for tool outputs, logs, errors, audit events and model-visible context.
---

# Runtime Redaction Boundary

Redact secrets before model exposure and before persistent logs. If redaction fails for high-risk output, block output.

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
