#!/usr/bin/env python3
"""Validate the Approved 0.8.0 Foundation and Governance baseline."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

DOCS = [
    "docs/00-foundation/PROJECT-CHARTER.md",
    "docs/00-foundation/SCOPE.md",
    "docs/00-foundation/PRINCIPLES.md",
    "docs/00-foundation/GLOSSARY.md",
    "docs/00-foundation/CONTENT-ARCHITECTURE.md",
    "docs/00-foundation/DOCUMENT-CATALOG.md",
    "docs/00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md",
    "docs/40-governance/NORMATIVE-LANGUAGE.md",
    "docs/40-governance/DOCUMENT-LIFECYCLE.md",
    "docs/40-governance/DOCUMENT-METADATA.md",
    "docs/40-governance/VERSIONING.md",
    "docs/40-governance/CHANGE-PROCESS.md",
    "docs/40-governance/EXCEPTIONS.md",
    "docs/40-governance/COMPLIANCE.md",
]
RECORD = "docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-0.8.0.md"
CHECKLIST = "docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-CHECKLIST-0.8.0.md"


def frontmatter(text: str) -> str:
    return text.split("---", 2)[1] if text.startswith("---") else ""


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    failures = 0

    for rel in DOCS:
        path = repo / rel
        if not path.exists():
            print(f"FAIL missing: {rel}")
            failures += 1
            continue
        fm = frontmatter(path.read_text(encoding="utf-8"))
        required = [
            "status: Approved",
            "version: 0.8.0",
            "approved-on: 2026-07-24",
            "approval-record: SASD-REF-GOV-005",
        ]
        missing = [item for item in required if item not in fm]
        if missing:
            print(f"FAIL {rel}: missing {missing}")
            failures += 1
        else:
            print(f"OK   {rel}")

    compliance = (repo / "docs/40-governance/COMPLIANCE.md").read_text(encoding="utf-8")
    expected_dependency = (
        "depends-on: [SASD-FND-004, SASD-GOV-001, SASD-GOV-002, SASD-GOV-006]"
    )
    if expected_dependency not in compliance:
        print("FAIL Compliance dependency does not use the Approved glossary baseline")
        failures += 1

    for rel in [RECORD, CHECKLIST]:
        path = repo / rel
        if not path.exists():
            print(f"FAIL missing approval evidence: {rel}")
            failures += 1
        elif "status: Approved" not in frontmatter(path.read_text(encoding="utf-8")):
            print(f"FAIL approval evidence not Approved: {rel}")
            failures += 1

    result = subprocess.run(
        [sys.executable, str(repo / "tooling/generate-foundation-governance-approval-manifest.py"), "--check"],
        check=False,
    )
    if result.returncode:
        failures += 1

    catalog = (repo / "docs/00-foundation/DOCUMENT-CATALOG.md").read_text(encoding="utf-8")
    for rel in DOCS:
        text = (repo / rel).read_text(encoding="utf-8")
        match = re.search(r"document-id:\s*([^\n]+)", text)
        if not match:
            print(f"FAIL document-id missing: {rel}")
            failures += 1
            continue
        doc_id = match.group(1).strip()
        if not re.search(rf"\| {re.escape(doc_id)} \| .*? \| Normativ \| Approved \|", catalog):
            print(f"FAIL catalog does not show Approved: {doc_id}")
            failures += 1

    print(f"\nValidated {len(DOCS)} Approved documents; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
