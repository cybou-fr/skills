#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
p=Path('evals/v10/bilingual_external_devops_selection.yaml')
if not p.exists(): raise SystemExit('missing evals/v10/bilingual_external_devops_selection.yaml')
data=yaml.safe_load(p.read_text())
sc=data.get('scenarios',[])
errors=[]
skills={'debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring'}
for sid in skills:
    langs={s.get('lang') for s in sc if s.get('skill')==sid}
    for needed in ['en','fr','mixed','fr_negative']:
        if needed not in langs: errors.append(f'{sid}: missing {needed} eval')
for s in sc:
    if not s.get('expected_skills') and not s.get('forbidden_skills'):
        errors.append(f"{s.get('id')}: must declare expected or forbidden skills")
    if 'must_include' not in s or 'must_not_include' not in s:
        errors.append(f"{s.get('id')}: missing must_include/must_not_include")
    if not s.get('metric') == 'selected_relevant_skill':
        errors.append(f"{s.get('id')}: metric must be selected_relevant_skill")
if errors:
    print('\n'.join(errors), file=sys.stderr); raise SystemExit(1)
print('OK: v10 bilingual selection evals validated')
