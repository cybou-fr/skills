#!/usr/bin/env python3
"""
Validate CYBOU DevOps/SecOps Agent Skills Pack.

Checks:
- every SKILL.md has valid AgentSkills-style frontmatter;
- registry paths exist;
- registry id matches SKILL.md frontmatter name;
- related skills exist;
- output templates exist;
- required tools are declared or known external tools;
- policy regex compiles;
- test required skills exist;
- test files follow expected structure.
"""

from pathlib import Path
import re
import sys
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_RISKS = {"low", "medium", "high", "critical"}
ALLOWED_MODES = {"read_only", "guarded", "draft_only", "approval_required"}
KNOWN_TOOLS = {
    "shell", "kubectl", "terraform", "docker", "git", "database", "cloud_cli",
    "package_manager", "http_fetch", "helm", "ci_logs_reader", "log_reader",
    "metrics_reader", "backup_api", "repo_api", "secret_scanner", "secrets_manager",
    "vulnerability_scanner", "siem", "github_api", "package_registry", "pentest", "ai_security"
}

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data

def main():
    errors = []
    warnings = []

    registry = load_yaml(ROOT / "registry.yaml")
    templates = load_yaml(ROOT / "output_templates.yaml").get("templates", {})
    tool_policies = load_yaml(ROOT / "tool_policies.yaml")
    external_tools_path = ROOT / "external_tools.yaml"
    if external_tools_path.exists():
        ext = load_yaml(external_tools_path)
        for t in ext.get("tools", {}).keys():
            KNOWN_TOOLS.add(t)


    skill_ids = {s["id"] for s in registry.get("skills", [])}

    # SKILL.md validation
    skill_files = list(ROOT.rglob("SKILL.md"))
    for sf in skill_files:
        fm = frontmatter(sf)
        if not fm:
            errors.append(f"Missing/bad frontmatter: {sf.relative_to(ROOT)}")
            continue
        if "name" not in fm or "description" not in fm:
            errors.append(f"Missing name/description: {sf.relative_to(ROOT)}")
        if "name" in fm and not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", fm["name"]):
            errors.append(f"Bad skill name: {fm['name']} in {sf.relative_to(ROOT)}")

    # Registry validation
    for s in registry.get("skills", []):
        sid = s.get("id")
        path = ROOT / s.get("path", "")
        if not path.exists():
            errors.append(f"Registry path missing: {sid} -> {s.get('path')}")
            continue
        fm = frontmatter(path)
        if fm and fm.get("name") != sid:
            errors.append(f"Registry id != SKILL.md name: {sid} != {fm.get('name')} ({s.get('path')})")

        if s.get("default_risk") not in ALLOWED_RISKS:
            errors.append(f"Invalid default_risk for {sid}: {s.get('default_risk')}")
        if s.get("default_mode") not in ALLOWED_MODES:
            errors.append(f"Invalid default_mode for {sid}: {s.get('default_mode')}")

        tmpl = s.get("output_template")
        if tmpl and tmpl not in templates:
            errors.append(f"Missing output template for {sid}: {tmpl}")

        for rel in s.get("related_skills", []) or []:
            if rel not in skill_ids:
                errors.append(f"Missing related skill for {sid}: {rel}")

        for tool in s.get("requires_tools", []) or []:
            if tool not in KNOWN_TOOLS:
                warnings.append(f"Unknown tool name for {sid}: {tool}")

    # Policy regex validation
    for pf in (ROOT / "policy_rules").glob("*.yaml"):
        data = load_yaml(pf)
        if "tool" not in data or "rules" not in data:
            errors.append(f"Bad policy file structure: {pf.relative_to(ROOT)}")
            continue
        for rule in data.get("rules", []):
            for field in ["id", "match_regex", "decision", "risk"]:
                if field not in rule:
                    errors.append(f"Missing {field} in policy {pf.name}")
            if "match_regex" in rule:
                try:
                    re.compile(rule["match_regex"])
                except Exception as e:
                    errors.append(f"Bad regex {pf.name}:{rule.get('id')}: {e}")

    # tool_policies references
    for tool, info in tool_policies.get("tools", {}).items():
        rule_path = ROOT / info.get("rules", "")
        if not rule_path.exists():
            errors.append(f"tool_policies missing rule file for {tool}: {info.get('rules')}")


    # activity policy validation
    activity_dir = ROOT / "activity_policies"
    if activity_dir.exists():
        for ap in activity_dir.glob("*.yaml"):
            data = load_yaml(ap)
            for field in ["activity", "version", "default", "denied_by_default"]:
                if field not in data:
                    errors.append(f"Missing {field} in activity policy {ap.name}")

    # pentest scope template presence
    pst = ROOT / "templates" / "pentest_scope.yaml"
    if not pst.exists():
        errors.append("Missing templates/pentest_scope.yaml")


    # v4 runtime validation
    for required_path in [
        "runtime/integration_manifest.yaml",
        "autonomy_profiles.yaml",
        "skill_graph.yaml",
        "runtime/decision_enums.yaml",
    ]:
        if not (ROOT / required_path).exists():
            errors.append(f"Missing v4 runtime file: {required_path}")

    # tool adapter validation
    adapter_dir = ROOT / "tool_adapters"
    if adapter_dir.exists():
        for ap in adapter_dir.glob("*.yaml"):
            data = load_yaml(ap)
            for field in ["tool", "version", "adapter_type", "decision_inputs"]:
                if field not in data:
                    errors.append(f"Missing {field} in tool adapter {ap.name}")
    else:
        errors.append("Missing tool_adapters/ directory")

    # scope object examples
    scope_dir = ROOT / "scope_objects"
    if not scope_dir.exists():
        errors.append("Missing scope_objects/ directory")

    # skill graph references
    sg_path = ROOT / "skill_graph.yaml"
    if sg_path.exists():
        sg = load_yaml(sg_path)
        for sid, node in sg.get("skills", {}).items():
            if sid not in skill_ids:
                errors.append(f"Skill graph references unknown skill: {sid}")
            for rel in node.get("related", []) or []:
                if rel not in skill_ids:
                    errors.append(f"Skill graph {sid} related unknown skill: {rel}")
            for before in node.get("always_load_before", []) or []:
                if before not in skill_ids:
                    errors.append(f"Skill graph {sid} always_load_before unknown skill: {before}")


    # v4.2 external tools and runtime schemas
    ext_path = ROOT / "external_tools.yaml"
    if not ext_path.exists():
        errors.append("Missing external_tools.yaml")
    else:
        ext = load_yaml(ext_path)
        for tool_name, tool_info in ext.get("tools", {}).items():
            adapter_path = ROOT / tool_info.get("adapter", "")
            if not adapter_path.exists():
                errors.append(f"External tool {tool_name} missing adapter: {tool_info.get('adapter')}")
    for required_schema in [
        "schemas/tool_adapter.schema.json",
        "schemas/skill_graph.schema.json",
        "schemas/autonomy_profiles.schema.json",
        "schemas/policy_decision.schema.json",
        "schemas/normalized_action.schema.json",
        "schemas/task_state.schema.json",
        "schemas/tool_call_state.schema.json",
    ]:
        if not (ROOT / required_schema).exists():
            errors.append(f"Missing runtime schema: {required_schema}")

    # tests validation
    test_count = 0
    for tf in (ROOT / "tests").glob("*.yaml"):
        data = load_yaml(tf)
        if "scenarios" not in data:
            errors.append(f"Test file missing scenarios: {tf.name}")
            continue
        for scenario in data["scenarios"]:
            test_count += 1
            if "id" not in scenario or "input" not in scenario or "expected" not in scenario:
                errors.append(f"Bad test scenario shape in {tf.name}: {scenario}")
                continue
            for req in scenario.get("expected", {}).get("required_skills", []) or []:
                if req not in skill_ids:
                    errors.append(f"Test {scenario['id']} requires unknown skill: {req}")

    report = {
        "skill_files": len(skill_files),
        "registry_skills": len(skill_ids),
        "output_templates": len(templates),
        "policy_rule_files": len(list((ROOT / "policy_rules").glob("*.yaml"))),
        "test_files": len(list((ROOT / "tests").glob("*.yaml"))),
        "test_scenarios": test_count,
        "activity_policy_files": len(list((ROOT / "activity_policies").glob("*.yaml"))) if (ROOT / "activity_policies").exists() else 0,
        "tool_adapter_files": len(list((ROOT / "tool_adapters").glob("*.yaml"))) if (ROOT / "tool_adapters").exists() else 0,
        "scope_object_files": len(list((ROOT / "scope_objects").glob("*.yaml"))) if (ROOT / "scope_objects").exists() else 0,
        "errors": errors,
        "warnings": warnings,
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
