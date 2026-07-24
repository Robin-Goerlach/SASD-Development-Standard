#!/usr/bin/env python3
"""Validate structure and requirement IDs of the Proposed C#/.NET profile."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

FILES = [
    "DOTNET-PROFILE.md", "SOLUTION-STRUCTURE.md", "CODING-STANDARD.md",
    "ERROR-HANDLING.md", "LOGGING.md", "CONFIGURATION.md",
    "PERSISTENCE.md", "DOTNET-TESTING.md",
]
ROW = re.compile(r"^\|\s*(SASD-DOTNET-REQ-(\d{3}))\s*\|\s*(.*?)\s*\|\s*$")
NORMATIVE = re.compile(r"\b(?:MUSS|MÜSSEN|DARF NICHT|DÜRFEN NICHT|SOLLTE|SOLLTEN|SOLLTE NICHT|SOLLTEN NICHT|KANN|KÖNNEN)\b")
PLACEHOLDER = re.compile(r"(?:^|\s)(?:TODO|TBD|FIXME)\s*:", re.IGNORECASE | re.MULTILINE)
RANGES = {
    "DOTNET-PROFILE.md": range(1, 100),
    "SOLUTION-STRUCTURE.md": range(100, 200),
    "CODING-STANDARD.md": range(200, 300),
    "ERROR-HANDLING.md": range(300, 400),
    "LOGGING.md": range(400, 500),
    "CONFIGURATION.md": range(500, 600),
    "PERSISTENCE.md": range(600, 700),
    "DOTNET-TESTING.md": range(700, 800),
}


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    profile = repo / "docs" / "20-profiles" / "dotnet"
    failures = 0
    ids: dict[str, str] = {}
    normalized: dict[str, list[tuple[str, str]]] = defaultdict(list)
    total = 0

    for name in FILES:
        path = profile / name
        errors: list[str] = []
        if not path.exists():
            print(f"FAIL missing profile document: {path.relative_to(repo)}")
            failures += 1
            continue
        text = path.read_text(encoding="utf-8")
        meta = text.split("---", 2)[1] if text.startswith("---") else ""
        if "status: Proposed" not in meta:
            errors.append("metadata status is not Proposed")
        if "version: 0.4.0" not in meta:
            errors.append("metadata version is not 0.4.0")
        for heading in ["Zweck", "Geltungsbereich", "Normative Anforderungen", "Zuordnung zu Qualitätsstufen", "Verantwortlichkeiten", "Nachweise und Prüfkriterien", "Ausnahmen und Abweichungen", "Verwandte Dokumente"]:
            if heading not in text:
                errors.append(f"missing section concept: {heading}")
        if PLACEHOLDER.search(text):
            errors.append("contains TODO/TBD/FIXME placeholder")
        found = 0
        for line in text.splitlines():
            match = ROW.match(line)
            if not match:
                continue
            found += 1
            total += 1
            rid, number, statement = match.groups()
            num = int(number)
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
            errors.append("contains no requirement rows")
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(repo)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path.relative_to(repo)}: {found} requirements")

    for statement, occurrences in normalized.items():
        if len(occurrences) > 1:
            failures += 1
            details = ", ".join(f"{rid} ({name})" for rid, name in occurrences)
            print(f"FAIL exact duplicate requirement text: {details}")

    result = subprocess.run([sys.executable, str(repo / "tooling" / "generate-dotnet-requirements-index.py"), "--check"], check=False)
    if result.returncode:
        failures += 1

    print(f"\nValidated {total} C#/.NET profile requirements; failures: {failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
