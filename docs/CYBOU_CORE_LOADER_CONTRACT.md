# Cybou Core Loader Contract v1

CIP039 Phase 1 needs a strict loader contract so `cybou-core` can consume the external skills repository safely.

## Purpose

The loader contract defines what Cybou may read from this pack before any skill body is trusted.

## Default rule

```text
Load metadata first.
Do not load full skill bodies by default.
```

## Phase 1 loader algorithm

```text
1. Open integration/loader_manifest.yaml.
2. Verify required files exist.
3. Reject forbidden legacy/runtime directories.
4. Load registry.yaml.
5. For every registry skill:
   - verify path exists;
   - parse SKILL.md frontmatter as strict YAML;
   - require name + description;
   - verify frontmatter name == registry id;
   - verify output_template exists;
   - verify requires_tools are classified in integration/tool_classes.yaml.
6. Load output_templates.yaml.
7. Load integration/decision_mapping.yaml.
8. Validate all policy rule decisions are known.
9. Emit compact metadata only to SkillLibrary.
10. Keep full body inaccessible until SkillVetter accepts it.
```

## Compact metadata structure

```rust
pub struct SkillMetadata {
    pub id: String,
    pub path: String,
    pub name: String,
    pub description: String,
    pub category: SkillCategory,
    pub triggers: Vec<String>,
    pub default_risk: RiskLevel,
    pub default_mode: String,
    pub requires_tools: Vec<String>,
    pub output_template: Option<String>,
    pub trust_level: SkillTrustLevel,
}
```

## Trust defaults

```text
skills.enabled = false
allow_full_body = false
require_vetting = true
```

## Loader failure policy

The loader should fail closed for:

```text
missing registry.yaml
invalid YAML frontmatter
missing SKILL.md path
missing output template
unknown tool class
unknown policy decision
forbidden runtime directory
*.pyc / __pycache__
```

## Runtime boundary

The loader never grants execution permission. Runtime authority remains:

```text
immunity.rs -> approval.rs -> GuestExecutor -> MicroVM
```
