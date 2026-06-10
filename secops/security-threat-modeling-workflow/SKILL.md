---
name: security-threat-modeling-workflow
description: Create defensive threat models for applications, infrastructure, AI systems, agents, APIs, data flows, and integrations using assets, trust boundaries, threats, controls, and tests.
---

# Security Threat Modeling Workflow

## Procedure

1. Identify system and assets.
2. Map data flows.
3. Identify trust boundaries.
4. Identify threats.
5. Map existing controls.
6. Prioritize gaps.
7. Define security tests.
8. Connect findings to owners.

## Useful threat categories

- spoofing;
- tampering;
- repudiation;
- information disclosure;
- denial of service;
- elevation of privilege;
- prompt/tool injection for AI systems.

## Output

- assets;
- data flows;
- trust boundaries;
- threats;
- controls;
- gaps;
- test plan.

## Required output

End with:
- scope;
- summary;
- artifacts produced or changed;
- checks performed;
- risks or approvals;
- next steps.

## Runtime notes

Follow CYBOU policy, tool adapters, scope objects, approval state, redaction, and audit requirements.

If the task touches production, external publishing, repository writes, credentials, customer data, or third-party services, check policy and request approval before any side effect.
