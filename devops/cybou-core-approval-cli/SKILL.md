---
name: cybou-core-approval-cli
description: Implement and review CLI workflows for creating, listing, revoking and evaluating scoped approvals in CYBOU runtime
  prototype.
---

# Runtime Approval CLI

Provides create/list/revoke/evaluate workflows. No global implicit approval.

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
