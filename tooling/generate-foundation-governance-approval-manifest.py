#!/usr/bin/env python3
"""Generate or check the Foundation/Governance 0.8.0 approval hash manifest."""
from __future__ import annotations
import argparse
import hashlib
import sys
from pathlib import Path

DOCS = [
    ("SASD-FND-001", "docs/00-foundation/PROJECT-CHARTER.md"),
    ("SASD-FND-002", "docs/00-foundation/SCOPE.md"),
    ("SASD-FND-003", "docs/00-foundation/PRINCIPLES.md"),
    ("SASD-FND-004", "docs/00-foundation/GLOSSARY.md"),
    ("SASD-FND-005", "docs/00-foundation/CONTENT-ARCHITECTURE.md"),
    ("SASD-FND-006", "docs/00-foundation/DOCUMENT-CATALOG.md"),
    ("SASD-FND-007", "docs/00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md"),
    ("SASD-GOV-001", "docs/40-governance/NORMATIVE-LANGUAGE.md"),
    ("SASD-GOV-002", "docs/40-governance/DOCUMENT-LIFECYCLE.md"),
    ("SASD-GOV-003", "docs/40-governance/DOCUMENT-METADATA.md"),
    ("SASD-GOV-004", "docs/40-governance/VERSIONING.md"),
    ("SASD-GOV-005", "docs/40-governance/CHANGE-PROCESS.md"),
    ("SASD-GOV-006", "docs/40-governance/EXCEPTIONS.md"),
    ("SASD-GOV-007", "docs/40-governance/COMPLIANCE.md"),
]
TARGET = "docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-MANIFEST-0.8.0.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(repo: Path) -> str:
    rows = "\n".join(
        f'| `{doc_id}` | `{rel}` | `0.8.0` | `Approved` | `{sha(repo / rel)}` |'
        for doc_id, rel in DOCS
    )
    return f'''---
title: "Foundation and Governance Approval Manifest 0.8.0"
document-id: SASD-REF-GOV-006
document-type: informative
status: Approved
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-GOV-005
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-GOV-005]
normative-keywords: []
generated: true
generator: tooling/generate-foundation-governance-approval-manifest.py
---

# Foundation and Governance Approval Manifest 0.8.0

Dieses erzeugte Manifest identifiziert die 14 im Approval Record freigegebenen normativen Dokumente über ihre repositoryrelativen Pfade und SHA-256-Prüfsummen.

| Dokument-ID | Pfad | Version | Status | SHA-256 |
|---|---|---:|---|---|
{rows}

## Prüfregel

Die Prüfsummen beziehen sich auf die UTF-8-Dateien einschließlich YAML-Front-Matter im Approval-Paket. Das Manifest selbst und informative Reviewdokumente sind nicht Teil des normativen Hashumfangs.
'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / TARGET
    expected = render(repo)
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != expected:
            print(f"FAIL stale approval manifest: {TARGET}")
            return 1
        print(f"OK   approval manifest: {len(DOCS)} documents")
        return 0
    target.write_text(expected, encoding="utf-8")
    print(f"Wrote {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
