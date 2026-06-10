---
name: cloud-asset-exposure-review
description: Review cloud asset exposure: public buckets, public IPs, security groups/firewall rules, load balancers, storage ACLs and exposed secrets.
---

# Cloud Asset Exposure Review

Analyze exposure posture using read-only evidence.

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
