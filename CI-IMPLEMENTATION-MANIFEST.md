# Repository CI Implementation Manifest 0.9.0

## Status

```text
Implementation prepared: Yes
Static and local validation: Passed
First GitHub Actions run: Pending
Branch rule activated: No
Stable Version 1.0 release: No
```

This manifest records the initial repository CI implementation for the SASD
Development Standard. It does not claim that GitHub Actions has already run or
that a branch rule is active. Those claims require evidence from the committed
and pushed revision.

## Scope

The implementation adds:

- cross-platform validation on Ubuntu and Windows,
- a stable `SASD merge gate` check,
- read-only workflow permissions,
- concurrency cancellation for superseded runs,
- explicit job timeouts,
- immutable full-commit action pins,
- disabled checkout credential persistence,
- GitHub Actions updates through Dependabot,
- CODEOWNERS for governance-sensitive paths,
- one local and CI validation entry point,
- JSON, Markdown, and per-check evidence logs,
- deterministic repository-manifest validation,
- repository hygiene and CI-policy validation.

## Pinned GitHub Actions

| Action | Release | Full commit SHA |
|---|---:|---|
| `actions/checkout` | `v7.0.1` | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| `actions/setup-python` | `v7.0.0` | `5fda3b95a4ea91299a34e894583c3862153e4b97` |
| `actions/upload-artifact` | `v7.0.1` | `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` |

Dependabot is configured for the `github-actions` ecosystem so future update
pull requests can refresh both the immutable SHA and its same-line release
comment.

## Blocking checks

The orchestrator runs these blocking checks:

1. repository hygiene,
2. document metadata and dependencies,
3. relative Markdown links,
4. Core requirement IDs and consistency,
5. C#/.NET profile consistency,
6. Desktop profile consistency,
7. operational process consistency,
8. reference-pilot manifests and generated views,
9. Approved Foundation and Governance baseline,
10. CI security and governance policy,
11. deterministic repository manifest.

The Version 1.0 readiness report is generated as informational evidence. Its
remaining Proposed documents do not make routine CI fail before the formal
approval stage.

## Evidence

Each operating-system job uploads an evidence artifact containing:

- `quality-gates.json`,
- `quality-gates.md`,
- one log per validator,
- the informational Version 1.0 readiness report.

The workflow uploads evidence even when a validator fails. Artifacts are kept
for 14 days.

## Activation sequence

1. Copy this update into the repository.
2. Run the local quality gates.
3. Commit and push the update.
4. Confirm that Ubuntu and Windows validation pass.
5. Confirm that `SASD merge gate` reports success.
6. Only then configure the `main` branch ruleset to require `SASD merge gate`.
7. Record the workflow URL and commit SHA in the activation checklist.

## Files introduced

```text
.github/CODEOWNERS
.github/dependabot.yml
.github/workflows/quality-gates.yml
CI-IMPLEMENTATION-MANIFEST.md
checklists/development/REPOSITORY-CI-REVIEW-CHECKLIST.md
checklists/releases/REPOSITORY-CI-ACTIVATION-CHECKLIST.md
scripts/README.md
scripts/validate-repository.ps1
scripts/validate-repository.sh
tooling/generate-repository-manifest.py
tooling/run-quality-gates.py
tooling/validate-ci-policy.py
tooling/validate-repository-hygiene.py
```

## References

- GitHub secure-use guidance: <https://docs.github.com/en/actions/reference/security/secure-use>
- GitHub ruleset status checks: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets>
- Dependabot updates for Actions: <https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions>
