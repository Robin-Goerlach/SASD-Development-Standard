#!/usr/bin/env python3
"""Validate repository CI activation assets without contacting GitHub."""

from __future__ import annotations

import json
import sys
from pathlib import Path


EXPECTED_FILES = (
    ".github/rulesets/main-merge-gate.json",
    "docs/50-reference-implementations/repository-self-hosting/README.md",
    "docs/50-reference-implementations/repository-self-hosting/CI-RECOVERY-AND-ACTIVATION.md",
    "docs/50-reference-implementations/repository-self-hosting/BRANCH-RULESET-PLAN.md",
    "docs/50-reference-implementations/repository-self-hosting/CI-ACTIVATION-RECORD.md",
    "tooling/ci_activation_common.py",
    "tooling/capture-ci-activation.py",
    "tooling/manage-main-ruleset.py",
    "templates/documents/REPOSITORY-CI-ACTIVATION-RECORD-TEMPLATE.md",
    "checklists/releases/REPOSITORY-CI-ACTIVATION-CHECKLIST.md",
    "prompts/review/REPOSITORY-CI-ACTIVATION-REVIEW-PROMPT.md",
)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    for relative in EXPECTED_FILES:
        if not (repo / relative).is_file():
            failures.append(f"missing required CI activation file: {relative}")

    payload_path = repo / ".github" / "rulesets" / "main-merge-gate.json"
    if payload_path.is_file():
        try:
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            failures.append(f"invalid ruleset JSON: {error}")
            payload = {}

        if payload.get("name") != "Protect main with SASD merge gate":
            failures.append("ruleset name does not match the governed baseline")
        if payload.get("target") != "branch":
            failures.append("ruleset target must be 'branch'")
        if payload.get("enforcement") != "active":
            failures.append("desired ruleset payload must use active enforcement")

        conditions = payload.get("conditions", {}).get("ref_name", {})
        if "~DEFAULT_BRANCH" not in conditions.get("include", []):
            failures.append("ruleset must target ~DEFAULT_BRANCH")

        rules = payload.get("rules", [])
        rule_types = {rule.get("type") for rule in rules if isinstance(rule, dict)}
        for required in ("deletion", "non_fast_forward", "required_status_checks"):
            if required not in rule_types:
                failures.append(f"ruleset missing required rule: {required}")

        status_rule = next(
            (rule for rule in rules if isinstance(rule, dict) and rule.get("type") == "required_status_checks"),
            None,
        )
        parameters = status_rule.get("parameters", {}) if status_rule else {}
        contexts = {
            item.get("context")
            for item in parameters.get("required_status_checks", [])
            if isinstance(item, dict)
        }
        if "SASD merge gate" not in contexts:
            failures.append("ruleset does not require the SASD merge gate context")
        if parameters.get("strict_required_status_checks_policy") is not True:
            failures.append("ruleset strict required-status-check policy must be true")

    record_path = (
        repo
        / "docs"
        / "50-reference-implementations"
        / "repository-self-hosting"
        / "CI-ACTIVATION-RECORD.md"
    )
    if record_path.is_file():
        text = record_path.read_text(encoding="utf-8")
        for marker in (
            "Repository boundary repaired:",
            "Green Ubuntu run:",
            "Green Windows run:",
            "Green SASD merge gate:",
            "Ruleset active:",
            "Activation complete:",
        ):
            if marker not in text:
                failures.append(f"activation record missing status marker: {marker}")

    evidence_path = record_path.with_name("CI-ACTIVATION-EVIDENCE.json")
    if evidence_path.is_file():
        try:
            evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            failures.append(f"invalid activation evidence JSON: {error}")
            evidence = {}
        if evidence.get("repository") != "Robin-Goerlach/SASD-Development-Standard":
            failures.append("activation evidence references the wrong repository")
        commit = evidence.get("commit")
        if not isinstance(commit, str) or len(commit) != 40:
            failures.append("activation evidence lacks a full commit SHA")
        workflow = evidence.get("workflow") or {}
        if workflow.get("conclusion") != "success":
            failures.append("committed activation evidence must reference a successful workflow")

    if failures:
        print("CI activation asset validation failed:")
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nFailures: {len(failures)}")
        return 1

    print("OK   CI recovery and activation documents are present")
    print("OK   desired ruleset payload protects the default branch")
    print("OK   required status check is SASD merge gate with strict policy")
    print("OK   activation evidence is either pending or internally consistent")
    print("\nCI activation failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
