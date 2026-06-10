---
name: issue-tracker-workflow
description: Work with issue trackers such as Linear/Jira-style systems: convert notes to issues, prioritize, write acceptance criteria, link implementation tasks, and preserve security boundaries.
---

# Issue Tracker Workflow

## Procedure

1. Identify objective and project.
2. Convert request into clear issue.
3. Add acceptance criteria.
4. Add dependencies and owner if known.
5. Add security/privacy labels if relevant.
6. Do not change external tracker state without approval.

## Output

- issue title;
- description;
- acceptance criteria;
- labels;
- priority rationale.

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
