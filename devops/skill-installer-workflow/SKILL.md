---
name: skill-installer-workflow
description: Safely install or import external Agent Skills into CYBOU: review source, license, safety, compatibility, dependencies, scripts, permissions, and registry integration.
---

# Skill Installer Workflow

## Procedure

1. Identify source repository and skill path.
2. Review license and compatibility.
3. Inspect `SKILL.md`, scripts, resources, and dependencies.
4. Detect unsafe instructions or side effects.
5. Convert to CYBOU adapter if needed.
6. Register with risk, tools, templates, tests.
7. Do not install executable scripts without review.

## Output

- import decision;
- license notes;
- safety review;
- compatibility changes;
- added files.

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
