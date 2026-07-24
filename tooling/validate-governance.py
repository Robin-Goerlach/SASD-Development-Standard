#!/usr/bin/env python3
"""Validate Foundation and Governance Proposed 0.8.0."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

FILES = [
    "NORMATIVE-LANGUAGE.md", "DOCUMENT-LIFECYCLE.md", "DOCUMENT-METADATA.md",
    "VERSIONING.md", "CHANGE-PROCESS.md", "EXCEPTIONS.md", "COMPLIANCE.md",
]
RANGES = {
    "NORMATIVE-LANGUAGE.md": range(1, 100),
    "DOCUMENT-LIFECYCLE.md": range(100, 200),
    "DOCUMENT-METADATA.md": range(200, 300),
    "VERSIONING.md": range(300, 400),
    "CHANGE-PROCESS.md": range(400, 500),
    "EXCEPTIONS.md": range(500, 600),
    "COMPLIANCE.md": range(600, 700),
}
ROW = re.compile(r"^\|\s*`?(SASD-GOV-REQ-(\d{3}))`?\s*\|\s*(.*?)\s*\|\s*$")
NORMATIVE = re.compile(r"\b(?:MUSS|MÜSSEN|DARF NICHT|DÜRFEN NICHT|SOLLTE|SOLLTEN|SOLLTE NICHT|SOLLTEN NICHT|KANN|KÖNNEN)\b")
PLACEHOLDER = re.compile(r"(?:^|\s)(?:TODO|TBD|FIXME)\s*:", re.I | re.M)
FOUNDATION = [
    "PROJECT-CHARTER.md", "SCOPE.md", "PRINCIPLES.md", "GLOSSARY.md",
    "CONTENT-ARCHITECTURE.md", "DOCUMENT-CATALOG.md", "VERSION-1.0-ACCEPTANCE-CRITERIA.md",
]
TEMPLATES = [
    "templates/documents/STANDARD-CHANGE-PROPOSAL-TEMPLATE.md",
    "templates/documents/DOCUMENT-APPROVAL-RECORD-TEMPLATE.md",
    "templates/documents/STANDARD-RELEASE-RECORD-TEMPLATE.md",
    "templates/documents/DEPRECATION-RECORD-TEMPLATE.md",
]


def meta(text: str) -> str:
    return text.split("---", 2)[1] if text.startswith("---") else ""


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    folder = repo / "docs" / "40-governance"
    failures = 0
    total = 0
    ids = {}
    statements = {}

    for name in FILES:
        path = folder / name
        errors = []
        if not path.exists():
            print(f"FAIL missing Governance document: {path.relative_to(repo)}")
            failures += 1
            continue
        text = path.read_text(encoding="utf-8")
        fm = meta(text)
        if "status: Proposed" not in fm:
            errors.append("status is not Proposed")
        if "version: 0.8.0" not in fm:
            errors.append("version is not 0.8.0")
        if PLACEHOLDER.search(text):
            errors.append("contains TODO/TBD/FIXME placeholder")
        found = 0
        for line in text.splitlines():
            m = ROW.match(line)
            if not m:
                continue
            found += 1
            total += 1
            rid, n, statement = m.groups()
            number = int(n)
            if number not in RANGES[name]:
                errors.append(f"{rid} outside reserved range")
            if rid in ids:
                errors.append(f"duplicate ID also in {ids[rid]}")
            ids[rid] = name
            if not NORMATIVE.search(statement):
                errors.append(f"{rid} lacks normative keyword")
            normalized = re.sub(r"\s+", " ", statement.lower().strip())
            if normalized in statements:
                errors.append(f"exact duplicate text also in {statements[normalized]}")
            statements[normalized] = rid
        if not found:
            errors.append("contains no Governance requirement rows")
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(repo)}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"OK   {path.relative_to(repo)}: {found} requirements")

    for name in FOUNDATION:
        path = repo / "docs" / "00-foundation" / name
        if not path.exists():
            failures += 1
            print(f"FAIL missing Foundation document: {path.relative_to(repo)}")
            continue
        fm = meta(path.read_text(encoding="utf-8"))
        if "status: Proposed" not in fm or "version: 0.8.0" not in fm:
            failures += 1
            print(f"FAIL Foundation document not Proposed 0.8.0: {path.relative_to(repo)}")

    for rel in TEMPLATES:
        path = repo / rel
        if not path.exists() or path.stat().st_size < 250:
            failures += 1
            print(f"FAIL missing or too small Governance template: {rel}")

    result = subprocess.run([sys.executable, str(repo / "tooling" / "generate-governance-requirements-index.py"), "--check"], check=False)
    if result.returncode:
        failures += 1

    print(f"\nValidated {total} Governance requirements; failures: {failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
