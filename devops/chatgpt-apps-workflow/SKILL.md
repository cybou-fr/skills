---
name: chatgpt-apps-workflow
description: Plan ChatGPT app/integration workflows with manifest, auth, data boundaries, tool safety, UI behavior, testing,
  deployment, and security review.
---

# ChatGPT Apps Workflow

## Procedure

1. Define app purpose.
2. Define data flows and auth.
3. Define tool calls and permissions.
4. Add privacy and retention rules.
5. Add tests and evals.
6. Review app UX and error handling.
7. Prepare deployment checklist.

## Safety

Apps can expose user data and external tools. Use least privilege and approval gates.

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
