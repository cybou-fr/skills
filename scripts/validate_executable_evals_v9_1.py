#!/usr/bin/env python3
from pathlib import Path
import sys
try:
    import yaml
except Exception as exc:
    raise SystemExit('PyYAML required: python3 -m pip install pyyaml') from exc
p=Path('evals/v9/external_devops_selection.yaml')
data=yaml.safe_load(p.read_text(encoding='utf-8')) or {}
errors=[]
if data.get('schema')!='executable_matcher_v1': errors.append('schema must be executable_matcher_v1')
for s in data.get('scenarios',[]):
    for k in ['id','task','expected_skills','must_include','must_not_include','command_classification']:
        if k not in s or not s.get(k): errors.append(f"{s.get('id','?')}: missing {k}")
    if 'assertions' in s: errors.append(f"{s.get('id')}: old assertions field not allowed")
for s in data.get('negative_selection_scenarios',[]):
    if not s.get('forbidden_skills'): errors.append(f"negative {s.get('id')}: missing forbidden_skills")
    if not s.get('must_not_include'): errors.append(f"negative {s.get('id')}: missing must_not_include")
if errors:
    print('FAIL:'); [print('-',e) for e in errors]; raise SystemExit(1)
print('OK: v9.1 executable evals validated')
