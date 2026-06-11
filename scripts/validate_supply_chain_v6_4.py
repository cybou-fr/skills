#!/usr/bin/env python3
from pathlib import Path
import yaml, json, hashlib

ROOT = Path(__file__).resolve().parents[1]
def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
def main():
    errors, warnings = [], []
    manifest = load_yaml(ROOT / "integration" / "supply_chain_manifest.yaml")
    hashes = load_yaml(ROOT / manifest.get("file_hashes", "integration/file_hashes.yaml"))
    if manifest.get("hash_algorithm") != "sha256":
        errors.append("hash_algorithm must be sha256")
    seen = set()
    for item in hashes.get("files", []):
        rel, expected = item.get("path"), item.get("sha256")
        if not rel or not expected:
            errors.append(f"malformed hash entry: {item}"); continue
        if rel in seen: errors.append(f"duplicate hash entry: {rel}")
        seen.add(rel)
        p = ROOT / rel
        if not p.exists(): errors.append(f"hashed file missing: {rel}"); continue
        actual = sha256_file(p)
        if actual != expected: errors.append(f"hash mismatch {rel}: expected {expected}, got {actual}")
    result = {"status":"pass" if not errors else "fail","errors":errors,"warnings":warnings,"hashed_files":len(hashes.get("files", [])),"signed_release_required_for_enterprise":manifest.get("release_integrity", {}).get("signed_release_required_for_enterprise")}
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0
if __name__ == "__main__":
    raise SystemExit(main())
