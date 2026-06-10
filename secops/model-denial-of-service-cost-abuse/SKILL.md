---
name: model-denial-of-service-cost-abuse
description: Assess LLM application exposure to model denial of service, cost harvesting, excessive token usage, recursive
  agent loops, tool-call storms, and resource exhaustion.
---

# Model Denial of Service and Cost Abuse

## Purpose

Review whether an AI system can be overloaded or financially abused.

## Risk patterns

- extremely long inputs;
- recursive agent loops;
- unbounded tool calls;
- large retrieval expansions;
- repeated retries;
- expensive model routes;
- multi-agent loops;
- file expansion bombs;
- prompt chains that trigger high token usage;
- missing rate limits.

## Assessment procedure

1. Identify token and cost budgets.
2. Review maximum input/output limits.
3. Review tool-call limits.
4. Review retry policy.
5. Review recursion/loop limits.
6. Review per-user and per-tenant quotas.
7. Review monitoring and alerts.
8. Use synthetic load estimates, not abusive traffic.

## Controls

- token caps;
- per-user quotas;
- tool call budget;
- recursion limit;
- timeout;
- circuit breakers;
- queue limits;
- anomaly detection;
- cost alerts.

## Output

```md
## Model DoS / cost abuse review
System:
Budget controls:
Risk patterns:
Findings:
Recommended limits:
Monitoring:
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
