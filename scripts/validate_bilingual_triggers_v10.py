#!/usr/bin/env python3
from pathlib import Path
import re, yaml, sys
SKILLS = ['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
ROOT = Path.cwd()
FRENCH_SIGNALS = re.compile(r"[éèêàùçîôû]|\b(découvrir|découverte|unité|service fourni|paquet|créer|base|droits|utilisateur|écrire|fichier|configuration|rechargement|éviter|bloquer|refuser|environnement|géré|introuvable)\b", re.I)
BANNED = {'system','service','unit','http','url','and','file','write','config','database','sql','user','admin','python','nginx','php','wordpress','système','unité','fichier','écrire','configuration','base','utilisateur','et'}
errors=[]
for sid in SKILLS:
    p = ROOT / 'devops' / sid / 'SKILL.md'
    if not p.exists(): errors.append(f'missing {p}'); continue
    text = p.read_text()
    fm = yaml.safe_load(text.split('---',2)[1])
    tr = fm.get('triggers',{})
    if 'triggers_en' in fm or 'triggers_fr' in fm: errors.append(f'{sid}: split trigger fields are forbidden')
    include = tr.get('include',[]) if isinstance(tr, dict) else tr
    fr = [t for t in include if FRENCH_SIGNALS.search(t)]
    if len(fr) < 3: errors.append(f'{sid}: expected at least 3 French triggers, got {len(fr)}')
    en = [t for t in include if not FRENCH_SIGNALS.search(t)]
    if len(en) < 3: errors.append(f'{sid}: expected at least 3 English/tool triggers, got {len(en)}')
    bad = [t for t in include if t.strip().lower() in BANNED]
    if bad: errors.append(f'{sid}: banned single-token triggers present: {bad}')
    # commands/tool names must remain literal if present
    for translated in ['systèmectl','nginx tester','mysql -é','écrire_fichier']:
        if translated in text.lower(): errors.append(f'{sid}: possible translated command/tool token: {translated}')
if errors:
    print('\n'.join(errors), file=sys.stderr); raise SystemExit(1)
print('OK: v10 bilingual triggers validated')
