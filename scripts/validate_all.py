#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, time
ROOT=Path(__file__).resolve().parents[1]
VALIDATORS=['scripts/validate_pack_v6_1.py','scripts/validate_loader_contract_v6_2.py','scripts/validate_immunity_compat_v6_3.py','scripts/validate_supply_chain_v6_4.py','scripts/validate_skill_vetting_rules_v6_4.py','scripts/validate_command_patterns_v6_4.py','scripts/validate_eval_contract_v6_5.py','scripts/validate_adversarial_immunity_v6_5.py','scripts/validate_release_signing_v6_6.py','scripts/validate_policy_hardening_v6_7.py','scripts/validate_public_repository_cleanup_v6_8.py','scripts/validate_metadata_canonicalization_v6_8_1.py','scripts/validate_public_docs_v6_8_2.py','scripts/validate_semantic_review_v6_9.py']
def run(rel):
    path=ROOT/rel; start=time.time()
    if not path.exists(): return {'validator':rel,'status':'fail','errors':[f'missing validator: {rel}'],'warnings':[],'duration_ms':0}
    p=subprocess.run([sys.executable,str(path)],cwd=str(ROOT),text=True,capture_output=True,timeout=60)
    try: payload=json.loads(p.stdout)
    except Exception: payload={'status':'fail','errors':['validator did not return JSON'],'warnings':[],'stdout':p.stdout,'stderr':p.stderr}
    payload.update({'validator':rel,'returncode':p.returncode,'duration_ms':int((time.time()-start)*1000)})
    if p.returncode!=0 and payload.get('status')=='pass':
        payload['status']='fail'; payload.setdefault('errors',[]).append(f'non-zero returncode: {p.returncode}')
    return payload
def main():
    results=[run(v) for v in VALIDATORS]; failed=[r for r in results if r.get('status')!='pass']; warnings=sum(len(r.get('warnings',[])) for r in results)
    print(json.dumps({'status':'pass' if not failed else 'fail','validators':len(results),'passed':len(results)-len(failed),'failed':len(failed),'warnings':warnings,'results':results}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if failed else 0
if __name__=='__main__': raise SystemExit(main())
