#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Create a new Cybou skill template and register it in registry.yaml.")
    parser.add_argument("--id", required=True, help="Skill ID (e.g., custom-service-setup)")
    parser.add_argument("--category", required=True, choices=["core", "devops", "secops", "productivity"], help="Skill category")
    parser.add_argument("--description", required=True, help="English description of the skill")
    parser.add_argument("--description-fr", help="Optional French description of the skill")
    parser.add_argument("--triggers", required=True, help="Comma-separated triggers list")
    parser.add_argument("--risk", default="low", choices=["low", "medium", "high", "critical"], help="Risk level")

    args = parser.parse_args()

    skills_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(skills_dir, args.category, args.id)
    skill_file = os.path.join(target_dir, "SKILL.md")
    registry_file = os.path.join(skills_dir, "registry.yaml")

    # 1. Check if registry.yaml exists
    if not os.path.isfile(registry_file):
        print(f"Error: registry.yaml not found at {registry_file}", file=sys.stderr)
        sys.exit(1)

    # 2. Check if skill already exists on disk
    if os.path.exists(target_dir):
        print(f"Error: Skill directory already exists at {target_dir}", file=sys.stderr)
        sys.exit(1)

    # 3. Create target directory
    os.makedirs(target_dir, exist_ok=True)

    # 4. Generate SKILL.md boilerplate
    triggers_list = [t.strip() for t in args.triggers.split(",") if t.strip()]
    triggers_yaml = "\n".join(f"  - {t}" for t in triggers_list)

    description_fr_line = ""
    if args.description_fr:
        description_fr_line = f"description_fr: {args.description_fr}\n"

    skill_template = f"""---
name: {args.id}
description: {args.description}
{description_fr_line}category: {args.category}
triggers:
{triggers_yaml}
risk: {args.risk}
---

# {args.id.replace('-', ' ').title()}

## 1. Use when

Use this skill when ...

## 2. Operating mode

Default mode: guarded.

## 3. Risk mapping

### low
- ...

### medium
- ...

### high
- ...

## 4. Preferred tool order

1. ...

## 5. Command templates

```bash
# Provide typical command templates here
```

## 6. Stop / block conditions

Stop if ...

## 7. Verify-before-finish

Finish only after ...
"""

    with open(skill_file, "w") as f:
        f.write(skill_template)

    print(f"✓ Created skill template at {skill_file}")

    # 5. Append to registry.yaml before activity_policies:
    with open(registry_file, "r") as f:
        registry_content = f.read()

    target_marker = "activity_policies:"
    if target_marker not in registry_content:
        print("Warning: 'activity_policies:' marker not found in registry.yaml. Skill not appended to registry.", file=sys.stderr)
        sys.exit(0)

    # Format the registry entry
    triggers_registry = "\n".join(f"  - {t}" for t in triggers_list)
    registry_entry = f"""- id: {args.id}
  path: {args.category}/{args.id}/SKILL.md
  category: {args.category}
  triggers:
{triggers_registry}
  default_risk: {args.risk}
  default_mode: guarded
  requires_tools: []
  input_types:
  - user_request
  output_template: generic_task_report
  related_skills: []
  do_not_use_for:
  - general education
  autonomy_level: 1
"""

    parts = registry_content.split(target_marker, 1)
    new_registry_content = parts[0] + registry_entry + target_marker + parts[1]

    with open(registry_file, "w") as f:
        f.write(new_registry_content)

    print(f"✓ Registered skill '{args.id}' in registry.yaml")
    print(f"\nNext step: Run './target/debug/cybou vet-skills' or stage files in git.")

if __name__ == "__main__":
    main()
