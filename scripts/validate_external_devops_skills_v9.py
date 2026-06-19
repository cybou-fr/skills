#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "devops/debian13-service-discovery/SKILL.md",
    "devops/python-venv-service/SKILL.md",
    "devops/nginx-php-fpm-wordpress/SKILL.md",
    "devops/mariadb-wordpress-admin/SKILL.md",
    "devops/safe-file-authoring/SKILL.md",
]
REQUIRED_SECTIONS = ["## 1. Use when","## 2. Do not use when","## 3. Operating mode","## 4. Risk mapping","## 5. Preferred tool order","## 6. Command templates","## 7. Failure recovery","## 8. Stop / block conditions","## 9. Output contract","## 10. Eval requirements"]
errors=[]
for rel in SKILLS:
    p=ROOT/rel
    if not p.exists(): errors.append(f"missing skill: {rel}"); continue
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('---'): errors.append(f"missing frontmatter: {rel}"); continue
    meta=yaml.safe_load(txt.split('---',2)[1])
    if meta.get('version') not in {'9.0','9.1'}: errors.append(f"{rel}: version must be 9.0 or 9.1")
    if meta.get('skill_format') != 'operational_contract_v1': errors.append(f"{rel}: missing operational_contract_v1")
    if meta.get('selection_profile') != 'narrow': errors.append(f"{rel}: selection_profile must be narrow")
    if not meta.get('triggers',{}).get('include'): errors.append(f"{rel}: no include triggers")
    if not meta.get('triggers',{}).get('exclude'): errors.append(f"{rel}: no exclude triggers")
    if not meta.get('negative_triggers'): errors.append(f"{rel}: no negative_triggers")
    for s in REQUIRED_SECTIONS:
        if s not in txt: errors.append(f"{rel}: missing section {s}")
    for level in ['### low','### medium','### high','### critical']:
        if level not in txt: errors.append(f"{rel}: missing risk level {level}")
    for label in ['read_only', 'guarded', 'blocked']:
        if label not in txt: errors.append(f"{rel}: missing command classification {label}")
    if '```markdown' not in txt: errors.append(f"{rel}: missing inline markdown output template")
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v9 external DevOps skills validated')
