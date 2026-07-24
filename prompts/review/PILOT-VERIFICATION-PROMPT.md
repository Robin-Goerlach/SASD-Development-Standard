# Pilot Wave Verification Prompt

Review the supplied target-repository commit against the pilot wave plan.

Rules:

1. Distinguish source inspection, prepared artifacts, local execution, CI execution and reported claims.
2. Do not call a defect fixed unless the original scenario or an equivalent regression test is demonstrated.
3. Record exact commands, environment, commit ID, exit results and evidence locations.
4. Check fresh-data, existing-data, failure and rollback scenarios where applicable.
5. Treat an existing workflow file as configuration, not as a successful CI run.
6. Update each gap to Open, Artifact Prepared, Evidence Pending, Closed, Not Applicable or Exception.
7. Stop the next wave when a blocker, data-integrity risk or unverified migration remains.

Produce:

- verification summary,
- command/result table,
- runtime and data scenarios,
- CI evidence,
- failed or missing criteria,
- updated gap recommendations,
- decision: Passed, Partial or Failed.
