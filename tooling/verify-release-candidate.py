#!/usr/bin/env python3
"""Independently verify SASD release-candidate preview or release artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

from release_candidate_common import RC_VERSION

CHECKSUM_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")
FORBIDDEN_PARTS = {".git", "artifacts", "__pycache__", ".pytest_cache", ".mypy_cache", "bin", "obj"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_zip(path: Path, expected_kind: str, failures: list[str]) -> dict[str, object] | None:
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                failures.append(f"{path.name}: corrupt member {bad}")
            names = archive.namelist()
            if not names:
                failures.append(f"{path.name}: archive is empty")
                return None
            roots = {PurePosixPath(name).parts[0] for name in names if PurePosixPath(name).parts}
            if len(roots) != 1:
                failures.append(f"{path.name}: expected one root directory, found {sorted(roots)}")
            for name in names:
                pure = PurePosixPath(name)
                if pure.is_absolute() or ".." in pure.parts:
                    failures.append(f"{path.name}: unsafe member path {name}")
                if any(part in FORBIDDEN_PARTS for part in pure.parts):
                    failures.append(f"{path.name}: forbidden member path {name}")
            metadata_members = [name for name in names if name.endswith("/RELEASE-METADATA.json")]
            if len(metadata_members) != 1:
                failures.append(f"{path.name}: expected one RELEASE-METADATA.json")
                return None
            data = json.loads(archive.read(metadata_members[0]).decode("utf-8"))
            if data.get("standard_version") != RC_VERSION:
                failures.append(f"{path.name}: metadata standard version is invalid")
            if data.get("archive_kind") != expected_kind:
                failures.append(f"{path.name}: metadata archive kind is not {expected_kind}")
            return data
    except (zipfile.BadZipFile, json.JSONDecodeError, UnicodeDecodeError) as error:
        failures.append(f"{path.name}: {error}")
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", default="artifacts/release-candidate")
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    failures: list[str] = []
    checksum_path = directory / "SHA256SUMS.txt"
    if not checksum_path.is_file():
        print(f"FAIL missing {checksum_path}")
        return 1

    expected: dict[str, str] = {}
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        match = CHECKSUM_LINE.fullmatch(line)
        if not match:
            failures.append(f"invalid checksum line: {line!r}")
            continue
        digest, name = match.groups()
        if Path(name).name != name or name in expected:
            failures.append(f"unsafe or duplicate checksum filename: {name}")
            continue
        expected[name] = digest

    for name, digest in expected.items():
        path = directory / name
        if not path.is_file():
            failures.append(f"missing checksummed file: {name}")
        elif sha256(path) != digest:
            failures.append(f"checksum mismatch: {name}")

    manifests = [directory / name for name in expected if name.endswith("release-manifest.json")]
    if len(manifests) != 1:
        failures.append("expected exactly one release manifest in SHA256SUMS.txt")
        manifest = None
    else:
        try:
            manifest = json.loads(manifests[0].read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            failures.append(f"invalid release manifest: {error}")
            manifest = None

    if manifest:
        if manifest.get("standard_version") != RC_VERSION:
            failures.append("release manifest standard version is invalid")
        listed = {item.get("path"): item for item in manifest.get("artifacts", []) if isinstance(item, dict)}
        for name, item in listed.items():
            if name not in expected:
                failures.append(f"manifest artifact is absent from SHA256SUMS: {name}")
            elif item.get("sha256") != expected[name]:
                failures.append(f"manifest hash differs from SHA256SUMS: {name}")
        source = next((directory / name for name in listed if name and name.endswith("source.zip")), None)
        markdown = next((directory / name for name in listed if name and name.endswith("markdown.zip")), None)
        source_meta = verify_zip(source, "source", failures) if source else None
        markdown_meta = verify_zip(markdown, "markdown", failures) if markdown else None
        if not source:
            failures.append("release manifest contains no source archive")
        if not markdown:
            failures.append("release manifest contains no Markdown archive")
        if source_meta and markdown_meta:
            for key in ("standard_version", "source_commit", "source_timestamp", "mode"):
                if source_meta.get(key) != markdown_meta.get(key):
                    failures.append(f"archive metadata differs for {key}")
            if manifest.get("source_commit") != source_meta.get("source_commit"):
                failures.append("manifest and archive source commits differ")

    if failures:
        print("Release-candidate artifact verification failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nFailures: {len(failures)}")
        return 1

    print(f"OK   checksums: {len(expected)} files")
    print("OK   source and Markdown ZIP integrity")
    print("OK   archive paths are safe and contain no forbidden build state")
    print("OK   manifest and archive metadata are consistent")
    print("\nRelease-candidate artifact failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
