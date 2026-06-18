#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path.cwd()/'secops/prompt-injection-defense/SKILL.md'
text=p.read_text(encoding='utf-8') if p.exists() else ''
needles = ['ignore', 'previous', 'system override', 'developer message', 'reveal', 'system prompt', 'bypass', 'tool call']
missing=[n for n in needles if n.lower() not in text.lower()]
if missing:
    print('missing prompt injection indicators: ' + ', '.join(missing))
    sys.exit(1)
print('OK: prompt injection indicators validated')
