# SASD Development Standard — Project Status

> Canonical human-readable status summary for maintainers, reviewers, and new users.
>
> This file is informative. Generated readiness reports and Approved normative documents take precedence when details differ.

**Last reviewed:** 2026-08-05

**Current phase:** Pre-1.0 consolidation and release-evidence closure

**Next planned release:** `1.0.0-rc.1`

**Stable target:** `1.0.0`

## Status at a glance

| Area | Current state |
|---|---|
| Foundation and Governance | 14/14 normative documents Approved as `0.8.0` |
| Core, .NET, Desktop, Processes | 32/32 normative documents Approved as baseline `0.9.0` |
| Total normative documents | **46/46 Approved** |
| Normative requirements in the 0.9.0 baseline | **1,345** |
| Pilot size coverage | Small, Medium, and Large baselines documented |
| Technically verified pilots | **0/3** |
| Release Candidate readiness | **Not ready** |
| Blocking readiness checks | `RC-RDY-003`, `RC-RDY-004`, `RC-RDY-005` |
| Repository boundary cleanup | Completed |
| Historical root-manifest cleanup | Completed |

## What is complete

- The product charter, scope, principles, content architecture, document catalog, and Version 1.0 acceptance criteria are Approved.
- The technology-independent Core Standard is Approved.
- The C#/.NET and Desktop profiles are Approved.
- The seven operational processes are Approved.
- Stable document and requirement IDs, quality-level matrices, indexes, templates, checklists, prompt packages, and validation tooling are available.
- Small, Medium, and Large pilot baselines are documented.
- Release Candidate planning, blocker tracking, deterministic archive building, independent verification, and preview CI are prepared.
- The canonical repository boundary has been restored, foreign project code has been removed, and historical one-time update manifests have been archived.

## What still blocks `1.0.0-rc.1`

### 1. Practical pilot evidence — `RC-RDY-003`

At least one pilot must be executed in its real target repository and technically verified with `Passed`. The first target is Pilot 01, SASD TaskHost Local.

### 2. Exact-commit cross-platform CI — `RC-RDY-004`

Ubuntu, Windows, and the stable `SASD merge gate` status check must all succeed for the same immutable candidate commit.

### 3. Governed `main` decision — `RC-RDY-005`

The planned branch ruleset must be activated or its deferral must be explicitly documented and bounded.

After those three readiness checks close, the remaining RC work is to build and verify the release archives, complete the Release Record, make the Maintainer decision, tag the exact commit, publish the GitHub Pre-release, and re-verify the downloaded assets.

## What remains before stable `1.0.0`

- Practically review the published Release Candidate.
- Decide whether `rc.2` is required.
- Confirm all three pilot baselines against concrete target-repository commits and consolidate the main lessons learned.
- Produce Word and PDF publications from the same approved Markdown source commit.
- Visually review the generated publications.
- Finalize checksums, release records, notes, known issues, and the stable tag.

## Version 1.0 scope freeze

Version 1.0 is now under a hard scope freeze. Work before the stable release is limited to blocker closure, correctness, security, required usability, release evidence, and directly relevant pilot findings.

New technology profiles, organization-scale governance, certification, a full compliance auditor, and incompatible restructuring are deferred. See the [`Version 1.0 Scope Freeze`](docs/40-governance/VERSION-1.0-SCOPE-FREEZE.md).

## Evidence hierarchy

Use these sources in this order:

1. Approved normative documents and their approval records define the binding content.
2. [`VERSION-1.0-RELEASE-CANDIDATE-READINESS.md`](docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md) is the generated technical RC-readiness view.
3. [`VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md`](docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md) records release blockers and accepted decisions.
4. [`VERSION-1.0-PILOT-READINESS.md`](docs/50-reference-implementations/VERSION-1.0-PILOT-READINESS.md) is the generated pilot-coverage view.
5. This file summarizes the current situation for humans but does not replace the sources above.

## Current work sequence

1. Finish public status, entry-point, scope-freeze, and roadmap consolidation.
2. Freeze a clean candidate commit and obtain exact-commit Ubuntu, Windows, and merge-gate evidence.
3. Execute and verify TaskHost Local Wave 01.
4. Activate or explicitly defer the governed `main` ruleset.
5. Build and independently verify `1.0.0-rc.1` artifacts.
6. Publish and review the Release Candidate.
7. Produce and inspect Word/PDF publications.
8. Publish stable `1.0.0`.

See the release-oriented [`ROADMAP.md`](ROADMAP.md) for Version 1.0, 1.1, 1.2, and 2.0 boundaries.

## Non-claims

The current repository state is not yet:

- a published Release Candidate,
- a stable Version 1.0 release,
- an external certification,
- proof that all three pilots build and run successfully,
- proof that every future SASD project automatically complies with the standard.

Every technical claim remains tied to explicit evidence, a specific commit, and the applicable standard version.
