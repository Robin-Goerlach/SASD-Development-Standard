# Security Policy

## Reporting security issues

Do not publish vulnerabilities, exposed secrets, or exploitable weaknesses in a public issue.

Until a dedicated private reporting channel is established, contact the repository owner privately through an available GitHub contact method.

## Scope

This repository primarily contains documentation, templates, prompts, and development tooling. Security reports may concern:

- unsafe example configurations,
- exposed credentials or personal data,
- insecure templates,
- vulnerable tooling dependencies,
- guidance that could lead to insecure implementations.

## Supported versions

Before Version 1.0, only the latest repository state is maintained.
## CI and workflow security

Repository workflows use read-only permissions and pin external actions to full commit SHAs. Checkout credentials are not persisted. Dependabot monitors GitHub Actions references for updates. Changes to `.github`, `tooling`, and governance-sensitive documents should receive explicit maintainer review.

A workflow file or a successful local validation does not prove that GitHub Actions ran successfully for a committed revision. Use the workflow run and its uploaded evidence artifact as the execution record.

