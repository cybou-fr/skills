---
name: oauth-app-consent-review
description: Review OAuth/OIDC app consent, delegated permissions, high-risk scopes, publisher trust, redirect URIs and consent grant anomalies.
---

# OAuth App Consent Review

Analyze risky OAuth app consents and delegated permissions. Consent removal requires approval.

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
