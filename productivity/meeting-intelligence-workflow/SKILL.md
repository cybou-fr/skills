---
name: meeting-intelligence-workflow
description: Convert meeting notes/transcripts into summaries, decisions, action items, owners, risks, follow-ups, and structured knowledge without exposing sensitive data.
---

# Meeting Intelligence Workflow

## Procedure

1. Identify meeting purpose.
2. Extract decisions.
3. Extract action items and owners.
4. Capture risks and blockers.
5. Identify unanswered questions.
6. Produce follow-up draft if needed.

## Safety

Meeting content may include confidential business information. Redact sensitive data if sharing.

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
