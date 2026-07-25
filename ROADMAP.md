# Roadmap

## Phase 0 — Foundation

- [x] Establish the standard as an independent product.
- [x] Create the initial repository structure.
- [x] Record vision, mission, target groups, and guiding principles.
- [x] Prepare the binding content architecture for Version 1.0.
- [x] Define document roles, IDs, and dependencies.
- [x] Define normative language, document lifecycle, and metadata.
- [x] Define initial Version 1.0 acceptance criteria.
- [x] Review the proposed foundation and governance documents for consistency and approval readiness.
- [x] Record formal Maintainer approval of the Foundation and Governance baseline.

## Phase 1 — Core Standard

- [x] Draft the quality-level model.
- [x] Draft the project lifecycle and requirements management rules.
- [x] Draft documentation and repository requirements.
- [x] Draft architecture and decision-record requirements.
- [x] Draft quality, testing, security, release, and maintenance requirements.
- [x] Draft knowledge-management and AI-assisted-development requirements.
- [x] Add stable Core requirement IDs and validation tooling.
- [x] Add initial operational templates and Core adoption checklists.
- [x] Review proportionality across Minimum, Recommended, and Production.
- [x] Resolve duplicated or conflicting Core requirements.
- [x] Define applicability, precedence, and solo-developer role combination.
- [x] Add generated requirement and quality-level indexes.
- [x] Move the Core documents from Draft to Proposed.
- [x] Complete the integrated cross-layer review and unify Core as Proposed 0.9.0.
- [x] Document the outstanding pilot verification as an explicit release condition.
- [x] Approve the Core documents as normative baseline 0.9.0 with release conditions.

## Phase 2 — First Profiles

- [x] Create the C#/.NET profile.
- [x] Create the desktop application profile.
- [x] Define the standard .NET repository and solution structures.
- [x] Define .NET coding, logging, configuration, persistence, testing, and error-handling rules.
- [x] Complete the integrated cross-layer review and unify both profiles as Proposed 0.9.0.
- [x] Approve the C#/.NET and Desktop profiles in the normative-baseline Maintainer decision.

## Phase 3 — Processes and Supporting Assets

- [x] Define project classification and new-project initialization.
- [x] Define architecture-decision and review processes.
- [x] Define legacy migration, release, and project archival processes.
- [x] Add process templates, checklists, examples, prompts, indexes, and validation tooling.
- [ ] Complete remaining document templates.
- [ ] Complete remaining checklists.
- [ ] Complete prompt packages for the SASD Prompt Manager.
- [x] Add initial reusable `.editorconfig`, MSBuild, package-management, SDK, and CI templates.
- [x] Add initial WinForms and WPF project templates, desktop checklists, and deployment templates.
- [ ] Refine reusable templates after .NET and Desktop pilot feedback.
- [x] Extend governance validation tooling and add release-readiness reporting.
- [x] Add repository CI using the formally approved Foundation and Governance rules.
- [x] Add repository-boundary recovery and governed CI-activation tooling.
- [x] Complete the integrated process review and unify all seven processes as Proposed 0.9.0.
- [x] Approve the operational processes in the normative-baseline Approval commit.
- [ ] Commit the boundary repair and confirm the first green Ubuntu and Windows CI run for the exact commit.
- [ ] Capture CI evidence and activate the `SASD merge gate` ruleset for `main`.

## Phase 4 — Pilot Projects

- [x] Select and classify one small project: SASD TaskHost Local.
- [x] Prepare its evidence-based baseline assessment, gap register, migration plan, and Wave 01.
- [x] Prepare and statically review the Wave 01 implementation artifact for SASD TaskHost Local.
- [ ] Commit and validate Wave 01 in the SASD TaskHost Local repository.
- [x] Record interim lessons learned from the Wave 01 artifact.
- [ ] Record verified results and final lessons learned from the small-project pilot.
- [ ] Apply the full process chain to one medium project.
- [ ] Apply the full process chain to one more complex C#/.NET project.
- [ ] Consolidate deviations and lessons learned across all pilots.

## Phase 5 — Version 1.0

- [x] Formally approve all 32 normative baseline documents as version 0.9.0.
- [x] Add the approval record, checklist, SHA-256 manifest, and blocking approval validator.
- [x] Consolidate and approve Core, profiles, and processes as normative baseline 0.9.0.
- [ ] Consolidate verified feedback from pilot projects before the stable release.
- [x] Resolve contradictions, exact duplicates, and formal dependency cycles in the 0.9.0 baseline.
- [ ] Publish a release candidate.
- [ ] Produce Word and PDF publication artefacts.
- [ ] Publish Version 1.0.0.

## Repository CI recovery

Complete the controlled cleanup, obtain a green cross-platform CI run for the repair commit, capture remote evidence, and only then activate the governed `main` ruleset.
