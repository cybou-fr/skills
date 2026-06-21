#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in ROOT.rglob('SKILL.md'):
    if set(p.parts) & {'.git','.venv','node_modules','vendor'}: continue
    txt=p.read_text(encoding='utf-8', errors='replace')
    if not txt.startswith('---'):
        errors.append(f'{p.relative_to(ROOT)}: missing YAML frontmatter fence'); continue
    chunks=txt.split('---',2)
    if len(chunks)<3:
        errors.append(f'{p.relative_to(ROOT)}: unclosed YAML frontmatter'); continue
    try: meta=yaml.safe_load(chunks[1]) or {}
    except Exception as e:
        errors.append(f'{p.relative_to(ROOT)}: invalid YAML frontmatter: {e}'); continue
    for key in ['name','version','category']:
        if key not in meta: errors.append(f'{p.relative_to(ROOT)}: missing required frontmatter key {key}')
    if meta.get('skill_format') == 'operational_contract_v1':
        for key in ['default_mode','default_risk','requires_tools']:
            if key not in meta: errors.append(f'{p.relative_to(ROOT)}: v7+/v9 skill missing {key}')
if errors:
    print('Rejected skill files / frontmatter errors:')
    for e in errors: print('-', e)
    print(f'Total rejected: {len(errors)}')
    sys.exit(1)
print('OK: all SKILL.md frontmatter parsed')
