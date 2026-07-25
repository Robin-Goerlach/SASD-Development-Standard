#!/usr/bin/env python3
"""Validate the structural preparation of SASD Version 1.0 RC1."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from release_candidate_common import PREPARATION_VERSION, RC_VERSION, RC_TAG, parse_front_matter, repository_root

REQUIRED = [
    "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-PLAN.md",
    "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md",
    "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md",
    "docs/40-governance/VERSION-1.0-RELEASE-NOTES-DRAFT.md",
    "docs/40-governance/VERSION-1.0-RC1-RELEASE-RECORD-DRAFT.md",
    "docs/40-governance/VERSION-1.0-PUBLICATION-PROFILE.md",
    "templates/documents/RELEASE-CANDIDATE-RECORD-TEMPLATE.md",
    "templates/documents/KNOWN-ISSUES-TEMPLATE.md",
    "templates/documents/PUBLICATION-MANIFEST-TEMPLATE.json",
    "checklists/releases/VERSION-1.0-RC-CHECKLIST.md",
    "checklists/releases/RELEASE-ARTIFACT-VERIFICATION-CHECKLIST.md",
    "prompts/release/VERSION-1.0-RC-REVIEW-PROMPT.md",
    "tooling/release_candidate_common.py",
    "tooling/generate-release-candidate-readiness.py",
    "tooling/build-release-candidate.py",
    "tooling/verify-release-candidate.py",
    ".github/workflows/release-candidate-preview.yml",
    "RELEASE-CANDIDATE-PREPARATION-UPDATE-MANIFEST.md",
]


def main() -> int:
    repo = repository_root()
    failures: list[str] = []
    for rel in REQUIRED:
        if not (repo / rel).is_file():
            failures.append(f"missing required RC preparation file: {rel}")

    expected_docs = {
        "SASD-REF-RC-001",
        "SASD-REF-RC-002",
        "SASD-REF-RC-003",
        "SASD-REF-RC-004",
        "SASD-REF-RC-005",
        "SASD-REF-RC-006",
    }
    seen: set[str] = set()
    for path in sorted((repo / "docs/40-governance").glob("VERSION-1.0-*.md")):
        data = parse_front_matter(path)
        doc_id = data.get("document-id")
        if doc_id in expected_docs:
            seen.add(doc_id)
            if data.get("version") != PREPARATION_VERSION:
                failures.append(f"{path.relative_to(repo)} must be version {PREPARATION_VERSION}")
            if data.get("status") != "Draft":
                failures.append(f"{path.relative_to(repo)} must remain Draft before RC approval")
    missing_ids = expected_docs - seen
    if missing_ids:
        failures.append("missing RC document IDs: " + ", ".join(sorted(missing_ids)))

    plan = repo / "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-PLAN.md"
    if plan.is_file():
        text = plan.read_text(encoding="utf-8")
        for fragment in [RC_VERSION, RC_TAG, "G1 Normative Freigabe", "G8 Veröffentlichung"]:
            if fragment not in text:
                failures.append(f"RC plan missing fragment: {fragment!r}")

    blockers = repo / "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md"
    if blockers.is_file():
        text = blockers.read_text(encoding="utf-8")
        ids = set(re.findall(r"RC-BLK-\d{3}", text))
        if ids != {f"RC-BLK-{number:03d}" for number in range(1, 7)}:
            failures.append("RC blocker register must contain RC-BLK-001 through RC-BLK-006")

    template = repo / "templates/documents/PUBLICATION-MANIFEST-TEMPLATE.json"
    if template.is_file():
        try:
            data = json.loads(template.read_text(encoding="utf-8"))
            if data.get("standard_version") != RC_VERSION:
                failures.append("publication manifest template has wrong standard version")
        except json.JSONDecodeError as error:
            failures.append(f"publication manifest template is invalid JSON: {error}")

    workflow = repo / ".github/workflows/release-candidate-preview.yml"
    if workflow.is_file():
        text = workflow.read_text(encoding="utf-8")
        required = [
            "workflow_dispatch:",
            "permissions:\n  contents: read",
            "persist-credentials: false",
            "tooling/run-quality-gates.py",
            "tooling/build-release-candidate.py --mode preview",
            "tooling/verify-release-candidate.py",
            "actions/upload-artifact@",
            "timeout-minutes:",
        ]
        for fragment in required:
            if fragment not in text:
                failures.append(f"RC preview workflow missing: {fragment!r}")
        for forbidden in ["release:", "contents: write", "pull_request_target:", "gh release", "git tag"]:
            if forbidden in text:
                failures.append(f"RC preview workflow contains forbidden publishing fragment: {forbidden!r}")

    readiness = repo / "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md"
    if readiness.is_file():
        text = readiness.read_text(encoding="utf-8")
        if "technisch veröffentlichungsbereit: **Nein**" not in text and "technisch veröffentlichungsbereit: **Ja**" not in text:
            failures.append("RC readiness report has no explicit readiness result")

    readiness_check = subprocess.run(
        [sys.executable, str(repo / "tooling/generate-release-candidate-readiness.py"), "--check"],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if readiness_check.returncode != 0:
        failures.append("RC readiness report is stale")

    if failures:
        print("Release-candidate preparation validation failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nFailures: {len(failures)}")
        return 1

    print("OK   six RC governance documents are present and remain Draft")
    print("OK   blocker IDs, version, tag and release gates are explicit")
    print("OK   release templates, checklists, prompt and packaging tools are present")
    print("OK   preview workflow is read-only and cannot publish a release")
    print("OK   readiness report states an explicit current result")
    print("\nRelease-candidate preparation failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
