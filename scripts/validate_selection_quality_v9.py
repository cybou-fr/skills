#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
policy=ROOT/'selection/skill_selection_policy.v9.yaml'
if not policy.exists(): print('missing selection policy'); sys.exit(1)
data=yaml.safe_load(policy.read_text(encoding='utf-8'))
errors=[]
if data.get('selection_objective',{}).get('primary_metric') != 'selected_relevant_skill': errors.append('primary_metric must be selected_relevant_skill')
banned=set(data.get('banned_single_token_triggers',[]))
required={'system','and','url','http','service'}
if required-banned: errors.append(f'missing banned generic triggers: {sorted(required-banned)}')
if not data.get('category_allowlists'): errors.append('missing category_allowlists')
if not data.get('negative_selection_examples'): errors.append('missing negative_selection_examples')
for p in (ROOT/'devops').glob('*/SKILL.md'):
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('---'): continue
    meta=yaml.safe_load(txt.split('---',2)[1])
    for trig in meta.get('triggers',{}).get('include',[]):
        if trig.strip().lower() in banned: errors.append(f'{p}: banned single-token include trigger {trig!r}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v9 selection quality policy validated')
