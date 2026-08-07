# SASD Development Standard

> An open, practical development standard for reproducible, understandable, secure, and maintainable technical projects.

[![Status](https://img.shields.io/badge/status-specification%20candidate-orange)](PROJECT-STATUS.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![SASD Quality Gates](https://github.com/Robin-Goerlach/SASD-Development-Standard/actions/workflows/quality-gates.yml/badge.svg)](https://github.com/Robin-Goerlach/SASD-Development-Standard/actions/workflows/quality-gates.yml)
[![Authoritative language](https://img.shields.io/badge/authoritative%20language-German-lightgrey)](docs/40-governance/NORMATIVE-LANGUAGE.md)

## Start here

You do **not** need to read the complete standard before starting productive work.

SASD uses **progressive disclosure**: begin with the smallest useful entry path, then open the deeper specification only when your project, risk, quality level, or lifecycle stage requires it.

### I am starting a new project

1. Read the compact [`QUICKSTART.md`](QUICKSTART.md).
2. Create a short [`PROJECT-BRIEF`](templates/documents/PROJECT-BRIEF-TEMPLATE.md).
3. Classify the project only far enough to choose the appropriate quality level and profiles.
4. Establish a reproducible repository, build, and test baseline.
5. Go deeper when the project actually needs more requirements, architecture, security, release, or maintenance detail.

For a compact solo workflow, see the [`Solo Developer Guide`](docs/10-core-standard/SOLO-DEVELOPER-GUIDE.md).

### I am adopting SASD in an existing project

Start with the [`Legacy Migration Process`](docs/30-processes/LEGACY-MIGRATION.md). It is designed to preserve working software and introduce SASD proportionally rather than forcing a cosmetic rewrite.

### I maintain or review the SASD Development Standard

Start with [`PROJECT-STATUS.md`](PROJECT-STATUS.md), the [`Version 1.0 Specification Baseline`](docs/40-governance/VERSION-1.0-SPECIFICATION-BASELINE.md), and the [`Governance`](docs/40-governance/README.md) area.

## What SASD is

The **SASD Development Standard** defines a repeatable way to turn an idea into a maintainable technical product. It covers the project lifecycle rather than only source-code conventions:

- scope, requirements, architecture, and technical decisions,
- implementation quality, testing, security, and privacy,
- documentation, repositories, releases, maintenance, and archival,
- knowledge retention and responsible AI-assisted development.

It is aimed primarily at solo developers, freelancers, open-source maintainers, administrators with development tasks, learners with professional ambitions, and small technical teams.

The goal is not to maximize documentation. The goal is to preserve enough intent, evidence, and reproducibility that the product remains understandable and maintainable.

## Three views of the repository

| View | Use it when | Start with |
|---|---|---|
| **Using SASD** | You are building or maintaining a product | [`QUICKSTART.md`](QUICKSTART.md), [processes](docs/30-processes/README.md), [templates](templates/), [checklists](checklists/) |
| **SASD Specification** | You need the binding rule, rationale, profile, or process detail | [Core Standard](docs/10-core-standard/README.md), [profiles](docs/20-profiles/), [processes](docs/30-processes/README.md) |
| **Maintaining SASD** | You maintain this standard, its baselines, releases, pilots, or validation infrastructure | [`PROJECT-STATUS.md`](PROJECT-STATUS.md), [governance](docs/40-governance/README.md), [reference implementations](docs/50-reference-implementations/README.md), [tooling](tooling/) |

The documentation index in [`docs/README.md`](docs/README.md) follows the same separation.

## Standard and tooling are different things

> **The SASD Development Standard defines the rules, expected outcomes, and evidence. The SASD tooling supports and automates their application.**

The Python validators, schemas, workflows, generators, checklists, templates, and prompt packages in this repository are valuable supporting assets. They do not silently create new normative requirements, and the standard is not a runtime dependency on this repository's specific Python or CI environment.

A project must still satisfy applicable normative requirements and required evidence. Where a normative rule does not mandate a specific mechanism, equivalent project-appropriate automation or evidence may be used.

## Current status

The repository is a **Version 1.0 Specification Candidate**:

- the normative baseline is Approved,
- the specification is complete enough for practical application and evaluation,
- repository quality gates and the TaskHost remote technical baseline have passed,
- practical reference validation is still pending,
- Version `1.0.0` is **not** yet released.

> **Die Theorie ist vollständig genug, um praktisch angewendet und bewertet zu werden. Ihre Praxistauglichkeit ist noch nicht abschließend bestätigt.**

See [`PROJECT-STATUS.md`](PROJECT-STATUS.md) for the evidence-backed status and current release blockers.

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Foundation, normative specification, processes, governance, and pilot evidence |
| `templates/` | Reusable project and evidence templates |
| `checklists/` | Operational review and readiness aids |
| `examples/` | Examples that illustrate application without adding requirements |
| `prompts/` | Versioned AI-assisted work aids; not the normative core |
| `tooling/`, `scripts/`, `.github/` | Automation and validation for the standard and supported workflows |

## Normative authority

The authoritative normative language is German. The binding content is defined by Approved normative documents and the precedence rules in the [`Content Architecture`](docs/00-foundation/CONTENT-ARCHITECTURE.md) and [`Normative Language`](docs/40-governance/NORMATIVE-LANGUAGE.md).

Informative guides, examples, templates, checklists, prompts, and tooling support application but cannot silently introduce new normative obligations.

## Contributing, security, and license

- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [MIT License](LICENSE)
