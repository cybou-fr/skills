---
name: cloud-logging-control-plane-review
description: 'Review cloud logging/audit control-plane integrity: CloudTrail, Azure diagnostic settings, GCP audit logs, sinks,
  retention and tampering signals.'
---

# Cloud Logging Control Plane Review

Check if audit logging is enabled, complete, protected and tamper-evident.

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
