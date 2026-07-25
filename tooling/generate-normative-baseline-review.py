#!/usr/bin/env python3
"""Generate deterministic dependency and content manifests for the 0.9.0 review bundle."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from normative_baseline_common import (
    BUNDLE_NAME,
    BUNDLE_VERSION,
    bundle_documents,
    extract_requirements,
    load_documents,
    sha256,
    topological_order,
)

DEPENDENCY_PATH = Path("docs/40-governance/NORMATIVE-BASELINE-DEPENDENCY-MAP-0.9.0.md")
MANIFEST_PATH = Path("docs/40-governance/NORMATIVE-BASELINE-REVIEW-MANIFEST-0.9.0.md")


def front_matter(title: str, document_id: str, depends_on: list[str]) -> list[str]:
    dependencies = ", ".join(depends_on)
    return [
        "---",
        f'title: "{title}"',
        f"document-id: {document_id}",
        "document-type: informative",
        "status: Draft",
        f"version: {BUNDLE_VERSION}",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        "last-updated: 2026-07-24",
        "applies-to-quality-levels: [Minimum, Recommended, Production]",
        "applies-to-profiles: [Core, DotNet, Desktop]",
        f"depends-on: [{dependencies}]",
        "normative-keywords: []",
        "---",
        "",
    ]


def build_dependency_map(repo: Path) -> str:
    bundle = bundle_documents(repo)
    all_documents = load_documents(repo)
    bundle_ids = {document.document_id for document in bundle}
    order, cycles = topological_order(bundle)
    lines = front_matter(
        "Normative Baseline Dependency Map 0.9.0",
        "SASD-REF-BASELINE-003",
        sorted(bundle_ids),
    )
    lines.extend(
        [
            "# Normative Baseline Dependency Map 0.9.0",
            "",
            "## 1. Zweck",
            "",
            "Diese generierte Übersicht dokumentiert die direkten Abhängigkeiten der 32 Dokumente",
            f"des Freigabebündels `{BUNDLE_NAME}`. Sie ist ein Reviewnachweis und selbst nicht normativ.",
            "",
            "## 2. Ergebnis",
            "",
            f"- Dokumente im Bündel: **{len(bundle)}**",
            f"- Erkannte Abhängigkeitszyklen: **{len(cycles)}**",
            f"- Topologische Reihenfolge vollständig: **{'Ja' if len(order) == len(bundle) and not cycles else 'Nein'}**",
            "",
            "## 3. Empfohlene Lesereihenfolge",
            "",
        ]
    )
    for index, identifier in enumerate(order, start=1):
        document = all_documents[identifier]
        lines.append(f"{index}. `{identifier}` — [{document.metadata.get('title', identifier)}](../{document.relative_path[5:]})")
    lines.extend(
        [
            "",
            "## 4. Direkte Abhängigkeiten",
            "",
            "| Dokument | Schicht | Bündelinterne Abhängigkeiten | Bereits freigegebene externe Abhängigkeiten |",
            "|---|---|---|---|",
        ]
    )
    for document in bundle:
        internal = [dependency for dependency in document.dependencies if dependency in bundle_ids]
        external = [dependency for dependency in document.dependencies if dependency not in bundle_ids]
        lines.append(
            f"| `{document.document_id}` | {document.layer} | "
            f"{', '.join(f'`{item}`' for item in internal) or '—'} | "
            f"{', '.join(f'`{item}`' for item in external) or '—'} |"
        )
    lines.extend(
        [
            "",
            "## 5. Reviewregel",
            "",
            "Eine externe Abhängigkeit gilt für dieses Bündel nur dann als freigabefähig, wenn das",
            "referenzierte Dokument bereits den Status `Approved` besitzt. Bündelinterne Abhängigkeiten",
            "werden gemeinsam geprüft und dürfen keine Zyklen bilden.",
            "",
        ]
    )
    return "\n".join(lines)


def build_manifest(repo: Path) -> str:
    bundle = bundle_documents(repo)
    bundle_ids = sorted(document.document_id for document in bundle)
    total_requirements = sum(len(extract_requirements(document)) for document in bundle)
    layer_counts: dict[str, int] = {}
    for document in bundle:
        layer_counts[document.layer] = layer_counts.get(document.layer, 0) + 1
    lines = front_matter(
        "Normative Baseline Review Manifest 0.9.0",
        "SASD-REF-BASELINE-004",
        bundle_ids,
    )
    lines.extend(
        [
            "# Normative Baseline Review Manifest 0.9.0",
            "",
            "## 1. Zweck",
            "",
            "Dieses deterministisch erzeugte Manifest identifiziert den während des integrierten Reviews",
            "geprüften Inhalt. Eine spätere formale Freigabe benötigt ein eigenes Approval Manifest, weil",
            "die Statusänderung von `Proposed` zu `Approved` den Dateiinhalt verändert.",
            "",
            "## 2. Zusammenfassung",
            "",
            f"- Freigabebündel: `{BUNDLE_NAME}`",
            f"- Dokumentversion: `{BUNDLE_VERSION}`",
            f"- Normative Dokumente: **{len(bundle)}**",
            f"- Normative Anforderungen: **{total_requirements}**",
            f"- Core-Dokumente: **{layer_counts.get('Core', 0)}**",
            f"- C#/.NET-Profildokumente: **{layer_counts.get('C#/.NET', 0)}**",
            f"- Desktop-Profildokumente: **{layer_counts.get('Desktop', 0)}**",
            f"- Prozessdokumente: **{layer_counts.get('Prozess', 0)}**",
            "",
            "## 3. Inhaltsmanifest",
            "",
            "| Dokument-ID | Pfad | Anforderungen | SHA-256 |",
            "|---|---|---:|---|",
        ]
    )
    for document in bundle:
        lines.append(
            f"| `{document.document_id}` | `{document.relative_path}` | "
            f"{len(extract_requirements(document))} | `{sha256(document.path)}` |"
        )
    lines.extend(
        [
            "",
            "## 4. Interpretation",
            "",
            "Die Prüfsummen belegen den untersuchten Proposed-Inhalt. Sie sind kein Nachweis einer",
            "Maintainer-Freigabe, eines GitHub-Actions-Erfolgs oder eines veröffentlichten Releases.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Write the generated documents.")
    mode.add_argument("--check", action="store_true", help="Check that generated documents are current.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parents[1]
    expected = {
        repo / DEPENDENCY_PATH: build_dependency_map(repo),
        repo / MANIFEST_PATH: build_manifest(repo),
    }
    failures = 0
    for path, content in expected.items():
        content = content.rstrip() + "\n"
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"Wrote {path.relative_to(repo)}")
        else:
            actual = path.read_text(encoding="utf-8") if path.exists() else None
            if actual != content:
                failures += 1
                print(f"FAIL generated file is stale or missing: {path.relative_to(repo)}")
            else:
                print(f"OK   generated file is current: {path.relative_to(repo)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
