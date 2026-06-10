---
name: web-artifact-builder
description: Plan and build self-contained web artifacts, landing pages, demos, interactive prototypes, and static UI deliverables
  with security and deployment constraints.
---

# Web Artifact Builder

## Procedure

1. Clarify target artifact: landing page, demo, prototype, component, dashboard.
2. Choose minimal stack.
3. Keep artifact self-contained when possible.
4. Avoid secrets and external trackers by default.
5. Include accessibility and responsive checks.
6. Prepare deployment notes if needed.

## Safety

Do not embed credentials, private API keys, or tracking scripts without approval.

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
