---
name: gcp-audit-log-triage
description: Triage Google Cloud Audit Logs: IAM policy changes, service account key creation, workload identity misuse, firewall changes and logging sink tampering.
---

# GCP Audit Log Triage

Review GCP Admin Activity and Data Access logs for security events.

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
