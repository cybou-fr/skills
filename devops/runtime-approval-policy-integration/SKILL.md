---
name: runtime-approval-policy-integration
description: Integrate scoped approvals into policy evaluation so approval-required actions can become allow-with-approval only when action, target, scope and expiration match.
---

# Runtime Approval Policy Integration

`approval_required` can become `allow_with_approval`; hard deny remains deny.

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
