#!/usr/bin/env python3
"""Validate structural consistency of the Proposed SASD Core Standard."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

CORE_FILES = [
    "QUALITY-LEVELS.md", "PROJECT-LIFECYCLE.md", "REQUIREMENTS.md",
    "ARCHITECTURE.md", "DOCUMENTATION.md", "REPOSITORY.md", "QUALITY.md",
    "SECURITY.md", "TESTING.md", "RELEASES.md", "MAINTENANCE.md",
    "KNOWLEDGE-MANAGEMENT.md", "AI-ASSISTED-DEVELOPMENT.md",
]
REQ_ROW = re.compile(r"^\|\s*(SASD-(?:QL|LC|REQ|ARCH|DOC|REP|QUAL|SEC|TEST|REL|MNT|KM|AI)-\d{3})\s*\|\s*(.*?)\s*\|\s*$")
NORMATIVE = re.compile(r"\b(?:MUSS|MÜSSEN|DARF NICHT|DÜRFEN NICHT|SOLLTE|SOLLTEN|SOLLTE NICHT|SOLLTEN NICHT|KANN|KÖNNEN)\b")
FORBIDDEN_STATUS = re.compile(r"\b(?:Compliant with Exceptions|Compliant)\b")
PLACEHOLDER = re.compile(r"(?:^|\s)(?:TODO|TBD|FIXME)\s*:", re.IGNORECASE | re.MULTILINE)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    core = repo / "docs" / "10-core-standard"
    failures = 0
    normalized_statements: dict[str, list[tuple[str, str]]] = defaultdict(list)
    total = 0

    for name in CORE_FILES:
        path = core / name
        if not path.exists():
            print(f"FAIL missing Core document: {path.relative_to(repo)}")
            failures += 1
            continue
        text = path.read_text(encoding="utf-8")
        errors: list[str] = []
        if "status: Proposed" not in text.split("---", 2)[1]:
            errors.append("metadata status is not Proposed")
        if "version: 0.3.0" not in text.split("---", 2)[1]:
            errors.append("metadata version is not 0.3.0")
        for heading in ["Zweck", "Geltungsbereich", "Normative Anforderungen", "Verantwortlichkeiten", "Nachweise und Prüfkriterien", "Ausnahmen und Abweichungen", "Verwandte Dokumente"]:
            if heading not in text:
                errors.append(f"missing required section concept: {heading}")
        if PLACEHOLDER.search(text):
            errors.append("contains TODO/TBD/FIXME placeholder")
        if FORBIDDEN_STATUS.search(text):
            errors.append("contains obsolete Compliant terminology")
        found = 0
        for line in text.splitlines():
            match = REQ_ROW.match(line)
            if not match:
                continue
            found += 1
            total += 1
            req_id, statement = match.groups()
            if not NORMATIVE.search(statement):
                errors.append(f"{req_id} has no normative keyword")
            normalized = re.sub(r"\s+", " ", statement.strip().lower())
            normalized_statements[normalized].append((req_id, name))
        if found == 0:
            errors.append("contains no requirement rows")
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(repo)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path.relative_to(repo)}: {found} requirements")

    for statement, occurrences in sorted(normalized_statements.items()):
        files = {name for _req_id, name in occurrences}
        if len(occurrences) > 1 and len(files) > 1:
            failures += 1
            ids = ", ".join(f"{req_id} ({name})" for req_id, name in occurrences)
            print(f"FAIL exact duplicate requirement text: {ids}")

    for script in ["generate-core-requirements-index.py", "generate-core-quality-matrix.py"]:
        result = subprocess.run([sys.executable, str(repo / "tooling" / script), "--check"], check=False)
        if result.returncode:
            failures += 1

    print(f"\nValidated {total} Core requirements for consistency; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
