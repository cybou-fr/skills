from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List
import json, time, uuid, hashlib

def canonical_json(obj: Dict[str, Any]) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def record_hash(record: Dict[str, Any]) -> str:
    material = {k: v for k, v in record.items() if k != "record_hash"}
    return sha256_text(canonical_json(material))

class AuditStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def _read_records(self) -> List[Dict[str, Any]]:
        if not self.path.exists():
            return []
        out = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                out.append(json.loads(line))
        return out

    def list(self) -> List[Dict[str, Any]]:
        return self._read_records()

    def append(self, event: Dict[str, Any], record_type: str = "audit_event") -> Dict[str, Any]:
        records = self._read_records()
        prev_hash = records[-1]["record_hash"] if records else "GENESIS"
        record = {
            "sequence": len(records) + 1,
            "record_id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "record_type": record_type,
            "previous_hash": prev_hash,
            "event": event,
        }
        record["record_hash"] = record_hash(record)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")
        return record

    def verify(self) -> Dict[str, Any]:
        records = self._read_records()
        errors = []
        prev = "GENESIS"
        for expected_seq, record in enumerate(records, start=1):
            if record.get("sequence") != expected_seq:
                errors.append({"sequence": expected_seq, "error": "sequence_mismatch", "actual": record.get("sequence")})
            if record.get("previous_hash") != prev:
                errors.append({"sequence": expected_seq, "error": "previous_hash_mismatch"})
            expected_hash = record_hash(record)
            if record.get("record_hash") != expected_hash:
                errors.append({"sequence": expected_seq, "error": "record_hash_mismatch"})
            prev = record.get("record_hash")
        return {"valid": not errors, "record_count": len(records), "errors": errors}

    def export(self) -> Dict[str, Any]:
        records = self._read_records()
        verification = self.verify()
        return {
            "exported_at": time.time(),
            "record_count": len(records),
            "verification": verification,
            "records": records,
        }
