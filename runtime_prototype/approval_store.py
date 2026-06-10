from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List
import json, time, uuid
from .models import ApprovalState, NormalizedAction

DEFAULT_STORE = Path(".cybou_approvals.json")

def approval_from_dict(d: Dict[str, Any]) -> ApprovalState:
    return ApprovalState(
        approval_id=d["approval_id"],
        status=d.get("status", "approved"),
        scope=d.get("scope", "*"),
        approved_actions=d.get("approved_actions", []),
        expires_at=d.get("expires_at"),
        approved_by=d.get("approved_by"),
        approval_text=d.get("approval_text"),
    )

class ApprovalStore:
    def __init__(self, path: str | Path = DEFAULT_STORE):
        self.path = Path(path)

    def load(self) -> List[ApprovalState]:
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8") or "[]")
        return [approval_from_dict(x) for x in data]

    def save(self, approvals: List[ApprovalState]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps([a.__dict__ for a in approvals], indent=2, ensure_ascii=False), encoding="utf-8")

    def create(self, scope: str, approved_actions: list[str], ttl_seconds: int = 900, approved_by: str | None = None, approval_text: str | None = None) -> ApprovalState:
        approval = ApprovalState(
            approval_id=str(uuid.uuid4()),
            status="approved",
            scope=scope,
            approved_actions=approved_actions,
            expires_at=time.time() + ttl_seconds if ttl_seconds is not None else None,
            approved_by=approved_by,
            approval_text=approval_text,
        )
        approvals = self.load()
        approvals.append(approval)
        self.save(approvals)
        return approval

    def revoke(self, approval_id: str) -> bool:
        approvals = self.load()
        changed = False
        for a in approvals:
            if a.approval_id == approval_id:
                a.status = "revoked"
                changed = True
        self.save(approvals)
        return changed

    def find_valid_for(self, action: NormalizedAction) -> ApprovalState | None:
        for approval in self.load():
            if approval.is_valid_for(action):
                return approval
        return None
