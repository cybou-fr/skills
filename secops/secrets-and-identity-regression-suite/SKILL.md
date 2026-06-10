---
name: secrets-and-identity-regression-suite
description: Maintain tests for identity, secrets and key-management triage, secret classification, redaction, approval boundaries and hard-deny behavior.
---

# Secrets and Identity Regression Suite

Tests secret detection, identity risk triage, KMS review and approval boundaries.

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
