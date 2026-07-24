# Wave 01 Verification Update Manifest

## Target

- Repository: `Robin-Goerlach/SASD-TaskHost-Local`
- Required predecessor: Wave 01 implementation update
- Update purpose: make Wave 01 executable, evidence-producing and formally closable

## Added

- headless product self-check and JSON report,
- integration tests for the self-check,
- unified local/CI verification script,
- guarded closeout script,
- evidence-producing GitHub Actions workflow,
- verification, closeout and CI-evidence documentation,
- commit-bound manual test record template,
- extended static validator.

## Changed

- application entry point supports `--self-check`,
- CI executes the repository-owned verification script,
- README and changelog describe the evidence workflow,
- Wave 01 review points to the formal verification gate.

## Explicitly not claimed

This update does not claim that:

- restore, build or tests have run successfully,
- GitHub Actions has passed,
- the WinForms UI has started,
- an existing user database has been verified,
- Wave 01 is complete.

Those statements require generated evidence after the update has been committed and executed.
