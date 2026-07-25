#!/usr/bin/env python3
"""Generate or validate the Version 1.0 release-candidate readiness report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from release_candidate_common import PREPARATION_VERSION, RC_VERSION, readiness, repository_root

TARGET = "docs/40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md"


def render(repo: Path) -> str:
    result = readiness(repo)
    lines = [
        "---",
        'title: "Release-Candidate-Readiness 1.0.0-rc.1"',
        "document-id: SASD-REF-RC-002",
        "document-type: informative",
        "status: Draft",
        f"version: {PREPARATION_VERSION}",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        "last-updated: 2026-07-25",
        "applies-to-quality-levels: [Recommended, Production]",
        "applies-to-profiles: [Core]",
        "depends-on: [SASD-REF-RC-001, SASD-REF-RC-003, SASD-REF-PILOT-007, SASD-REF-CI-003]",
        "---",
        "",
        f"# Release-Candidate-Readiness {RC_VERSION}",
        "",
        "Diese Datei wird deterministisch aus dem Repository-Zustand erzeugt.",
        "",
        "## Ergebnis",
        "",
        f"- Release Candidate technisch veröffentlichungsbereit: **{'Ja' if result['ready'] else 'Nein'}**",
        f"- blockierende offene Checks: **{len(result['blocking_failures'])}**",
        f"- Approved normative Dokumente: **{result['approved_normative_documents']}/{result['normative_documents']}**",
        f"- Pilotbaselines: **{result['assessed_pilots']}/{result['pilots']}**",
        f"- technisch verifizierte Piloten: **{result['verified_pilots']}**",
        "",
        "## Checks",
        "",
        "| ID | Bedingung | Blockierend | Ergebnis | Detail |",
        "|---|---|---:|---:|---|",
    ]
    for item in result["checks"]:
        lines.append(
            f"| `{item['id']}` | {item['name']} | {'Ja' if item['blocking'] else 'Nein'} | "
            f"{'PASS' if item['passed'] else 'OPEN'} | {item['detail']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Ein `PASS` bestätigt nur den konkret beschriebenen Nachweis. Das Vorhandensein von",
            "Skripten, Testcode, Workflowdateien oder Vorlagen ersetzt keinen erfolgreichen Lauf.",
            "Diese Readiness-Datei erteilt keine Maintainer-Freigabe, erstellt keinen Tag und",
            "veröffentlicht keinen GitHub Release.",
            "",
            "## Aktuell blockierende Checks",
            "",
        ]
    )
    if result["blocking_failures"]:
        lines.extend(f"- `{item}`" for item in result["blocking_failures"])
    else:
        lines.append("- keine; eine getrennte Maintainer-Freigabe bleibt dennoch erforderlich")
    lines.extend(
        [
            "",
            "## Erneute Erzeugung",
            "",
            "```bash",
            "python tooling/generate-release-candidate-readiness.py --write",
            "python tooling/generate-release-candidate-readiness.py --check",
            "python tooling/generate-release-candidate-readiness.py --require-ready",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    group.add_argument("--require-ready", action="store_true")
    args = parser.parse_args()

    repo = repository_root()
    target = repo / TARGET
    expected = render(repo)
    current = target.read_text(encoding="utf-8") if target.is_file() else ""

    if args.write:
        target.write_text(expected, encoding="utf-8")
        print(f"Wrote {TARGET}")
        return 0
    if current != expected:
        print(f"FAIL {TARGET} is stale; run with --write")
        return 1
    result = readiness(repo)
    if args.require_ready and not result["ready"]:
        print("Release Candidate is not ready:")
        for item in result["checks"]:
            if item["blocking"] and not item["passed"]:
                print(f"FAIL {item['id']}: {item['name']} — {item['detail']}")
        return 1
    print(
        f"OK   {TARGET}; ready={result['ready']}; "
        f"blocking_failures={len(result['blocking_failures'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
