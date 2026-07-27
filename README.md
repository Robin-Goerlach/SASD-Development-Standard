# SASD Development Standard

> An open, practical development standard for reproducible, understandable, secure, and maintainable technical projects.

[![Status](https://img.shields.io/badge/status-pre--1.0-orange)](#project-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![SASD Quality Gates](https://github.com/Robin-Goerlach/SASD-Development-Standard/actions/workflows/quality-gates.yml/badge.svg)](https://github.com/Robin-Goerlach/SASD-Development-Standard/actions/workflows/quality-gates.yml)
[![Language](https://img.shields.io/badge/normative%20draft-German-lightgrey)](#language)

## Overview

The **SASD Development Standard** defines a complete and repeatable way to turn an idea into a maintainable technical product. It focuses not only on programming, but on the entire lifecycle of a project:

- project initiation and scope,
- requirements and architecture,
- repository and documentation structure,
- implementation quality,
- testing and reviews,
- security and privacy,
- releases and maintenance,
- knowledge management,
- prompt engineering and responsible AI-assisted development.

The standard is designed primarily for solo developers, freelancers, open-source maintainers, students, trainees, administrators with development tasks, and small technical teams.

## Vision

Every project created under the SASD Development Standard should remain understandable, reproducible, testable, and maintainable—even years later and by someone who did not originally create it.

Knowledge must not exist only in a developer's head, in temporary chats, or in undocumented routines.

## Core question

The standard does not primarily answer:

> How do I program?

It answers:

> How do I develop, document, test, release, operate, and maintain a professional technical project?

## Three product layers

```mermaid
flowchart LR
    A[Standard] --> B[Reference Implementations]
    A --> C[Development Tooling]
    B --> A
    C --> A
```

### 1. Standard

The normative rules, principles, profiles, processes, templates, and checklists.

### 2. Reference implementations

Existing SASD projects that demonstrate how the standard is applied in practice. The first focus is the consolidation of the SASD C#/.NET codebase.

### 3. Development tooling

Reusable files and tools that help create and verify compliant projects, such as `.editorconfig`, `Directory.Build.props`, repository templates, analyzers, checks, and prompt packages.

## Quality levels

The standard uses scalable quality levels so that small utilities are not burdened with the same requirements as production systems.

| Level | Intended use |
|---|---|
| **SASD Minimum** | Small tools, learning projects, experiments, and prototypes |
| **SASD Recommended** | Maintained applications, public repositories, and regular SASD projects |
| **SASD Production** | Business-critical, security-sensitive, customer-facing, or operational systems |

## Version 1.0 scope

Version 1.0 is intended to provide a stable foundation consisting of:

- a technology-independent core standard,
- a repository and documentation model,
- project lifecycle and governance rules,
- quality levels,
- fundamental testing and security requirements,
- a C#/.NET profile,
- a desktop application profile,
- GitHub conventions,
- prompt engineering guidance,
- reusable templates and checklists,
- initial technical configuration files,
- pilot migrations of selected SASD repositories.

Detailed Linux, database, Docker, Kubernetes, and advanced security profiles are part of the long-term vision but are not required to complete Version 1.0.

## Repository structure

```text
.
├── docs/
│   ├── 00-foundation/
│   ├── 10-core-standard/
│   ├── 20-profiles/
│   ├── 30-processes/
│   ├── 40-governance/
│   └── 50-reference-implementations/
├── templates/
├── checklists/
├── prompts/
├── tooling/
├── examples/
├── artefacts/
└── .github/
```

See the [content architecture](docs/00-foundation/CONTENT-ARCHITECTURE.md) and the [Version 1.0 document catalog](docs/00-foundation/DOCUMENT-CATALOG.md) for the planned standard structure.

## Getting started

1. Read the [`Project Charter`](docs/00-foundation/PROJECT-CHARTER.md).
2. Review the [`Version 1.0 Scope`](docs/00-foundation/SCOPE.md).
3. Review the [`Content Architecture`](docs/00-foundation/CONTENT-ARCHITECTURE.md) and [`Document Catalog`](docs/00-foundation/DOCUMENT-CATALOG.md).
4. Review the [`Governance Overview`](docs/40-governance/README.md), the [`Foundation & Governance Approval Record`](docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-0.8.0.md), and the rules for [`Normative Language`](docs/40-governance/NORMATIVE-LANGUAGE.md), [`Document Lifecycle`](docs/40-governance/DOCUMENT-LIFECYCLE.md), and [`Document Metadata`](docs/40-governance/DOCUMENT-METADATA.md).
5. Review the [`Normative Baseline Approval 0.9.0`](docs/40-governance/NORMATIVE-BASELINE-APPROVAL-0.9.0.md), its [`Approval Manifest`](docs/40-governance/NORMATIVE-BASELINE-APPROVAL-MANIFEST-0.9.0.md), and the preceding [`Integrated Review`](docs/40-governance/NORMATIVE-BASELINE-REVIEW-0.9.0.md).
6. Review the [`Core Standard`](docs/10-core-standard/README.md), starting with the [`Quality Levels`](docs/10-core-standard/QUALITY-LEVELS.md).
7. Review the [`C#/.NET Profile`](docs/20-profiles/dotnet/README.md) when working on a .NET project.
8. Apply the [`Desktop Application Profile`](docs/20-profiles/desktop/README.md) for WinForms or WPF applications.
9. Use the [`Operational Process Handbook`](docs/30-processes/README.md) to classify, initialize, review, migrate, release, and archive projects.
10. Review the [`Reference Implementation Program`](docs/50-reference-implementations/README.md), [`Pilot 01 – SASD TaskHost Local`](docs/50-reference-implementations/pilot-01-sasd-taskhost-local/README.md), [`Pilot 02 – SASD Prompt Manager`](docs/50-reference-implementations/pilot-02-sasd-prompt-manager/README.md), and [`Pilot 03 – SASD Mail Workbench`](docs/50-reference-implementations/pilot-03-sasd-mail-workbench/README.md).
11. Follow the [`Roadmap`](ROADMAP.md).
12. Use the [`New Project Checklist`](checklists/project-initiation/NEW-PROJECT-CHECKLIST.md), the [`.NET Profile Adoption Checklist`](checklists/project-initiation/DOTNET-PROFILE-ADOPTION-CHECKLIST.md), and for desktop projects the [`Desktop Profile Adoption Checklist`](checklists/project-initiation/DESKTOP-PROFILE-ADOPTION-CHECKLIST.md).
13. Record important technical decisions using the [`ADR Template`](templates/architecture-decisions/ADR-TEMPLATE.md).
14. Review and build the [`SASD Prompt Package`](prompts/README.md) when using AI-assisted project workflows.
15. Run the local repository quality gates with `python tooling/run-quality-gates.py` or the scripts in [`scripts/`](scripts/README.md).

## Normative language

The following terms are used intentionally:

- **MUST**: mandatory requirement,
- **SHOULD**: recommended requirement; deviations require a reason,
- **MAY**: optional practice.

The exact interpretation is defined in [`NORMATIVE-LANGUAGE.md`](docs/40-governance/NORMATIVE-LANGUAGE.md). Documents become binding only after reaching the `Approved` state defined by the document lifecycle.

## Project status

The project is currently in the **Approved normative-baseline and release-candidate preparation phase**. Foundation and Governance remain Approved as version 0.8.0. The 13 Core documents, eight C#/.NET documents, four Desktop documents, and seven operational processes are formally approved as the unified **Approved 0.9.0 normative baseline**. This approval is not yet a GitHub release, a release candidate, or a stable Version 1.0 release.

The approval is intentionally separated from remote CI evidence and publication. Ubuntu, Windows, and `SASD merge gate` validation for the Approval commit, the open TaskHost Local Wave 01 verification, and repository-ruleset evidence remain documented release conditions. The self-hosting procedure is documented under [`docs/50-reference-implementations/repository-self-hosting/`](docs/50-reference-implementations/repository-self-hosting/).

Current priorities:

1. close the exact-commit Ubuntu, Windows, and `SASD merge gate` evidence,
2. verify at least one practical pilot wave, beginning with TaskHost Local,
3. activate or explicitly defer the governed `main` ruleset,
4. build and independently verify the `1.0.0-rc.1` preview archives,
5. complete the Release Record, Known Issues, and Maintainer decision,
6. publish and practically review `1.0.0-rc.1`,
7. produce and visually inspect Word and PDF artefacts before stable `1.0.0`.

## Version 1.0 Release Candidate preparation

The repository now contains a controlled plan for `1.0.0-rc.1`, an explicit blocker register, a generated readiness report, draft Release Notes and Release Record, deterministic archive tooling, independent verification, and a read-only manually triggered preview workflow.

Start with the [`Release Candidate Plan`](docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-PLAN.md) and the generated [`Release Candidate Readiness`](docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md). A preview package can be built locally with:

```bash
python tooling/run-quality-gates.py
python tooling/build-release-candidate.py --mode preview
python tooling/verify-release-candidate.py --directory artifacts/release-candidate
```

Preview mode creates no tag and publishes no GitHub Release. Release mode remains blocked until the readiness report has no open blocking checks.

## SASD Prompt Package

The repository contains the candidate `sasd-development-standard-v1` prompt package with **39 versioned prompts**, **nine lifecycle categories**, a registry of **35 variables**, generated catalogs and checksums, JSON schemas, deterministic archive tooling, and independent artifact verification.

```bash
python tooling/validate-prompt-packages.py
python tooling/build-prompt-package.py --clean --output-dir artifacts/prompt-packages
python tooling/verify-prompt-package.py --directory artifacts/prompt-packages
```

The package is the canonical SASD exchange format. Direct import into a specific SASD Prompt Manager build is intentionally not claimed until an exact-version adapter passes the documented import/export roundtrip.

## Language

The normative pre-1.0 draft is initially written in German to allow precise development and review. An English edition is planned once the structure and terminology have stabilized.


## Repository identity and update packages

This repository declares its canonical identity in `REPOSITORY-IDENTITY.json`.
Repository quality gates reject foreign project roots, nested repository copies, and
unexpected top-level content. Update packages that require deletions must be applied
through a repository-aware script or patch; ZIP extraction alone is only suitable for
purely additive overlays.

## Contributing

The project is currently developed as a SASD reference initiative. Contributions, reviews, and experience reports are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This repository is licensed under the [MIT License](LICENSE), unless a document or included third-party material states otherwise.

## Current pilot status

The Version 1.0 portfolio now covers all three required project sizes. Pilot 01 (TaskHost Local) is `In Execution` with an unverified Wave 01 artifact. Pilot 02 (Prompt Manager) and Pilot 03 (Mail Workbench) are `Baseline Assessed`; their target commits, local builds, tests, runtime checks and migration evidence remain pending. See [`VERSION-1.0-PILOT-READINESS.md`](docs/50-reference-implementations/VERSION-1.0-PILOT-READINESS.md).
