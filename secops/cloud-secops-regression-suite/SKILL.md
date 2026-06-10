---
name: cloud-secops-regression-suite
description: Maintain Cloud SecOps tests for AWS, Azure and GCP alert triage, IAM review, logging control-plane checks and
  containment boundaries.
---

# Cloud SecOps Regression Suite

Tests provider-specific Cloud SecOps workflows.

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
