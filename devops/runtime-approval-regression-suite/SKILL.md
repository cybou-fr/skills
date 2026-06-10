---
name: runtime-approval-regression-suite
description: Create regression tests for scoped approvals, expiration, revocation, mismatched action, mismatched target, staging-vs-production
  mismatch and valid approval flows.
---

# Runtime Approval Regression Suite

Covers valid, expired, revoked, wrong action, wrong scope and hard-deny-not-overridden cases.

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
