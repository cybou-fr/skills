---
name: cybou-core-policy-decision-engine
description: Implement and review CYBOU PolicyDecision engine combining normalized actions, risk matrix, policies, profiles,
  scope and approval state.
---

# Runtime Policy Decision Engine

Produces deterministic `PolicyDecision` objects before tool execution.

Decision classes: `allow_read_only`, `allow_read_only_and_redact`, `approval_required`, `allow_with_approval`, `deny_by_default`.

Hard denies include pipe-to-shell, root deletion, destructive database commands and jailbreak/bypass generation.

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
