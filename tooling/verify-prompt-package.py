#!/usr/bin/env python3
"""Independently verify a built SASD prompt-package archive and checksums."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", default="artifacts/prompt-packages")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parents[1]
    directory = Path(args.directory)
    if not directory.is_absolute():
        directory = repo / directory
    failures: list[str] = []
    sums = directory / "SHA256SUMS.txt"
    if not sums.is_file():
        print("FAIL missing SHA256SUMS.txt")
        return 1
    expected: dict[str, str] = {}
    for line in sums.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            sha, name = line.split("  ", 1)
        except ValueError:
            failures.append(f"invalid checksum line: {line!r}")
            continue
        expected[name] = sha
    for name, sha in expected.items():
        path = directory / name
        if not path.is_file():
            failures.append(f"missing artifact: {name}")
        elif digest(path) != sha:
            failures.append(f"checksum mismatch: {name}")

    manifests = list(directory.glob("*-build-manifest.json"))
    archives = list(directory.glob("*.zip"))
    if len(manifests) != 1:
        failures.append(f"expected one build manifest; found {len(manifests)}")
    if len(archives) != 1:
        failures.append(f"expected one ZIP archive; found {len(archives)}")
    if manifests and archives:
        data = json.loads(manifests[0].read_text(encoding="utf-8"))
        archive = archives[0]
        if data.get("archive") != archive.name:
            failures.append("build manifest archive name mismatch")
        if data.get("archive_sha256") != digest(archive):
            failures.append("build manifest archive checksum mismatch")
        roots: set[str] = set()
        try:
            with zipfile.ZipFile(archive) as zf:
                bad = zf.testzip()
                if bad:
                    failures.append(f"ZIP CRC failure: {bad}")
                names = zf.namelist()
                for name in names:
                    pure = PurePosixPath(name)
                    if pure.is_absolute() or ".." in pure.parts:
                        failures.append(f"unsafe ZIP path: {name}")
                    if pure.parts:
                        roots.add(pure.parts[0])
                    if ".git" in pure.parts or "__pycache__" in pure.parts or "artifacts" in pure.parts:
                        failures.append(f"forbidden generated path in ZIP: {name}")
                if roots != {data.get("archive_root")}:
                    failures.append(f"unexpected archive roots: {sorted(roots)}")
                required_suffixes = {
                    "prompts/README.md",
                    "prompts/PACKAGE-SPECIFICATION.md",
                    "prompts/PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md",
                    "prompts/packages/sasd-development-standard-v1/manifest.json",
                    "prompts/packages/sasd-development-standard-v1/catalog.json",
                    "templates/documents/PROMPT-MANAGER-IMPORT-MAPPING-TEMPLATE.md",
                    "checklists/development/PROMPT-MANAGER-IMPORT-ROUNDTRIP-CHECKLIST.md",
                }
                present_suffixes = {"/".join(PurePosixPath(name).parts[1:]) for name in names}
                for suffix in required_suffixes:
                    if suffix not in present_suffixes:
                        failures.append(f"missing required package file in ZIP: {suffix}")
        except zipfile.BadZipFile as error:
            failures.append(f"invalid ZIP: {error}")

    if failures:
        print("Prompt-package artifact verification failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nVerification failures: {len(failures)}")
        return 1
    print(f"OK   checksums: {len(expected)} artifacts")
    print("OK   ZIP integrity and safe paths")
    print("OK   single deterministic archive root")
    print("OK   package identity and required files")
    print("\nVerification failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
