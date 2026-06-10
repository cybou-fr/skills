---
name: ai-evaluation-and-redteam-reporting
description: Create defensive AI security evaluation and red-team reports without revealing bypass content. Use for summarizing test coverage, failure modes, severity, controls, regression cases, and remediation status.
---

# AI Evaluation and Red-team Reporting

## Purpose

Produce useful defensive reports from AI security testing.

## Do not include

- jailbreak prompts;
- bypass recipes;
- harmful payloads;
- real secrets;
- customer data;
- third-party confidential data.

## Report sections

- system under test;
- scope;
- test categories;
- methodology;
- safety constraints;
- findings;
- severity;
- evidence summary;
- controls tested;
- failed controls;
- remediation plan;
- regression tests;
- residual risk.

## Evidence style

Use abstracted descriptions:

```text
A benign instruction-like marker in an untrusted document was incorrectly treated as an instruction.
```

Avoid publishing exploit strings.

## Output

```md
## AI security evaluation report
System:
Scope:
Test categories:
Findings:
Severity summary:
Controls:
Regression tests:
Remediation:
Residual risk:
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
