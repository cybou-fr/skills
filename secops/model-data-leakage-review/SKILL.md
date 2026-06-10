---
name: model-data-leakage-review
description: Review risks of sensitive information disclosure in LLM applications. Use for output leakage, prompt leakage,
  secret exposure, training data leakage, customer data exposure, logs, traces, and AI memory privacy reviews.
---

# Model Data Leakage Review

## Purpose

Assess whether an AI system may disclose sensitive data.

## Leakage channels

- model output;
- prompts;
- system messages;
- tool outputs;
- RAG retrieved documents;
- logs/traces;
- conversation memory;
- eval datasets;
- fine-tuning data;
- analytics events.

## Assessment procedure

1. Identify sensitive data classes.
2. Map where data enters the system.
3. Map where data is stored or logged.
4. Review output redaction.
5. Review memory and retention.
6. Review RAG corpus permissions.
7. Review eval and training datasets.
8. Verify no secrets appear in prompts or outputs.

## Controls

- redaction;
- secrets scanning;
- PII minimization;
- retention limits;
- access controls;
- no customer data in test fixtures;
- output sensitive data classifier;
- audit and deletion workflows.

## Output

```md
## Model data leakage review
System:
Sensitive data classes:
Leakage channels:
Findings:
Evidence:
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
