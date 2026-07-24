# Changelog

All notable changes to the SASD Development Standard will be documented in this file.

The format is based on Keep a Changelog principles, and the project intends to use Semantic Versioning once the first public versioning policy is approved.

## [Unreleased]

### Added

- Complete Proposed 0.8.0 Foundation and Governance baseline covering normative language, document lifecycle, metadata, versioning, change control, exceptions, Alignment and Version 1.0 acceptance gates.
- 232 stable Governance requirement IDs, generated requirement index, responsibility map, review record and approval-readiness record.
- Standard change proposal, document approval, release record and deprecation templates.
- Foundation/Governance approval, standard change review and release governance checklists.
- Governance review and release-readiness prompts, Governance validator and Version 1.0 readiness reporter.

- Pilot evidence class `A` for prepared artifacts and separate implementation/verification state tracking.
- Wave 01 implementation review, verification plan, interim retrospective, expanded evidence map, and updated gap/decision records for TaskHost Local.
- Pilot feedback log and generated summary capturing eight findings from the first implementation artifact.
- Implementation-review, verification-record, and standard-feedback templates; verification checklists and prompt.
- Extended pilot manifest schema 1.1, portfolio generation, feedback generation, and validation tooling.


- Reference-implementation pilot program, evidence model, machine-readable pilot manifests, generated portfolio, selection/baseline/wave/closeout checklists, pilot templates, and execution/retrospective prompts.
- Pilot 01 for SASD TaskHost Local with charter, Recommended classification, public baseline assessment, 15-item gap register, staged migration plan, executable Wave 01 plan, evidence map, decision log, and preparation review.
- Dependency-free pilot portfolio generator and reference-pilot validator.
- Target-layout example showing proportional Wave 01 additions without forcing `src/` migration or multiple production assemblies.


- Complete Proposed 0.6.0 operational process handbook for project classification, new-project initialization, architecture decisions, reviews, legacy migration, releases, and project archival.
- Stable operational process requirement IDs with generated requirement index and quality-level matrix.
- Process map, documented process review, project classification and initialization records, ADR index, review record, migration assessment and plan, release record, and project archival record.
- Classification, ADR, review, legacy migration, release readiness, and archival checklists.
- Project classification, ADR preparation, legacy migration review, and release preparation prompt templates.
- Process examples and dependency-free operational-process validator and generators.


- Complete Proposed 0.5.0 Desktop Application Profile covering technology selection, UI architecture, user experience, accessibility, application lifecycle, publishing, installation, updates, and support.
- 215 stable Desktop profile requirement IDs with generated requirement index and consolidated quality-level matrix.
- WinForms and WPF implementation guidance, desktop project sizing guide, primary-source reference baseline, and documented profile review.
- Desktop adoption, UX review, and release smoke-test checklists.
- Desktop application brief, UX test report, deployment plan, and profile assessment templates.
- Initial WinForms and WPF project-file templates, desktop structure examples, review prompt, validator, and requirements-index generator.

- Complete Proposed 0.4.0 C#/.NET Profile covering SDK and runtime baseline, solution structure, coding conventions, error handling, logging, configuration, persistence, and testing.
- 277 stable C#/.NET profile requirement IDs with generated requirement index and curated quality-level matrix.
- .NET Reference Baseline, project sizing guidance, and documented profile review.
- Initial `Directory.Build.props`, `Directory.Packages.props`, `global.json`, `.editorconfig`, and GitHub Actions templates for .NET repositories.
- .NET adoption and code-review checklists, profile assessment template, review prompt, and proportional structure examples.
- Dependency-free .NET profile validator and requirements-index generator.

- Core responsibility map separating primary ownership from intentional cross-cutting controls.
- Solo-developer guide with compact artefact sets, role combination, and self-review practices.
- Documented Core Standard consistency and proportionality review for Proposed 0.3.0.
- Generated Core requirement index and consolidated quality-level matrix.
- Requirement assessment matrix and exception record templates.
- Core self-review checklist for solo developers and small teams.
- Dependency-free Core consistency validator and generators for derived Core views.
- Complete technology-independent Core Standard drafts for project lifecycle, requirements, architecture, documentation, repositories, quality levels, quality, security, testing, releases, maintenance, knowledge management, and AI-assisted development.
- Stable requirement IDs for all Core requirements.
- Core adoption and Definition of Done checklists.
- Project brief, requirements, architecture, test strategy, security plan, maintenance plan, and release notes templates.
- Initial repository structure, project charter, Version 1.0 scope, content architecture, document catalog, governance drafts, and validation tools.

### Changed

- Promoted all seven Foundation documents and all seven Governance documents to Proposed 0.8.0 after consistency review.
- Separated document review, formal approval and GitHub publication as distinct states and evidence.
- Incorporated first-pilot evidence lessons directly into the normative Alignment model.

- Moved Pilot 01 from `Wave Planned` to `In Execution` with `Artifact Prepared` and `Pending` verification states.
- Clarified that patches, ZIP overlays, workflow files, test sources and static checks do not prove target integration, build, runtime or CI success.
- Added an explicit verification gate before Wave 02 and prohibited unverified claims that the historical SQLite defect is fixed.


- Moved reference-implementation documentation from a placeholder to a Proposed 0.7.0 pilot program.
- Expanded the content architecture and document catalog with pilot artefacts, evidence rules, execution criteria, and Pilot 01 records.
- Updated repository navigation, project status, roadmap, tooling documentation, and repository manifest for the first small-project pilot.


- Moved all seven operational process documents from Planned 0.1.0 to Proposed 0.6.0.
- Clarified the separation of structural project size, quality level, risk characteristics, lifecycle intent, and applicable profiles.
- Updated repository navigation, document catalog, roadmap, tooling documentation, and repository manifest for the operational processes.


- Moved all four Desktop profile documents from Planned 0.1.0 to Proposed 0.5.0.
- Updated repository navigation, document catalog, roadmap, tooling documentation, and repository manifest for the Desktop profile.

- Moved all eight C#/.NET profile documents from Planned 0.1.0 to Proposed 0.4.0.
- Updated repository navigation, document catalog, roadmap, tooling documentation, and repository manifest for the .NET profile.

- Moved all 13 Core documents from Draft 0.2.0 to Proposed 0.3.0 after consistency and proportionality review.
- Defined explicit applicability, quality-level precedence, profile hierarchy, `Not Applicable` evidence, and solo-developer role rules.
- Harmonized overall assessment terminology to Not Assessed, Assessment in Progress, Partially Aligned, Aligned with Exceptions, and Aligned.
- Expanded Compliance and Exception governance and moved both documents to Proposed 0.2.0.
- Reframed lifecycle requirement `SASD-LC-023` to remove an exact duplicate of the requirements-prioritization rule.
- Updated adoption guidance, compliance template, README navigation, roadmap, document catalog, and tooling documentation.
- Clarified that Draft and Proposed documents support pilot alignment only and cannot yet support a formal Version 1.0 alignment claim.
