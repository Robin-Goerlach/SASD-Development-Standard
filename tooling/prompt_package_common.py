#!/usr/bin/env python3
"""Shared helpers for SASD prompt-package generation and validation."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

PACKAGE_ID = "sasd-development-standard-v1"
PACKAGE_ROOT = Path("prompts/packages") / PACKAGE_ID
PROMPT_ID_PATTERN = re.compile(r"^SASD-PROMPT-[A-Z]+-[0-9]{3}$")
VARIABLE_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
PLACEHOLDER_PATTERN = re.compile(r"\{\{([a-z][a-z0-9_]*)\}\}")
SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
REQUIRED_SECTIONS = (
    "## Zweck",
    "## Eingaben",
    "## Arbeitsauftrag",
    "## Qualitätsregeln",
    "## Ausgabeformat",
)
REQUIRED_PROMPT_FIELDS = (
    "prompt-id",
    "title",
    "version",
    "status",
    "package-id",
    "category",
    "language",
    "summary",
    "variables",
    "tags",
    "quality-levels",
    "profiles",
    "last-reviewed",
)
ALLOWED_PROMPT_STATUSES = {"Draft", "Candidate", "Stable", "Deprecated", "Retired"}
ALLOWED_QUALITY_LEVELS = {"Minimum", "Recommended", "Production"}


@dataclass(frozen=True)
class PromptDocument:
    path: Path
    relative_path: str
    metadata: dict[str, Any]
    body: str
    sha256: str


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value[0] in '[{"' or value in {"true", "false", "null"}:
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            pass
    return value


def parse_prompt(path: Path, repo: Path | None = None) -> PromptDocument:
    repo = repo or repository_root()
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML-style frontmatter")
    try:
        _, raw_frontmatter, body = text.split("---\n", 2)
    except ValueError as exc:
        raise ValueError("invalid frontmatter delimiters") from exc
    metadata: dict[str, Any] = {}
    for line_number, line in enumerate(raw_frontmatter.splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"frontmatter line {line_number} has no colon")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if key in metadata:
            raise ValueError(f"duplicate frontmatter key: {key}")
        metadata[key] = parse_scalar(raw_value)
    relative = path.relative_to(repo).as_posix()
    return PromptDocument(path, relative, metadata, body.strip() + "\n", sha256_file(path))


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object in {path}")
    return data


def package_paths(repo: Path | None = None) -> dict[str, Path]:
    repo = repo or repository_root()
    base = repo / PACKAGE_ROOT
    return {
        "base": base,
        "manifest": base / "manifest.json",
        "catalog": base / "catalog.json",
        "catalog_markdown": base / "CATALOG.md",
        "variables": base / "variables.json",
        "categories": base / "categories.json",
        "workflow": base / "workflow.json",
        "checksums": base / "checksums.json",
    }


def discover_prompts(repo: Path | None = None, manifest: dict[str, Any] | None = None) -> list[PromptDocument]:
    repo = repo or repository_root()
    if manifest is None:
        manifest = load_json(package_paths(repo)["manifest"])
    documents: list[PromptDocument] = []
    for root_name in manifest.get("prompt_roots", []):
        root = repo / "prompts" / root_name
        if not root.is_dir():
            raise ValueError(f"missing prompt root: prompts/{root_name}")
        for path in sorted(root.glob("*.md"), key=lambda item: item.name.casefold()):
            if path.name == "README.md":
                continue
            documents.append(parse_prompt(path, repo))
    return sorted(documents, key=lambda item: item.metadata.get("prompt-id", ""))


def placeholders(body: str) -> set[str]:
    return set(PLACEHOLDER_PATTERN.findall(body))


def build_catalog(repo: Path | None = None) -> tuple[dict[str, Any], str, dict[str, Any]]:
    repo = repo or repository_root()
    paths = package_paths(repo)
    manifest = load_json(paths["manifest"])
    documents = discover_prompts(repo, manifest)
    entries: list[dict[str, Any]] = []
    for document in documents:
        metadata = document.metadata
        entries.append(
            {
                "prompt_id": metadata["prompt-id"],
                "title": metadata["title"],
                "summary": metadata["summary"],
                "version": metadata["version"],
                "status": metadata["status"],
                "category": metadata["category"],
                "language": metadata["language"],
                "variables": metadata["variables"],
                "tags": metadata["tags"],
                "quality_levels": metadata["quality-levels"],
                "profiles": metadata["profiles"],
                "source_file": document.relative_path,
                "sha256": document.sha256,
            }
        )
    catalog = {
        "schema_version": "1.0",
        "package_id": manifest["package_id"],
        "package_version": manifest["version"],
        "prompt_count": len(entries),
        "prompts": entries,
    }
    lines = [
        "# SASD Prompt Catalog",
        "",
        f"- Package: `{manifest['package_id']}`",
        f"- Version: `{manifest['version']}`",
        f"- Status: `{manifest['status']}`",
        f"- Prompts: **{len(entries)}**",
        "",
        "| ID | Category | Title | Variables | Tags |",
        "|---|---|---|---:|---|",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['prompt_id']}` | `{entry['category']}` | "
            f"[{entry['title']}](../../../{entry['source_file']}) | "
            f"{len(entry['variables'])} | {', '.join(f'`{tag}`' for tag in entry['tags'])} |"
        )
    lines.extend(
        [
            "",
            "## Evidence boundary",
            "",
            "Catalog inclusion proves package structure and content hashing. It does not prove",
            "successful execution of a prompt or direct import compatibility with a specific",
            "SASD Prompt Manager build.",
            "",
        ]
    )
    checksum_entries: list[dict[str, str]] = []
    tracked = [
        paths["manifest"],
        paths["variables"],
        paths["categories"],
        paths["workflow"],
        repo / "prompts/README.md",
        repo / "prompts/PACKAGE-SPECIFICATION.md",
        repo / "prompts/QUALITY-GUIDE.md",
        repo / "prompts/SECURITY-GUIDE.md",
        repo / "prompts/VARIABLES.md",
        repo / "prompts/PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md",
        repo / "prompts/schema/prompt.schema.json",
        repo / "prompts/schema/prompt-package.schema.json",
        paths["base"] / "README.md",
        repo / "templates/prompts/VERSIONED-PROMPT-TEMPLATE.md",
        repo / "templates/prompts/PROMPT-PACKAGE-MANIFEST-TEMPLATE.json",
        repo / "templates/documents/PROMPT-MANAGER-IMPORT-MAPPING-TEMPLATE.md",
        repo / "checklists/development/PROMPT-PACKAGE-REVIEW-CHECKLIST.md",
        repo / "checklists/development/PROMPT-MANAGER-IMPORT-ROUNDTRIP-CHECKLIST.md",
    ] + [doc.path for doc in documents]
    tracked.extend(
        document.path.parent / "README.md"
        for document in documents
        if (document.path.parent / "README.md").is_file()
    )
    tracked = list(dict.fromkeys(tracked))
    for path in sorted(tracked, key=lambda item: item.relative_to(repo).as_posix().casefold()):
        checksum_entries.append(
            {
                "path": path.relative_to(repo).as_posix(),
                "sha256": sha256_file(path),
            }
        )
    checksums = {
        "schema_version": "1.0",
        "package_id": manifest["package_id"],
        "package_version": manifest["version"],
        "file_count": len(checksum_entries),
        "files": checksum_entries,
    }
    return catalog, "\n".join(lines), checksums


def canonical_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def package_source_files(repo: Path | None = None) -> list[Path]:
    repo = repo or repository_root()
    paths = package_paths(repo)
    manifest = load_json(paths["manifest"])
    documents = discover_prompts(repo, manifest)
    selected: set[Path] = {
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
        repo / "templates/documents/PROMPT-MANAGER-IMPORT-MAPPING-TEMPLATE.md",
        repo / "checklists/development/PROMPT-PACKAGE-REVIEW-CHECKLIST.md",
        repo / "checklists/development/PROMPT-MANAGER-IMPORT-ROUNDTRIP-CHECKLIST.md",
        paths["manifest"],
        paths["catalog"],
        paths["catalog_markdown"],
        paths["variables"],
        paths["categories"],
        paths["workflow"],
        paths["checksums"],
        paths["base"] / "README.md",
    }
    for document in documents:
        selected.add(document.path)
        readme = document.path.parent / "README.md"
        if readme.is_file():
            selected.add(readme)
    return sorted(selected, key=lambda item: item.relative_to(repo).as_posix().casefold())


def unique(values: Iterable[str]) -> bool:
    items = list(values)
    return len(items) == len(set(items))
