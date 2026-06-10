# Policy to Immunity Mapping

`immunity.rs` is the runtime source of truth.

The pack may contain rich policy metadata, but runtime verdicts must collapse to:

```text
Allow
Deny
NeedsApproval
```

Unknown policy decisions, unknown tools, malformed rules, missing paths and missing templates should become validation errors before runtime use.

Critical checks before guest dispatch:

```text
shell metacharacters
nested interpreters
remote-pipe-to-shell
destructive filesystem operations
sensitive target paths
package-manager mutations
kubectl/terraform/docker/git destructive operations
```
