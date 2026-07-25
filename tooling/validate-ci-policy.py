#!/usr/bin/env python3
"""Validate the security and governance baseline of repository CI workflows."""

from __future__ import annotations

import re
import sys
from pathlib import Path

USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)(?:\s+#\s*(.+))?\s*$", re.MULTILINE)
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
WRITE_PERMISSION = re.compile(r"^\s+[a-zA-Z0-9_-]+:\s*write\s*$", re.MULTILINE)
DEPENDABOT_ECOSYSTEM = re.compile(r"package-ecosystem:\s*[\"']?([^\"'\s]+)[\"']?")
DEPENDABOT_ROOT = re.compile(r"directory:\s*[\"']?/[\"']?(?:\s|$)")
DEPENDABOT_WEEKLY = re.compile(r"interval:\s*[\"']?weekly[\"']?(?:\s|$)")


def validate_action_references(label: str, text: str, failures: list[str]) -> None:
    matches = list(USES.finditer(text))
    if not matches:
        failures.append(f"{label} contains no action references")
    for match in matches:
        reference, version_comment = match.groups()
        if "@" not in reference:
            failures.append(f"{label} has invalid action reference: {reference}")
            continue
        action, revision = reference.rsplit("@", 1)
        if not action.startswith("actions/"):
            failures.append(f"{label} uses non-baseline third-party action: {action}")
        if not FULL_SHA.fullmatch(revision):
            failures.append(f"{label} action is not pinned to a full commit SHA: {reference}")
        if not version_comment or not re.search(r"\bv\d", version_comment):
            failures.append(f"{label} action pin lacks a same-line release comment: {reference}")


def validate_common_workflow(label: str, text: str, failures: list[str]) -> None:
    for fragment in [
        "permissions:\n  contents: read",
        "concurrency:",
        "cancel-in-progress: true",
        "persist-credentials: false",
        "timeout-minutes:",
    ]:
        if fragment not in text:
            failures.append(f"{label} missing required policy fragment: {fragment!r}")
    for fragment in ["pull_request_target:", "write-all", "GITHUB_TOKEN", "curl |", "wget |"]:
        if fragment in text:
            failures.append(f"{label} contains forbidden fragment: {fragment!r}")
    if WRITE_PERMISSION.search(text):
        failures.append(f"{label} grants a write permission")
    validate_action_references(label, text, failures)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    quality_workflow = repo / ".github/workflows/quality-gates.yml"
    preview_workflow = repo / ".github/workflows/release-candidate-preview.yml"
    dependabot = repo / ".github/dependabot.yml"
    codeowners = repo / ".github/CODEOWNERS"
    failures: list[str] = []

    required = [
        quality_workflow,
        preview_workflow,
        dependabot,
        codeowners,
        repo / "tooling/run-quality-gates.py",
        repo / "tooling/validate-ci-activation.py",
        repo / "tooling/build-release-candidate.py",
        repo / "tooling/verify-release-candidate.py",
        repo / ".github/rulesets/main-merge-gate.json",
    ]
    for path in required:
        if not path.is_file():
            failures.append(f"missing required CI file: {path.relative_to(repo)}")

    if quality_workflow.is_file():
        text = quality_workflow.read_text(encoding="utf-8")
        validate_common_workflow("quality-gates workflow", text, failures)
        for fragment in [
            "push:",
            "pull_request:",
            "workflow_dispatch:",
            "tooling/run-quality-gates.py",
            "if: ${{ always() }}",
            "SASD merge gate",
        ]:
            if fragment not in text:
                failures.append(f"quality-gates workflow missing required fragment: {fragment!r}")
        if text.count("timeout-minutes:") < 2:
            failures.append("each quality-gates workflow job must define a timeout")

    if preview_workflow.is_file():
        text = preview_workflow.read_text(encoding="utf-8")
        validate_common_workflow("RC preview workflow", text, failures)
        for fragment in [
            "workflow_dispatch:",
            "tooling/run-quality-gates.py",
            "tooling/build-release-candidate.py --mode preview",
            "tooling/verify-release-candidate.py",
            "actions/upload-artifact@",
            "retention-days: 14",
        ]:
            if fragment not in text:
                failures.append(f"RC preview workflow missing required fragment: {fragment!r}")
        for forbidden in ["contents: write", "gh release", "git tag", "create-release", "softprops/action-gh-release"]:
            if forbidden in text:
                failures.append(f"RC preview workflow may not publish: {forbidden!r}")

    if dependabot.is_file():
        text = dependabot.read_text(encoding="utf-8")
        if not re.search(r"^version:\s*2\s*$", text, re.MULTILINE):
            failures.append("Dependabot configuration must use version 2")
        ecosystems = DEPENDABOT_ECOSYSTEM.findall(text)
        if ecosystems != ["github-actions"]:
            failures.append(
                "Dependabot must contain exactly one github-actions update block; found: "
                + (", ".join(ecosystems) if ecosystems else "none")
            )
        if not DEPENDABOT_ROOT.search(text):
            failures.append("Dependabot github-actions directory must be repository root /")
        if not DEPENDABOT_WEEKLY.search(text):
            failures.append("Dependabot schedule must be weekly")

    if codeowners.is_file():
        text = codeowners.read_text(encoding="utf-8")
        for fragment in [
            "* @Robin-Goerlach",
            "/.github/ @Robin-Goerlach",
            "/tooling/ @Robin-Goerlach",
            "/docs/40-governance/ @Robin-Goerlach",
        ]:
            if fragment not in text:
                failures.append(f"CODEOWNERS missing ownership rule: {fragment!r}")

    ruleset = repo / ".github/rulesets/main-merge-gate.json"
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

    print("OK   quality-gate and RC-preview workflows use read-only permissions")
    print("OK   action references use full commit SHAs with release comments")
    print("OK   checkout credentials are not persisted")
    print("OK   RC-preview workflow cannot create tags or releases")
    print("OK   Dependabot monitors only GitHub Actions from the repository root")
    print("OK   governance-sensitive paths have CODEOWNERS")
    print("OK   governed main-branch ruleset payload is present")
    print("\nCI policy failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
