---
name: kms-key-policy-review
description: 'Review KMS/key policy risks across AWS KMS, Azure Key Vault keys and GCP Cloud KMS: grants, rotation, public/cross-account
  access and deletion windows.'
---

# KMS Key Policy Review

Analyze key policies, grants, rotation, deletion, external access and envelope encryption boundaries.

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
