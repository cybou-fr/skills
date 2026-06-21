#!/usr/bin/env python3
from pathlib import Path
import sys, re
ROOT=Path.cwd()
SKILLS=['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
banned=[r'<<\s*EOF', r'cat\s+>', r'cat\s+<<', r'\btee\b\s+[^\n]*(>|/)', r'echo\s+[^\n]*>']
errors=[]
for sid in SKILLS:
    for path in ROOT.glob(f'**/{sid}/*.md'):
        s=path.read_text(encoding='utf-8')
        if 'write_file' not in s and sid!='debian13-service-discovery': errors.append(f'{path}: missing write_file')
        for pat in banned:
            if re.search(pat,s): errors.append(f'{path}: banned shell file authoring pattern {pat}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v10.1 write_file-first file authoring validated')
