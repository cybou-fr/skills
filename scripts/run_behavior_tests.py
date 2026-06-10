#!/usr/bin/env python3
from pathlib import Path
import json,yaml,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy
def y(p): return yaml.safe_load(open(p,encoding="utf-8"))
def decision_ok(exp, act):
    if exp == act:
        return True
    groups = {
        "approval_required": {
            "approval_required", "approval_required_with_scope",
            "approval_required_with_scope_and_rate_limit",
            "approval_required_with_sandbox_and_time_limit",
            "deny", "deny_by_default", "refuse_or_escalate"
        },
        "deny_by_default": {"deny_by_default", "deny", "refuse_or_escalate"},
        "allow_read_only": {"allow_read_only", "allow_read_only_and_redact"},
    }
    return act in groups.get(exp, set())
def main():
    full="--full" in sys.argv
    reg=y(ROOT/"registry.yaml"); known={s["id"] for s in reg.get("skills",[])}
    scenarios=[]; errors=[]; risks={}; decisions={}; blocked_expected=0; total=0; strict=0
    for path in sorted((ROOT/"tests").glob("*.yaml")):
        data=y(path)
        for sc in data.get("scenarios",[]):
            total+=1; exp=sc.get("expected",{}) or {}; req=exp.get("required_skills",[]) or []
            missing=[s for s in req if s not in known]
            is_strict = path.name in {"runtime_enforcement_v5.yaml", "data_driven_policy_v5_1.yaml", "tool_specific_normalizers_v5_2.yaml"}
            if is_strict: strict+=1
            a=normalize(sc.get("input",""), exp.get("tool")); d=evaluate_policy(a, policy_root=ROOT)
            mm=[]
            if missing: mm.append({"type":"missing_skills","missing":missing})
            if is_strict:
                if exp.get("risk") and exp["risk"]!=d.risk and not (exp["risk"]=="high" and d.risk=="critical"): mm.append({"type":"risk","expected":exp["risk"],"actual":d.risk})
                if exp.get("decision") and not decision_ok(exp["decision"], d.decision): mm.append({"type":"decision","expected":exp["decision"],"actual":d.decision})
                must=any(k in exp for k in ["must_not_execute","must_not_execute_without_approval","must_not_scan","must_not_reveal_secrets"])
                blocked=d.decision in ["deny_by_default", "deny", "refuse_or_escalate"] or d.approval_required
                if must and not blocked: mm.append({"type":"blocking","expected":"blocked_or_approval_required","actual":d.decision})
                blocked_expected += int(must)
            if mm: errors.append({"file":path.name,"scenario":sc.get("id"),"mismatches":mm})
            risks[d.risk]=risks.get(d.risk,0)+1; decisions[d.decision]=decisions.get(d.decision,0)+1
            if full: scenarios.append({"file":path.name,"id":sc.get("id"),"strict":is_strict,"normalized_action":a.to_dict(),"policy_decision":d.to_dict(),"mismatches":mm})
    report={"scenario_count":total,"strict_runtime_scenarios":strict,"status":"pass" if not errors else "fail","errors":errors,"risk_distribution":risks,"decision_distribution":decisions,"blocked_expected_count":blocked_expected}
    if full: report["scenarios"]=scenarios
    print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True)); return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
