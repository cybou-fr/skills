---
name: runtime-approval-store
description: Implement and review local approval store prototype with create/list/revoke/expire operations, JSON persistence and audit-friendly records.
---

# Runtime Approval Store

Stores scoped approvals in a local JSON file for prototype/runtime testing. Production must replace it with authenticated durable storage.

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
