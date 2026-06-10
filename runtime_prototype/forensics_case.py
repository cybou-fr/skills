from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List
import json, time, uuid, hashlib
from .redaction import redact
from .ioc_extractor import extract_iocs

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

class CaseStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def load(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {"cases": []}
        return json.loads(self.path.read_text(encoding="utf-8") or '{"cases": []}')

    def save(self, data: Dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")

    def create_case(self, title: str, severity: str = "medium", owner: str | None = None) -> Dict[str, Any]:
        data = self.load()
        case = {
            "case_id": str(uuid.uuid4()),
            "title": title,
            "severity": severity,
            "status": "open",
            "owner": owner,
            "created_at": time.time(),
            "updated_at": time.time(),
            "affected_assets": [],
            "evidence": [],
            "timeline": [],
            "notes": [],
        }
        data["cases"].append(case)
        self.save(data)
        return case

    def get_case(self, case_id: str) -> Dict[str, Any] | None:
        for c in self.load().get("cases", []):
            if c["case_id"] == case_id:
                return c
        return None

    def update_case(self, case: Dict[str, Any]) -> None:
        data = self.load()
        for i, c in enumerate(data.get("cases", [])):
            if c["case_id"] == case["case_id"]:
                case["updated_at"] = time.time()
                data["cases"][i] = case
                self.save(data)
                return
        raise KeyError(case["case_id"])

    def add_note(self, case_id: str, note: str, author: str = "analyst", note_type: str = "analyst_note") -> Dict[str, Any]:
        case = self.get_case(case_id)
        if not case:
            raise KeyError(case_id)
        safe_note, redacted = redact(note)
        rec = {"note_id": str(uuid.uuid4()), "timestamp": time.time(), "author": author, "note_type": note_type, "text": safe_note, "redaction_applied": redacted}
        case["notes"].append(rec)
        self.update_case(case)
        return rec

    def attach_evidence(self, case_id: str, source: str, content: str, collector: str = "analyst", evidence_type: str = "log") -> Dict[str, Any]:
        case = self.get_case(case_id)
        if not case:
            raise KeyError(case_id)
        safe_content, redacted = redact(content)
        rec = {
            "evidence_id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "source": source,
            "collector": collector,
            "evidence_type": evidence_type,
            "sha256": sha256_text(safe_content),
            "redaction_applied": redacted,
            "content_ref": f"inline:{len(safe_content)}",
            "chain_of_custody": [{"timestamp": time.time(), "actor": collector, "action": "collected", "source": source}],
            "iocs": extract_iocs(safe_content),
        }
        case["evidence"].append(rec)
        self.update_case(case)
        return rec

    def add_timeline_event(self, case_id: str, ts: float, summary: str, source: str, confidence: str = "medium") -> Dict[str, Any]:
        case = self.get_case(case_id)
        if not case:
            raise KeyError(case_id)
        safe_summary, redacted = redact(summary)
        event = {"event_id": str(uuid.uuid4()), "timestamp": ts, "summary": safe_summary, "source": source, "confidence": confidence, "redaction_applied": redacted}
        case["timeline"].append(event)
        case["timeline"].sort(key=lambda e: e["timestamp"])
        self.update_case(case)
        return event

    def export_case(self, case_id: str) -> Dict[str, Any]:
        case = self.get_case(case_id)
        if not case:
            raise KeyError(case_id)
        return {
            "exported_at": time.time(),
            "case": case,
            "chain_of_custody_status": verify_chain_of_custody(case),
            "timeline_event_count": len(case.get("timeline", [])),
            "evidence_count": len(case.get("evidence", [])),
        }

def verify_chain_of_custody(case: Dict[str, Any]) -> Dict[str, Any]:
    errors = []
    for ev in case.get("evidence", []):
        if not ev.get("sha256"):
            errors.append({"evidence_id": ev.get("evidence_id"), "error": "missing_hash"})
        if not ev.get("chain_of_custody"):
            errors.append({"evidence_id": ev.get("evidence_id"), "error": "missing_chain_of_custody"})
        for step in ev.get("chain_of_custody", []):
            if not all(k in step for k in ["timestamp", "actor", "action"]):
                errors.append({"evidence_id": ev.get("evidence_id"), "error": "custody_step_incomplete"})
    return {"valid": not errors, "errors": errors}

def reconstruct_timeline_from_text(case_id: str, text: str) -> List[Dict[str, Any]]:
    events = []
    # Simple ISO-like timestamp extraction for prototype.
    import re, datetime
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2}[T ][0-9:]{8}Z?)\s+(.*)")
    for line in text.splitlines():
        m = pattern.search(line)
        if m:
            ts_s, summary = m.group(1), m.group(2)
            try:
                ts = datetime.datetime.fromisoformat(ts_s.replace("Z", "+00:00")).timestamp()
            except Exception:
                ts = time.time()
            events.append({"case_id": case_id, "timestamp": ts, "summary": summary, "source": "text_import", "confidence": "medium"})
    return events
