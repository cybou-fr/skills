import time
from .models import AuditEvent, PolicyDecision
def audit_from_decision(decision: PolicyDecision, skills=None):
    a=decision.normalized_action
    return AuditEvent(time.time(),"policy_decision",decision.decision,decision.risk,skills or [],tool=decision.tool,action=a.get("operation"),policy_rule=",".join(decision.matched_rules),redaction_applied=decision.redaction_required)
