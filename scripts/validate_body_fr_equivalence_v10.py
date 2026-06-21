#!/usr/bin/env python3
from pathlib import Path
import re, yaml, sys
SKILLS = ['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
ROOT=Path.cwd(); errors=[]
for sid in SKILLS:
    p=ROOT/'devops'/sid/'SKILL.md'
    bodyp=ROOT/'devops'/sid/'body.fr.md'
    if not bodyp.exists(): errors.append(f'{sid}: missing body.fr.md'); continue
    en = p.read_text().split('\n---\n',1)[1]
    fr = bodyp.read_text()
    for n in range(1,11):
        if f'## {n}.' not in fr: errors.append(f'{sid}: body.fr.md missing section ## {n}.')
    # ensure key commands from EN body appear in FR body if they exist
    for token in ['systemctl','nginx -t','mysql','mariadb','write_file','tee <target>','python3 -m venv','dpkg']:
        if token in en and token not in fr:
            errors.append(f'{sid}: body.fr.md missing command/tool token {token}')
    for bad in ['systèmectl','nginx tester','écrire_fichier','risque_estime']:
        if bad in fr.lower(): errors.append(f'{sid}: body.fr.md contains translated runtime token {bad}')
if errors:
    print('\n'.join(errors), file=sys.stderr); raise SystemExit(1)
print('OK: v10 French body structural equivalence validated')
