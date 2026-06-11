#!/usr/bin/env python3
from pathlib import Path
import yaml, json, re

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    errors = []
    warnings = []

    forbidden_dirs = ["patches", "rust_scaffold", "cybou-core", "cybou_core"]
    for d in forbidden_dirs:
        if (ROOT / d).exists():
            errors.append(f"forbidden runtime implementation directory present: {d}")

    forbidden_suffixes = [".rs"]
    forbidden_files = []
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix in forbidden_suffixes:
            forbidden_files.append(str(p.relative_to(ROOT)))
    if forbidden_files:
        errors.append(f"forbidden Rust implementation files present: {forbidden_files}")

    required_docs = [
        "CONTRIBUTING.md",
        "SECURITY.md",
        "SKILL_AUTHORING_GUIDE.md",
        "RELEASE.md",
        "docs/REPOSITORY_BOUNDARIES.md",
        "docs/SKILL_CORPUS_FORMAT.md",
        "docs/PUBLIC_REPOSITORY_CLEANUP_V6_8.md",
    ]
    for rel in required_docs:
        if not (ROOT / rel).exists():
            errors.append(f"missing public repo document: {rel}")

    registry = load_yaml(ROOT / "registry.yaml")
    runtime_ids = [s.get("id") for s in registry.get("skills", []) if str(s.get("id", "")).startswith("runtime-")]
    if runtime_ids:
        errors.append(f"runtime-* skill ids remain: {runtime_ids[:10]}")

    cybou_core_ids = [s.get("id") for s in registry.get("skills", []) if str(s.get("id", "")).startswith("cybou-core-")]

    for skill in registry.get("skills", []):
        sid = skill.get("id")
        path = skill.get("path")
        if not sid or not path:
            errors.append(f"malformed skill registry entry: {skill}")
            continue
        fp = ROOT / path
        if not fp.exists():
            errors.append(f"{sid}: missing path {path}")
            continue
        text = fp.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"{sid}: missing frontmatter")
            continue
        try:
            meta = yaml.safe_load(text.split("---", 2)[1]) or {}
        except Exception as e:
            errors.append(f"{sid}: invalid frontmatter: {e}")
            continue
        if meta.get("name") != sid:
            errors.append(f"{sid}: frontmatter name mismatch: {meta.get('name')}")

    package = load_yaml(ROOT / "package.yaml")
    if package.get("repository_role") != "skills_corpus_only":
        errors.append("package.repository_role must be skills_corpus_only")
    if package.get("contains_runtime_code") is not False:
        errors.append("package.contains_runtime_code must be false")
    if package.get("cybou_core_patches") is not False:
        errors.append("package.cybou_core_patches must be false")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "skills": len(registry.get("skills", [])),
        "cybou_core_prefixed_skills": len(cybou_core_ids),
        "forbidden_rust_files": len(forbidden_files),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
