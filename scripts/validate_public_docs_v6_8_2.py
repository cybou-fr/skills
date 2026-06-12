#!/usr/bin/env python3
from pathlib import Path
import json, yaml
ROOT = Path(__file__).resolve().parents[1]
def main():
    errors=[]; warnings=[]
    required=["README.md","CONTRIBUTING.md","SECURITY.md","SKILL_AUTHORING_GUIDE.md","RELEASE.md","docs/VALIDATION_GUIDE.md","docs/PUBLIC_RELEASE_CHECKLIST.md",".github/workflows/validate.yml","scripts/validate_all.py","examples/skills/minimal/EXAMPLE_SKILL.md","examples/evals/minimal_eval.yaml","examples/policies/minimal_policy.yaml","examples/signing/unsigned_dev_release.md"]
    for rel in required:
        if not (ROOT/rel).exists(): errors.append(f"missing public docs/CI artifact: {rel}")
    wf=ROOT/'.github/workflows/validate.yml'
    if wf.exists():
        text=wf.read_text(encoding='utf-8')
        if 'scripts/validate_all.py' not in text: errors.append('validate.yml must run scripts/validate_all.py')
        if 'python-version' not in text: warnings.append('validate.yml does not explicitly set python-version')
    skill=ROOT/'examples/skills/minimal/EXAMPLE_SKILL.md'
    if skill.exists():
        text=skill.read_text(encoding='utf-8')
        if not text.startswith('---'): errors.append('minimal example skill missing frontmatter')
        else:
            meta=yaml.safe_load(text.split('---',2)[1]) or {}
            for key in ['name','description']:
                if not meta.get(key): errors.append(f'minimal example skill missing frontmatter key: {key}')
    readme=(ROOT/'README.md').read_text(encoding='utf-8') if (ROOT/'README.md').exists() else ''
    if 'does **not** contain Cybou runtime implementation code' not in readme: errors.append('README must state the no-runtime-code boundary')
    release=(ROOT/'RELEASE.md').read_text(encoding='utf-8') if (ROOT/'RELEASE.md').exists() else ''
    if 'validate_all.py' not in release: errors.append('RELEASE.md must mention validate_all.py')
    print(json.dumps({'status':'pass' if not errors else 'fail','errors':errors,'warnings':warnings,'required_artifacts':len(required)}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
