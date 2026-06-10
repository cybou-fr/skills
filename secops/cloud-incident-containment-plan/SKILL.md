---
name: cloud-incident-containment-plan
description: Draft safe cloud incident containment plans with approval boundaries for key revocation, instance isolation, security group changes and identity disablement.
---

# Cloud Incident Containment Plan

Produce read-only containment plan and mark every mutating action as approval-required.

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
