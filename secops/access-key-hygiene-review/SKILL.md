---
name: access-key-hygiene-review
description: Review access key hygiene: long-lived keys, unused keys, keys without rotation, root keys, leaked keys and CI/CD key usage.
---

# Access Key Hygiene Review

Evaluate cloud/API access keys and recommend rotation/removal plan without exposing values.

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
