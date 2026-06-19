#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
checks={
 'devops/debian13-service-discovery/SKILL.md': ['systemctl list-unit-files', 'dpkg-query -L', 'php*fpm'],
 'devops/python-venv-service/SKILL.md': ['python3 -m venv', '.venv/bin/python -m pip', '.venv/bin/python -m uvicorn', '--break-system-packages'],
 'devops/nginx-php-fpm-wordpress/SKILL.md': ['nginx -t', 'xmlrpc.php', 'fastcgi_pass unix:', 'systemctl reload nginx'],
 'devops/mariadb-wordpress-admin/SKILL.md': ['sudo mysql -e', 'CREATE DATABASE', 'GRANT SELECT', 'psql'],
 'devops/safe-file-authoring/SKILL.md': ["<<'EOF'", 'install -d', 'tee <target>', 'systemd-analyze verify'],
}
errors=[]
for rel, needles in checks.items():
    p=ROOT/rel
    if not p.exists(): errors.append(f'missing {rel}'); continue
    txt=p.read_text(encoding='utf-8')
    for n in needles:
        if n not in txt: errors.append(f'{rel}: missing command/pattern {n}')
for rel in ['devops/python-venv-service/SKILL.md','devops/mariadb-wordpress-admin/SKILL.md']:
    txt=(ROOT/rel).read_text(encoding='utf-8')
    if rel.endswith('python-venv-service/SKILL.md') and 'blocked' not in txt.lower(): errors.append(f'{rel}: blocked section missing')
    if rel.endswith('mariadb-wordpress-admin/SKILL.md') and 'Do not use for PostgreSQL' not in txt: errors.append(f'{rel}: missing PostgreSQL drift block')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v9 external DevOps command templates validated')
