#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
SKILLS = ['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
ROOT=Path.cwd(); errors=[]
for sid in SKILLS:
    p=ROOT/'devops'/sid/'SKILL.md'
    fm=yaml.safe_load(p.read_text().split('---',2)[1])
    if fm.get('version') != '10.0': errors.append(f'{sid}: version must be 10.0')
    i18n=fm.get('i18n')
    if not isinstance(i18n,dict) or 'fr' not in i18n: errors.append(f'{sid}: missing i18n.fr'); continue
    body=i18n['fr'].get('body')
    if body != 'body.fr.md': errors.append(f'{sid}: i18n.fr.body must be body.fr.md')
    if not (p.parent/body).exists(): errors.append(f'{sid}: referenced body.fr.md missing')
    for key in ['name','category','default_risk','default_mode','path']:
        if key in fm and isinstance(fm[key],str) and any(w in fm[key].lower() for w in ['faible','moyen','élevé','chemin']):
            errors.append(f'{sid}: runtime key/enums appear translated in {key}')
if errors:
    print('\n'.join(errors), file=sys.stderr); raise SystemExit(1)
print('OK: v10 i18n frontmatter validated')
