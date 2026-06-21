#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
ROOT=Path.cwd()
entries_path=ROOT/'registry.v10.1.bilingual_external_devops_active_entries.yaml'
if not entries_path.exists(): entries_path=ROOT/'repo-overlay'/'registry.v10.1.bilingual_external_devops_active_entries.yaml'
entries=yaml.safe_load(entries_path.read_text(encoding='utf-8'))['skills']
errors=[]
for e in entries:
    for key in ['id','path','description','description_fr','summary_fr','triggers','selection_profile']:
        if key not in e: errors.append(f"{e.get('id')}: missing {key}")
    if e.get('selection_profile')!='narrow_bilingual': errors.append(f"{e.get('id')}: wrong selection_profile")
    if not (ROOT/e['path']).exists() and not (ROOT/'repo-overlay'/e['path']).exists(): errors.append(f"{e.get('id')}: path missing {e['path']}")
    if len(e.get('triggers',[])) < 8: errors.append(f"{e.get('id')}: not enough bilingual triggers")
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v10.1 registry bilingual integration entries validated')
