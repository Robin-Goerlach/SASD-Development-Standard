# Repository CI Review Checklist

Use this checklist when reviewing a change to the standard repository's CI.

## Workflow safety

- [ ] Workflow permissions remain read-only unless an approved change requires more.
- [ ] Every external action is pinned to a full 40-character commit SHA.
- [ ] The release tag or version is documented on the same line as the SHA.
- [ ] Checkout does not persist credentials.
- [ ] `pull_request_target` is not used.
- [ ] Untrusted event content is not interpolated into shell commands.
- [ ] Every job has a timeout.
- [ ] Concurrent obsolete runs are cancelled.

## Validation behavior

- [ ] Local and GitHub execution use `tooling/run-quality-gates.py`.
- [ ] Blocking checks fail the workflow when they fail.
- [ ] The readiness report remains informational until the release gate requires approval.
- [ ] Ubuntu and Windows both run the full validation set.
- [ ] Evidence is uploaded on success and failure.
- [ ] The stable merge check remains named `SASD merge gate`.

## Repository integration

- [ ] Dependabot monitors GitHub Actions.
- [ ] CODEOWNERS covers `.github`, `tooling`, Foundation, and Governance.
- [ ] `REPOSITORY-MANIFEST.txt` is regenerated after file additions or removals.
- [ ] README, contributing guidance, workflow documentation, and changelog remain consistent.
- [ ] No successful CI execution is claimed without a run linked to the committed revision.
