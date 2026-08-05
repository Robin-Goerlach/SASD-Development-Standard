# Release Candidate Preparation Update Manifest 0.12.0

## Target

```text
Repository: Robin-Goerlach/SASD-Development-Standard
Update type: additive and replacement overlay
Deletion operations: none
Changed or added files: 38
Target phase: Version 1.0 release-candidate preparation
```

## Purpose

This update prepares, but does not publish, `1.0.0-rc.1`. It adds release planning, blocker tracking, release-document drafts, deterministic packaging, independent verification, a manually triggered preview workflow, and blocking structural validation.

## Evidence boundary

```text
Normative baseline approved: Yes
Pilot size coverage: Yes
At least one technically verified pilot: No
Exact-commit remote CI evidence: Pending
Active ruleset evidence: Pending
Release Candidate published: No
Stable Version 1.0 published: No
```

## Application

Extract into the repository root, run `python tooling/run-quality-gates.py`, inspect the generated readiness report, then commit the update. The update does not create a tag, GitHub Release or final release artifact automatically.
