#!/usr/bin/env python3
"""Shared helpers for SASD repository CI activation tooling."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

API_VERSION = "2026-03-10"
USER_AGENT = "SASD-Development-Standard-CI-Activation"
RULESET_NAME = "Protect main with SASD merge gate"
WORKFLOW_FILE = "quality-gates.yml"
REQUIRED_CHECK = "SASD merge gate"
EXPECTED_JOBS = (
    "Validate (ubuntu-latest)",
    "Validate (windows-latest)",
    REQUIRED_CHECK,
)


class ActivationError(RuntimeError):
    """Raised when activation evidence or remote state is invalid."""


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_identity(repo: Path) -> dict[str, Any]:
    path = repo / "REPOSITORY-IDENTITY.json"
    if not path.is_file():
        raise ActivationError("REPOSITORY-IDENTITY.json is missing")
    data = json.loads(path.read_text(encoding="utf-8"))
    canonical = data.get("canonical_repository")
    if not isinstance(canonical, str) or "/" not in canonical:
        raise ActivationError("canonical_repository is missing or invalid")
    return data


def split_repository(identity: dict[str, Any]) -> tuple[str, str]:
    owner, repository = identity["canonical_repository"].split("/", 1)
    return owner, repository


def git_value(repo: Path, *arguments: str) -> str:
    process = subprocess.run(
        ["git", *arguments],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if process.returncode != 0:
        message = process.stderr.strip() or process.stdout.strip() or "git command failed"
        raise ActivationError(message)
    return process.stdout.strip()


def resolve_commit(repo: Path, value: str | None) -> str:
    reference = value or "HEAD"
    commit = git_value(repo, "rev-parse", reference)
    if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit.lower()):
        raise ActivationError(f"resolved commit is not a full SHA: {commit!r}")
    return commit.lower()


def discover_token() -> str | None:
    for variable in ("GITHUB_TOKEN", "GH_TOKEN"):
        value = os.environ.get(variable)
        if value:
            return value.strip()

    if shutil.which("gh"):
        process = subprocess.run(
            ["gh", "auth", "token"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if process.returncode == 0 and process.stdout.strip():
            return process.stdout.strip()
    return None


def api_request(
    method: str,
    endpoint: str,
    *,
    token: str | None = None,
    data: dict[str, Any] | None = None,
) -> Any:
    url = endpoint if endpoint.startswith("https://") else f"https://api.github.com{endpoint}"
    body = None
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": USER_AGENT,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=body, headers=headers, method=method.upper())
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = response.read()
            if not payload:
                return None
            return json.loads(payload.decode("utf-8"))
    except urllib.error.HTTPError as error:
        payload = error.read().decode("utf-8", errors="replace")
        try:
            details = json.loads(payload).get("message", payload)
        except json.JSONDecodeError:
            details = payload
        raise ActivationError(f"GitHub API {error.code} for {url}: {details}") from error
    except urllib.error.URLError as error:
        raise ActivationError(f"GitHub API request failed for {url}: {error.reason}") from error


def get_default_branch_commit(owner: str, repository: str, branch: str, token: str | None) -> str:
    encoded = urllib.parse.quote(branch, safe="")
    data = api_request("GET", f"/repos/{owner}/{repository}/commits/{encoded}", token=token)
    sha = data.get("sha") if isinstance(data, dict) else None
    if not isinstance(sha, str) or len(sha) != 40:
        raise ActivationError("could not resolve the remote default-branch commit")
    return sha.lower()


def list_workflow_runs(owner: str, repository: str, branch: str, token: str | None) -> list[dict[str, Any]]:
    query = urllib.parse.urlencode({"branch": branch, "per_page": 100})
    data = api_request(
        "GET",
        f"/repos/{owner}/{repository}/actions/workflows/{WORKFLOW_FILE}/runs?{query}",
        token=token,
    )
    runs = data.get("workflow_runs") if isinstance(data, dict) else None
    return [item for item in runs or [] if isinstance(item, dict)]


def find_workflow_run(
    owner: str,
    repository: str,
    branch: str,
    commit: str,
    token: str | None,
) -> dict[str, Any]:
    matching = [run for run in list_workflow_runs(owner, repository, branch, token) if run.get("head_sha") == commit]
    if not matching:
        raise ActivationError(
            f"no {WORKFLOW_FILE} workflow run was found for commit {commit}; push the commit and wait for Actions"
        )
    matching.sort(key=lambda item: (item.get("run_attempt", 0), item.get("id", 0)), reverse=True)
    return matching[0]


def list_jobs(owner: str, repository: str, run_id: int, token: str | None) -> list[dict[str, Any]]:
    data = api_request(
        "GET",
        f"/repos/{owner}/{repository}/actions/runs/{run_id}/jobs?per_page=100",
        token=token,
    )
    jobs = data.get("jobs") if isinstance(data, dict) else None
    return [item for item in jobs or [] if isinstance(item, dict)]


def verify_run(run: dict[str, Any], jobs: list[dict[str, Any]]) -> dict[str, Any]:
    failures: list[str] = []
    if run.get("status") != "completed":
        failures.append(f"workflow status is {run.get('status')!r}, expected 'completed'")
    if run.get("conclusion") != "success":
        failures.append(f"workflow conclusion is {run.get('conclusion')!r}, expected 'success'")

    by_name = {str(job.get("name")): job for job in jobs}
    job_records: list[dict[str, Any]] = []
    for expected in EXPECTED_JOBS:
        job = by_name.get(expected)
        if not job:
            failures.append(f"expected job is missing: {expected}")
            job_records.append({"name": expected, "status": "missing", "conclusion": None, "html_url": None})
            continue
        conclusion = job.get("conclusion")
        status = job.get("status")
        if status != "completed" or conclusion != "success":
            failures.append(
                f"job {expected!r} is status={status!r}, conclusion={conclusion!r}; expected completed/success"
            )
        job_records.append(
            {
                "name": expected,
                "status": status,
                "conclusion": conclusion,
                "html_url": job.get("html_url"),
                "started_at": job.get("started_at"),
                "completed_at": job.get("completed_at"),
            }
        )

    return {"passed": not failures, "failures": failures, "jobs": job_records}


def list_rulesets(owner: str, repository: str, token: str | None) -> list[dict[str, Any]]:
    data = api_request("GET", f"/repos/{owner}/{repository}/rulesets?per_page=100", token=token)
    return [item for item in data or [] if isinstance(item, dict)]


def get_ruleset(owner: str, repository: str, ruleset_id: int, token: str | None) -> dict[str, Any]:
    data = api_request("GET", f"/repos/{owner}/{repository}/rulesets/{ruleset_id}", token=token)
    if not isinstance(data, dict):
        raise ActivationError("GitHub returned an invalid ruleset response")
    return data


def find_ruleset(owner: str, repository: str, token: str | None) -> dict[str, Any] | None:
    for item in list_rulesets(owner, repository, token):
        if item.get("name") == RULESET_NAME:
            identifier = item.get("id")
            if isinstance(identifier, int):
                return get_ruleset(owner, repository, identifier, token)
    return None


def summarize_ruleset(ruleset: dict[str, Any] | None) -> dict[str, Any]:
    if not ruleset:
        return {
            "present": False,
            "active": False,
            "id": None,
            "name": RULESET_NAME,
            "html_url": None,
            "required_check_present": False,
            "strict_policy": False,
            "deletion_blocked": False,
            "force_push_blocked": False,
            "targets_default_branch": False,
        }

    rules = ruleset.get("rules") or []
    rule_types = {item.get("type") for item in rules if isinstance(item, dict)}
    required = next(
        (item for item in rules if isinstance(item, dict) and item.get("type") == "required_status_checks"),
        None,
    )
    parameters = required.get("parameters", {}) if isinstance(required, dict) else {}
    contexts = {
        item.get("context")
        for item in parameters.get("required_status_checks", [])
        if isinstance(item, dict)
    }
    conditions = ruleset.get("conditions") or {}
    ref_name = conditions.get("ref_name") if isinstance(conditions, dict) else {}
    includes = ref_name.get("include", []) if isinstance(ref_name, dict) else []

    links = ruleset.get("_links") or {}
    html_link = links.get("html") if isinstance(links, dict) else {}
    return {
        "present": True,
        "active": ruleset.get("enforcement") == "active",
        "id": ruleset.get("id"),
        "name": ruleset.get("name"),
        "html_url": html_link.get("href") if isinstance(html_link, dict) else None,
        "enforcement": ruleset.get("enforcement"),
        "required_check_present": REQUIRED_CHECK in contexts,
        "strict_policy": parameters.get("strict_required_status_checks_policy") is True,
        "deletion_blocked": "deletion" in rule_types,
        "force_push_blocked": "non_fast_forward" in rule_types,
        "targets_default_branch": "~DEFAULT_BRANCH" in includes,
    }


def load_ruleset_payload(repo: Path) -> dict[str, Any]:
    path = repo / ".github" / "rulesets" / "main-merge-gate.json"
    if not path.is_file():
        raise ActivationError(f"ruleset payload is missing: {path.relative_to(repo)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ActivationError("ruleset payload must be a JSON object")
    return data
