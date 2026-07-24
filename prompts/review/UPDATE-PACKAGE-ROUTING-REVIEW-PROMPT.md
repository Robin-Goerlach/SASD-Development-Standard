# SASD Update Package Routing Review Prompt

Review the supplied update package before it is applied.

Determine and report:

1. the exact canonical target repository,
2. the repository markers that prove the current directory is that target,
3. whether the package only adds/replaces files or also requires deletions,
4. whether direct ZIP extraction is safe,
5. which existing files may be overwritten,
6. which validation commands must run before commit,
7. which claims remain unverified until CI or runtime execution,
8. the exact rollback procedure.

Reject the application when the target repository cannot be established unambiguously.
Do not infer successful deletion from ZIP extraction and do not treat test or workflow
source files as evidence that tests or CI have passed.
