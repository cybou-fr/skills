#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT = Path.cwd()
SKILLS = ['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
def text(path): return path.read_text(encoding='utf-8')
def frontmatter(s):
    if not s.startswith('---'): return ''
    return s.split('---',2)[1]
errors=[]
for sid in SKILLS:
    matches=list(ROOT.glob(f'**/{sid}/SKILL.md'))
    if not matches: errors.append(f'missing {sid}/SKILL.md'); continue
    fm=frontmatter(text(matches[0]))
    for key in ['description:', 'description_fr:', 'summary_fr:', 'triggers:']:
        if key not in fm: errors.append(f'{sid}: missing {key}')
    if 'i18n:' in fm: errors.append(f'{sid}: nested i18n is not required for current YAML-lite loader; use flat description_fr/summary_fr')
    triggers = re.findall(r'^\s*-\s*(.+)$', fm, flags=re.M)
    fr = [t for t in triggers if any(ch in t.lower() for ch in 'éèêàçùôîûâ') or any(w in t.lower() for w in ['découvrir','configuration','écrire','utilisateur','droits','éviter','bloquer','fichier','service systemd','environnement','virtuel','géré','rechargement','refuser','base mariadb','authentification','wordpress','nginx','python','avec','avant','sans'])]
    if len(fr) < 4: errors.append(f'{sid}: too few French triggers')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v10.1 flat bilingual metadata validated')
