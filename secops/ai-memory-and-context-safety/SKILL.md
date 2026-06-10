---
name: ai-memory-and-context-safety
description: Review safety of AI memory, context windows, conversation state, user-specific memory, long-term memory, cross-tenant
  memory isolation, and context injection risks.
---

# AI Memory and Context Safety

## Purpose

Assess whether AI memory and context handling can leak data, preserve unsafe instructions, or mix tenant/user state.

## Review areas

- short-term context;
- long-term memory;
- user profile memory;
- tenant isolation;
- tool result memory;
- retrieved context;
- summarization memory;
- deletion/forget workflows;
- prompt injection persistence;
- sensitive data retention.

## Risks

- cross-user memory leakage;
- tenant data mixing;
- malicious instruction persistence;
- secrets stored in memory;
- stale authorization context;
- unbounded retention;
- unsafe summaries.

## Controls

- tenant-scoped memory;
- memory allowlist;
- secret/PII redaction before storage;
- expiration;
- user deletion workflow;
- source labels;
- memory review/audit;
- no tool output auto-memory without filtering.

## Output

```md
## AI memory/context safety review
System:
Memory types:
Isolation model:
Leakage risks:
Persistence risks:
Recommended controls:
Approval required:
```

## Required output

End with:
- assessment scope;
- summary;
- evidence;
- risk level;
- actions taken;
- recommended controls;
- approval required, if any.

## Safety notes

This skill is for defensive AI security assessment and hardening.

Do not generate jailbreak prompts, bypass recipes, exploit payloads, data exfiltration instructions, stealth techniques, credential theft steps, or instructions for evading model safety systems.

When testing is needed, use benign placeholders, synthetic examples, allowlisted test cases, and approved evaluation harnesses.

If a policy rule conflicts with this skill, the policy rule wins.
