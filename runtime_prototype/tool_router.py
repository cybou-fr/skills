from __future__ import annotations
from pathlib import Path
from typing import Any, Dict

from .normalizers import normalize
from .policy import evaluate_policy
from .sandbox_profiles import select_sandbox_profile
from .execution_boundary import ToolExecutionBoundary
from .audit import audit_from_decision
from .audit_store import AuditStore
from .evidence_store import EvidenceStore

class ToolRouter:
    def __init__(self, root: str | Path, workdir: str | Path | None = None, audit_path: str | Path | None = None, evidence_dir: str | Path | None = None):
        self.root = Path(root)
        self.workdir = Path(workdir) if workdir else self.root
        self.audit = AuditStore(audit_path or (self.root / ".cybou_audit.jsonl"))
        self.evidence = EvidenceStore(evidence_dir or (self.root / ".cybou_evidence"), self.audit)
        self.executor = ToolExecutionBoundary(self.workdir)

    def route(self, command: str, approval=None, dry_run: bool = True) -> Dict[str, Any]:
        action = normalize(command)
        decision = evaluate_policy(action, approval=approval, policy_root=self.root)
        sandbox_name, sandbox, sandbox_reasons = select_sandbox_profile(action, decision, self.root)
        audit_record = self.audit.append(audit_from_decision(decision).to_dict(), "policy_decision")
        execution = self.executor.execute(action, decision, sandbox_name, sandbox, dry_run=dry_run)
        evidence_record = self.evidence.capture_text(
            json_text(execution),
            "tool_execution_result",
            {"audit_record_id": audit_record["record_id"], "command": command},
        )
        return {
            "normalized_action": action.to_dict(),
            "policy_decision": decision.to_dict(),
            "sandbox_profile": sandbox_name,
            "sandbox_reasons": sandbox_reasons,
            "execution_result": execution,
            "audit_record": audit_record,
            "evidence_record": evidence_record,
            "audit_verification": self.audit.verify(),
            "evidence_verification": self.evidence.verify(),
        }

def json_text(obj: Any) -> str:
    import json
    return json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True)
