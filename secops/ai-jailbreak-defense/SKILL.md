---
name: ai-jailbreak-defense
description: Assess and harden defenses against jailbreak attempts and direct prompt injection in LLM applications. Use for defensive AI security reviews, safety policy testing with benign fixtures, instruction hierarchy review, refusal consistency, and jailbreak-resilience reporting without generating bypass prompts.
---

# AI Jailbreak Defense

## Purpose

Defensively assess whether an LLM application resists attempts to bypass its safety rules or instruction hierarchy.

## Default mode

Benign evaluation and design review only.

## Do not

- generate jailbreak prompts;
- optimize bypass strings;
- provide evasion tactics;
- test third-party systems without authorization;
- include harmful content in examples;
- automate adversarial prompt search.

## Safe assessment procedure

1. Confirm system owner and assessment scope.
2. Review instruction hierarchy:
   - system/runtime policy;
   - tool policy;
   - developer instructions;
   - user request;
   - retrieved content.
3. Check whether the app separates trusted instructions from untrusted data.
4. Use benign placeholder test cases only.
5. Evaluate whether the model:
   - preserves safety policy;
   - refuses unsafe transformations;
   - asks for scope/approval when needed;
   - avoids executing tool instructions from untrusted content.
6. Record failure modes without publishing bypass content.
7. Recommend controls.

## Defensive controls

- strict tool gating;
- prompt/content boundary markers;
- untrusted content labeling;
- output moderation;
- scoped approvals;
- role and capability separation;
- jailbreak regression tests;
- audit logs for refusal overrides.

## Output

```md
## AI jailbreak defense assessment
System:
Scope:
Instruction hierarchy reviewed:
Benign tests used:
Observed weaknesses:
Risk:
Recommended controls:
Regression tests:
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
