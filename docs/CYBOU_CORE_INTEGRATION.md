# Cybou Core Integration

This pack is an external skills/policies/templates/evals corpus for the existing Cybou Rust architecture.

## Target runtime

```text
cybou-core -> host runtime, worker, immunity, memory, TUI, MicroVM orchestration
cybou-guest -> daemon inside Debian MicroVM
cybou-proto -> host↔guest protocol and framed codec
```

## Correct chain

```text
Task
  -> SkillLibrary selects compact metadata
  -> decision.rs adds relevant hints
  -> Brain returns CybouDecision
  -> immunity.rs evaluates command
  -> approval.rs asks operator if required
  -> risk.rs / dryrun.rs / snapshot.rs apply controls
  -> GuestExecutor sends command over vsock
  -> cybou-guest executes inside MicroVM
  -> AgentEvent stream
  -> audit.rs + memory learning
```

## What this pack must not do

- execute tools directly;
- replace MicroVM isolation;
- replace `immunity.rs`;
- replace `approval.rs`;
- replace `audit.rs`.

## Main integration points

| Pack | Cybou |
|---|---|
| registry.yaml | memory/skills.rs |
| SKILL.md frontmatter | compact metadata |
| SKILL.md body | vetted on-demand excerpt |
| policy_rules | immunity.rs / risk.rs |
| activity_policies | decision.rs constitution |
| evals | Testing-as-Learning |
