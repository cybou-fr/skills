---
name: session-token-and-cookie-review
description: Review session tokens, cookies and refresh tokens for leakage, lifetime, scope, revocation needs and evidence
  redaction.
---

# Session Token and Cookie Review

Assess token/cookie leakage safely; revocation requires approval.

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
