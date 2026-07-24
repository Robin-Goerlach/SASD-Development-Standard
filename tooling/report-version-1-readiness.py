#!/usr/bin/env python3
"""Report current Version 1.0 document readiness without claiming approval."""
from __future__ import annotations
import re
import sys
from collections import Counter
from pathlib import Path


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    block = text.split("---", 2)[1]
    data = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"')
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
    print("=" * 52)
    print(f"Normative documents: {len(records)}")
    for status in ["Planned", "Draft", "Proposed", "Approved", "Deprecated", "Retired"]:
        if counts[status]:
            print(f"{status:10}: {counts[status]}")
    not_approved = [r for r in records if r[2] != "Approved"]
    print(f"Release-blocking non-Approved normative documents: {len(not_approved)}")
    if not_approved:
        print("\nNot yet Approved:")
        for path, doc_id, status, version in not_approved:
            print(f"- {doc_id} {status} {version}: {path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
