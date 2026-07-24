#!/usr/bin/env python3
"""Validate YAML front matter of SASD standard documents.

The validator intentionally supports the simple top-level metadata format used
by this repository and has no external Python dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

VALID_TYPES = {"normative", "informative", "supporting"}
VALID_STATUSES = {"Planned", "Draft", "Proposed", "Approved", "Deprecated", "Retired"}
REQUIRED_NORMATIVE = {
    "title",
    "document-id",
    "document-type",
    "status",
    "version",
    "standard-version",
    "language",
    "authoritative",
    "owner",
    "last-updated",
    "applies-to-quality-levels",
    "applies-to-profiles",
    "depends-on",
    "normative-keywords",
}
ID_PATTERN = re.compile(r"^SASD-[A-Z0-9-]+$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_front_matter(path: Path) -> tuple[dict[str, str] | None, str | None]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML front matter"

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data, None
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None, f"invalid metadata line: {line!r}"
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return None, "front matter is not closed"


def validate(path: Path) -> tuple[list[str], str | None]:
    data, error = parse_front_matter(path)
    if error:
        return [error], None
    assert data is not None
    errors: list[str] = []
    doc_type = data.get("document-type")
    if doc_type not in VALID_TYPES:
        errors.append(f"unknown document-type: {doc_type!r}")
    if data.get("status") not in VALID_STATUSES:
        errors.append(f"unknown status: {data.get('status')!r}")
    if doc_type == "normative":
        missing = sorted(REQUIRED_NORMATIVE - data.keys())
        if missing:
            errors.append("missing fields: " + ", ".join(missing))
    doc_id = data.get("document-id")
    if not doc_id or not ID_PATTERN.match(doc_id):
        errors.append(f"invalid document-id: {doc_id!r}")
    date = data.get("last-updated")
    if date and not DATE_PATTERN.match(date):
        errors.append(f"invalid last-updated date: {date!r}")
    return errors, doc_id


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip('"') for item in value[1:-1].split(",") if item.strip()]
    return [value.strip('"')] if value else []


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    docs = sorted((repo / "docs").rglob("*.md"))
    document_ids: dict[str, Path] = {}
    results: dict[Path, tuple[list[str], dict[str, str] | None]] = {}

    # First pass: validate basic metadata and collect all document IDs.
    for path in docs:
        if path.name == "README.md":
            continue
        errors, doc_id = validate(path)
        data, parse_error = parse_front_matter(path)
        if parse_error:
            data = None
        if doc_id:
            if doc_id in document_ids:
                errors.append(
                    f"duplicate document-id; also used by {document_ids[doc_id].relative_to(repo)}"
                )
            else:
                document_ids[doc_id] = path
        results[path] = (errors, data)

    # Second pass: validate document dependencies after all IDs are known.
    for path, (errors, data) in results.items():
        if not data:
            continue
        for dependency in parse_inline_list(data.get("depends-on", "[]")):
            if dependency not in document_ids:
                errors.append(f"unknown dependency document-id: {dependency}")

    failures = 0
    for path, (errors, _data) in results.items():
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(repo)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path.relative_to(repo)}")

    print(f"\nValidated {len(results)} standard documents; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
