#!/usr/bin/env python3
"""Run all blocking SASD repository checks and capture reproducible evidence.

The script is intentionally dependency-free so the same command can be used
locally and by GitHub Actions on Windows and Linux.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BLOCKING_CHECKS: tuple[tuple[str, str], ...] = (
    ("repository-hygiene", "validate-repository-hygiene.py"),
    ("repository-boundary", "validate-repository-boundary.py"),
    ("document-metadata", "validate-document-metadata.py"),
    ("markdown-links", "validate-markdown-links.py"),
    ("core-requirements", "validate-core-requirements.py"),
    ("core-consistency", "validate-core-consistency.py"),
    ("dotnet-profile", "validate-dotnet-profile.py"),
    ("desktop-profile", "validate-desktop-profile.py"),
    ("operational-processes", "validate-operational-processes.py"),
    ("reference-pilots", "validate-reference-pilots.py"),
    ("governance", "validate-governance.py"),
    ("normative-baseline-review", "validate-normative-baseline-review.py"),
    ("normative-baseline-approval", "validate-normative-baseline-approval.py"),
    ("ci-policy", "validate-ci-policy.py"),
    ("ci-activation", "validate-ci-activation.py"),
    ("repository-manifest", "generate-repository-manifest.py"),
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def git_value(repo: Path, *arguments: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *arguments],
            cwd=repo,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def run_command(repo: Path, name: str, command: list[str], output_dir: Path, blocking: bool) -> dict[str, Any]:
    started = time.monotonic()
    process = subprocess.run(
        command,
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONUTF8": "1"},
    )
    duration = round(time.monotonic() - started, 3)
    output = process.stdout
    if process.stderr:
        output += ("\n" if output and not output.endswith("\n") else "") + process.stderr
    log_path = output_dir / f"{name}.log"
    log_path.write_text(output, encoding="utf-8")

    status = "passed" if process.returncode == 0 else "failed"
    print(f"[{status.upper():6}] {name} ({duration:.3f}s)")
    if output:
        print(output.rstrip())

    return {
        "name": name,
        "blocking": blocking,
        "status": status,
        "exit_code": process.returncode,
        "duration_seconds": duration,
        "command": command,
        "log": log_path.name,
    }


def build_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# SASD Repository Quality-Gate Evidence",
        "",
        f"- Generated: `{report['generated_at']}`",
        f"- Platform: `{report['platform']}`",
        f"- Python: `{report['python_version']}`",
        f"- Commit: `{report.get('commit') or 'not available'}`",
        f"- Overall result: **{report['status'].upper()}**",
        "",
        "## Checks",
        "",
        "| Check | Type | Result | Exit | Duration | Log |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in report["checks"]:
        result = "PASS" if item["status"] == "passed" else "FAIL"
        check_type = "Blocking" if item["blocking"] else "Informational"
        lines.append(
            f"| `{item['name']}` | {check_type} | {result} | {item['exit_code']} | "
            f"{item['duration_seconds']:.3f}s | `{item['log']}` |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A successful report proves that the committed repository content passed the listed",
            "validators in this execution environment. It does not by itself approve Proposed",
            "normative documents or publish a SASD Development Standard release.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default="artifacts/quality-gates/local",
        help="Directory for logs and machine-readable evidence, relative to the repository root unless absolute.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parents[1]
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = repo / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    checks: list[dict[str, Any]] = []
    for name, script in BLOCKING_CHECKS:
        command = [sys.executable, str(repo / "tooling" / script)]
        if name == "repository-manifest":
            command.append("--check")
        checks.append(run_command(repo, name, command, output_dir, blocking=True))

    checks.append(
        run_command(
            repo,
            "version-1-readiness",
            [sys.executable, str(repo / "tooling" / "report-version-1-readiness.py")],
            output_dir,
            blocking=False,
        )
    )

    failed_blocking = [item for item in checks if item["blocking"] and item["status"] != "passed"]
    report: dict[str, Any] = {
        "schema_version": "1.0",
        "generated_at": utc_now(),
        "status": "passed" if not failed_blocking else "failed",
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "commit": git_value(repo, "rev-parse", "HEAD"),
        "branch": git_value(repo, "branch", "--show-current"),
        "checks": checks,
        "blocking_failures": [item["name"] for item in failed_blocking],
    }

    json_path = output_dir / "quality-gates.json"
    markdown_path = output_dir / "quality-gates.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown = build_markdown(report)
    markdown_path.write_text(markdown, encoding="utf-8")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with Path(summary_path).open("a", encoding="utf-8") as summary:
            summary.write(markdown)

    print(f"\nEvidence written to: {output_dir.relative_to(repo) if output_dir.is_relative_to(repo) else output_dir}")
    print(f"Overall result: {report['status'].upper()}")
    return 1 if failed_blocking else 0


if __name__ == "__main__":
    sys.exit(main())
