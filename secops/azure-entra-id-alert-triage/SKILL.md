---
name: azure-entra-id-alert-triage
description: Triage Microsoft Entra ID identity alerts: impossible travel, risky sign-in, MFA fatigue, consent grant, app credential and privilege role changes.
---

# Azure / Entra ID Alert Triage

Review Entra ID sign-in and audit signals, focusing on identity compromise patterns.

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
