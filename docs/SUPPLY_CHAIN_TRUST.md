# Supply Chain Trust

v6.4 adds machine-readable supply-chain metadata for the external Cybou skills repository.

The loader should verify file hashes, quarantine invalid skills, keep full bodies unavailable until vetted, and record trust level in audit.

Supply-chain trust does not grant execution permission. Execution still flows through:

```text
immunity.rs -> approval.rs -> GuestExecutor -> MicroVM
```
