#!/usr/bin/env python3
"""Validate the reviewed content of the 0.9.0 normative baseline through its lifecycle."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from normative_baseline_common import (
    BUNDLE_NAME,
    BUNDLE_VERSION,
    EXPECTED_DOCUMENT_COUNT,
    EXPECTED_REQUIREMENT_COUNT,
    bundle_documents,
    extract_requirements,
    load_documents,
    normalize_requirement,
    topological_order,
)

REQUIRED_REVIEW_FILES = (
    "docs/40-governance/NORMATIVE-BASELINE-REVIEW-0.9.0.md",
    "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-READINESS-0.9.0.md",
    "docs/40-governance/NORMATIVE-BASELINE-DEPENDENCY-MAP-0.9.0.md",
    "docs/40-governance/NORMATIVE-BASELINE-REVIEW-MANIFEST-0.9.0.md",
    "docs/40-governance/NORMATIVE-BASELINE-REVIEW-CHECKLIST-0.9.0.md",
    "docs/40-governance/NORMATIVE-BASELINE-REVIEW-UPDATE-MANIFEST-0.9.0.md",
)
REQUIRED_HEADING_PATTERNS = (
    re.compile(r"^##\s+\d+\.\s+Zweck", re.MULTILINE),
    re.compile(r"^##\s+\d+\.\s+Geltungsbereich", re.MULTILINE),
    re.compile(r"Normative Anforderungen", re.IGNORECASE),
    re.compile(r"Qualitätsstufe", re.IGNORECASE),
    re.compile(r"Nachweise|Prüfkriterien", re.IGNORECASE),
    re.compile(r"Ausnahmen und Abweichungen", re.IGNORECASE),
    re.compile(r"Verwandte Dokumente", re.IGNORECASE),
)
UNRESOLVED_PATTERN = re.compile(r"(?:^|[\s\[(])(?:TODO|TBD|FIXME|XXX)(?:\s*:|\s*\]|\s*$)", re.IGNORECASE | re.MULTILINE)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    documents = load_documents(repo)
    bundle = bundle_documents(repo)
    bundle_ids = {document.document_id for document in bundle}
    failures: list[str] = []

    if len(bundle) != EXPECTED_DOCUMENT_COUNT:
        failures.append(f"expected {EXPECTED_DOCUMENT_COUNT} bundle documents, found {len(bundle)}")

    requirement_ids: dict[str, str] = {}
    requirement_texts: dict[str, tuple[str, str]] = {}
    requirement_count = 0

    for document in bundle:
        metadata = document.metadata
        status = metadata.get("status")
        if status not in {"Proposed", "Approved"}:
            failures.append(f"{document.document_id}: expected status Proposed or Approved")
        if metadata.get("version") != BUNDLE_VERSION:
            failures.append(f"{document.document_id}: expected version {BUNDLE_VERSION}")
        expected_review_state = "approved" if status == "Approved" else "integrated-review-complete"
        if metadata.get("approval-review-state") != expected_review_state:
            failures.append(f"{document.document_id}: expected approval-review-state {expected_review_state}")
        if UNRESOLVED_PATTERN.search(document.text):
            failures.append(f"{document.document_id}: unresolved TODO/TBD/FIXME marker")
        for pattern in REQUIRED_HEADING_PATTERNS:
            if not pattern.search(document.text):
                failures.append(f"{document.document_id}: required section not found: {pattern.pattern}")
        requirements = extract_requirements(document)
        requirement_count += len(requirements)
        if not requirements:
            failures.append(f"{document.document_id}: no normative requirements found")
        for requirement_id, text in requirements:
            previous = requirement_ids.get(requirement_id)
            if previous:
                failures.append(f"duplicate requirement ID {requirement_id}: {previous} and {document.document_id}")
            requirement_ids[requirement_id] = document.document_id
            normalized = normalize_requirement(text)
            previous_text = requirement_texts.get(normalized)
            if previous_text:
                failures.append(
                    f"exact duplicate requirement text: {previous_text[0]} and {requirement_id}"
                )
            requirement_texts[normalized] = (requirement_id, document.document_id)

        for dependency in document.dependencies:
            target = documents.get(dependency)
            if target is None:
                failures.append(f"{document.document_id}: unknown dependency {dependency}")
            elif dependency not in bundle_ids and target.metadata.get("status") != "Approved":
                failures.append(
                    f"{document.document_id}: external dependency {dependency} is "
                    f"{target.metadata.get('status')}, not Approved"
                )

    if requirement_count != EXPECTED_REQUIREMENT_COUNT:
        failures.append(
            f"expected {EXPECTED_REQUIREMENT_COUNT} requirements, found {requirement_count}"
        )

    order, cycles = topological_order(bundle)
    if cycles:
        for cycle in cycles:
            failures.append("dependency cycle: " + " -> ".join(cycle))
    if len(order) != len(bundle):
        failures.append("topological order does not include all bundle documents")

    for relative in REQUIRED_REVIEW_FILES:
        if not (repo / relative).is_file():
            failures.append(f"missing review evidence: {relative}")

    statuses = {document.metadata.get("status") for document in bundle}
    if statuses == {"Proposed"}:
        generator = subprocess.run(
            [sys.executable, str(repo / "tooling" / "generate-normative-baseline-review.py"), "--check"],
            cwd=repo, check=False, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        )
        if generator.stdout:
            print(generator.stdout.rstrip())
        if generator.stderr:
            print(generator.stderr.rstrip())
        if generator.returncode != 0:
            failures.append("generated review evidence is stale")
    elif statuses == {"Approved"}:
        if not (repo / "docs/40-governance/NORMATIVE-BASELINE-APPROVAL-0.9.0.md").is_file():
            failures.append("Approved bundle has no approval record")
    else:
        failures.append("bundle contains a mixed Proposed/Approved lifecycle state")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
    else:
        print(f"OK   bundle: {BUNDLE_NAME}")
        print(f"OK   normative documents: {len(bundle)}")
        print(f"OK   normative requirements: {requirement_count}")
        print("OK   dependency graph is acyclic")
        print("OK   every external dependency is Approved")
        print("OK   no exact duplicate requirements or unresolved markers")

    print(f"\nNormative baseline review failures: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
