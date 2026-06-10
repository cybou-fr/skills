---
name: screenshot-analysis-workflow
description: Analyze screenshots and UI captures for product, security, documentation, error triage, visual evidence, and
  artifact extraction without exposing sensitive information.
---

# Screenshot Analysis Workflow

## Use for

- UI review;
- error screenshots;
- security evidence;
- design feedback;
- documentation;
- visual extraction.

## Procedure

1. Identify screenshot type and context.
2. Extract visible text only when needed.
3. Note uncertain visual details.
4. Redact secrets, tokens, usernames, emails, and customer data.
5. Connect screenshot evidence to the task.
6. Recommend next safe diagnostic step.

## Safety

Screenshots often contain secrets and PII. Redact before reporting.

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
