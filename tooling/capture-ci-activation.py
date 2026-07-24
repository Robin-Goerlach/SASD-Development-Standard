#!/usr/bin/env python3
"""Verify remote SASD Quality Gates and optionally write activation evidence."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ci_activation_common import (
    ActivationError,
    discover_token,
    find_ruleset,
    find_workflow_run,
    get_default_branch_commit,
    list_jobs,
    load_identity,
    repository_root,
    resolve_commit,
    split_repository,
    summarize_ruleset,
    verify_run,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def markdown(record: dict[str, Any]) -> str:
    lines = [
        "---",
        'title: "Repository-CI-Aktivierungsrecord"',
        "document-id: SASD-REF-CI-003",
        "document-type: informative",
        "status: Draft",
        "version: 0.10.0",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        f"last-updated: {record['generated_at'][:10]}",
        "applies-to-quality-levels: [Recommended, Production]",
        "applies-to-profiles: [Core]",
        "depends-on: [SASD-REF-CI-001, SASD-REF-CI-002, SASD-REF-PILOT-002]",
        "---",
        "",
        "# Repository-CI-Aktivierungsrecord",
        "",
        "## Status",
        "",
        "```text",
        "Repository boundary repaired: Verified by committed quality gates",
        "Local quality gates:           Passed before push",
        "Green Ubuntu run:              Yes",
        "Green Windows run:             Yes",
        "Green SASD merge gate:         Yes",
        "Evidence JSON:                 Present",
        f"Ruleset created:               {'Yes' if record['ruleset']['present'] else 'No'}",
        f"Ruleset active:                {'Yes' if record['ruleset']['active'] else 'No'}",
        f"Activation complete:           {'Yes' if record['activation_complete'] else 'No'}",
        "```",
        "",
        "## Geprüfte Revision",
        "",
        f"- Repository: `{record['repository']}`",
        f"- Commit SHA: `{record['commit']}`",
        f"- Branch: `{record['branch']}`",
        f"- Workflow run ID: `{record['workflow']['id']}`",
        f"- Workflow run URL: {record['workflow']['html_url']}",
        f"- Workflow conclusion: `{record['workflow']['conclusion']}`",
        f"- Erfasst: `{record['generated_at']}`",
        "",
        "## Jobnachweise",
        "",
        "| Erwarteter Job | Ergebnis | URL |",
        "|---|---|---|",
    ]
    for job in record["workflow"]["jobs"]:
        url = job.get("html_url") or "Nicht verfügbar"
        lines.append(f"| `{job['name']}` | `{job.get('conclusion')}` | {url} |")

    ruleset = record["ruleset"]
    lines.extend(
        [
            "",
            "## Rulesetnachweis",
            "",
            f"- Ruleset name: `{ruleset['name']}`",
            f"- Ruleset ID: `{ruleset.get('id') or 'Pending'}`",
            f"- Ruleset URL: {ruleset.get('html_url') or 'Pending'}",
            f"- Enforcement: `{ruleset.get('enforcement') or 'not present'}`",
            f"- Default-Branch-Bedingung vorhanden: `{ruleset['targets_default_branch']}`",
            f"- Required check `SASD merge gate`: `{ruleset['required_check_present']}`",
            f"- Strict status-check policy: `{ruleset['strict_policy']}`",
            f"- Force pushes blocked: `{ruleset['force_push_blocked']}`",
            f"- Branch deletion blocked: `{ruleset['deletion_blocked']}`",
            "",
            "## Aussagegrenze",
            "",
            "Der Record belegt den Remote-CI-Zustand der genannten Commit-SHA und, sofern",
            "aktiv, den zurückgelesenen Ruleset-Zustand. Er erteilt keine fachliche Freigabe",
            "für Proposed-Dokumente und veröffentlicht keinen Release Candidate.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", help="Git reference or full commit SHA; defaults to HEAD")
    parser.add_argument("--verify-only", action="store_true", help="Verify and print evidence without writing files")
    parser.add_argument("--write", action="store_true", help="Write JSON evidence and the Markdown activation record")
    parser.add_argument(
        "--require-active-ruleset",
        action="store_true",
        help="Fail unless the expected ruleset is active and complete",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.verify_only and not args.write:
        args.verify_only = True

    repo = repository_root()
    identity = load_identity(repo)
    owner, repository = split_repository(identity)
    branch = str(identity.get("default_branch") or "main")
    commit = resolve_commit(repo, args.commit)
    token = discover_token()

    remote_commit = get_default_branch_commit(owner, repository, branch, token)
    if commit != remote_commit:
        raise ActivationError(
            f"local commit {commit} is not the current remote {branch} commit {remote_commit}; "
            "push or check out the intended revision first"
        )

    run = find_workflow_run(owner, repository, branch, commit, token)
    jobs = list_jobs(owner, repository, int(run["id"]), token)
    verified = verify_run(run, jobs)
    if not verified["passed"]:
        raise ActivationError("; ".join(verified["failures"]))

    ruleset_summary = summarize_ruleset(find_ruleset(owner, repository, token))
    if args.require_active_ruleset:
        required_flags = (
            "active",
            "required_check_present",
            "strict_policy",
            "deletion_blocked",
            "force_push_blocked",
            "targets_default_branch",
        )
        missing = [name for name in required_flags if not ruleset_summary.get(name)]
        if missing:
            raise ActivationError("active ruleset evidence is incomplete: " + ", ".join(missing))

    record: dict[str, Any] = {
        "schema_version": "1.0",
        "generated_at": utc_now(),
        "repository": identity["canonical_repository"],
        "branch": branch,
        "commit": commit,
        "workflow": {
            "id": run.get("id"),
            "run_number": run.get("run_number"),
            "run_attempt": run.get("run_attempt"),
            "status": run.get("status"),
            "conclusion": run.get("conclusion"),
            "event": run.get("event"),
            "html_url": run.get("html_url"),
            "created_at": run.get("created_at"),
            "updated_at": run.get("updated_at"),
            "jobs": verified["jobs"],
        },
        "ruleset": ruleset_summary,
        "activation_complete": bool(
            verified["passed"]
            and ruleset_summary.get("active")
            and ruleset_summary.get("required_check_present")
            and ruleset_summary.get("strict_policy")
            and ruleset_summary.get("deletion_blocked")
            and ruleset_summary.get("force_push_blocked")
            and ruleset_summary.get("targets_default_branch")
        ),
    }

    print(json.dumps(record, indent=2, ensure_ascii=False))

    if args.write:
        target = repo / "docs" / "50-reference-implementations" / "repository-self-hosting"
        target.mkdir(parents=True, exist_ok=True)
        (target / "CI-ACTIVATION-EVIDENCE.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (target / "CI-ACTIVATION-RECORD.md").write_text(markdown(record), encoding="utf-8")
        print(f"\nEvidence written under {target.relative_to(repo)}")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ActivationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
