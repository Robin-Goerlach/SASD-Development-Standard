#!/usr/bin/env python3
"""Build a deterministic distributable SASD prompt-package archive."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from prompt_package_common import load_json, package_paths, package_source_files, repository_root, sha256_file

FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)


def git_value(repo: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(["git", *args], cwd=repo, check=False, capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError:
        return None
    value = result.stdout.strip()
    return value if result.returncode == 0 and value else None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="artifacts/prompt-packages")
    parser.add_argument("--clean", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = repository_root()
    output = Path(args.output_dir)
    if not output.is_absolute():
        output = repo / output
    if args.clean and output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    manifest = load_json(package_paths(repo)["manifest"])
    root_name = f"SASD-Development-Standard-Prompt-Package-{manifest['version']}-{manifest['status']}"
    archive_name = root_name + ".zip"
    archive = output / archive_name
    source_files = package_source_files(repo)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in source_files:
            relative = path.relative_to(repo).as_posix()
            target = f"{root_name}/{relative}"
            info = zipfile.ZipInfo(target, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes())

    build_manifest = {
        "schema_version": "1.0",
        "format": "sasd-prompt-package-build/1.0",
        "package_id": manifest["package_id"],
        "package_version": manifest["version"],
        "package_status": manifest["status"],
        "source_commit": git_value(repo, "rev-parse", "HEAD") or "not-available",
        "source_file_count": len(source_files),
        "archive": archive.name,
        "archive_sha256": sha256_file(archive),
        "archive_root": root_name,
        "fixed_zip_timestamp": "2026-01-01T00:00:00Z",
    }
    manifest_path = output / (root_name + "-build-manifest.json")
    manifest_path.write_text(json.dumps(build_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sums_path = output / "SHA256SUMS.txt"
    sums_path.write_text(
        f"{sha256_file(archive)}  {archive.name}\n{sha256_file(manifest_path)}  {manifest_path.name}\n",
        encoding="utf-8",
    )
    report = output / "BUILD-REPORT.md"
    report.write_text(
        "# Prompt Package Build Report\n\n"
        f"- Package: `{manifest['package_id']}`\n"
        f"- Version: `{manifest['version']}`\n"
        f"- Status: `{manifest['status']}`\n"
        f"- Source commit: `{build_manifest['source_commit']}`\n"
        f"- Source files: **{len(source_files)}**\n"
        f"- Archive: `{archive.name}`\n"
        f"- SHA-256: `{build_manifest['archive_sha256']}`\n"
        "- Deterministic ZIP timestamp: `2026-01-01T00:00:00Z`\n",
        encoding="utf-8",
    )
    print(f"Built {archive.relative_to(repo) if archive.is_relative_to(repo) else archive}")
    print(f"Files: {len(source_files)}")
    print(f"SHA-256: {build_manifest['archive_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
