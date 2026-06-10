#!/usr/bin/env python3
from pathlib import Path
import sys,json,yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from runtime_prototype.ioc_extractor import extract_iocs
from runtime_prototype.detection_rules import sigma_rule, yara_rule
from runtime_prototype.incident_timeline import build_timeline
from runtime_prototype.soc_triage import triage_alert

def load_yaml(p): return yaml.safe_load(open(p,encoding='utf-8')) or {}
def main():
    errors=[]; total=0
    for path in sorted((ROOT/'detection_tests').glob('*.yaml')):
        data=load_yaml(path)
        for sc in data.get('scenarios',[]):
            total+=1; mm=[]
            if 'text' in sc:
                actual=extract_iocs(sc['text']); exp=sc['expected']
                for k,v in exp.items():
                    for item in v:
                        if item not in actual.get(k,[]): mm.append({'field':k,'missing':item,'actual':actual.get(k)})
            elif 'sigma' in sc:
                x=sc['sigma']; rule=sigma_rule(x['title'], {'product':x['product'],'service':x['service']}, x['keywords'])
                for s in sc['expected_contains']:
                    if s not in rule: mm.append({'missing':s,'rule':rule})
            elif 'yara' in sc:
                x=sc['yara']; rule=yara_rule(x['name'], x['strings'])
                for s in sc['expected_contains']:
                    if s not in rule: mm.append({'missing':s,'rule':rule})
            elif 'events' in sc:
                tl=build_timeline(sc['events'])
                if tl['timeline'][0]['action'] != sc['expected_first_action']: mm.append({'timeline':tl})
            elif 'alert' in sc:
                tri=triage_alert(sc['alert'])
                if tri['severity'] != sc['expected_severity']: mm.append({'triage':tri})
            if mm: errors.append({'scenario':sc.get('id'),'mismatches':mm})
    print(json.dumps({'status':'pass' if not errors else 'fail','detection_scenarios':total,'errors':errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
