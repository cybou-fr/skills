#!/usr/bin/env python3
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from runtime_prototype.policy_loader import load_policy_bundle
bundle=load_policy_bundle(ROOT)
print(json.dumps(bundle.to_summary(),indent=2,ensure_ascii=False,sort_keys=True))
