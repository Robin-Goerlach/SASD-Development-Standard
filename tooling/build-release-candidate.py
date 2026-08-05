#!/usr/bin/env python3
"""Build deterministic SASD Version 1.0 RC source and Markdown archives."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

from release_candidate_common import (
    AUTHORITATIVE_LANGUAGE,
    RC_TAG,
    RC_VERSION,
    git_value,
    readiness,
    repository_root,
    safe_relative_files,
    sha256_file,
)

SOURCE_DIRECTORIES = [
    ".github",
    "artefacts",
    "checklists",
    "docs",
    "examples",
    "prompts",
    "scripts",
    "templates",
    "tooling",
]
SOURCE_FILES = [
    ".editorconfig",
    ".gitignore",
    ".markdownlint.json",
    "CHANGELOG.md",
    "CI-IMPLEMENTATION-MANIFEST.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "docs/90-project-history/update-manifests/FOUNDATION-GOVERNANCE-APPROVAL-UPDATE-MANIFEST.md",
    "docs/90-project-history/update-manifests/FOUNDATION-GOVERNANCE-UPDATE-MANIFEST.md",
    "GITHUB-SETUP.md",
    "LICENSE",
    "docs/90-project-history/update-manifests/PILOT-PORTFOLIO-EXPANSION-UPDATE-MANIFEST.md",
    "README.md",
    "PROJECT-STATUS.md",
    "docs/90-project-history/update-manifests/RELEASE-CANDIDATE-PREPARATION-UPDATE-MANIFEST.md",
    "REPOSITORY-DESCRIPTION.txt",
    "REPOSITORY-IDENTITY.json",
    "REPOSITORY-MANIFEST.txt",
    "ROADMAP.md",
    "SECURITY.md",
]
MARKDOWN_DIRECTORIES = ["checklists", "docs", "examples", "prompts", "templates"]
MARKDOWN_FILES = [
    "README.md",
    "PROJECT-STATUS.md",
    "LICENSE",
    "CHANGELOG.md",
    "ROADMAP.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
]
FORBIDDEN_ARCHIVE_PARTS = {".git", "artifacts", "__pycache__", ".pytest_cache", ".mypy_cache", "bin", "obj"}


def run_git(repo: Path, *args: str) -> str | None:
    return git_value(repo, *args)


def commit_timestamp(repo: Path, commit: str | None) -> tuple[str, tuple[int, int, int, int, int, int]]:
    raw = run_git(repo, "show", "-s", "--format=%ct", commit or "HEAD") if commit else None
    try:
        value = int(raw) if raw else 315532800
    except ValueError:
        value = 315532800
    dt = datetime.fromtimestamp(max(value, 315532800), tz=timezone.utc).replace(microsecond=0)
    # ZIP timestamps have 2-second precision and cannot precede 1980.
    second = dt.second - (dt.second % 2)
    return dt.isoformat().replace("+00:00", "Z"), (dt.year, dt.month, dt.day, dt.hour, dt.minute, second)


def validate_member(relative: Path) -> None:
    pure = PurePosixPath(relative.as_posix())
    if pure.is_absolute() or ".." in pure.parts:
        raise ValueError(f"unsafe archive path: {relative}")
    if any(part in FORBIDDEN_ARCHIVE_PARTS for part in pure.parts):
        raise ValueError(f"forbidden archive path: {relative}")


def zip_info(name: str, timestamp: tuple[int, int, int, int, int, int]) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=timestamp)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def metadata_bytes(mode: str, commit: str, source_time: str, archive_kind: str, dirty: bool) -> bytes:
    data: dict[str, Any] = {
        "schema_version": "1.0",
        "standard_version": RC_VERSION,
        "tag": RC_TAG,
        "mode": mode,
        "archive_kind": archive_kind,
        "source_commit": commit,
        "source_timestamp": source_time,
        "authoritative_language": AUTHORITATIVE_LANGUAGE,
        "working_tree_dirty": dirty,
        "publication_status": "preview" if mode == "preview" else "release-candidate",
    }
    return (json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def build_zip(
    repo: Path,
    output: Path,
    root_name: str,
    files: list[Path],
    metadata: bytes,
    timestamp: tuple[int, int, int, int, int, int],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr(zip_info(f"{root_name}/RELEASE-METADATA.json", timestamp), metadata)
        for relative in files:
            validate_member(relative)
            path = repo / relative
            archive.writestr(
                zip_info(f"{root_name}/{relative.as_posix()}", timestamp),
                path.read_bytes(),
            )


def selected_files(repo: Path, directories: list[str], files: list[str]) -> list[Path]:
    result = safe_relative_files(repo, directories)
    for name in files:
        path = repo / name
        if path.is_file():
            result.append(Path(name))
    return sorted(set(result), key=lambda item: item.as_posix().casefold())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("preview", "release"), default="preview")
    parser.add_argument("--output-dir", default="artifacts/release-candidate")
    args = parser.parse_args()

    repo = repository_root()
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = repo / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    commit = run_git(repo, "rev-parse", "HEAD") or "unavailable"
    status = run_git(repo, "status", "--porcelain")
    dirty = bool(status) if status is not None else True
    branch = run_git(repo, "branch", "--show-current") or "unavailable"

    if args.mode == "release":
        state = readiness(repo)
        if not state["ready"]:
            print("ERROR: release readiness is not satisfied: " + ", ".join(state["blocking_failures"]), file=sys.stderr)
            return 1
        if commit == "unavailable" or len(commit) != 40:
            print("ERROR: release mode requires a Git checkout with a full HEAD commit", file=sys.stderr)
            return 1
        if dirty:
            print("ERROR: release mode requires a clean working tree", file=sys.stderr)
            return 1

    source_time, timestamp = commit_timestamp(repo, commit if commit != "unavailable" else None)
    qualifier = "preview-" if args.mode == "preview" else ""
    base = f"SASD-Development-Standard-{RC_VERSION}"
    source_name = f"{base}-{qualifier}source.zip"
    markdown_name = f"{base}-{qualifier}markdown.zip"
    manifest_name = f"{base}-{qualifier}release-manifest.json"

    source_files = selected_files(repo, SOURCE_DIRECTORIES, SOURCE_FILES)
    markdown_files = selected_files(repo, MARKDOWN_DIRECTORIES, MARKDOWN_FILES)

    root_source = f"{base}-{qualifier}source".rstrip("-")
    root_markdown = f"{base}-{qualifier}markdown".rstrip("-")
    build_zip(
        repo,
        output_dir / source_name,
        root_source,
        source_files,
        metadata_bytes(args.mode, commit, source_time, "source", dirty),
        timestamp,
    )
    build_zip(
        repo,
        output_dir / markdown_name,
        root_markdown,
        markdown_files,
        metadata_bytes(args.mode, commit, source_time, "markdown", dirty),
        timestamp,
    )

    artifacts = []
    for name in (source_name, markdown_name):
        path = output_dir / name
        artifacts.append({"path": name, "sha256": sha256_file(path), "size_bytes": path.stat().st_size})

    manifest: dict[str, Any] = {
        "schema_version": "1.0",
        "standard_version": RC_VERSION,
        "tag": RC_TAG,
        "mode": args.mode,
        "source_commit": commit,
        "source_branch": branch,
        "source_timestamp": source_time,
        "working_tree_dirty": dirty,
        "authoritative_language": AUTHORITATIVE_LANGUAGE,
        "source_file_count": len(source_files),
        "markdown_file_count": len(markdown_files),
        "artifacts": artifacts,
        "readiness": readiness(repo),
    }
    manifest_path = output_dir / manifest_name
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")

    checksums = [(item["sha256"], item["path"]) for item in artifacts]
    checksums.append((sha256_file(manifest_path), manifest_name))
    (output_dir / "SHA256SUMS.txt").write_text(
        "".join(f"{digest}  {name}\n" for digest, name in checksums), encoding="utf-8"
    )

    report = [
        "# Release Candidate Package Build",
        "",
        f"- Mode: `{args.mode}`",
        f"- Standard version: `{RC_VERSION}`",
        f"- Source commit: `{commit}`",
        f"- Working tree dirty: `{dirty}`",
        f"- Source files: `{len(source_files)}`",
        f"- Markdown files: `{len(markdown_files)}`",
        "",
        "## Artifacts",
        "",
        "| File | SHA-256 | Size |",
        "|---|---|---:|",
    ]
    for item in artifacts:
        report.append(f"| `{item['path']}` | `{item['sha256']}` | {item['size_bytes']} |")
    report.extend(
        [
            f"| `{manifest_name}` | `{sha256_file(manifest_path)}` | {manifest_path.stat().st_size} |",
            "",
            "Preview mode does not prove release readiness, create a tag, or publish a GitHub Release.",
            "",
        ]
    )
    (output_dir / "BUILD-REPORT.md").write_text("\n".join(report), encoding="utf-8")

    print(f"Built {source_name} with {len(source_files)} files")
    print(f"Built {markdown_name} with {len(markdown_files)} files")
    print(f"Wrote {manifest_name} and SHA256SUMS.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
