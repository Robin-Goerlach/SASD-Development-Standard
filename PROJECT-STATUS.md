# SASD Development Standard — Project Status

> Canonical human-readable status summary for maintainers, reviewers, and new users.
>
> This file is informative. Generated readiness reports and Approved normative documents take precedence when details differ.

**Last reviewed:** 2026-08-06

**Current phase:** Version 1.0 specification-baseline closure

**Next development phase:** Practical validation through reference implementations

**Next planned release:** `1.0.0-rc.1` after practical validation

**Stable target:** `1.0.0`

## Status at a glance

| Area | Current state |
|---|---|
| Foundation and Governance | 14/14 normative documents Approved as `0.8.0` |
| Core, .NET, Desktop, Processes | 32/32 normative documents Approved as baseline `0.9.0` |
| Total normative documents | **46/46 Approved** |
| Normative requirements in the 0.9.0 baseline | **1,345** |
| Specification baseline | **Complete enough for practical application and evaluation** |
| Pilot size coverage | Small, Medium, and Large baselines documented |
| TaskHost remote technical baseline | **Passed** for exact target commit `2404feb0904b22274972b5803520e6d86a70047d` |
| Technically verified pilots | **0/3** |
| Practical reference validation | **Pending** |
| Release Candidate readiness | **Not ready; preparation intentionally paused** |
| Blocking readiness checks | `RC-RDY-003`, `RC-RDY-004`, `RC-RDY-005` |
| Repository boundary cleanup | Completed |
| Historical root-manifest cleanup | Completed |

## Maintainer position

> **Die Theorie ist vollständig genug, um praktisch angewendet und bewertet zu werden. Ihre Praxistauglichkeit ist noch nicht abschließend bestätigt.**

The repository is therefore treated as a **Version 1.0 Specification Candidate**. It is a stable working baseline for reference-product development, not a published Release Candidate and not the stable Version 1.0 release.

See the [Version 1.0 Specification Baseline and Validation Handoff](docs/40-governance/VERSION-1.0-SPECIFICATION-BASELINE.md).

## What is complete

- The product charter, scope, principles, content architecture, document catalog, and Version 1.0 acceptance criteria are Approved.
- The technology-independent Core Standard is Approved.
- The C#/.NET and Desktop profiles are Approved.
- The seven operational processes are Approved.
- Stable document and requirement IDs, quality-level matrices, indexes, templates, checklists, prompt packages, and validation tooling are available.
- Small, Medium, and Large pilot baselines are documented.
- Release Candidate planning, blocker tracking, deterministic archive building, independent verification, and preview CI are prepared.
- The canonical repository boundary has been restored, foreign project code has been removed, and historical one-time update manifests have been archived.
- Ubuntu, Windows, and the stable `SASD merge gate` have succeeded for an immutable standard commit.
- The public TaskHost Local repository has passed an exact-commit Windows remote baseline covering restore, build, NuGet audit, and publish.

## Why Version 1.0 is not yet complete

The remaining uncertainty is not primarily missing theory. It is the practical question whether real projects can apply the standard proportionally, clearly, and without unjustified overhead.

The reference products must now show:

- whether requirements are understandable and applicable,
- whether quality levels scale to Small, Medium, and Large projects,
- whether templates and checklists support rather than obstruct the work,
- whether build, test, security, runtime, maintenance, and release expectations are realistic,
- which findings are genuine standard defects, project-specific exceptions, or future improvements.

## Practical validation handoff

The next work phase takes place primarily in the separate reference-product repositories:

1. SASD TaskHost Local,
2. SASD Prompt Manager,
3. SASD Mail Workbench.

The Specification Candidate remains the fixed starting point. Findings are first recorded as evidence, gaps, deviations, exceptions, or feedback. Only justified corrections return through the standard change process.

## What still blocks `1.0.0-rc.1`

### 1. Practical pilot evidence — `RC-RDY-003`

At least one reference product must apply the standard in its real target repository and reach an appropriately evidenced practical verification state. The successful TaskHost remote baseline is retained as preliminary technical evidence but does not close this check.

### 2. Exact-candidate cross-platform CI — `RC-RDY-004`

Ubuntu, Windows, and the stable `SASD merge gate` must all succeed for the same immutable commit that is later proposed as the Release Candidate. Existing successful runs prove the mechanism but must be refreshed after practical findings and final corrections.

### 3. Governed `main` decision — `RC-RDY-005`

The planned branch ruleset must be activated or its deferral must be explicitly documented and bounded before release preparation resumes.

## Version 1.0 scope freeze

Version 1.0 remains under a hard scope freeze. Work is limited to documentation closure, correctness, security, required usability, practical reference validation, evidence, and directly relevant pilot findings.

New technology profiles, organization-scale governance, certification, a full compliance auditor, and incompatible restructuring are deferred. See the [Version 1.0 Scope Freeze](docs/40-governance/VERSION-1.0-SCOPE-FREEZE.md).

## Evidence hierarchy

Use these sources in this order:

1. Approved normative documents and their approval records define the binding content.
2. [Version 1.0 Specification Baseline and Validation Handoff](docs/40-governance/VERSION-1.0-SPECIFICATION-BASELINE.md) records the current Maintainer strategy.
3. [VERSION-1.0-RELEASE-CANDIDATE-READINESS.md](docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md) is the generated technical RC-readiness view.
4. [VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md](docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md) records release blockers and accepted decisions.
5. [VERSION-1.0-PILOT-READINESS.md](docs/50-reference-implementations/VERSION-1.0-PILOT-READINESS.md) is the generated pilot-coverage view.
6. [TaskHost Remote Baseline Evidence](docs/50-reference-implementations/pilot-01-sasd-taskhost-local/REMOTE-BASELINE-EVIDENCE-2026-08-06.md) records the completed preliminary technical check.
7. This file summarizes the current situation for humans but does not replace the sources above.

## Current work sequence

1. Complete and verify the Version 1.0 Specification Candidate documentation.
2. Freeze the resulting documentation baseline as the practical validation starting point.
3. Continue each reference product in its own repository and project conversation.
4. Collect concrete implementation, test, runtime, security, maintenance, and release evidence.
5. Classify pilot findings and feed only justified changes back into the standard.
6. Re-run approval and quality gates after the practical correction cycle.
7. Resume Release Candidate preparation only when the practical validation threshold is met.
8. Build, verify, tag, publish, and review `1.0.0-rc.1`.
9. Produce and inspect Word/PDF publications before stable `1.0.0`.

See the release-oriented [ROADMAP.md](ROADMAP.md) for the complete phase sequence.

## Non-claims

The current repository state is not yet:

- a published Release Candidate,
- a stable Version 1.0 release,
- an external certification,
- proof that all three pilots build and run successfully,
- proof that every normative requirement has already survived practical project use,
- proof that every future SASD project automatically complies with the standard.

Every technical claim remains tied to explicit evidence, a specific commit, and the applicable standard version.
