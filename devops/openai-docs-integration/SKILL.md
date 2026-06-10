---
name: openai-docs-integration
description: 'Design OpenAI API integration workflows safely: docs lookup, API usage planning, auth handling, model/tool configuration,
  evals, logging, cost controls, and migration notes.'
---

# OpenAI Docs Integration

## Procedure

1. Identify API/product area.
2. Use current official docs when implementation details matter.
3. Plan auth and key management.
4. Define model/tool usage.
5. Add retries, rate limits, cost controls.
6. Add eval and logging strategy.
7. Redact API keys and sensitive outputs.

## Safety

Do not expose API keys or customer data. Use current docs for API-specific details.

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
