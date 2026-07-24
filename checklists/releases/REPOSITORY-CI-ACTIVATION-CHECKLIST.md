# Repository CI Activation Checklist

Complete this checklist only for an immutable committed revision.

## Repository boundary

- [ ] `REPOSITORY-IDENTITY.json` identifies the intended repository.
- [ ] `validate-repository-boundary.py` passes.
- [ ] No nested repository root is present.
- [ ] No foreign project marker is present.
- [ ] The deterministic repository manifest passes.

## Committed revision

- Commit SHA:
- Push date:
- Workflow run ID:
- Workflow run URL:

## Automated evidence

- [ ] The workflow run belongs to the recorded commit SHA.
- [ ] Ubuntu validation completed successfully.
- [ ] Windows validation completed successfully.
- [ ] `SASD merge gate` completed successfully.
- [ ] Evidence artifacts were uploaded for both operating systems.
- [ ] `quality-gates.json` reports `passed` for both validation jobs.
- [ ] The readiness report still describes non-Approved documents accurately.
- [ ] `capture-ci-activation.py --verify-only` succeeds.

## Ruleset plan

- [ ] The desired payload is `.github/rulesets/main-merge-gate.json`.
- [ ] The ruleset targets `~DEFAULT_BRANCH`.
- [ ] The required context is exactly `SASD merge gate`.
- [ ] Strict required-status-check policy is enabled.
- [ ] Force pushes are blocked.
- [ ] Branch deletion is blocked.
- [ ] No external approval count is invented for the solo-maintainer phase.
- [ ] The switch from direct pushes to branch/PR work is understood.

## Activation

- [ ] `manage-main-ruleset.py --plan` reports no blocker.
- [ ] The ruleset was created or updated intentionally.
- [ ] The activated ruleset was read back from GitHub.
- [ ] `capture-ci-activation.py --write --require-active-ruleset` succeeds.
- [ ] Ruleset ID and URL are recorded.

## Closeout

- [ ] Any first-run defect was corrected in a separate commit.
- [ ] The final successful commit and workflow URL are recorded.
- [ ] No release or normative approval is inferred solely from CI success.
- [ ] The activation record and evidence JSON are committed separately.
- [ ] A documented disable path remains available.
