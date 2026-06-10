---
name: mcp-server-builder
description: Design and scaffold MCP-style server integrations safely: tool definitions, resource contracts, auth model, input validation, logging, rate limits, and test plan.
---

# MCP Server Builder

## Procedure

1. Define use case and resources/tools.
2. Specify tool schemas.
3. Define auth and permission model.
4. Add validation and redaction.
5. Define audit logging.
6. Provide test cases.
7. Keep dangerous operations approval-gated.

## Safety

MCP tools can expose sensitive data or actions. Use least privilege and explicit scopes.

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
