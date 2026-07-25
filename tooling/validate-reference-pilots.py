#!/usr/bin/env python3
"""Validate reference-pilot manifests, evidence states and documentation."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

VALID_SCHEMAS = {"1.0", "1.1", "1.2"}
VALID_STATUSES = {
    "Candidate",
    "Selected",
    "Baseline Assessed",
    "Wave Planned",
    "In Execution",
    "Wave Validated",
    "Pilot Closed",
}
VALID_LEVELS = {"Minimum", "Recommended", "Production"}
VALID_IMPL = {"Not Started", "Artifact Prepared", "Committed", "Verified"}
VALID_VERIFY = {"Pending", "Partial", "Passed", "Failed"}
VALID_EVIDENCE = {"O", "R", "A", "B", "T", "C", "M", "I", "U"}
REQUIRED_KEYS = {
    "schema_version",
    "pilot_id",
    "title",
    "target_repository",
    "category",
    "project_size",
    "quality_level",
    "profiles",
    "status",
    "baseline_date",
    "standard_documents",
    "execution_statement",
    "documents",
}
REQUIRED_DOCUMENT_KEYS = {
    "charter",
    "classification",
    "baseline",
    "gaps",
    "migration_plan",
    "wave_01",
    "evidence",
    "decisions",
    "review",
}
LIFECYCLE_KEYS = {
    "implementation_state",
    "verification_state",
    "current_wave",
    "target_commit",
    "implementation_artifact",
}
PILOT_ID_RE = re.compile(r"^SASD-PILOT-\d{3}$")
GAP_ID_RE = re.compile(r"^\|\s*P\d{2}-GAP-\d{3}\s*\|", re.MULTILINE)
DECISION_ID_RE = re.compile(r"^\|\s*P\d{2}-DEC-\d{3}\s*\|", re.MULTILINE)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_artifact(artifact: Any, required: bool, errors: list[str]) -> None:
    if artifact is None and not required:
        return
    if not isinstance(artifact, dict):
        errors.append("implementation_artifact must be an object when an artifact exists")
        return
    for key in ("name", "sha256", "file_count", "prepared_on"):
        if key not in artifact:
            errors.append(f"implementation_artifact missing {key}")
    if not SHA256_RE.fullmatch(str(artifact.get("sha256", ""))):
        errors.append("invalid artifact sha256")
    if not isinstance(artifact.get("file_count"), int) or artifact.get("file_count", 0) < 1:
        errors.append("invalid artifact file_count")
    if not DATE_RE.fullmatch(str(artifact.get("prepared_on", ""))):
        errors.append("invalid artifact prepared_on date")


def validate_observation(data: dict[str, Any], errors: list[str]) -> None:
    observation = data.get("observation")
    if not isinstance(observation, dict):
        errors.append("schema 1.2 requires an observation object")
        return
    for key in ("branch", "observed_on", "commit_sha", "evidence_classes"):
        if key not in observation:
            errors.append(f"observation missing {key}")
    if not str(observation.get("branch", "")).strip():
        errors.append("observation branch must not be empty")
    if not DATE_RE.fullmatch(str(observation.get("observed_on", ""))):
        errors.append("invalid observation date")
    observed_commit = observation.get("commit_sha")
    if observed_commit is not None and not COMMIT_RE.fullmatch(str(observed_commit)):
        errors.append("observation commit_sha must be null or a full 40-character SHA")
    classes = observation.get("evidence_classes")
    if not isinstance(classes, list) or not classes:
        errors.append("observation evidence_classes must be a non-empty list")
    elif unknown := sorted(set(classes) - VALID_EVIDENCE):
        errors.append("unknown observation evidence classes: " + ", ".join(unknown))


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    base = repo / "docs/50-reference-implementations"
    manifests = sorted(base.glob("pilot-*/pilot.json"))
    failures = 0
    ids: set[str] = set()
    repositories: set[str] = set()

    if not manifests:
        print("FAIL no pilot manifests found")
        return 1

    for manifest in manifests:
        rel = manifest.relative_to(repo)
        errors: list[str] = []
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - defensive error reporting
            print(f"FAIL {rel}: invalid JSON: {exc}")
            failures += 1
            continue

        missing = sorted(REQUIRED_KEYS - data.keys())
        if missing:
            errors.append("missing keys: " + ", ".join(missing))

        schema = str(data.get("schema_version", ""))
        if schema not in VALID_SCHEMAS:
            errors.append(f"unsupported schema_version: {schema!r}")

        pid = str(data.get("pilot_id", ""))
        if not PILOT_ID_RE.fullmatch(pid):
            errors.append(f"invalid pilot_id: {pid!r}")
        elif pid in ids:
            errors.append(f"duplicate pilot_id: {pid}")
        ids.add(pid)

        target_repository = str(data.get("target_repository", ""))
        if not target_repository.startswith("https://github.com/"):
            errors.append("target_repository must be a canonical GitHub HTTPS URL")
        elif target_repository.casefold() in repositories:
            errors.append(f"duplicate target_repository: {target_repository}")
        repositories.add(target_repository.casefold())

        if data.get("status") not in VALID_STATUSES:
            errors.append(f"invalid status: {data.get('status')!r}")
        if data.get("quality_level") not in VALID_LEVELS:
            errors.append(f"invalid quality level: {data.get('quality_level')!r}")
        if not DATE_RE.fullmatch(str(data.get("baseline_date", ""))):
            errors.append("baseline_date must use YYYY-MM-DD")
        if not isinstance(data.get("profiles"), list) or "Core" not in data.get("profiles", []):
            errors.append("profiles must be a list containing Core")
        if not isinstance(data.get("standard_documents"), dict):
            errors.append("standard_documents must be an object")

        docs = data.get("documents", {})
        if not isinstance(docs, dict):
            errors.append("documents must be an object")
            docs = {}
        required_docs = set(REQUIRED_DOCUMENT_KEYS)

        if schema in {"1.1", "1.2"}:
            missing_lifecycle = sorted(LIFECYCLE_KEYS - data.keys())
            if missing_lifecycle:
                errors.append("missing lifecycle keys: " + ", ".join(missing_lifecycle))
            implementation_state = data.get("implementation_state")
            verification_state = data.get("verification_state")
            if implementation_state not in VALID_IMPL:
                errors.append(f"invalid implementation_state: {implementation_state!r}")
            if verification_state not in VALID_VERIFY:
                errors.append(f"invalid verification_state: {verification_state!r}")

            artifact_required = implementation_state in {"Artifact Prepared", "Committed", "Verified"}
            validate_artifact(data.get("implementation_artifact"), artifact_required, errors)

            target_commit = data.get("target_commit")
            if implementation_state in {"Committed", "Verified"}:
                if not COMMIT_RE.fullmatch(str(target_commit or "")):
                    errors.append("Committed or Verified implementation requires a full target_commit SHA")
            elif target_commit is not None and not COMMIT_RE.fullmatch(str(target_commit)):
                errors.append("target_commit must be null or a full 40-character SHA")

            if implementation_state == "Artifact Prepared":
                required_docs.update({"implementation_review", "verification_plan"})
            if implementation_state == "Verified" and verification_state != "Passed":
                errors.append("Verified implementation requires Passed verification")
            if data.get("status") in {"Wave Validated", "Pilot Closed"} and verification_state != "Passed":
                errors.append(f"{data.get('status')} requires Passed verification")

        if schema == "1.2":
            required_docs.add("lessons_learned")
            validate_observation(data, errors)

        missing_docs = sorted(required_docs - docs.keys())
        if missing_docs:
            errors.append("missing document mappings: " + ", ".join(missing_docs))
        for key, filename in docs.items():
            if not isinstance(filename, str) or not filename:
                errors.append(f"invalid mapped document {key}: {filename!r}")
            elif not (manifest.parent / filename).is_file():
                errors.append(f"missing mapped document {key}: {filename}")

        gap = manifest.parent / docs.get("gaps", "")
        if gap.is_file() and not GAP_ID_RE.search(gap.read_text(encoding="utf-8")):
            errors.append("gap register has no pilot gap IDs")
        decision = manifest.parent / docs.get("decisions", "")
        if decision.is_file() and not DECISION_ID_RE.search(decision.read_text(encoding="utf-8")):
            errors.append("decision log has no pilot decision IDs")
        lessons = manifest.parent / docs.get("lessons_learned", "")
        if schema == "1.2" and lessons.is_file() and len(lessons.read_text(encoding="utf-8").strip()) < 200:
            errors.append("lessons learned document is unexpectedly short")

        if errors:
            failures += 1
            print(f"FAIL {rel}")
            for error in errors:
                print("  - " + error)
        else:
            print(
                f"OK   {rel}: {pid} "
                f"({data['status']}; {data.get('implementation_state', '—')}/"
                f"{data.get('verification_state', '—')})"
            )

    for script in (
        "generate-pilot-portfolio.py",
        "generate-pilot-feedback-summary.py",
        "generate-pilot-readiness.py",
    ):
        result = subprocess.run(
            [sys.executable, str(repo / "tooling" / script), "--check"],
            cwd=repo,
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(result.stderr.strip())
        if result.returncode:
            failures += 1

    print(f"Validated {len(manifests)} pilot manifests; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
