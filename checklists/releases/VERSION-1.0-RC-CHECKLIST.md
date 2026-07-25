# Version 1.0 Release-Candidate Checklist

## Repository and identity

- [ ] Work is performed in `Robin-Goerlach/SASD-Development-Standard`.
- [ ] Working tree is clean.
- [ ] Releasecommit is pushed and exactly identified.
- [ ] Repository boundary and manifest checks pass.

## Normative basis

- [ ] All 46 required normative documents are `Approved`.
- [ ] Approval Records and SHA-256 manifests are valid.
- [ ] No unapproved normative change was introduced after approval.
- [ ] Version and authoritative language are explicit.

## CI and governance

- [ ] Ubuntu validation passed for the releasecommit.
- [ ] Windows validation passed for the releasecommit.
- [ ] `SASD merge gate` passed for the releasecommit.
- [ ] Ruleset state is recorded.
- [ ] Any deferral is explicitly approved and time-bounded.

## Pilot evidence

- [ ] Small, Medium and Large baselines are documented.
- [ ] At least one pilot wave is technically verified with `Passed`.
- [ ] Pilot commit, build, test, runtime and CI evidence are referenced.
- [ ] Lessons learned and remaining limitations are visible.

## Release documents

- [ ] Release Notes are complete and user-oriented.
- [ ] Release Record contains commit, CI, artifacts and decision.
- [ ] Known Issues are reviewed.
- [ ] Changelog contains the RC entry.
- [ ] No `Pending` value remains in fields required for publication.

## Artefacts

- [ ] Source archive built from clean releasecommit.
- [ ] Markdown archive built from the same commit.
- [ ] Release manifest generated.
- [ ] SHA256SUMS generated.
- [ ] Independent verifier passed.
- [ ] A second build produced identical hashes.

## Publication

- [ ] Annotated tag `v1.0.0-rc.1` targets the approved commit.
- [ ] GitHub Release is marked Pre-release.
- [ ] Uploaded artifacts match the verified hashes.
- [ ] Downloaded release artifacts were reverified.
- [ ] Release URL and final decision are recorded.
