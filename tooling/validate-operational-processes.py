#!/usr/bin/env python3
"""Validate the 0.9.0 operational process handbook."""

from __future__ import annotations
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

FILES = [
    "NEW-PROJECT.md",
    "PROJECT-CLASSIFICATION.md",
    "ARCHITECTURE-DECISION-PROCESS.md",
    "REVIEW-PROCESS.md",
    "LEGACY-MIGRATION.md",
    "RELEASE-PROCESS.md",
    "PROJECT-ARCHIVAL.md",
]
RANGES = {
    "NEW-PROJECT.md": range(1, 100),
    "PROJECT-CLASSIFICATION.md": range(100, 200),
    "ARCHITECTURE-DECISION-PROCESS.md": range(200, 300),
    "REVIEW-PROCESS.md": range(300, 400),
    "LEGACY-MIGRATION.md": range(400, 500),
    "RELEASE-PROCESS.md": range(500, 600),
    "PROJECT-ARCHIVAL.md": range(600, 700),
}
ROW = re.compile(r"^\|\s*(SASD-PROC-REQ-(\d{3}))\s*\|\s*(.*?)\s*\|\s*$")
NORMATIVE = re.compile(r"\b(?:MUSS|MÜSSEN|DARF NICHT|DÜRFEN NICHT|SOLLTE|SOLLTEN|SOLLTE NICHT|SOLLTEN NICHT|KANN|KÖNNEN)\b")
PLACEHOLDER = re.compile(r"(?:^|\s)(?:TODO|TBD|FIXME)\s*:", re.IGNORECASE | re.MULTILINE)
SECTIONS = ["Zweck", "Geltungsbereich", "Auslöser", "Benötigte Eingaben", "Rollen und Verantwortlichkeiten", "Prozessablauf", "Normative Anforderungen", "Zuordnung zu Qualitätsstufen", "Ergebnisse und Nachweise", "Abschlusskriterien", "Ausnahmen und Abweichungen", "Verwandte Dokumente"]
TEMPLATES = [
    "templates/documents/PROJECT-CLASSIFICATION-TEMPLATE.md",
    "templates/documents/PROJECT-INITIALIZATION-RECORD-TEMPLATE.md",
    "templates/architecture-decisions/ADR-TEMPLATE.md",
    "templates/architecture-decisions/ADR-INDEX-TEMPLATE.md",
    "templates/documents/REVIEW-RECORD-TEMPLATE.md",
    "templates/documents/LEGACY-MIGRATION-ASSESSMENT-TEMPLATE.md",
    "templates/documents/LEGACY-MIGRATION-PLAN-TEMPLATE.md",
    "templates/documents/RELEASE-RECORD-TEMPLATE.md",
    "templates/documents/PROJECT-ARCHIVAL-RECORD-TEMPLATE.md",
]


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    folder = repo / "docs" / "30-processes"
    failures = 0
    ids = {}
    normalized = defaultdict(list)
    total = 0
    for name in FILES:
        path = folder / name
        errors = []
        if not path.exists():
            print(f"FAIL missing process document: {path.relative_to(repo)}")
            failures += 1
            continue
        text = path.read_text(encoding="utf-8")
        meta = text.split("---", 2)[1] if text.startswith("---") else ""
        if not any(marker in meta for marker in ("status: Proposed", "status: Approved")):
            errors.append("metadata status is neither Proposed nor Approved")
        if "version: 0.9.0" not in meta:
            errors.append("metadata version is not 0.9.0")
        for section in SECTIONS:
            if section not in text:
                errors.append(f"missing section concept: {section}")
        if PLACEHOLDER.search(text):
            errors.append("contains TODO/TBD/FIXME placeholder")
        found = 0
        for line in text.splitlines():
            match = ROW.match(line)
            if not match:
                continue
            found += 1
            total += 1
            rid, num_text, statement = match.groups()
            num = int(num_text)
            if num not in RANGES[name]:
                errors.append(f"{rid} is outside allocated range for {name}")
            if rid in ids:
                errors.append(f"duplicate ID; also used in {ids[rid]}")
            ids[rid] = name
            if not NORMATIVE.search(statement):
                errors.append(f"{rid} has no normative keyword")
            norm = re.sub(r"\s+", " ", statement.strip().lower())
            normalized[norm].append((rid, name))
        if found == 0:
            errors.append("contains no process requirement rows")
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(repo)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path.relative_to(repo)}: {found} requirements")

    for _statement, occurrences in normalized.items():
        if len(occurrences) > 1:
            failures += 1
            details = ", ".join(f"{rid} ({name})" for rid, name in occurrences)
            print(f"FAIL exact duplicate process requirement text: {details}")

    for rel in TEMPLATES:
        path = repo / rel
        if not path.exists() or path.stat().st_size < 150:
            failures += 1
            print(f"FAIL missing or too small process template: {rel}")

    for script in ["generate-process-requirements-index.py", "generate-process-quality-matrix.py"]:
        result = subprocess.run([sys.executable, str(repo / "tooling" / script), "--check"], check=False)
        if result.returncode:
            failures += 1

    print(f"\nValidated {total} operational process requirements; failures: {failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
