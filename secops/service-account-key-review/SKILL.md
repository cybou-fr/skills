---
name: service-account-key-review
description: Review service account keys and machine identities for age, scope, ownership, rotation, workload identity options
  and leakage risk.
---

# Service Account Key Review

Find stale, long-lived or overprivileged service account keys and propose read-only remediation plan.

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
