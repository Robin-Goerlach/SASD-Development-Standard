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
4. Review the [`Governance Overview`](docs/40-governance/README.md), the [`Foundation & Governance Approval Record`](docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-0.8.0.md), and then the rules for [`Normative Language`](docs/40-governance/NORMATIVE-LANGUAGE.md), [`Document Lifecycle`](docs/40-governance/DOCUMENT-LIFECYCLE.md), and [`Document Metadata`](docs/40-governance/DOCUMENT-METADATA.md).
5. Review the [`Core Standard`](docs/10-core-standard/README.md), starting with the [`Quality Levels`](docs/10-core-standard/QUALITY-LEVELS.md).
6. Review the [`C#/.NET Profile`](docs/20-profiles/dotnet/README.md) when working on a .NET project.
7. Apply the [`Desktop Application Profile`](docs/20-profiles/desktop/README.md) for WinForms or WPF applications.
8. Use the [`Operational Process Handbook`](docs/30-processes/README.md) to classify, initialize, review, migrate, release, and archive projects.
9. Review the [`Reference Implementation Program`](docs/50-reference-implementations/README.md) and [`Pilot 01 – SASD TaskHost Local`](docs/50-reference-implementations/pilot-01-sasd-taskhost-local/README.md).
10. Follow the [`Roadmap`](ROADMAP.md).
11. Use the [`New Project Checklist`](checklists/project-initiation/NEW-PROJECT-CHECKLIST.md), the [`.NET Profile Adoption Checklist`](checklists/project-initiation/DOTNET-PROFILE-ADOPTION-CHECKLIST.md), and for desktop projects the [`Desktop Profile Adoption Checklist`](checklists/project-initiation/DESKTOP-PROFILE-ADOPTION-CHECKLIST.md).
12. Record important technical decisions using the [`ADR Template`](templates/architecture-decisions/ADR-TEMPLATE.md).
13. Run the local repository quality gates with `python tooling/run-quality-gates.py` or the scripts in [`scripts/`](scripts/README.md).

## Normative language

The following terms are used intentionally:

- **MUST**: mandatory requirement,
- **SHOULD**: recommended requirement; deviations require a reason,
- **MAY**: optional practice.

The exact interpretation is defined in [`NORMATIVE-LANGUAGE.md`](docs/40-governance/NORMATIVE-LANGUAGE.md). Documents become binding only after reaching the `Approved` state defined by the document lifecycle.

## Project status

The project is currently in the **first pilot execution and normative-baseline development phase**. Foundation and Governance are formally approved as version 0.8.0 and provide the binding organizational basis for further work. The technology-independent Core is available as Proposed 0.3.0, the C#/.NET Profile as Proposed 0.4.0, the Desktop Application Profile as Proposed 0.5.0, and all seven operational processes as Proposed 0.6.0. The Foundation/Governance approval is not yet a stable Version 1.0 release.

Repository CI is implemented with cross-platform local and GitHub quality gates. The first remote execution exposed a repository-boundary violation; the repair, remote recovery proof, and activation of the required `SASD merge gate` ruleset remain deliberately separated evidence steps. The self-hosting activation procedure is documented under [`docs/50-reference-implementations/repository-self-hosting/`](docs/50-reference-implementations/repository-self-hosting/).

Current priorities:

1. commit the repository-boundary repair and confirm a green Ubuntu and Windows CI run for the exact commit,
2. capture the remote evidence and activate the governed `SASD merge gate` ruleset,
3. execute Wave 01 of Pilot 01 on SASD TaskHost Local and record verified evidence,
4. refine repository templates and assessment tooling from pilot feedback,
5. select the medium and complex pilot projects,
6. complete and review the prompt packages,
7. move Core, profiles, and processes toward approval.

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

Pilot 01 (SASD TaskHost Local) is `In Execution`. A Wave 01 update artifact has been prepared and statically reviewed, while target commit, .NET build/test, Windows runtime and CI verification remain pending. See `docs/50-reference-implementations/`.
