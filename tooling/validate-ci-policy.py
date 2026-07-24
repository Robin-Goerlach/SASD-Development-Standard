#!/usr/bin/env python3
"""Validate the security and governance baseline of repository CI workflows."""

from __future__ import annotations

import re
import sys
from pathlib import Path


USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)(?:\s+#\s*(.+))?\s*$", re.MULTILINE)
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
WRITE_PERMISSION = re.compile(r"^\s+[a-zA-Z0-9_-]+:\s*write\s*$", re.MULTILINE)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    workflow = repo / ".github" / "workflows" / "quality-gates.yml"
    dependabot = repo / ".github" / "dependabot.yml"
    codeowners = repo / ".github" / "CODEOWNERS"
    failures: list[str] = []

    required = [
        workflow,
        dependabot,
        codeowners,
        repo / "tooling/run-quality-gates.py",
        repo / "tooling/validate-ci-activation.py",
        repo / ".github/rulesets/main-merge-gate.json",
    ]
    for path in required:
        if not path.is_file():
            failures.append(f"missing required CI file: {path.relative_to(repo)}")

    if workflow.is_file():
        text = workflow.read_text(encoding="utf-8")
        required_fragments = [
            "push:",
            "pull_request:",
            "workflow_dispatch:",
            "permissions:\n  contents: read",
            "concurrency:",
            "cancel-in-progress: true",
            "persist-credentials: false",
            "tooling/run-quality-gates.py",
            "if: ${{ always() }}",
            "SASD merge gate",
            "timeout-minutes:",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"workflow missing required policy fragment: {fragment!r}")

        forbidden = ["pull_request_target:", "write-all", "GITHUB_TOKEN", "curl |", "wget |"]
        for fragment in forbidden:
            if fragment in text:
                failures.append(f"workflow contains forbidden fragment: {fragment!r}")
        if WRITE_PERMISSION.search(text):
            failures.append("workflow grants a write permission")

        matches = list(USES.finditer(text))
        if not matches:
            failures.append("workflow contains no action references")
        for match in matches:
            reference, version_comment = match.groups()
            if "@" not in reference:
                failures.append(f"invalid action reference: {reference}")
                continue
            action, revision = reference.rsplit("@", 1)
            if not action.startswith("actions/"):
                failures.append(f"third-party action is not allowed in baseline workflow: {action}")
            if not FULL_SHA.fullmatch(revision):
                failures.append(f"action is not pinned to a full commit SHA: {reference}")
            if not version_comment or not re.search(r"\bv\d", version_comment):
                failures.append(f"action pin lacks a same-line release comment: {reference}")

        if text.count("timeout-minutes:") < 2:
            failures.append("each workflow job must define a timeout")

    if dependabot.is_file():
        text = dependabot.read_text(encoding="utf-8")
        for fragment in ["version: 2", "package-ecosystem: github-actions", "directory: /", "interval: weekly"]:
            if fragment not in text:
                failures.append(f"Dependabot configuration missing: {fragment!r}")

    if codeowners.is_file():
        text = codeowners.read_text(encoding="utf-8")
        for fragment in ["* @Robin-Goerlach", "/.github/ @Robin-Goerlach", "/tooling/ @Robin-Goerlach"]:
            if fragment not in text:
                failures.append(f"CODEOWNERS missing ownership rule: {fragment!r}")

    ruleset = repo / ".github" / "rulesets" / "main-merge-gate.json"
    if ruleset.is_file():
        text = ruleset.read_text(encoding="utf-8")
        for fragment in [
            "Protect main with SASD merge gate",
            "~DEFAULT_BRANCH",
            "required_status_checks",
            "SASD merge gate",
            "non_fast_forward",
            "deletion",
        ]:
            if fragment not in text:
                failures.append(f"ruleset payload missing: {fragment!r}")

    if failures:
        print("CI policy validation failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nFailures: {len(failures)}")
        return 1

    print("OK   workflow triggers, permissions, concurrency and timeouts")
    print("OK   action references use full commit SHAs with release comments")
    print("OK   checkout credentials are not persisted")
    print("OK   Dependabot monitors GitHub Actions")
    print("OK   governance-sensitive paths have CODEOWNERS")
    print("OK   governed main-branch ruleset payload is present")
    print("\nCI policy failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
