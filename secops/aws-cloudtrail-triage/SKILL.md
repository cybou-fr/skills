---
name: aws-cloudtrail-triage
description: Triage AWS CloudTrail security events: suspicious AssumeRole, ConsoleLogin, IAM changes, access key usage, CloudTrail tampering and region anomalies.
---

# AWS CloudTrail Triage

Review CloudTrail security events and produce an investigation plan without mutating cloud resources.

Focus on identity, source IP, user agent, region, action, resource, MFA, error codes and session context.

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
