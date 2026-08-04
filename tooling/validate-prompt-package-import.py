#!/usr/bin/env python3
"""Statische, dependency-freie Prüfung für den Phase-25-Promptpaketimport."""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest_path = root / "SASD-PROMPT-PACKAGE-IMPORT-UPDATE-MANIFEST.json"
required = [
    "src/Sasd.PromptManager.Application/PromptPackages/SasdPromptPackageModels.cs",
    "src/Sasd.PromptManager.Application/PromptPackages/SasdPromptPackageReader.cs",
    "src/Sasd.PromptManager.Application/PromptPackages/SasdPromptPackageImportService.cs",
    "src/Sasd.PromptManager.App/Dialogs/SasdPromptPackageImportDialog.cs",
    "tests/Sasd.PromptManager.Domain.Tests/PromptPackages/SasdPromptPackageReaderTests.cs",
    "tests/Sasd.PromptManager.Domain.Tests/PromptPackages/SasdPromptPackageImportServiceTests.cs",
    "docs/250_SASD_Prompt_Package_Import.md",
    "docs/251_SASD_Prompt_Package_Verification.md",
    "scripts/verify-prompt-package-import.ps1",
    manifest_path.name,
]
errors: list[str] = []

for relative in required:
    if not (root / relative).is_file():
        errors.append(f"Missing: {relative}")

main_form = root / "src/Sasd.PromptManager.App/MainForm.cs"
if main_form.is_file():
    text = main_form.read_text(encoding="utf-8")
    for token in (
        "SASD-Promptpaket importieren",
        "ImportSasdPromptPackage()",
        "SasdPromptPackageImportDialog",
        "0.25.0-phase25",
    ):
        if token not in text:
            errors.append(f"MainForm integration missing: {token}")

if manifest_path.is_file():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("target_repository") != "Robin-Goerlach/SASD-Prompt-Manager":
            errors.append("Update manifest targets the wrong repository")
        entries = manifest.get("files", [])
        if manifest.get("file_count") != len(entries):
            errors.append("Update manifest file_count does not match files")
        seen: set[str] = set()
        for entry in entries:
            relative = entry.get("path", "")
            expected = entry.get("sha256", "")
            if relative in seen:
                errors.append(f"Duplicate update-manifest path: {relative}")
                continue
            seen.add(relative)
            file = root / relative
            if not file.is_file():
                errors.append(f"Manifest file missing: {relative}")
                continue
            actual = hashlib.sha256(file.read_bytes()).hexdigest()
            if actual.lower() != str(expected).lower():
                errors.append(f"Manifest SHA-256 mismatch: {relative}")
    except (OSError, json.JSONDecodeError) as exception:
        errors.append(f"Invalid update manifest: {exception}")

for file in root.rglob("*.cs"):
    try:
        text = file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"Not UTF-8: {file.relative_to(root)}")
        continue
    if "\t" in text:
        errors.append(f"Tab character: {file.relative_to(root)}")
    if not text.endswith("\n"):
        errors.append(f"No final newline: {file.relative_to(root)}")

print(f"Phase 25 static validation errors: {len(errors)}")
for error in errors:
    print("ERROR:", error)
sys.exit(1 if errors else 0)
