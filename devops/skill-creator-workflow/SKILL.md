---
name: skill-creator-workflow
description: Create AgentSkills-compatible skills with SKILL.md frontmatter, clear routing descriptions, instructions, safety boundaries, references, templates, tests, and validation metadata.
---

# Skill Creator Workflow

## Procedure

1. Define the repeatable task.
2. Write `name` and `description` frontmatter.
3. Add activation boundaries.
4. Add step-by-step procedure.
5. Add safety and escalation rules.
6. Add output template.
7. Add tests.
8. Register in `registry.yaml`.

## Quality checks

- description is specific;
- no unsafe side effects;
- examples are safe;
- related skills are linked;
- validation passes.

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
