---
title: "C#/.NET Quality Level Matrix"
document-id: SASD-REF-DOTNET-005
document-type: informative
status: Draft
version: 0.4.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [DotNet]
depends-on: [SASD-PROF-DOTNET-001, SASD-CORE-006]
generated: false
---

# C#/.NET Quality Level Matrix

## Zweck

Diese informative Übersicht konsolidiert die wichtigsten Skalierungen der acht Profildokumente. Im Konfliktfall gilt das jeweilige normative Quelldokument.

| Control | Minimum | Recommended | Production | Source |
|---|---|---|---|---|
| .NET support | supported stable | supported LTS preferred | supported LTS or approved exception | [Profile](DOTNET-PROFILE.md) |
| SDK pinning | documented | `global.json` preferred | pinned and controlled | [Profile](DOTNET-PROFILE.md) |
| clean build | local reproducible | script or CI | automated clean build | [Profile](DOTNET-PROFILE.md) |
| nullable | new code enabled | enabled | enabled and warnings reviewed | [Coding](CODING-STANDARD.md) |
| analyzer | compiler | quality analyzer | quality and security gates | [Coding](CODING-STANDARD.md) |
| solution layers | minimal | responsibility-based | enforced critical boundaries | [Structure](SOLUTION-STRUCTURE.md) |
| error boundary | executable app preferred | required | required and operationally tested | [Errors](ERROR-HANDLING.md) |
| correlation | optional | preferred | required for multi-step operations | [Logging](LOGGING.md) |
| log retention | when files used | defined | defined and enforced | [Logging](LOGGING.md) |
| typed options | preferred | required | required and startup-validated | [Configuration](CONFIGURATION.md) |
| secrets | protected source | protected store | Production secret mechanism | [Configuration](CONFIGURATION.md) |
| migrations | when schema exists | reproducible | tested and released | [Persistence](PERSISTENCE.md) |
| backup/restore | for valuable data | required / restore tested | automated and regularly tested | [Persistence](PERSISTENCE.md) |
| integration tests | when relevant | required | Production-near required | [Testing](DOTNET-TESTING.md) |
| CI | optional with reproducible script | required | required with quality gates | [Testing](DOTNET-TESTING.md) |
| publish/install tests | for distribution preferred | required | required on target platforms | [Testing](DOTNET-TESTING.md) |
