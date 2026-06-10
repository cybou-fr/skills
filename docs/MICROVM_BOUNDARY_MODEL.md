# MicroVM Boundary Model

The real Cybou execution boundary is:

```text
cybou-core host
  -> Virtio-vsock
  -> cybou-guest inside Debian MicroVM
  -> shell execution
```

This pack adds knowledge and policy. It does not replace the MicroVM.
