#!/usr/bin/env python3
"""Validate that files belong to the canonical SASD Development Standard repository."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

IDENTITY_FILE = "REPOSITORY-IDENTITY.json"
IGNORED_TOP_LEVEL = {".git", "artifacts", "__pycache__"}


def load_identity(repo: Path) -> dict[str, Any]:
    path = repo / IDENTITY_FILE
    if not path.is_file():
        raise ValueError(f"missing {IDENTITY_FILE}")
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "schema_version",
        "canonical_repository",
        "repository_kind",
        "required_markers",
        "allowed_top_level_directories",
        "allowed_top_level_files",
        "forbidden_repository_markers",
    }
    missing = sorted(required - data.keys())
    if missing:
        raise ValueError("identity file missing fields: " + ", ".join(missing))
    return data


def git_remote(repo: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=repo,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return None
    value = result.stdout.strip()
    return value if result.returncode == 0 and value else None


def remote_matches(remote: str, canonical_repository: str) -> bool:
    normalized = remote.replace("\\", "/").lower().removesuffix(".git").rstrip("/")
    expected = canonical_repository.lower().strip("/")
    return normalized.endswith("/" + expected) or normalized.endswith(":" + expected)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    try:
        identity = load_identity(repo)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL repository identity: {error}")
        return 1

    for marker in identity["required_markers"]:
        if not (repo / marker).exists():
            failures.append(f"missing canonical repository marker: {marker}")

    for marker in identity["forbidden_repository_markers"]:
        if (repo / marker).exists():
            failures.append(f"foreign or nested repository marker found: {marker}")

    allowed_dirs = set(identity["allowed_top_level_directories"])
    allowed_files = set(identity["allowed_top_level_files"])
    for path in sorted(repo.iterdir(), key=lambda item: item.name.casefold()):
        if path.name in IGNORED_TOP_LEVEL:
            continue
        if path.is_dir() and path.name not in allowed_dirs:
            failures.append(f"unexpected top-level directory: {path.name}/")
        if path.is_file() and path.name not in allowed_files:
            failures.append(f"unexpected top-level file: {path.name}")

    remote = git_remote(repo)
    if remote and not remote_matches(remote, identity["canonical_repository"]):
        failures.append(
            "origin remote does not match canonical repository: "
            f"{remote!r} != {identity['canonical_repository']!r}"
        )

    if failures:
        print("Repository boundary validation failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nRepository boundary failures: {len(failures)}")
        return 1

    print(f"OK   canonical repository: {identity['canonical_repository']}")
    print(f"OK   repository kind: {identity['repository_kind']}")
    print("OK   required repository markers are present")
    print("OK   no foreign or nested repository markers were found")
    print("OK   top-level layout matches the repository identity")
    if remote:
        print(f"OK   origin remote matches: {remote}")
    else:
        print("INFO origin remote not available; content identity was still validated")
    print("\nRepository boundary failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
