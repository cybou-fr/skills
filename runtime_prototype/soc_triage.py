from __future__ import annotations
from typing import Dict, Any
from .ioc_extractor import summarize_iocs

def triage_alert(alert: Dict[str, Any]) -> Dict[str, Any]:
    text = ' '.join(str(v) for v in alert.values())
    iocs = summarize_iocs(text)
    severity = str(alert.get('severity') or alert.get('level') or 'medium').lower()
    score = {'low':1,'medium':2,'high':3,'critical':4}.get(severity,2)
    msg = text.lower()
    if any(x in msg for x in ['privilege escalation','credential','exfiltration','ransomware','persistence']): score += 1
    if iocs['ioc_count'] >= 3: score += 1
    final = 'critical' if score >= 4 else 'high' if score == 3 else 'medium' if score == 2 else 'low'
    recommendations = ['preserve evidence', 'validate affected assets', 'check related alerts']
    if final in ['high','critical']: recommendations.append('consider containment with approval')
    return {'severity': final, 'confidence': 'medium', 'iocs': iocs['iocs'], 'recommendations': recommendations, 'approval_required_for': ['containment','blocking','disable_user','close_alert']}
