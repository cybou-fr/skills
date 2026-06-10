---
name: azure-activity-log-triage
description: 'Triage Azure Activity Log security events: role assignments, key vault access, NSG changes, defender alerts
  and diagnostic setting changes.'
---

# Azure Activity Log Triage

Review Azure Activity Log events for control-plane security anomalies.

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
