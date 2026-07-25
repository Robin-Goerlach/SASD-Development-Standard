#!/usr/bin/env python3
"""Shared helpers for the SASD Version 1.0 normative baseline review."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

BUNDLE_NAME = "SASD-NORMATIVE-BASELINE-0.9.0"
BUNDLE_VERSION = "0.9.0"
EXPECTED_DOCUMENT_COUNT = 32
EXPECTED_REQUIREMENT_COUNT = 1345

REQUIREMENT_PATTERN = re.compile(r"^\|\s*(SASD-[A-Z0-9-]+)\s*\|\s*(.*?)\s*\|\s*$")


@dataclass(frozen=True)
class Document:
    path: Path
    relative_path: str
    metadata: dict[str, str]
    text: str

    @property
    def document_id(self) -> str:
        return self.metadata["document-id"]

    @property
    def dependencies(self) -> list[str]:
        return parse_inline_list(self.metadata.get("depends-on", "[]"))

    @property
    def layer(self) -> str:
        identifier = self.document_id
        if identifier.startswith("SASD-CORE-"):
            return "Core"
        if identifier.startswith("SASD-PROF-DOTNET-"):
            return "C#/.NET"
        if identifier.startswith("SASD-PROF-DESKTOP-"):
            return "Desktop"
        if identifier.startswith("SASD-PROC-"):
            return "Prozess"
        return "Sonstiges"


def parse_front_matter_text(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML front matter")
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid metadata line: {line!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    raise ValueError("front matter is not closed")


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip('"') for item in value[1:-1].split(",") if item.strip()]
    return [value.strip('"')]


def load_documents(repo: Path) -> dict[str, Document]:
    documents: dict[str, Document] = {}
    for path in sorted((repo / "docs").rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        metadata = parse_front_matter_text(text)
        document_id = metadata.get("document-id")
        if not document_id:
            continue
        documents[document_id] = Document(
            path=path,
            relative_path=path.relative_to(repo).as_posix(),
            metadata=metadata,
            text=text,
        )
    return documents


def bundle_documents(repo: Path) -> list[Document]:
    documents = load_documents(repo)
    result = [
        document
        for document in documents.values()
        if document.metadata.get("document-type") == "normative"
        and document.metadata.get("approval-bundle") == BUNDLE_NAME
    ]
    return sorted(result, key=lambda item: item.document_id)


def extract_requirements(document: Document) -> list[tuple[str, str]]:
    requirements: list[tuple[str, str]] = []
    for line in document.text.splitlines():
        match = REQUIREMENT_PATTERN.match(line)
        if match:
            requirements.append((match.group(1), match.group(2).strip()))
    return requirements


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def topological_order(bundle: list[Document]) -> tuple[list[str], list[list[str]]]:
    ids = {document.document_id for document in bundle}
    graph = {
        document.document_id: [dependency for dependency in document.dependencies if dependency in ids]
        for document in bundle
    }
    state: dict[str, int] = {}
    order: list[str] = []
    cycles: list[list[str]] = []
    stack: list[str] = []

    def visit(node: str) -> None:
        current = state.get(node, 0)
        if current == 2:
            return
        if current == 1:
            if node in stack:
                start = stack.index(node)
                cycle = stack[start:] + [node]
                if cycle not in cycles:
                    cycles.append(cycle)
            return
        state[node] = 1
        stack.append(node)
        for dependency in sorted(graph[node]):
            visit(dependency)
        stack.pop()
        state[node] = 2
        order.append(node)

    for identifier in sorted(ids):
        visit(identifier)
    return order, cycles


def normalize_requirement(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().casefold())
