---
name: cloud-iam-least-privilege-diff
description: Create least-privilege review and diff plan for AWS IAM, Azure RBAC/Entra roles and GCP IAM bindings.
---

# Cloud IAM Least Privilege Diff

Compare current permissions to required actions and propose least-privilege deltas.

## Runtime enforcement rule

This skill belongs to Cloud SecOps.

Cloud actions must be read-only by default. Any action that changes IAM, disables security controls, suppresses findings, modifies logging, changes keys/secrets, blocks production traffic, quarantines resources, or deletes evidence requires explicit approval or must be denied by policy.

## Required output

End with:

- cloud provider;
- account/subscription/project scope;
- finding/event summary;
- identity/resource impacted;
- evidence to collect;
- risk/severity;
- recommended read-only next steps;
- approval-required actions.
