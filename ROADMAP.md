# SASD Development Standard Roadmap

This roadmap is release-oriented. It separates what must be completed for the next release from useful work that can wait.

The current human-readable state is maintained in [`PROJECT-STATUS.md`](PROJECT-STATUS.md). Generated release readiness and pilot readiness remain the technical evidence sources.

## Planning principles

1. **No rewrite:** the Approved 0.8.0/0.9.0 baseline is the product foundation.
2. **Hard Version 1.0 scope freeze:** no new major profile or governance domain before stable `1.0.0`.
3. **Evidence before claims:** prepared scripts, tests, or artifacts do not count as successful execution.
4. **One release boundary at a time:** finish the current release before expanding the next one.
5. **Breaking changes require Version 2.0:** compatible guidance and optional profiles do not automatically justify a major version.

## Current baseline

Completed before this roadmap revision:

- [x] Foundation and Governance Approved as `0.8.0`.
- [x] Core, C#/.NET, Desktop, and operational processes Approved as normative baseline `0.9.0`.
- [x] 46 normative documents Approved.
- [x] 1,345 requirements validated in the integrated 0.9.0 baseline.
- [x] Small, Medium, and Large pilot baselines documented.
- [x] Release Candidate plan, blockers, readiness generation, packaging, verification, and preview workflow prepared.
- [x] Versioned SASD Prompt Package prepared and independently verifiable.
- [x] Canonical repository boundary restored.
- [x] Historical one-time update manifests moved out of the repository root.
- [x] Version 1.0 scope freeze and canonical project status established.

## Version `1.0.0-rc.1` — First publishable candidate

### Goal

Publish the Approved Version 1.0 product basis as a reproducible GitHub Pre-release backed by real CI, pilot, governance, and artifact evidence.

### Release blockers

- [ ] `RC-RDY-003`: technically verify at least one practical pilot in its target repository.
- [ ] `RC-RDY-004`: obtain Ubuntu, Windows, and `SASD merge gate` success for the same exact candidate commit.
- [ ] `RC-RDY-005`: activate the governed `main` ruleset or document an explicit, bounded deferral decision.

### Candidate preparation

- [ ] Confirm the intended RC commit from a clean working tree.
- [ ] Run all local quality gates for the exact candidate commit.
- [ ] Capture and store exact-commit remote CI evidence.
- [ ] Execute and verify TaskHost Local Wave 01 as the first practical pilot.
- [ ] Update pilot manifests, evidence maps, feedback, and readiness views from executed evidence.
- [ ] Close or explicitly decide every RC blocker.
- [ ] Build deterministic Source and Markdown archives.
- [ ] Independently verify archive paths, contents, metadata, and SHA-256 checksums.
- [ ] Complete Release Notes, Known Issues, Release Record, and Maintainer decision.
- [ ] Create annotated tag `v1.0.0-rc.1` on the approved commit.
- [ ] Publish the GitHub Pre-release without rebuilding the verified assets.
- [ ] Download the published assets and verify them again.

### RC stop condition

`1.0.0-rc.1` is complete when the tagged commit, remote CI, pilot evidence, ruleset decision, release records, archives, checksums, and published GitHub assets all refer to the same approved source state.

No new profile, language edition, certification mechanism, or major repository restructuring is added before this stop condition.

## Version `1.0.0` — Stable foundation

### Goal

Publish a stable, understandable, practically reviewed Version 1.0 with authoritative Markdown sources and visually inspected Word/PDF editions.

### Work after the Release Candidate

- [ ] Perform a clean-user walkthrough starting from README and the release archives.
- [ ] Record RC findings and classify them as blocker, correction, clarification, or deferred improvement.
- [ ] Decide whether `1.0.0-rc.2` is required.
- [ ] Confirm all three pilot baselines against concrete target-repository commits.
- [ ] Consolidate the main pilot lessons, deviations, and justified standard changes.
- [ ] Resolve stable-release blockers and approved RC findings.
- [ ] Generate Word and PDF publications from the same approved Markdown source commit.
- [ ] Visually review contents, tables, page breaks, code blocks, links, and metadata.
- [ ] Record conversion tools, versions, manifests, and SHA-256 checksums.
- [ ] Complete the stable Release Record and Release Notes.
- [ ] Tag and publish `v1.0.0`.
- [ ] Re-download and verify the stable release assets.

### Version 1.0 stop condition

Version 1.0 ends with:

- a stable technology-independent Core Standard,
- the C#/.NET and Desktop profiles,
- seven operational lifecycle processes,
- proportional quality levels,
- usable templates, checklists, prompts, examples, and validators,
- Small, Medium, and Large pilot baselines,
- at least one fully executed and technically verified pilot,
- consolidated pilot lessons sufficient for the stable decision,
- reproducible Source/Markdown archives,
- reviewed Word/PDF publications,
- a complete and verifiable GitHub release.

## Version `1.1.0` — Adoption and usability

### Goal

Make the stable standard substantially easier to start and apply without weakening its evidence or quality model.

### Planned work

- [ ] Add a compact Quick Start for new projects.
- [ ] Add a compact migration path for existing projects.
- [ ] Provide filtered requirement views for `Minimum`, `Recommended`, and `Production`.
- [ ] Improve the Solo Developer Guide with end-to-end examples.
- [ ] Add clearer “required, recommended, optional, not applicable” adoption views.
- [ ] Reduce duplicate navigation and shorten common user journeys.
- [ ] Refine templates and checklists from Version 1.0 adoption feedback.
- [ ] Publish errata and compatible clarifications discovered after `1.0.0`.
- [ ] Add practical examples for a small tool and a maintained application.

### Version 1.1 stop condition

A new user can classify a project, select the applicable standard subset, create the minimum required artifacts, run the relevant checks, and prepare a compliant release without reading the entire standard first.

Version 1.1 does not require new technology profiles or breaking normative changes.

## Version `1.2.0` — Evidence, ecosystem, and automation

### Goal

Increase confidence and reduce repeated manual work through broader pilot execution, stronger evidence automation, and proven integrations.

### Planned work

- [ ] Execute and verify the Prompt Manager pilot wave.
- [ ] Execute and verify the Mail Workbench pilot wave or an explicitly selected equivalent complex pilot.
- [ ] Consolidate cross-size pilot evidence and recurring deviations.
- [ ] Add automated alignment or evidence reports where they save repeated work.
- [ ] Improve publication automation while retaining independent verification.
- [ ] Roundtrip-test a direct Prompt Manager adapter against an exact application commit, if still valuable.
- [ ] Add release-health and adoption diagnostics without creating a certification claim.
- [ ] Evaluate compatible Linux, database, container, Web API, or Security profile packages individually.

### Version 1.2 stop condition

At least the initial Small, Medium, and Large reference path has meaningful executed evidence, recurring manual checks are automated where justified, and optional ecosystem integrations are tied to exact versions and reproducible tests.

## Version `2.0.0` — Breaking evolution only when justified

### Entry criteria

Version 2.0 is started only when real Version 1.x use demonstrates that a compatible change is insufficient.

A Version 2.0 proposal must include:

- concrete evidence from projects or maintainers,
- the incompatible behavior or structural limitation,
- rejected compatible alternatives,
- impact on requirement IDs, profiles, processes, tooling, publications, and adopters,
- a migration strategy,
- a measurable benefit that justifies the disruption.

### Possible, not pre-approved topics

- changing normative language or keyword semantics,
- replacing the quality-level or compliance model,
- restructuring the document hierarchy,
- splitting the standard, tooling, prompts, and examples into separate repositories,
- introducing a substantially different machine-readable specification,
- changing compatibility guarantees or requirement-ID rules,
- adding governance designed for materially larger teams or organizations.

### Version 2.0 stop condition

Version 2.0 provides a documented migration path from 1.x, preserves historical traceability, and solves evidenced problems that could not reasonably be addressed by compatible 1.x releases.

## Deferred profile backlog

The following areas remain part of the long-term product vision but have no automatic release assignment:

- Linux administration,
- databases,
- containers and Kubernetes,
- Web APIs,
- advanced Security,
- additional language and framework profiles,
- English normative publication.

Each area receives its own proposal, scope, pilot, maintenance owner, and compatibility assessment before it enters a release.
