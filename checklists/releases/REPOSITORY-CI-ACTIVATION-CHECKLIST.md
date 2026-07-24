# Repository CI Activation Checklist

Complete this checklist after the CI implementation commit has been pushed.

## Committed revision

- Commit SHA:
- Push date:
- Workflow run URL:

## Automated evidence

- [ ] Ubuntu validation completed successfully.
- [ ] Windows validation completed successfully.
- [ ] `SASD merge gate` completed successfully.
- [ ] Evidence artifacts were uploaded for both operating systems.
- [ ] `quality-gates.json` reports `passed` for both jobs.
- [ ] The readiness report still describes non-Approved documents accurately.

## Repository settings

- [ ] Actions workflow permissions are set to read repository contents by default.
- [ ] Dependabot version updates are enabled or the committed configuration is recognized.
- [ ] A branch ruleset or protection rule targets `main`.
- [ ] `SASD merge gate` is selected as a required status check.
- [ ] Direct-push behavior is intentionally decided for the solo-maintainer phase.
- [ ] The ruleset is not enabled before the first successful check exists.

## Closeout

- [ ] Any first-run defect was corrected in a separate commit.
- [ ] The final successful commit and workflow URL are recorded.
- [ ] No release or normative approval is inferred solely from CI success.
- [ ] Activation result is recorded in the changelog or a dedicated implementation record.
