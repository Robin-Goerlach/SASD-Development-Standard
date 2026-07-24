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

## Repository CI activation

The repository contains `.github/workflows/quality-gates.yml`. Before enabling
a required status check:

1. commit and push the CI update,
2. open **Actions → SASD Quality Gates**,
3. confirm successful Ubuntu and Windows validation,
4. confirm the aggregate check named `SASD merge gate`,
5. inspect the uploaded evidence artifacts,
6. only then create or update the `main` branch ruleset.

Recommended `main` ruleset settings for the current solo-maintainer phase:

- require the status check `SASD merge gate`,
- decide deliberately whether direct pushes remain allowed,
- do not require an approving review from another person while no second
  maintainer exists,
- do not enable a merge queue for the current low-volume repository,
- keep force pushes and branch deletion disabled.

The required check must already have run successfully before it can be selected
reliably in repository rules. The completed activation should be recorded using
`checklists/releases/REPOSITORY-CI-ACTIVATION-CHECKLIST.md`.

## Actions security settings

- Keep default workflow permissions read-only.
- Do not enable workflows to create or approve pull requests unless an approved
  use case requires it.
- Review Dependabot pull requests for GitHub Actions rather than merging them
  without a successful quality-gate run.
- Preserve full-SHA action pins and the same-line release comments.

