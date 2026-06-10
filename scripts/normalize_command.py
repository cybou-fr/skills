#!/usr/bin/env python3

from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from runtime_prototype.normalizers import normalize
if len(sys.argv)<2:
    print("Usage: normalize_command.py '<command>' [tool_hint]", file=sys.stderr); raise SystemExit(2)
print(json.dumps(normalize(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None).to_dict(),indent=2,ensure_ascii=False,sort_keys=True))
