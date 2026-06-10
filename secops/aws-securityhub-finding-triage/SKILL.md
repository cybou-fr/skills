---
name: aws-securityhub-finding-triage
description: Triage AWS Security Hub findings, correlate with CloudTrail/GuardDuty and produce severity-adjusted remediation
  plan.
---

# AWS Security Hub Finding Triage

Analyze Security Hub findings and correlate with evidence.

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
