---
name: cybou-core-scope-matcher
description: 'Implement and review scope matching for normalized actions: environment, target, tool, operation, namespace,
  workspace, repository, and explicit scope object matching.'
---

# Runtime Scope Matcher

Matches `NormalizedAction` against scope object and approval scope.

## Runtime enforcement rule

Approvals must be explicit, scoped, expiring, auditable, revocable and matched against the normalized action immediately before execution.

Important: approval can satisfy `approval_required`; it must not override `deny`, `deny_by_default` or `refuse_or_escalate`.

## Required output

End with:

- approval scope;
- approved actions;
- expiration behavior;
- revocation behavior;
- policy decision impact;
- audit impact;
- tests required.
