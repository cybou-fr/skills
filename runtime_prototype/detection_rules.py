from __future__ import annotations
from typing import Dict, Any, List
import re, textwrap

def sigma_rule(title: str, logsource: Dict[str, str], keywords: List[str], level: str = 'medium') -> str:
    safe_title = re.sub(r'[^A-Za-z0-9 _-]', '', title).strip() or 'CYBOU Detection Draft'
    kws = [k for k in keywords if k and len(k) < 200]
    lines = ['title: ' + safe_title, 'id: draft-generated-by-cybou', 'status: experimental', 'description: Defensive detection draft generated from reviewed evidence.', 'logsource:']
    for k,v in logsource.items(): lines.append(f'  {k}: {v}')
    lines += ['detection:', '  selection:']
    if kws:
        lines.append('    Keywords|contains:')
        for k in kws: lines.append(f'      - "{k}"')
    else:
        lines.append('    EventID: 0')
    lines += ['  condition: selection', 'falsepositives:', '  - Administrative activity', 'level: ' + level]
    return '\n'.join(lines) + '\n'

def yara_rule(name: str, strings: List[str], condition: str = 'any of them') -> str:
    safe_name = re.sub(r'[^A-Za-z0-9_]', '_', name) or 'CYBOU_Detection_Draft'
    safe_strings = [s for s in strings if s and len(s) < 200][:20]
    out = [f'rule {safe_name} {{', '  meta:', '    description = "Defensive YARA draft generated from reviewed indicators"', '    author = "CYBOU"', '  strings:']
    for i,s in enumerate(safe_strings):
        esc = s.replace('\\','\\\\').replace('"','\\"')
        out.append(f'    $s{i} = "{esc}" nocase')
    if not safe_strings: out.append('    $placeholder = "CHANGE_ME"')
    out += ['  condition:', f'    {condition}', '}']
    return '\n'.join(out) + '\n'
