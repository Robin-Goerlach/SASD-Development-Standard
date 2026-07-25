#!/usr/bin/env python3
"""Validate Version 1.0 pilot portfolio coverage without overstating execution evidence."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_SIZES = {"Small", "Medium", "Large"}
REQUIRED_PILOTS = {"SASD-PILOT-001", "SASD-PILOT-002", "SASD-PILOT-003"}
ASSESSED_STATUSES = {"Baseline Assessed", "Wave Planned", "In Execution", "Wave Validated", "Pilot Closed"}
REQUIRED_STANDARD_AREAS = {"core", "dotnet", "processes"}
REQUIRED_DOCUMENTS = {"baseline", "gaps", "migration_plan", "lessons_learned"}
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    base = repo / "docs/50-reference-implementations"
    failures: list[str] = []
    manifests: list[tuple[Path, dict]] = []

    for path in sorted(base.glob("pilot-*/pilot.json")):
        try:
            manifests.append((path, json.loads(path.read_text(encoding="utf-8"))))
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"invalid pilot manifest {path.relative_to(repo)}: {error}")

    ids = {data.get("pilot_id") for _, data in manifests}
    sizes = {data.get("project_size") for _, data in manifests}
    missing_pilots = sorted(REQUIRED_PILOTS - ids)
    missing_sizes = sorted(REQUIRED_SIZES - sizes)
    if missing_pilots:
        failures.append("missing required pilots: " + ", ".join(missing_pilots))
    if missing_sizes:
        failures.append("missing project-size coverage: " + ", ".join(missing_sizes))

    for path, data in manifests:
        rel = path.relative_to(repo)
        pid = data.get("pilot_id", rel.as_posix())
        if data.get("status") not in ASSESSED_STATUSES:
            failures.append(f"{pid} has not reached Baseline Assessed: {data.get('status')!r}")
        standard_areas = set(data.get("standard_documents", {}))
        missing_areas = sorted(REQUIRED_STANDARD_AREAS - standard_areas)
        if missing_areas:
            failures.append(f"{pid} lacks standard areas: {', '.join(missing_areas)}")

        documents = data.get("documents", {})
        # Pilot 01 historically used interim_retrospective; schema 1.2 maps it as lessons_learned.
        missing_docs = sorted(REQUIRED_DOCUMENTS - set(documents))
        if missing_docs:
            failures.append(f"{pid} lacks portfolio evidence documents: {', '.join(missing_docs)}")
        for key in REQUIRED_DOCUMENTS:
            filename = documents.get(key)
            if filename and not (path.parent / filename).is_file():
                failures.append(f"{pid} missing evidence file for {key}: {filename}")

        observation = data.get("observation", {})
        commit_sha = observation.get("commit_sha") if isinstance(observation, dict) else None
        if commit_sha is not None and not COMMIT_RE.fullmatch(str(commit_sha)):
            failures.append(f"{pid} observation commit is not a full SHA")

    readiness = base / "VERSION-1.0-PILOT-READINESS.md"
    if not readiness.is_file():
        failures.append("missing Version 1.0 pilot-readiness report")

    if failures:
        print("Version 1.0 pilot coverage validation failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nPilot coverage failures: {len(failures)}")
        return 1

    verified = sum(data.get("verification_state") == "Passed" for _, data in manifests)
    print(f"OK   required pilots present: {', '.join(sorted(REQUIRED_PILOTS))}")
    print(f"OK   project-size coverage: {', '.join(sorted(REQUIRED_SIZES))}")
    print(f"OK   all {len(manifests)} pilots reached at least Baseline Assessed")
    print("OK   baseline, gap, migration and lessons-learned evidence is mapped")
    print(f"INFO technically verified pilots: {verified}/{len(manifests)}")
    print("INFO structural coverage does not claim successful target builds, tests or CI")
    print("\nPilot coverage failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
