# Usability & Pilot Readiness external review — 2026-08-07

## Purpose

This informative record preserves the substantive concerns from an external review that triggered the **SASD Usability & Pilot Readiness Pass**. The review is retained as decision evidence; it does not alter the normative baseline by itself.

The Maintainer response is intentionally conservative: improve navigation and pilot observation now, preserve the Approved normative work, and defer substantive reduction until real pilot evidence exists.

## Review themes and current assessment

| Review theme | Assessment on Specification Candidate | Current response |
|---|---|---|
| Entry feels too complex | **Partly true** | Add a compact Quick Start and role-oriented progressive-disclosure navigation. |
| Full normative depth is too visible on first contact | **Partly true** | Shorten the root entrance and move deep governance/readiness material behind maintainer links. |
| User, specification, and maintainer views are mixed | **Partly true** | Introduce explicit navigation views without physically restructuring stable directories. |
| Tooling can look mandatory for using SASD | **Partly true as a presentation problem** | State clearly that normative requirements and supporting automation are different layers. |
| PROJECT-BRIEF is missing as a minimal start | **Does not currently apply** | The existing Project Brief already covers problem, goal, audience, scope, non-goals, risks, milestones and success criteria. Build/test readiness remains in the existing initialization record to avoid duplicate maintenance. |
| Real technically verified pilot evidence is missing | **True** | Keep release blocked and execute the existing reference products against the Specification Candidate. |
| Pilot process does not capture day-to-day friction sufficiently | **Partly true** | Add lightweight friction observations and retrospective metrics without creating a new mandatory governance artifact. |
| Risk of meta-overengineering | **Can only be judged reliably through pilots** | Preserve proportionality principles; measure whether SASD effort displaces product work before changing normative content. |
| Standard repository self-conformity is questionable | **Partly addressed already** | Repository identity, boundary, metadata, CI and quality gates exist; recheck before Version 1.0. |
| Versioned AI prompts may age quickly | **Partly true as a maintenance risk** | Keep prompts as versioned supporting assets, explicitly decoupled from vendor/model choice and the normative core. |
| Root contains excessive historical wave/update material | **Mostly outdated** | Historical update manifests had already been moved out of the root before this review pass. |

## Decisions for the current pass

The current pass may change:

- root and documentation navigation,
- informative Quick Start guidance,
- pilot friction observation aids,
- supporting prompt-package wording,
- project status, roadmap, changelog, repository identity, and history records required by those UX changes.

The current pass does **not**:

- delete Approved requirements,
- introduce Nano/Enterprise editions,
- change quality-level semantics,
- add new mandatory project documents merely for UX reasons,
- reorganize normative directories for aesthetics,
- claim that practical validation has been completed,
- release Version 1.0.

## Before Version 1.0, revisit these review questions

1. What measurable documentation or bureaucracy overhead appeared in real pilots?
2. Which requirements created repeated value, and which created repeated friction?
3. Did SASD tooling save more maintenance effort than it consumed?
4. Could a new developer find the right rule and become productive quickly?
5. Did the standard repository continue to satisfy its own applicable rules and quality gates?
6. Did prompt packages remain useful and maintainable without coupling the normative core to particular models?

For every item, the final Version 1.0 review should be able to record either **what changed** or **why no change was justified by evidence**.

## Strategic maxim

> **Complexity available, not imposed.**

SASD should support development of the actual product and must not become the dominant product of the project team.
