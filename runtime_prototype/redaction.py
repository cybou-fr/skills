import re
PATTERNS=[re.compile(r"(?i)(api[_-]?key|token|secret|password|credential)\s*[:=]\s*['\"]?([A-Za-z0-9_\-./+=]{8,})"),re.compile(r"AKIA[0-9A-Z]{16}"),re.compile(r"(?i)bearer\s+[A-Za-z0-9_\-./+=]{12,}")]
def redact(text):
    changed=False; out=text
    for p in PATTERNS:
        new=p.sub(lambda m: m.group(1)+"=<REDACTED>" if len(m.groups())>=1 else "<REDACTED>", out)
        changed = changed or new!=out; out=new
    return out, changed
