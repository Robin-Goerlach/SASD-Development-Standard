#!/usr/bin/env python3
"""Validate SASD prompt packages, prompt metadata, variables and workflow coverage."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from prompt_package_common import (
    ALLOWED_PROMPT_STATUSES,
    ALLOWED_QUALITY_LEVELS,
    PACKAGE_ID,
    PROMPT_ID_PATTERN,
    REQUIRED_PROMPT_FIELDS,
    REQUIRED_SECTIONS,
    SEMVER_PATTERN,
    VARIABLE_PATTERN,
    build_catalog,
    canonical_json,
    discover_prompts,
    load_json,
    package_paths,
    placeholders,
    repository_root,
    unique,
)

REQUIRED_CATEGORIES = {
    "project-initiation",
    "research",
    "requirements",
    "architecture",
    "development",
    "debugging",
    "review",
    "documentation",
    "release",
}
FORBIDDEN_MARKERS = ("[HIER EINFÜGEN]", "TODO", "TBD", "FIXME")
SECRET_PATTERNS = (
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def main() -> int:
    repo = repository_root()
    paths = package_paths(repo)
    failures: list[str] = []

    required_files = [
        *paths.values(),
        repo / "prompts/README.md",
        repo / "prompts/PACKAGE-SPECIFICATION.md",
        repo / "prompts/QUALITY-GUIDE.md",
        repo / "prompts/SECURITY-GUIDE.md",
        repo / "prompts/VARIABLES.md",
        repo / "prompts/PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md",
        repo / "prompts/schema/prompt.schema.json",
        repo / "prompts/schema/prompt-package.schema.json",
        repo / "templates/prompts/VERSIONED-PROMPT-TEMPLATE.md",
        repo / "templates/prompts/PROMPT-PACKAGE-MANIFEST-TEMPLATE.json",
        repo / "checklists/development/PROMPT-PACKAGE-REVIEW-CHECKLIST.md",
        repo / "templates/documents/PROMPT-MANAGER-IMPORT-MAPPING-TEMPLATE.md",
        repo / "checklists/development/PROMPT-MANAGER-IMPORT-ROUNDTRIP-CHECKLIST.md",
    ]
    for path in required_files:
        if not path.exists():
            failures.append(f"missing required prompt-package file: {path.relative_to(repo)}")

    try:
        manifest = load_json(paths["manifest"])
        variables_doc = load_json(paths["variables"])
        categories_doc = load_json(paths["categories"])
        workflow_doc = load_json(paths["workflow"])
        json.loads((repo / "prompts/schema/prompt.schema.json").read_text(encoding="utf-8"))
        json.loads((repo / "prompts/schema/prompt-package.schema.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL cannot load prompt package: {error}")
        return 1

    expected_manifest = {
        "schema_version": "1.0",
        "format": "sasd-prompt-package/1.0",
        "package_id": PACKAGE_ID,
        "status": "candidate",
        "authoritative_language": "de",
    }
    for key, expected in expected_manifest.items():
        if manifest.get(key) != expected:
            failures.append(f"manifest {key!r} must be {expected!r}; found {manifest.get(key)!r}")
    if not SEMVER_PATTERN.fullmatch(str(manifest.get("version", ""))):
        failures.append("manifest version is not semantic versioning")
    compatibility = manifest.get("compatibility", {})
    if compatibility.get("prompt_manager_direct_import") is not False:
        failures.append("direct Prompt Manager import may not be claimed before an exact-version roundtrip")
    roots = manifest.get("prompt_roots", [])
    if set(roots) != REQUIRED_CATEGORIES or not unique(roots):
        failures.append("manifest prompt_roots must contain every required category exactly once")
    declared_resources = manifest.get("supporting_resources", [])
    expected_resources = [
        "prompts/PACKAGE-SPECIFICATION.md",
        "prompts/QUALITY-GUIDE.md",
        "prompts/SECURITY-GUIDE.md",
        "prompts/VARIABLES.md",
        "prompts/PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md",
        "prompts/schema/prompt.schema.json",
        "prompts/schema/prompt-package.schema.json",
        "templates/prompts/VERSIONED-PROMPT-TEMPLATE.md",
        "templates/prompts/PROMPT-PACKAGE-MANIFEST-TEMPLATE.json",
        "templates/documents/PROMPT-MANAGER-IMPORT-MAPPING-TEMPLATE.md",
        "checklists/development/PROMPT-PACKAGE-REVIEW-CHECKLIST.md",
        "checklists/development/PROMPT-MANAGER-IMPORT-ROUNDTRIP-CHECKLIST.md",
    ]
    if declared_resources != expected_resources or not unique(declared_resources):
        failures.append("manifest supporting_resources must match the controlled resource list")
    for resource in declared_resources:
        resource_path = repo / resource
        if not resource_path.is_file():
            failures.append(f"declared supporting resource is missing: {resource}")

    variable_items = variables_doc.get("variables", [])
    variable_names = [item.get("name") for item in variable_items if isinstance(item, dict)]
    if not unique(variable_names):
        failures.append("variable registry contains duplicate names")
    known_variables: set[str] = set()
    for index, item in enumerate(variable_items, start=1):
        if not isinstance(item, dict):
            failures.append(f"variables item {index} is not an object")
            continue
        name = item.get("name", "")
        if not VARIABLE_PATTERN.fullmatch(str(name)):
            failures.append(f"invalid variable name: {name!r}")
        else:
            known_variables.add(name)
        if not item.get("description"):
            failures.append(f"variable lacks description: {name!r}")
        if item.get("type") != "string":
            failures.append(f"variable type must be string: {name!r}")
        if not isinstance(item.get("sensitive"), bool):
            failures.append(f"variable sensitive flag must be boolean: {name!r}")

    categories = categories_doc.get("categories", [])
    category_ids = [item.get("id") for item in categories if isinstance(item, dict)]
    if set(category_ids) != REQUIRED_CATEGORIES or not unique(category_ids):
        failures.append("categories.json must define every required category exactly once")

    try:
        documents = discover_prompts(repo, manifest)
    except (OSError, ValueError) as error:
        print(f"FAIL cannot discover prompts: {error}")
        return 1
    if len(documents) < 30:
        failures.append(f"prompt package must contain at least 30 prompts; found {len(documents)}")
    prompt_ids: list[str] = []
    source_paths: list[str] = []
    for document in documents:
        label = document.relative_path
        metadata = document.metadata
        source_paths.append(label)
        for field in REQUIRED_PROMPT_FIELDS:
            if field not in metadata:
                failures.append(f"{label}: missing metadata field {field!r}")
        prompt_id = str(metadata.get("prompt-id", ""))
        prompt_ids.append(prompt_id)
        if not PROMPT_ID_PATTERN.fullmatch(prompt_id):
            failures.append(f"{label}: invalid prompt-id {prompt_id!r}")
        if metadata.get("package-id") != PACKAGE_ID:
            failures.append(f"{label}: wrong package-id")
        if metadata.get("version") != manifest.get("version"):
            failures.append(f"{label}: prompt version differs from package version")
        if metadata.get("status") not in ALLOWED_PROMPT_STATUSES:
            failures.append(f"{label}: invalid prompt status")
        category = metadata.get("category")
        expected_category = Path(label).parent.name
        if category != expected_category:
            failures.append(f"{label}: category metadata {category!r} differs from directory {expected_category!r}")
        if category not in REQUIRED_CATEGORIES:
            failures.append(f"{label}: unknown category {category!r}")
        if metadata.get("language") != "de":
            failures.append(f"{label}: package prompt language must be de")
        if not str(metadata.get("summary", "")).strip():
            failures.append(f"{label}: summary is empty")
        declared = metadata.get("variables")
        if not isinstance(declared, list) or not unique(declared):
            failures.append(f"{label}: variables must be a unique JSON list")
            declared_set: set[str] = set()
        else:
            declared_set = set(str(item) for item in declared)
            unknown = sorted(declared_set - known_variables)
            if unknown:
                failures.append(f"{label}: unknown declared variables: {', '.join(unknown)}")
        used = placeholders(document.body)
        undeclared = sorted(used - declared_set)
        unused = sorted(declared_set - used)
        if undeclared:
            failures.append(f"{label}: undeclared placeholders: {', '.join(undeclared)}")
        if unused:
            failures.append(f"{label}: declared but unused variables: {', '.join(unused)}")
        tags = metadata.get("tags")
        if not isinstance(tags, list) or not tags or not unique(tags):
            failures.append(f"{label}: tags must be a non-empty unique JSON list")
        levels = metadata.get("quality-levels")
        if not isinstance(levels, list) or set(levels) != ALLOWED_QUALITY_LEVELS:
            failures.append(f"{label}: quality-levels must contain Minimum, Recommended and Production")
        profiles = metadata.get("profiles")
        if not isinstance(profiles, list) or not profiles:
            failures.append(f"{label}: profiles must be a non-empty JSON list")
        for section in REQUIRED_SECTIONS:
            if section not in document.body:
                failures.append(f"{label}: missing required section {section!r}")
        for marker in FORBIDDEN_MARKERS:
            if marker in document.body:
                failures.append(f"{label}: unresolved marker {marker!r}")
        full_text = document.path.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(full_text):
                failures.append(f"{label}: possible embedded secret matching {pattern.pattern!r}")

    if not unique(prompt_ids):
        failures.append("prompt IDs are not unique")
    if not unique(source_paths):
        failures.append("prompt source paths are not unique")

    workflow_ids: list[str] = []
    stages = workflow_doc.get("stages", [])
    stage_numbers: list[int] = []
    for stage in stages:
        if not isinstance(stage, dict):
            failures.append("workflow stage is not an object")
            continue
        stage_numbers.append(stage.get("stage"))
        workflow_ids.extend(stage.get("prompt_ids", []))
    if stage_numbers != sorted(stage_numbers) or not unique(stage_numbers):
        failures.append("workflow stage numbers must be unique and sorted")
    if set(workflow_ids) != set(prompt_ids) or not unique(workflow_ids):
        missing = sorted(set(prompt_ids) - set(workflow_ids))
        extra = sorted(set(workflow_ids) - set(prompt_ids))
        failures.append(f"workflow must reference every prompt exactly once; missing={missing}, extra={extra}")

    try:
        catalog, markdown, checksums = build_catalog(repo)
        expected_generated = {
            paths["catalog"]: canonical_json(catalog),
            paths["catalog_markdown"]: markdown,
            paths["checksums"]: canonical_json(checksums),
        }
        for path, content in expected_generated.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                failures.append(f"generated prompt-package file is missing or stale: {path.relative_to(repo)}")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        failures.append(f"cannot generate prompt catalog: {error}")

    if failures:
        print("Prompt-package validation failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nPrompt-package failures: {len(failures)}")
        return 1

    print(f"OK   package: {manifest['package_id']} {manifest['version']} ({manifest['status']})")
    print(f"OK   prompts: {len(documents)} across {len(REQUIRED_CATEGORIES)} categories")
    print(f"OK   unique variables: {len(known_variables)}")
    print("OK   workflow covers every prompt exactly once")
    print("OK   metadata, sections, placeholders and security markers are valid")
    print("OK   catalog and checksums are current")
    print("OK   direct Prompt Manager import is not overclaimed")
    print("\nPrompt-package failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
