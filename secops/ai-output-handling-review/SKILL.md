---
name: ai-output-handling-review
description: Review insecure output handling risks when LLM outputs are passed to code, shell, SQL, HTML, browsers, tickets, email, CI/CD, or other tools. Use for output validation and downstream execution safety.
---

# AI Output Handling Review

## Purpose

Assess whether AI-generated output can cause downstream security issues.

## Risky sinks

- shell;
- SQL;
- HTML/Markdown rendering;
- browser automation;
- CI/CD config;
- Terraform/Kubernetes manifests;
- code execution;
- emails/messages;
- tickets;
- API calls;
- file writes.

## Assessment procedure

1. Identify where model output goes.
2. Classify sinks by risk.
3. Check validation/sanitization.
4. Check approval gates.
5. Check escaping/encoding.
6. Check dry-run behavior.
7. Check audit logs.
8. Check rollback.

## Controls

- output schema validation;
- command allowlists;
- sandbox execution;
- human approval;
- escaping/encoding;
- SQL parameterization;
- safe renderers;
- no auto-execute for high-risk outputs.

## Output

```md
## AI output handling review
System:
Output sinks:
High-risk sinks:
Validation:
Approval gates:
Findings:
Recommended controls:
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
