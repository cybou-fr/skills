#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    errors = []
    warnings = []
    registry = load_yaml(ROOT / "registry.yaml")
    templates = load_yaml(ROOT / "output_templates.yaml").get("templates", {})
    decision_mapping = load_yaml(ROOT / "integration" / "decision_mapping.yaml").get("mapping", {})
    tool_classes = load_yaml(ROOT / "integration" / "tool_classes.yaml").get("classes", {})
    known_tools = set()
    for tools in tool_classes.values():
        known_tools.update(tools)

    skills = registry.get("skills", [])
    skill_paths = set()

    for skill in skills:
        sid = skill.get("id")
        path = skill.get("path")
        if not sid:
            errors.append("registry skill missing id")
            continue
        if not path:
            errors.append(f"{sid}: missing path")
            continue
        fp = ROOT / path
        if not fp.exists():
            errors.append(f"{sid}: missing SKILL.md path {path}")
            continue
        skill_paths.add(path)
        text = fp.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"{sid}: missing frontmatter")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append(f"{sid}: malformed frontmatter block")
            continue
        try:
            meta = yaml.safe_load(parts[1]) or {}
        except Exception as e:
            errors.append(f"{sid}: invalid YAML frontmatter: {e}")
            continue
        if not meta.get("name"):
            errors.append(f"{sid}: frontmatter missing name")
        if not meta.get("description"):
            errors.append(f"{sid}: frontmatter missing description")
        if meta.get("name") != sid:
            warnings.append(f"{sid}: frontmatter name differs from registry id: {meta.get('name')}")
        ot = skill.get("output_template")
        if ot and ot not in templates:
            errors.append(f"{sid}: missing output template {ot}")
        for t in skill.get("requires_tools", []) or []:
            if t not in known_tools:
                errors.append(f"{sid}: unknown required tool {t}")

    actual_skill_files = {str(p.relative_to(ROOT)) for p in ROOT.rglob("SKILL.md")}
    unregistered = sorted(actual_skill_files - skill_paths)
    if unregistered:
        errors.append(f"unregistered SKILL.md files: {unregistered[:10]}")

    for p in (ROOT / "policy_rules").glob("*.yaml"):
        data = load_yaml(p)
        for rule in data.get("rules", []):
            dec = rule.get("decision")
            if dec and dec not in decision_mapping:
                errors.append(f"{p.relative_to(ROOT)}:{rule.get('id')}: unknown decision {dec}")

    forbidden = []
    forbidden.extend(ROOT.rglob("*.pyc"))
    forbidden.extend([p for p in ROOT.rglob("__pycache__") if p.is_dir()])
    if forbidden:
        errors.append(f"forbidden generated files present: {[str(p.relative_to(ROOT)) for p in forbidden[:10]]}")

    legacy_dirs = [
        "runtime_prototype", "reference_prototype", "tests", "normalizer_tests", "approval_tests",
        "audit_tests", "sandbox_tests", "detection_tests", "cloud_secops_tests",
        "identity_secrets_tests", "forensics_tests"
    ]
    present_legacy = [d for d in legacy_dirs if (ROOT / d).exists()]
    if present_legacy:
        errors.append(f"legacy dirs should not be present in v6.1 clean pack: {present_legacy}")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "registry_skills": len(skills),
        "skill_files": len(actual_skill_files),
        "output_templates": len(templates),
        "policy_rule_files": len(list((ROOT / "policy_rules").glob("*.yaml"))),
        "eval_files": len(list((ROOT / "evals").rglob("*.yaml"))),
        "known_tools": len(known_tools),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
