#!/usr/bin/env python3
"""Plan, activate, update, or disable the SASD main-branch ruleset."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from ci_activation_common import (
    ActivationError,
    RULESET_NAME,
    api_request,
    discover_token,
    find_ruleset,
    find_workflow_run,
    get_default_branch_commit,
    list_jobs,
    load_identity,
    load_ruleset_payload,
    repository_root,
    resolve_commit,
    split_repository,
    summarize_ruleset,
    verify_run,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--plan", action="store_true", help="Show the intended change without writing")
    group.add_argument("--activate", action="store_true", help="Create or update the active ruleset")
    group.add_argument("--disable", action="store_true", help="Disable the existing SASD ruleset")
    parser.add_argument(
        "--confirm-switch-to-pull-requests",
        action="store_true",
        help="Required for activation because direct pushes to main are no longer the normal workflow",
    )
    parser.add_argument("--commit", help="Git reference or full SHA to verify before activation; defaults to HEAD")
    return parser.parse_args()


def verify_green_main(owner: str, repository: str, branch: str, commit: str, token: str | None) -> dict[str, Any]:
    remote_commit = get_default_branch_commit(owner, repository, branch, token)
    if remote_commit != commit:
        raise ActivationError(
            f"local commit {commit} is not the remote {branch} commit {remote_commit}; activation is blocked"
        )
    run = find_workflow_run(owner, repository, branch, commit, token)
    verified = verify_run(run, list_jobs(owner, repository, int(run["id"]), token))
    if not verified["passed"]:
        raise ActivationError("remote quality gates are not green: " + "; ".join(verified["failures"]))
    return {"run": run, "verification": verified}


def main() -> int:
    args = parse_args()
    repo = repository_root()
    identity = load_identity(repo)
    owner, repository = split_repository(identity)
    branch = str(identity.get("default_branch") or "main")
    token = discover_token()
    existing = find_ruleset(owner, repository, token)
    payload = load_ruleset_payload(repo)

    if args.plan:
        commit = resolve_commit(repo, args.commit)
        output = {
            "repository": identity["canonical_repository"],
            "branch": branch,
            "commit_to_verify": commit,
            "existing_ruleset": summarize_ruleset(existing),
            "operation": "update" if existing else "create",
            "desired_payload": payload,
            "activation_warning": (
                "After activation, use a branch and pull request so SASD merge gate can run before main is updated."
            ),
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return 0

    if not token:
        raise ActivationError(
            "write operation requires GITHUB_TOKEN, GH_TOKEN, or an authenticated GitHub CLI session"
        )

    if args.disable:
        if not existing:
            print(f"Ruleset {RULESET_NAME!r} does not exist; nothing to disable.")
            return 0
        ruleset_id = existing.get("id")
        response = api_request(
            "PUT",
            f"/repos/{owner}/{repository}/rulesets/{ruleset_id}",
            token=token,
            data={"enforcement": "disabled"},
        )
        print(json.dumps(summarize_ruleset(response), indent=2, ensure_ascii=False))
        return 0

    if not args.confirm_switch_to_pull_requests:
        raise ActivationError(
            "activation requires --confirm-switch-to-pull-requests because the required check changes the normal main workflow"
        )

    commit = resolve_commit(repo, args.commit)
    verification = verify_green_main(owner, repository, branch, commit, token)
    print(
        f"Verified green workflow run {verification['run'].get('html_url')} for remote {branch} commit {commit}."
    )

    if existing:
        ruleset_id = existing.get("id")
        response = api_request(
            "PUT",
            f"/repos/{owner}/{repository}/rulesets/{ruleset_id}",
            token=token,
            data=payload,
        )
        operation = "updated"
    else:
        response = api_request(
            "POST",
            f"/repos/{owner}/{repository}/rulesets",
            token=token,
            data=payload,
        )
        operation = "created"

    summary = summarize_ruleset(response)
    required = (
        "active",
        "required_check_present",
        "strict_policy",
        "deletion_blocked",
        "force_push_blocked",
        "targets_default_branch",
    )
    missing = [name for name in required if not summary.get(name)]
    if missing:
        raise ActivationError(f"ruleset was {operation}, but read-back is incomplete: {', '.join(missing)}")

    print(f"Ruleset {operation} and verified:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ActivationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
