#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path.cwd()/'secops/malicious-dependency-review/SKILL.md'
text=p.read_text(encoding='utf-8') if p.exists() else ''
needles = ['npm view', 'git diff -- package.json', 'python -m pip', 'poetry show', 'cargo tree', 'go list -m all', 'apt-cache policy', 'Do not execute scripts']
missing=[n for n in needles if n not in text]
if missing:
    print('missing dependency review commands: ' + ', '.join(missing))
    sys.exit(1)
print('OK: dependency review commands validated')
