---
name: cli-creator-workflow
description: Design and scaffold command-line tools safely with command structure, argument parsing, help text, config, tests,
  packaging, and security review.
---

# CLI Creator Workflow

## Procedure

1. Define command goals.
2. Specify commands/subcommands.
3. Define arguments and config.
4. Add safe defaults.
5. Add dry-run for risky operations.
6. Add tests and examples.
7. Add packaging notes.

## Safety

- no secrets in CLI output;
- no destructive default action;
- clear confirmation for write/delete operations.

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
