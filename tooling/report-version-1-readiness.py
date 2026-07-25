#!/usr/bin/env python3
"""Report current Version 1.0 document and pilot readiness without overstating evidence."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    block = text.split("---", 2)[1]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    records = []
    for path in sorted((repo / "docs").rglob("*.md")):
        if path.name == "README.md":
            continue
        data = front_matter(path)
        if data.get("document-type") == "normative":
            records.append((path.relative_to(repo), data.get("document-id"), data.get("status"), data.get("version")))

    counts = Counter(status for _, _, status, _ in records)
    print("SASD Development Standard Version 1.0 readiness")
    print("=" * 56)
    print(f"Normative documents: {len(records)}")
    for status in ["Planned", "Draft", "Proposed", "Approved", "Deprecated", "Retired"]:
        if counts[status]:
            print(f"{status:10}: {counts[status]}")
    not_approved = [record for record in records if record[2] != "Approved"]
    print(f"Release-blocking non-Approved normative documents: {len(not_approved)}")

    pilot_base = repo / "docs/50-reference-implementations"
    pilots = []
    for path in sorted(pilot_base.glob("pilot-*/pilot.json")):
        pilots.append(json.loads(path.read_text(encoding="utf-8")))
    size_counts = Counter(item.get("project_size") for item in pilots)
    assessed = sum(item.get("status") in {"Baseline Assessed", "Wave Planned", "In Execution", "Wave Validated", "Pilot Closed"} for item in pilots)
    verified = sum(item.get("verification_state") == "Passed" for item in pilots)
    print("\nReference pilot portfolio")
    print("-" * 56)
    print(f"Registered pilots: {len(pilots)}")
    print(f"At least Baseline Assessed: {assessed}")
    print(f"Technically verified (Passed): {verified}")
    print("Size coverage: " + ", ".join(f"{size}={size_counts.get(size, 0)}" for size in ("Small", "Medium", "Large")))
    print("Interpretation: portfolio coverage is not target-repository execution evidence.")

    if not_approved:
        print("\nNot yet Approved:")
        for path, doc_id, status, version in not_approved:
            print(f"- {doc_id} {status} {version}: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
