#!/usr/bin/env python3
"""Shared helpers for SASD Version 1.0 release-candidate tooling."""

from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

RC_VERSION = "1.0.0-rc.1"
RC_TAG = "v1.0.0-rc.1"
PREPARATION_VERSION = "0.12.0"
AUTHORITATIVE_LANGUAGE = "de"
EXPECTED_NORMATIVE_DOCUMENTS = 46
EXPECTED_PILOT_SIZES = {"Small", "Medium", "Large"}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def normative_documents(repo: Path) -> list[tuple[Path, dict[str, str]]]:
    result: list[tuple[Path, dict[str, str]]] = []
    for path in sorted((repo / "docs").rglob("*.md")):
        if path.name == "README.md":
            continue
        data = parse_front_matter(path)
        if data.get("document-type") == "normative":
            result.append((path, data))
    return result


def pilot_manifests(repo: Path) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    base = repo / "docs" / "50-reference-implementations"
    for path in sorted(base.glob("pilot-*/pilot.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_path"] = path.relative_to(repo).as_posix()
        result.append(data)
    return result


def ci_activation_evidence(repo: Path) -> dict[str, Any] | None:
    path = (
        repo
        / "docs"
        / "50-reference-implementations"
        / "repository-self-hosting"
        / "CI-ACTIVATION-EVIDENCE.json"
    )
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def git_value(repo: Path, *arguments: str) -> str | None:
    try:
        process = subprocess.run(
            ["git", *arguments],
            cwd=repo,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return None
    return process.stdout.strip() if process.returncode == 0 else None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def readiness(repo: Path) -> dict[str, Any]:
    normative = normative_documents(repo)
    approved = [(path, data) for path, data in normative if data.get("status") == "Approved"]
    pilots = pilot_manifests(repo)
    size_counts = Counter(str(item.get("project_size")) for item in pilots)
    assessed_states = {"Baseline Assessed", "Wave Planned", "In Execution", "Wave Validated", "Pilot Closed"}
    assessed = [item for item in pilots if item.get("status") in assessed_states]
    verified = [item for item in pilots if item.get("verification_state") == "Passed"]
    evidence = ci_activation_evidence(repo)

    ci_workflow_passed = False
    ruleset_active = False
    ci_commit = None
    workflow_url = None
    if evidence:
        workflow = evidence.get("workflow") or {}
        jobs = workflow.get("jobs") or []
        expected = {"Validate (ubuntu-latest)", "Validate (windows-latest)", "SASD merge gate"}
        successful = {
            str(item.get("name"))
            for item in jobs
            if isinstance(item, dict)
            and item.get("status") == "completed"
            and item.get("conclusion") == "success"
        }
        ci_workflow_passed = (
            workflow.get("status") == "completed"
            and workflow.get("conclusion") == "success"
            and expected.issubset(successful)
        )
        ruleset = evidence.get("ruleset") or {}
        ruleset_active = all(
            bool(ruleset.get(key))
            for key in (
                "active",
                "required_check_present",
                "strict_policy",
                "deletion_blocked",
                "force_push_blocked",
                "targets_default_branch",
            )
        )
        ci_commit = evidence.get("commit")
        workflow_url = workflow.get("html_url")

    required_files = [
        "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-PLAN.md",
        "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md",
        "docs/40-governance/VERSION-1.0-RELEASE-NOTES-DRAFT.md",
        "docs/40-governance/VERSION-1.0-RC1-RELEASE-RECORD-DRAFT.md",
        "docs/40-governance/VERSION-1.0-PUBLICATION-PROFILE.md",
        "checklists/releases/VERSION-1.0-RC-CHECKLIST.md",
        "tooling/build-release-candidate.py",
        "tooling/verify-release-candidate.py",
    ]
    missing_files = [item for item in required_files if not (repo / item).is_file()]

    checks = [
        {
            "id": "RC-RDY-001",
            "name": "All normative documents are Approved",
            "passed": len(normative) == EXPECTED_NORMATIVE_DOCUMENTS and len(approved) == EXPECTED_NORMATIVE_DOCUMENTS,
            "detail": f"{len(approved)}/{len(normative)} Approved",
            "blocking": True,
        },
        {
            "id": "RC-RDY-002",
            "name": "Small, Medium and Large pilot baselines are documented",
            "passed": EXPECTED_PILOT_SIZES.issubset(size_counts) and len(assessed) >= 3,
            "detail": f"sizes={dict(size_counts)}, assessed={len(assessed)}",
            "blocking": True,
        },
        {
            "id": "RC-RDY-003",
            "name": "At least one pilot is technically verified",
            "passed": len(verified) >= 1,
            "detail": f"verified={len(verified)}",
            "blocking": True,
        },
        {
            "id": "RC-RDY-004",
            "name": "Exact-commit cross-platform GitHub Actions evidence exists",
            "passed": ci_workflow_passed,
            "detail": f"commit={ci_commit or 'pending'}, workflow={workflow_url or 'pending'}",
            "blocking": True,
        },
        {
            "id": "RC-RDY-005",
            "name": "Governed main ruleset is active",
            "passed": ruleset_active,
            "detail": "active" if ruleset_active else "pending or incomplete",
            "blocking": True,
        },
        {
            "id": "RC-RDY-006",
            "name": "Release-candidate documents and tools are present",
            "passed": not missing_files,
            "detail": "complete" if not missing_files else "missing: " + ", ".join(missing_files),
            "blocking": True,
        },
        {
            "id": "RC-RDY-007",
            "name": "Word and PDF publication artefacts exist",
            "passed": any((repo / "artefacts/publications").glob("*.docx"))
            and any((repo / "artefacts/publications").glob("*.pdf")),
            "detail": "required for stable 1.0.0, not for initial RC publication",
            "blocking": False,
        },
    ]

    blocking_failures = [item for item in checks if item["blocking"] and not item["passed"]]
    return {
        "schema_version": "1.0",
        "release_candidate": RC_VERSION,
        "tag": RC_TAG,
        "checks": checks,
        "ready": not blocking_failures,
        "blocking_failures": [item["id"] for item in blocking_failures],
        "normative_documents": len(normative),
        "approved_normative_documents": len(approved),
        "pilots": len(pilots),
        "assessed_pilots": len(assessed),
        "verified_pilots": len(verified),
        "pilot_sizes": dict(size_counts),
        "ci_commit": ci_commit,
        "ci_workflow_url": workflow_url,
        "ruleset_active": ruleset_active,
    }


def safe_relative_files(repo: Path, roots: Iterable[str]) -> list[Path]:
    excluded_parts = {
        ".git",
        "artifacts",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".idea",
        ".vscode",
        ".vs",
        "bin",
        "obj",
    }
    excluded_names = {".DS_Store", "Thumbs.db", "Desktop.ini"}
    result: list[Path] = []
    for root_name in roots:
        root = repo / root_name
        if not root.exists():
            continue
        paths = [root] if root.is_file() else root.rglob("*")
        for path in paths:
            if not path.is_file():
                continue
            rel = path.relative_to(repo)
            if any(part in excluded_parts for part in rel.parts):
                continue
            if rel.name in excluded_names or rel.suffix.lower() in {".pyc", ".pyo"}:
                continue
            if rel.parts[:2] == ("artefacts", "publications") and rel.suffix.lower() in {".docx", ".pdf"}:
                continue
            result.append(rel)
    return sorted(set(result), key=lambda item: item.as_posix().casefold())
