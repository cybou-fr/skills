---
name: runtime-behavior-test-engine
description: Implement real behavior tests comparing expected skills, normalized action, policy risk, decision, blocking, redaction and audit flags.
---

# Runtime Behavior Test Engine

Strictly validates v5 runtime scenarios and keeps older tests as routing/safety coverage.

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
