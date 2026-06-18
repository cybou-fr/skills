#!/usr/bin/env python3
from pathlib import Path
import sys, re
ROOT = Path.cwd()
SKILLS = [
 'secops/prompt-injection-defense/SKILL.md',
 'secops/malicious-dependency-review/SKILL.md',
 'secops/supply-chain-security/SKILL.md',
 'secops/secret-detection/SKILL.md',
 'secops/model-data-leakage-review/SKILL.md',
 'secops/rag-poisoning-defense/SKILL.md',
 'secops/ai-agent-tool-abuse-review/SKILL.md',
]
REQUIRED = [
 'version: "8.0"', 'skill_format: operational_contract_v1',
 '## 1. Use when', '## 2. Do not use when', '## 3. Operating mode',
 '## 4. Risk mapping', '## 5. Preferred tool order', '## 6. Command templates',
 '## 7. Failure recovery', '## 8. Stop / block conditions', '## 9. Output contract',
 '## 10. Eval requirements', '## Required output format'
]
failed = []
for rel in SKILLS:
    p = ROOT / rel
    if not p.exists():
        failed.append(f"missing {rel}")
        continue
    text = p.read_text(encoding='utf-8')
    for needle in REQUIRED:
        if needle not in text:
            failed.append(f"{rel}: missing {needle}")
    for risk in ['### low','### medium','### high','### critical']:
        if risk not in text:
            failed.append(f"{rel}: missing risk tier {risk}")
if failed:
    print('\n'.join(failed))
    sys.exit(1)
print('OK: v8 AI/SecOps operational contracts validated')
