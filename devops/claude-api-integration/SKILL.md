---
name: claude-api-integration
description: Design Claude API integration workflows safely: API usage planning, key handling, tool/skill integration, evals, logging, cost controls, and migration notes.
---

# Claude API Integration

## Procedure

1. Identify API use case.
2. Use current official docs when implementation details matter.
3. Plan auth and key management.
4. Define tool/skill usage.
5. Add retries, rate limits, and cost controls.
6. Add eval and logging strategy.
7. Redact secrets.

## Safety

Do not expose API keys, system prompts, or customer data.

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
