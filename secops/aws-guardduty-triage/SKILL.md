---
name: aws-guardduty-triage
description: Triage AWS GuardDuty findings with severity, affected resource, evidence, likely attack path and safe containment
  plan.
---

# AWS GuardDuty Triage

Review GuardDuty findings and produce a safe SOC investigation plan.

Do not suppress/archive findings or block resources without approval.

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
