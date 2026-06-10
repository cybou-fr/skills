from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List
import json, time, uuid, hashlib
from .redaction import redact
from .audit_store import AuditStore

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

class EvidenceStore:
    def __init__(self, root: str | Path, audit_store: AuditStore | None = None):
        self.root = Path(root)
        self.audit_store = audit_store

    def capture_text(self, text: str, evidence_type: str = "tool_output", linked: Dict[str, Any] | None = None) -> Dict[str, Any]:
        safe_text, redacted = redact(text)
        data = safe_text.encode("utf-8")
        evidence_id = str(uuid.uuid4())
        record = {
            "evidence_id": evidence_id,
            "timestamp": time.time(),
            "evidence_type": evidence_type,
            "content_type": "text/plain",
            "redaction_applied": redacted,
            "sha256": sha256_bytes(data),
            "linked": linked or {},
        }
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / f"{evidence_id}.txt").write_text(safe_text, encoding="utf-8")
        (self.root / f"{evidence_id}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")
        if self.audit_store:
            self.audit_store.append({"event_type": "evidence_captured", "evidence": record}, "evidence_event")
        return record

    def list(self) -> List[Dict[str, Any]]:
        if not self.root.exists():
            return []
        out = []
        for p in sorted(self.root.glob("*.json")):
            out.append(json.loads(p.read_text(encoding="utf-8")))
        return out

    def verify(self) -> Dict[str, Any]:
        errors = []
        records = self.list()
        for rec in records:
            content_path = self.root / f"{rec['evidence_id']}.txt"
            if not content_path.exists():
                errors.append({"evidence_id": rec["evidence_id"], "error": "content_missing"})
                continue
            actual = sha256_bytes(content_path.read_bytes())
            if actual != rec.get("sha256"):
                errors.append({"evidence_id": rec["evidence_id"], "error": "sha256_mismatch"})
        return {"valid": not errors, "evidence_count": len(records), "errors": errors}
