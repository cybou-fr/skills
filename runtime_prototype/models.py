from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
import time, uuid

@dataclass
class NormalizedAction:
    tool: str
    operation: str
    raw_input: str
    args: Dict[str, Any] = field(default_factory=dict)
    target: Optional[str] = None
    environment: str = "unknown"
    scope: Optional[str] = None
    side_effects: List[str] = field(default_factory=list)
    sensitive_data_possible: bool = False
    def to_dict(self): return asdict(self)

@dataclass
class PolicyDecision:
    decision: str
    risk: str
    tool: str
    normalized_action: Dict[str, Any]
    matched_rules: List[str] = field(default_factory=list)
    approval_required: bool = False
    approval_scope: Optional[str] = None
    redaction_required: bool = False
    audit_required: bool = True
    reason: str = ""
    def to_dict(self): return asdict(self)

@dataclass
class ApprovalState:
    approval_id: str
    status: str
    scope: str
    approved_actions: List[str]
    expires_at: Optional[float] = None
    approved_by: Optional[str] = None
    approval_text: Optional[str] = None
    def is_valid_for(self, action: NormalizedAction) -> bool:
        if self.status != "approved": return False
        if self.expires_at is not None and time.time() > self.expires_at: return False
        if "*" not in self.approved_actions and action.operation not in self.approved_actions: return False
        if self.scope not in ["*", action.scope, action.target, action.environment]: return False
        return True

@dataclass
class AuditEvent:
    timestamp: float
    event_type: str
    decision: str
    risk: str
    skills: List[str]
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tool: Optional[str] = None
    action: Optional[str] = None
    policy_rule: Optional[str] = None
    approval_id: Optional[str] = None
    redaction_applied: bool = False
    def to_dict(self): return asdict(self)
