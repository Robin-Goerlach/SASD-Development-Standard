# Repository CI Implementation Manifest 0.10.0

## Status

```text
Implementation prepared: Yes
Static and local validation: Passed
First GitHub Actions run: Failed - repository boundary contamination detected
Boundary repair prepared: Yes
Recovery verification tooling: Prepared
Green repair-commit run: Pending
Branch ruleset plan: Prepared
Branch ruleset activated: No
Stable Version 1.0 release: No
```

This manifest records the initial repository CI implementation for the SASD
Development Standard. It does not claim that GitHub Actions has already run or
that a branch rule is active. Those claims require evidence from the committed
and pushed revision.


## First execution result

The first GitHub Actions execution for commit `3ea1a88` completed with failure on
Ubuntu and Windows. The quality-gate workflow itself produced evidence correctly.
The blocking findings showed that TaskHost Local update files and a nested starter
repository had been committed to the Development Standard repository.

The branch rule remains disabled until a repair commit produces a successful run on
both operating systems and the `SASD merge gate` reports success.

Version 0.10.0 adds remote evidence capture and guarded ruleset management. The
tools verify the exact remote `main` commit, the Ubuntu and Windows matrix jobs,
and the aggregate merge gate before allowing activation. The desired ruleset is
committed as data but is not applied by merely copying or committing this update.

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

1. Apply the repository-boundary repair and this activation update.
2. Run the local quality gates.
3. Commit and push the repaired repository state.
4. Verify the exact remote commit with `capture-ci-activation.py --verify-only`.
5. Review the intended ruleset with `manage-main-ruleset.py --plan`.
6. Activate only after confirming the switch to branch and pull-request work.
7. Read the active ruleset back from GitHub.
8. Generate and commit the activation record and evidence JSON separately.

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
tooling/validate-ci-activation.py
tooling/capture-ci-activation.py
tooling/manage-main-ruleset.py
.github/rulesets/main-merge-gate.json
docs/50-reference-implementations/repository-self-hosting/
```

## References

- GitHub secure-use guidance: <https://docs.github.com/en/actions/reference/security/secure-use>
- GitHub ruleset status checks: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets>
- Dependabot updates for Actions: <https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions>

## Release Candidate preview workflow

Version 0.12.0 adds a separate, manually triggered, read-only preview workflow. It runs the canonical quality gates, builds deterministic Source and Markdown preview archives, verifies them, and uploads temporary evidence. The workflow does not possess write permissions and cannot create tags or GitHub Releases. Its existence is preparation evidence only; a successful run must be captured separately.
