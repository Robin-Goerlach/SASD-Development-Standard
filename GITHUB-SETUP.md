# GitHub Repository Setup

## Recommended repository settings

- **Name:** `SASD-Development-Standard`
- **Visibility:** Public
- **Default branch:** `main`
- **License:** MIT
- **Wiki:** Disabled initially; documentation remains versioned in the repository
- **Discussions:** Optional after the first public draft
- **Issues:** Enabled
- **Projects:** Optional; use only when the roadmap requires a board

## Description

> Open, practical development standard for solo developers and small teams. Defines repeatable project lifecycles, architecture, documentation, quality, security, testing, GitHub workflows, AI-assisted development, templates, checklists, and reference implementations.

## Suggested topics

- development-standard
- software-engineering
- software-architecture
- documentation
- quality-assurance
- secure-development
- dotnet
- csharp
- prompt-engineering
- ai-assisted-development
- open-source
- project-management

## Initial release strategy

Do not publish Version 1.0 immediately. Begin with a pre-release such as `v0.1.0` after the content architecture is approved.

## Repository CI recovery and activation

The repository contains `.github/workflows/quality-gates.yml`. The first remote
execution correctly exposed a repository-boundary violation. Do not enable a
required status check until the repair commit itself has passed on Ubuntu and
Windows.

### 1. Verify the repaired commit

After committing and pushing the controlled boundary repair:

```bash
python tooling/capture-ci-activation.py --verify-only
```

This command verifies that the current local commit is also the current remote
`main` commit and that the expected Ubuntu, Windows, and aggregate jobs all
completed successfully.

### 2. Review the intended ruleset

```bash
python tooling/manage-main-ruleset.py --plan
```

The governed payload is:

```text
.github/rulesets/main-merge-gate.json
```

It targets the default branch, blocks deletion and force pushes, and requires
`SASD merge gate` with the strict status-check policy.

### 3. Activate deliberately

```bash
python tooling/manage-main-ruleset.py \
  --activate \
  --confirm-switch-to-pull-requests
```

Activation requires a token with repository `Administration: write`. The token
must be supplied through `GITHUB_TOKEN`, `GH_TOKEN`, or an authenticated GitHub
CLI session and is never stored in the repository.

After activation, normal changes use a branch and pull request. A direct push to
`main` cannot already possess the required successful check.

### 4. Capture the activated state

```bash
python tooling/capture-ci-activation.py --write --require-active-ruleset
```

Complete
`checklists/releases/REPOSITORY-CI-ACTIVATION-CHECKLIST.md` and commit the
activation record and evidence JSON in a separate evidence commit.

The complete procedure and rollback path are documented in
`docs/50-reference-implementations/repository-self-hosting/`.

## Actions security settings

- Keep default workflow permissions read-only.
- Do not enable workflows to create or approve pull requests unless an approved
  use case requires it.
- Review Dependabot pull requests for GitHub Actions rather than merging them
  without a successful quality-gate run.
- Preserve full-SHA action pins and the same-line release comments.


## Repository-boundary prerequisite

Before enabling `SASD merge gate` as a required check, confirm that
`python tooling/validate-repository-boundary.py` passes and that no foreign project
root or nested repository copy is present. The first CI run exposed such a boundary
violation; branch protection remains intentionally disabled until the repair commit
passes on Ubuntu and Windows.


## Release Candidate preview workflow

`.github/workflows/release-candidate-preview.yml` is intentionally manual and read-only. It runs all repository quality gates, builds deterministic preview archives, verifies checksums and safe paths, and uploads the result as a temporary Actions artifact. It cannot create a tag or GitHub Release.

Run it from **Actions → SASD Release Candidate Preview → Run workflow** only after the branch commit has passed the normal `SASD Quality Gates`. Publication of `v1.0.0-rc.1` remains a separate Maintainer decision using the completed Release Record and RC checklist.


## Prompt-package preview workflow

`.github/workflows/prompt-package-preview.yml` is manual and read-only. It runs the repository quality gates, builds the deterministic candidate prompt package, verifies checksums and ZIP safety, and uploads the result for 14 days. It does not modify Prompt Manager data, create a release, or claim application-version compatibility.

Run it from **Actions → SASD Prompt Package Preview → Run workflow** after the current commit has passed the standard quality gates.
