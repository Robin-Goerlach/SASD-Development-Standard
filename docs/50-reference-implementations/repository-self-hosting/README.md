# Repository Self-Hosting Reference

This directory records how the SASD Development Standard applies its own
Foundation, Governance, repository-quality, evidence, and change-control rules.

The records deliberately separate four states:

1. implementation prepared,
2. repository boundary repaired,
3. cross-platform CI verified for an immutable commit,
4. the `main` ruleset activated and independently read back from GitHub.

No document in this directory may infer a successful GitHub Actions run from the
presence of a workflow file or from a successful local validator execution.

## Documents

- [`CI-RECOVERY-AND-ACTIVATION.md`](CI-RECOVERY-AND-ACTIVATION.md) — controlled recovery and activation procedure.
- [`BRANCH-RULESET-PLAN.md`](BRANCH-RULESET-PLAN.md) — intended protection model for `main`.
- [`CI-ACTIVATION-RECORD.md`](CI-ACTIVATION-RECORD.md) — current evidence and activation state.
- `CI-ACTIVATION-EVIDENCE.json` — machine-readable evidence generated only after a successful remote run.
