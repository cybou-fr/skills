---
name: runtime-tool-router
description: Implement Tool Router dispatching tool calls only after normalization, policy decision, approval validation,
  output limits, redaction and audit hooks.
---

# Runtime Tool Router

No direct tool execution outside router. Every adapter call goes through normalization, policy, approval, output bounds, redaction and audit.

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
