#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path.cwd()
paths = sorted((ROOT/'secops').glob('*/SKILL.md')) if (ROOT/'secops').exists() else []
targets = [p for p in paths if p.read_text(encoding='utf-8', errors='ignore').find('version: "8.0"') >= 0]
failed=[]
for p in targets:
    text = p.read_text(encoding='utf-8')
    if '## Required output format' not in text:
        failed.append(f'{p}: missing Required output format')
    if '```markdown' not in text:
        failed.append(f'{p}: missing fenced markdown output template')
    for section in ['### Summary','### Tools or commands used','### Risk classification','### Actions taken','### Blocked actions']:
        if section not in text:
            failed.append(f'{p}: output template missing {section}')
if failed:
    print('\n'.join(failed))
    sys.exit(1)
print('OK: inline output templates present')
