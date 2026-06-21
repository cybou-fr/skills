#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
SKILLS = ['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
ROOT=Path.cwd(); errors=[]
for sid in SKILLS:
    p=ROOT/'devops'/sid/'SKILL.md'
    if not p.exists(): errors.append(f'missing {p}'); continue
    fm=yaml.safe_load(p.read_text().split('---',2)[1])
    summary=fm.get('summary','')
    summary_fr=fm.get('summary_fr','')
    if ' / ' not in summary: errors.append(f'{sid}: summary must be bilingual one-line with " / " separator')
    if not summary_fr: errors.append(f'{sid}: missing summary_fr')
    if summary_fr and summary_fr == summary: errors.append(f'{sid}: summary_fr equals bilingual summary')
    i18n=fm.get('i18n',{}).get('fr',{}) if isinstance(fm.get('i18n'),dict) else {}
    if i18n.get('summary') != summary_fr: errors.append(f'{sid}: i18n.fr.summary must equal summary_fr')
if errors:
    print('\n'.join(errors), file=sys.stderr); raise SystemExit(1)
print('OK: v10 bilingual summaries validated')
