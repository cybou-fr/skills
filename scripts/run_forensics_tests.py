#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys, tempfile
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.forensics_case import CaseStore, verify_chain_of_custody

def load_yaml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def main():
    errors = []
    total = 0
    for path in sorted((ROOT / "forensics_tests").glob("*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            with tempfile.TemporaryDirectory() as td:
                store = CaseStore(Path(td)/"cases.json")
                current = None
                for action in sc.get("actions", []):
                    if "create" in action:
                        c = action["create"]
                        current = store.create_case(c["title"], c.get("severity", "medium"), c.get("owner"))
                    elif "evidence" in action:
                        e = action["evidence"]
                        store.attach_evidence(current["case_id"], e["source"], e["content"], e.get("collector","analyst"), e.get("type","log"))
                    elif "timeline" in action:
                        t = action["timeline"]
                        store.add_timeline_event(current["case_id"], t["timestamp"], t["summary"], t["source"], t.get("confidence","medium"))
                exp = sc["expected"]
                data_out = store.load()
                case = data_out["cases"][0] if data_out["cases"] else None
                mismatches = []
                if "case_count" in exp and len(data_out["cases"]) != exp["case_count"]:
                    mismatches.append({"field":"case_count","expected":exp["case_count"],"actual":len(data_out["cases"])})
                if "status" in exp and case.get("status") != exp["status"]:
                    mismatches.append({"field":"status","expected":exp["status"],"actual":case.get("status")})
                if "evidence_count" in exp and len(case.get("evidence",[])) != exp["evidence_count"]:
                    mismatches.append({"field":"evidence_count","expected":exp["evidence_count"],"actual":len(case.get("evidence",[]))})
                if "redaction_applied" in exp and case["evidence"][0].get("redaction_applied") != exp["redaction_applied"]:
                    mismatches.append({"field":"redaction_applied","expected":exp["redaction_applied"],"actual":case["evidence"][0].get("redaction_applied")})
                if "custody_valid" in exp and verify_chain_of_custody(case)["valid"] != exp["custody_valid"]:
                    mismatches.append({"field":"custody_valid","expected":exp["custody_valid"],"actual":verify_chain_of_custody(case)})
                if "timeline_count" in exp and len(case.get("timeline",[])) != exp["timeline_count"]:
                    mismatches.append({"field":"timeline_count","expected":exp["timeline_count"],"actual":len(case.get("timeline",[]))})
                if "first_summary" in exp and case["timeline"][0].get("summary") != exp["first_summary"]:
                    mismatches.append({"field":"first_summary","expected":exp["first_summary"],"actual":case["timeline"][0].get("summary")})
                if "export_evidence_count" in exp:
                    exported = store.export_case(case["case_id"])
                    if exported["evidence_count"] != exp["export_evidence_count"]:
                        mismatches.append({"field":"export_evidence_count","expected":exp["export_evidence_count"],"actual":exported["evidence_count"]})
                    if exported["chain_of_custody_status"]["valid"] != exp["custody_valid"]:
                        mismatches.append({"field":"export_custody","expected":exp["custody_valid"],"actual":exported["chain_of_custody_status"]})
                if mismatches:
                    errors.append({"scenario":sc["id"],"mismatches":mismatches})
    print(json.dumps({"status":"pass" if not errors else "fail","forensics_scenarios":total,"errors":errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
