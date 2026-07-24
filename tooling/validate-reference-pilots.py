#!/usr/bin/env python3
"""Validate reference-pilot manifests and required documentation."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

VALID_STATUSES = {
    "Candidate", "Selected", "Baseline Assessed", "Wave Planned",
    "In Execution", "Wave Validated", "Pilot Closed",
}
VALID_LEVELS = {"Minimum", "Recommended", "Production"}
REQUIRED_KEYS = {
    "schema_version", "pilot_id", "title", "target_repository", "category",
    "project_size", "quality_level", "profiles", "status", "baseline_date",
    "standard_documents", "execution_statement", "documents",
}
REQUIRED_DOCUMENT_KEYS = {
    "charter", "classification", "baseline", "gaps", "migration_plan",
    "wave_01", "evidence", "decisions", "review",
}
PILOT_ID_RE = re.compile(r"^SASD-PILOT-\d{3}$")
GAP_ID_RE = re.compile(r"^\|\s*P\d{2}-GAP-\d{3}\s*\|", re.M)
DECISION_ID_RE = re.compile(r"^\|\s*P\d{2}-DEC-\d{3}\s*\|", re.M)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    base = repo / "docs" / "50-reference-implementations"
    manifests = sorted(base.glob("pilot-*/pilot.json"))
    failures = 0
    ids: set[str] = set()

    if not manifests:
        print("FAIL no pilot manifests found")
        return 1

    for manifest in manifests:
        rel = manifest.relative_to(repo)
        errors: list[str] = []
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"FAIL {rel}: invalid JSON: {exc}")
            failures += 1
            continue

        missing = sorted(REQUIRED_KEYS - data.keys())
        if missing:
            errors.append("missing keys: " + ", ".join(missing))
        pilot_id = data.get("pilot_id", "")
        if not PILOT_ID_RE.match(pilot_id):
            errors.append(f"invalid pilot_id: {pilot_id!r}")
        elif pilot_id in ids:
            errors.append(f"duplicate pilot_id: {pilot_id}")
        ids.add(pilot_id)
        if data.get("status") not in VALID_STATUSES:
            errors.append(f"invalid status: {data.get('status')!r}")
        if data.get("quality_level") not in VALID_LEVELS:
            errors.append(f"invalid quality level: {data.get('quality_level')!r}")
        if not isinstance(data.get("profiles"), list) or "Core" not in data.get("profiles", []):
            errors.append("profiles must be a list containing Core")
        documents = data.get("documents", {})
        if not isinstance(documents, dict):
            errors.append("documents must be an object")
        else:
            missing_docs = sorted(REQUIRED_DOCUMENT_KEYS - documents.keys())
            if missing_docs:
                errors.append("missing document mappings: " + ", ".join(missing_docs))
            for key, filename in documents.items():
                if not (manifest.parent / filename).is_file():
                    errors.append(f"missing mapped document {key}: {filename}")

        gap_file = manifest.parent / documents.get("gaps", "")
        if gap_file.is_file() and not GAP_ID_RE.search(gap_file.read_text(encoding="utf-8")):
            errors.append("gap register has no pilot gap IDs")
        decision_file = manifest.parent / documents.get("decisions", "")
        if decision_file.is_file() and not DECISION_ID_RE.search(decision_file.read_text(encoding="utf-8")):
            errors.append("decision log has no pilot decision IDs")

        if errors:
            failures += 1
            print(f"FAIL {rel}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {rel}: {pilot_id} ({data['status']})")

    generator = repo / "tooling" / "generate-pilot-portfolio.py"
    result = subprocess.run([sys.executable, str(generator), "--check"], cwd=repo, text=True, capture_output=True)
    print(result.stdout.strip())
    if result.returncode:
        failures += 1

    print(f"Validated {len(manifests)} pilot manifests; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
