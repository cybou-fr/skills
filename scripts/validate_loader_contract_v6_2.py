#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json, re

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def main():
    errors = []
    warnings = []

    manifest_path = ROOT / "integration" / "loader_manifest.yaml"
    if not manifest_path.exists():
        errors.append("missing integration/loader_manifest.yaml")
        print(json.dumps({"status":"fail","errors":errors,"warnings":warnings}, indent=2))
        return 1

    manifest = load_yaml(manifest_path)
    for req in manifest.get("required_files", []):
        if not (ROOT / req).exists():
            errors.append(f"missing required file: {req}")

    for d in manifest.get("non_canonical_dirs_forbidden", []):
        if (ROOT / d).exists():
            errors.append(f"forbidden directory present: {d}")

    for schema in [
        "skill_frontmatter.schema.json",
        "registry.schema.json",
        "policy_rule.schema.json",
        "tool_classes.schema.json",
        "eval_scenario.schema.json",
        "loader_manifest.schema.json",
    ]:
        p = ROOT / "schemas" / schema
        if not p.exists():
            errors.append(f"missing schema: schemas/{schema}")
        else:
            try:
                load_json(p)
            except Exception as e:
                errors.append(f"invalid schema JSON {schema}: {e}")

    registry = load_yaml(ROOT / "registry.yaml")
    templates = load_yaml(ROOT / "output_templates.yaml").get("templates", {})
    decision_mapping = load_yaml(ROOT / "integration" / "decision_mapping.yaml").get("mapping", {})
    tool_classes = load_yaml(ROOT / "integration" / "tool_classes.yaml").get("classes", {})
    known_tools = set()
    for tools in tool_classes.values():
        known_tools.update(tools)

    skill_ids = set()
    skill_paths = set()
    for skill in registry.get("skills", []):
        sid = skill.get("id")
        if not sid:
            errors.append("registry skill missing id")
            continue
        if sid in skill_ids:
            errors.append(f"duplicate skill id: {sid}")
        skill_ids.add(sid)

        path = skill.get("path")
        if not path:
            errors.append(f"{sid}: missing path")
            continue
        skill_paths.add(path)
        fp = ROOT / path
        if not fp.exists():
            errors.append(f"{sid}: missing path {path}")
            continue
        text = fp.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"{sid}: missing YAML frontmatter")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append(f"{sid}: malformed YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(parts[1]) or {}
        except Exception as e:
            errors.append(f"{sid}: invalid YAML frontmatter: {e}")
            continue
        if meta.get("name") != sid:
            errors.append(f"{sid}: frontmatter name must equal registry id; got {meta.get('name')}")
        if not isinstance(meta.get("description"), str) or len(meta.get("description")) < 8:
            errors.append(f"{sid}: missing/too short description")
        ot = skill.get("output_template")
        if ot and ot not in templates:
            errors.append(f"{sid}: unknown output_template {ot}")
        for tool in skill.get("requires_tools", []) or []:
            if tool not in known_tools:
                errors.append(f"{sid}: unclassified required tool {tool}")

    actual_skill_paths = {str(p.relative_to(ROOT)) for p in ROOT.rglob("SKILL.md")}
    for extra in sorted(actual_skill_paths - skill_paths):
        errors.append(f"unregistered skill file: {extra}")

    for p in (ROOT / "policy_rules").glob("*.yaml"):
        data = load_yaml(p)
        for rule in data.get("rules", []):
            dec = rule.get("decision")
            if dec and dec not in decision_mapping:
                errors.append(f"{p.relative_to(ROOT)}:{rule.get('id')}: unknown decision {dec}")

    pyc = list(ROOT.rglob("*.pyc"))
    if pyc:
        errors.append(f"python bytecode present: {[str(p.relative_to(ROOT)) for p in pyc[:10]]}")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "registry_skills": len(registry.get("skills", [])),
        "skill_files": len(actual_skill_paths),
        "output_templates": len(templates),
        "known_tools": len(known_tools),
        "policy_rule_files": len(list((ROOT / "policy_rules").glob("*.yaml"))),
        "eval_files": len(list((ROOT / "evals").rglob("*.yaml"))),
        "schemas": len(list((ROOT / "schemas").glob("*.json"))),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
