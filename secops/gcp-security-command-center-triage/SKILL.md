---
name: gcp-security-command-center-triage
description: Triage GCP Security Command Center findings, affected assets, source properties, severity, mute status and remediation options.
---

# GCP Security Command Center Triage

Analyze SCC findings and prepare safe response plan.

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
