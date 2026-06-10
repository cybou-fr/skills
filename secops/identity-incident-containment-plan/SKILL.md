---
name: identity-incident-containment-plan
description: Draft identity incident containment plans: disable account, revoke sessions, rotate keys, remove app consent, reset credentials and preserve evidence.
---

# Identity Incident Containment Plan

Read-only containment planning with approval boundaries for all mutating actions.

## Runtime enforcement rule

This skill belongs to identity, secrets and key-management security.

Identity and secret workflows are read-only by default. Rotation, revocation, disablement, key deletion, policy update, app consent removal, session revocation, password reset, and KMS/key policy changes require explicit approval. Secret values must never be printed, stored raw, or placed in audit/evidence.

## Required output

End with:

- identity/secret/key scope;
- principal or secret reference;
- exposure/privilege risk;
- evidence to collect;
- redaction status;
- read-only next steps;
- approval-required actions.
