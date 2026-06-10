---
name: privileged-access-review
description: Review privileged access across AWS IAM, Azure RBAC/Entra roles, GCP IAM, SaaS admins and break-glass identities.
---

# Privileged Access Review

Identify high-risk admin paths, break-glass gaps, direct grants and missing MFA/PIM/JIT controls.

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
