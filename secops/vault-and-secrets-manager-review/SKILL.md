---
name: vault-and-secrets-manager-review
description: Review HashiCorp Vault, AWS Secrets Manager, Azure Key Vault and GCP Secret Manager access patterns, policies, rotation and audit logging.
---

# Vault and Secrets Manager Review

Analyze secrets manager controls, access policy, rotation and audit posture.

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
