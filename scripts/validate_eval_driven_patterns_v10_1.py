#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path.cwd()
errors=[]
for p in ROOT.glob('**/SKILL.md'):
    s=p.read_text(encoding='utf-8')
    if 'CREATE DATABASE IF NOT EXISTS' in s: errors.append(f'{p}: invalid CREATE DATABASE IF NOT EXISTS pattern')
for sid in ['python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']:
    matches=list(ROOT.glob(f'**/{sid}/SKILL.md'))
    if not matches: continue
    s=matches[0].read_text(encoding='utf-8')
    if 'Verify-before-finish' not in s and 'Vérifier avant de terminer' not in s: errors.append(f'{sid}: missing verify-before-finish')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v10.1 eval-driven operational patterns validated')
