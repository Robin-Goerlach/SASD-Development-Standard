# Changelog

All notable changes to the SASD Development Standard will be documented in this file.

The format is based on Keep a Changelog principles, and the project intends to use Semantic Versioning once the first public versioning policy is approved.

## [Unreleased]

### Added
- Root `QUICKSTART.md` providing a deliberately small new-project entry path based on progressive disclosure.
- Lightweight Pilot Friction Log template for time-to-productivity, findability, duplication, tooling friction, and concrete SASD benefits without creating a new mandatory conformance artifact.
- Informative external usability-review record preserving the 2026-08-07 critique, current assessment, decisions, and Version 1.0 revisit questions.
- Version 1.0 Specification Candidate strategy defining the honest documentation baseline, practical-validation handoff, release pause, and criteria for resuming Release Candidate preparation.
- Permanent TaskHost Local remote-baseline evidence record for standard commit `d80baf0cccf66b5c940cfd7f05e399c83f880e1a`, target commit `2404feb0904b22274972b5803520e6d86a70047d`, and GitHub Actions run `31100169566`.

- Candidate `sasd-development-standard-v1` prompt package 0.13.0 with 39 stable prompt IDs across nine project-lifecycle categories and a central registry of 35 variables.
- Prompt-package specification, quality and security guidance, schemas, generated JSON/Markdown catalogs, checksums, workflow ordering, templates, review and import-roundtrip checklists.
- Dependency-free catalog generation, structural validation, deterministic ZIP building, independent artifact verification, local wrappers, and a read-only manual GitHub Actions preview workflow.
- Explicit Prompt Manager adapter plan that prevents direct-import compatibility claims until an exact application version passes lossless import/export roundtrip testing.

- Version `1.0.0-rc.1` release-candidate plan, explicit blocker register, generated readiness report, draft Release Notes, draft Release Record, and publication profile.
- Deterministic source and Markdown archive builder with stable ordering, timestamps, embedded metadata, SHA-256 manifest, and independent safe-path verifier.
- Read-only manually triggered GitHub Actions preview workflow that runs all quality gates, builds preview packages, verifies them, and uploads evidence without creating tags or releases.
- Release Candidate record, Known Issues, and publication-manifest templates; RC and artifact-verification checklists; release-review prompt; PowerShell and shell wrappers.
- Blocking structural RC-preparation validation and Version 1.0 readiness integration that keep publication blocked while pilot and remote CI/ruleset evidence remain open.

- Pilot 02 for SASD Prompt Manager with Medium/Recommended classification, public baseline assessment, 12-item gap register, two-wave migration plan, verification plan, evidence map, decision log, baseline review, and initial lessons learned.
- Pilot 03 for SASD Mail Workbench with Large/Complex classification, staged Recommended-to-Production gate, public baseline assessment, 12-item gap register, recovery- and security-focused migration plan, verification plan, evidence map, decision log, baseline review, and initial lessons learned.
- Version 1.0 pilot-readiness record covering Small, Medium, and Large/Complex project categories.
- Pilot manifest schema 1.2 and validation for baseline-assessed projects without a prepared implementation artifact.
- Blocking pilot-coverage validation for the three required project sizes and generated portfolio/readiness views.

- Formal normative-baseline Approval Record 0.9.0, completed approval checklist, and SHA-256 manifest for 32 documents and 1,345 requirements.
- Blocking approval validator and lifecycle-aware Core, profile, process, and integrated-review validators.
- Documented release conditions separating normative approval from remote CI, TaskHost pilot verification, ruleset evidence, and publication.
- Integrated 0.9.0 normative-baseline review for the 13 Core, eight C#/.NET, four Desktop, and seven operational-process documents.
- Deterministic dependency map and SHA-256 review manifest for the 32-document approval bundle.
- Bundle-wide validation for 1,345 requirements, duplicate obligations, unresolved markers, external dependency approval, and dependency cycles.
- Approval-readiness record, completed review checklist, approval-record template, review checklist, and reusable approval-review prompt.

- Repository self-hosting records for CI recovery, exact-commit remote evidence, and guarded `main` ruleset activation.
- Governed ruleset payload requiring `SASD merge gate`, blocking force pushes and default-branch deletion.
- Dependency-free remote workflow evidence capture, GitHub ruleset management, activation validation, platform wrappers, checklist, template, and review prompt.
- Machine-readable repository identity, blocking repository-boundary validator, controlled cleanup scripts, update-package manifest template, routing checklist, and review prompt.
- Incident record and pilot feedback for the accidental cross-repository application of TaskHost Local update packages.
- Cross-platform repository quality-gate workflow for Ubuntu and Windows with a stable `SASD merge gate` status check.
- Dependency-free quality-gate orchestrator, CI-policy validator, repository-hygiene validator, and deterministic repository-manifest generator.
- Immutable full-SHA action pins, read-only workflow permissions, non-persisted checkout credentials, concurrency cancellation, explicit timeouts, Dependabot for GitHub Actions, and CODEOWNERS.
- Local PowerShell and shell validation entry points, evidence artifacts, CI review and activation checklists, and implementation manifest.

- Formal Foundation and Governance Approval Record 0.8.0, completed approval checklist, and SHA-256 manifest for all 14 Approved normative documents.
- Approval validation and manifest-generation tooling with deterministic Git commit resolution guidance.

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
- Reworked root and documentation navigation into **Using SASD**, **SASD Specification**, and **Maintaining SASD** views so full complexity remains available without being imposed at first contact.
- Clarified that SASD tooling and prompt packages support the standard but do not silently define new normative requirements or require a particular AI vendor/model.
- Extended pilot-program and retrospective guidance to observe practical friction and measurable value before changing normative content.
- Reframed the current project state from immediate release-evidence closure to specification-baseline closure followed by practical validation through the separate reference-product repositories.
- Kept every practical-pilot and release blocker open while distinguishing the passed TaskHost remote technical baseline from full product and standard validation.
- Replaced the misplaced in-repository TaskHost build with an exact-commit cross-repository baseline verification against the public TaskHost Local repository.
- Consolidated the canonical project status, public README entry paths, Version 1.0 scope freeze, and release-oriented roadmap.
- Reframed post-1.0 planning around explicit Version 1.1, 1.2, and 2.0 stop conditions instead of an open-ended build-phase backlog.

- Updated the pilot programme and evidence model to distinguish public baseline assessment from implementation and technical verification.
- Hardened CI-policy validation so semantically valid quoted Dependabot directory values are accepted while the repository remains limited to GitHub Actions dependency updates.
- Updated repository navigation and roadmap for the complete three-size pilot portfolio.

- Promoted all 13 Core, eight C#/.NET, four Desktop, and seven operational-process documents from Proposed to Approved 0.9.0.
- Updated document catalog, navigation, roadmap, readiness reporting, and quality gates for the approved normative baseline.
- Unified all 32 remaining normative documents as Proposed 0.9.0 without granting formal Maintainer approval.
- Removed three formal dependency cycles by clarifying direction between Architecture and Security, Quality and Testing, Repository and Releases, and Knowledge Management and Maintenance.
- Integrated the normative-baseline validator into the canonical repository quality gates.
- Updated Core, profile, process, repository, roadmap, and tooling navigation for the integrated approval candidate.
- Split CI recovery into boundary repair, green remote run, evidence capture, ruleset activation, and read-back evidence.
- Made ruleset activation require explicit acknowledgement that normal changes will move from direct `main` pushes to branch and pull-request work.
- Added CI activation assets to the blocking repository quality-gate chain without claiming that the pending remote run or ruleset has succeeded.
- Recorded the first repository quality-gate run as failed evidence rather than pending and kept branch protection disabled.
- Removed misplaced TaskHost Local projects, workflows, project documentation, verification scripts, and the nested starter-repository copy from the intended repository state.
- Restored the Development Standard `.gitignore` policy and made repository identity a blocking quality gate.
- Activated repository CI after formal approval of the Foundation and Governance baseline while keeping the first GitHub run and branch-rule activation as pending evidence.
- Replaced the manually maintained repository manifest with a deterministic generated-file check and removed stale nested-root entries.
- Updated repository navigation, contribution guidance, GitHub setup instructions, workflow documentation, and roadmap for the CI baseline.
- Corrected one trailing-whitespace finding and one tab character detected by the new repository-hygiene gate.

- Promoted all seven Foundation documents and all seven Governance documents from Proposed to Approved 0.8.0 after the documented Maintainer review.
- Corrected the Alignment model dependency from the still-Proposed Core quality-level document to the Approved glossary definition, removing the final approval blocker.
- Updated repository navigation, roadmap, document catalog, readiness reporting, and governance validation for the Approved baseline.

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
