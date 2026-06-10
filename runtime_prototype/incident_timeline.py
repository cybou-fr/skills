from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Dict, List

def _parse_ts(ts):
    if isinstance(ts, (int, float)): return float(ts)
    if not ts: return 0.0
    s=str(ts).replace('Z','+00:00')
    try: return datetime.fromisoformat(s).timestamp()
    except Exception: return 0.0

def build_timeline(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    normalized=[]
    for e in events:
        normalized.append({
            'timestamp': e.get('timestamp') or e.get('time') or e.get('@timestamp'),
            'sort_ts': _parse_ts(e.get('timestamp') or e.get('time') or e.get('@timestamp')),
            'source': e.get('source') or e.get('tool') or 'unknown',
            'actor': e.get('actor') or e.get('user') or e.get('principal') or 'unknown',
            'asset': e.get('asset') or e.get('host') or e.get('resource') or 'unknown',
            'action': e.get('action') or e.get('event') or e.get('message') or 'unknown',
            'severity': e.get('severity') or 'unknown',
            'evidence_ref': e.get('evidence_ref'),
        })
    normalized.sort(key=lambda x: x['sort_ts'])
    return {'event_count': len(normalized), 'timeline': [{k:v for k,v in e.items() if k!='sort_ts'} for e in normalized]}
