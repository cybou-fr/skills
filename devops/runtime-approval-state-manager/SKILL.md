---
name: runtime-approval-state-manager
description: Implement scoped approval state manager with expiration, approved actions, revocation and audit integration.
---

# Runtime Approval State Manager

Approvals are scoped, explicit and expiring. Approval for `plan` does not allow `apply`; staging approval does not allow production.

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
