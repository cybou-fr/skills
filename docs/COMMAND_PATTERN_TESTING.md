# Command Pattern Testing

v6.4 adds command-pattern regression tests for immunity compatibility.

```text
immunity_mapping/command_pattern_tests.yaml
scripts/validate_command_patterns_v6_4.py
```

The tests cover `rm -rf /`, remote pipe-to-shell, base64 execution, Terraform auto-approve, Kubernetes namespace deletion and privileged Docker.
