# Prompt: Review Version 1.0 Release Candidate

Review the proposed SASD Development Standard `1.0.0-rc.1` without assuming that prepared tooling or documents prove successful execution.

## Required inputs

- exact repository and commit,
- Release Candidate Plan,
- blocker register,
- release readiness report,
- Release Record,
- Release Notes,
- Known Issues,
- quality-gate evidence,
- pilot evidence,
- release manifest and checksums.

## Review tasks

1. Confirm that all normative documents are Approved and unchanged from their approval manifests.
2. Confirm Ubuntu, Windows and `SASD merge gate` for the exact releasecommit.
3. Confirm at least one practically executed pilot with build, tests and runtime evidence.
4. Distinguish active ruleset evidence from a committed ruleset template.
5. Verify release archives, checksums, safe paths and reproducibility.
6. Identify every remaining `Pending`, unresolved blocker or unstated exception.
7. Check that Release Notes accurately describe limitations and pre-release status.
8. Recommend one of: Approve RC, Approve with explicit temporary decision, or Do not approve.

Do not approve based only on source code, workflow files, test files, generated templates or local static validation.
