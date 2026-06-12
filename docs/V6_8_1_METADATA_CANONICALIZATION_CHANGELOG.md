# v6.8.1 Metadata Canonicalization & Legacy Reference Purge

## Added

- `docs/METADATA_CANONICALIZATION_V6_8_1.md`
- `docs/V6_8_1_METADATA_CANONICALIZATION_CHANGELOG.md`
- `scripts/validate_metadata_canonicalization_v6_8_1.py`

## Changed

- Rewrote `cybou.yaml` as canonical skills-only corpus manifest.
- Rewrote `package.yaml` to remove stale extension references.
- Updated `AGENTS.md` to Cybou Skills Corpus v6.8.1.
- Migrated useful runtime metadata into `integration/`.

## Removed

- Top-level `runtime/`.
- Live metadata references to old runtime prototype paths.
- Live metadata references to old deleted script/test directories.
