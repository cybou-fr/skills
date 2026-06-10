#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.ioc_extractor import summarize_iocs
from runtime_prototype.detection_rules import sigma_rule, yara_rule
from runtime_prototype.incident_timeline import build_timeline
from runtime_prototype.soc_triage import triage_alert
from runtime_prototype.audit_store import AuditStore
from runtime_prototype.evidence_store import EvidenceStore

def main():
    parser = argparse.ArgumentParser(description='CYBOU SOC/detection engineering prototype')
    sub = parser.add_subparsers(dest='cmd', required=True)
    x=sub.add_parser('extract-iocs'); x.add_argument('--text', required=True)
    s=sub.add_parser('sigma'); s.add_argument('--title', required=True); s.add_argument('--keywords', required=True); s.add_argument('--product', default='linux'); s.add_argument('--service', default='process_creation')
    y=sub.add_parser('yara'); y.add_argument('--name', required=True); y.add_argument('--strings', required=True)
    t=sub.add_parser('timeline'); t.add_argument('--events-json', required=True)
    a=sub.add_parser('triage-alert'); a.add_argument('--alert-json', required=True)
    args=parser.parse_args()
    if args.cmd=='extract-iocs': print(json.dumps(summarize_iocs(args.text), indent=2, ensure_ascii=False)); return 0
    if args.cmd=='sigma': print(sigma_rule(args.title, {'product':args.product,'service':args.service}, [k.strip() for k in args.keywords.split(',') if k.strip()])); return 0
    if args.cmd=='yara': print(yara_rule(args.name, [k.strip() for k in args.strings.split(',') if k.strip()])); return 0
    if args.cmd=='timeline': print(json.dumps(build_timeline(json.loads(args.events_json)), indent=2, ensure_ascii=False)); return 0
    if args.cmd=='triage-alert': print(json.dumps(triage_alert(json.loads(args.alert_json)), indent=2, ensure_ascii=False)); return 0
if __name__ == '__main__': raise SystemExit(main())
