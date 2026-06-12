# Public Release Checklist

Before tagging a public release:

```text
1. Run python scripts/validate_all.py.
2. Confirm status: pass.
3. Confirm no runtime implementation code is present.
4. Confirm registry skills equal SKILL.md files.
5. Confirm cybou.yaml canonical entrypoints exist.
6. Confirm package.yaml extensions exist.
7. Confirm file hashes are current.
8. Confirm release signing status.
9. Sign the release for enterprise use.
10. Publish the tag and release archive.
```

Enterprise release requires a valid signature from a trusted publisher.
