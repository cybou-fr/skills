#!/usr/bin/env python3
from pathlib import Path
import sys, re
ROOT = Path.cwd()
TARGETS = [
 'secops/prompt-injection-defense/SKILL.md',
 'secops/secret-detection/SKILL.md',
 'secops/model-data-leakage-review/SKILL.md',
 'secops/rag-poisoning-defense/SKILL.md',
 'secops/ai-agent-tool-abuse-review/SKILL.md',
]
failed=[]
for rel in TARGETS:
    p=ROOT/rel
    if not p.exists():
        failed.append(f'missing {rel}')
        continue
    text=p.read_text(encoding='utf-8')
    if 'mcp:' not in text:
        failed.append(f'{rel}: missing MCP tooling reference')
    if not re.search(r'(fallback shell|shell/regex|regex scan|rg -n|ripgrep)', text, re.I):
        failed.append(f'{rel}: missing fallback scanner/regex path')
    if 'unavailable' not in text.lower():
        failed.append(f'{rel}: missing unavailable-tool behavior')
if failed:
    print('\n'.join(failed))
    sys.exit(1)
print('OK: scanner/tool fallbacks validated')
