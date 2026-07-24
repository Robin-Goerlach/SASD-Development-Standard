#!/usr/bin/env python3
"""Static and SQLite validation for TaskHost Local Wave 01.

This validator intentionally does not replace `dotnet build`, `dotnet test`,
the published application's headless self-check, GitHub Actions or the manual
Windows smoke test. It verifies only repository structure and portable syntax.
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - optional dependency for local convenience.
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
FAILURES: list[str] = []

REQUIRED = [
    "global.json",
    "Directory.Build.props",
    "Directory.Packages.props",
    "LICENSE",
    "SECURITY.md",
    ".github/workflows/ci.yml",
    "TaskHostLocal.Tests/TaskHostLocal.Tests.csproj",
    "TaskHostLocal.Tests/Verification/SelfCheckRunnerTests.cs",
    "TaskHostLocal.WinForms/Database/DatabaseInitializer.cs",
    "TaskHostLocal.WinForms/Verification/SelfCheckOptions.cs",
    "TaskHostLocal.WinForms/Verification/SelfCheckReport.cs",
    "TaskHostLocal.WinForms/Verification/SelfCheckRunner.cs",
    "docs/110_SASD_Alignment.md",
    "docs/120_Wave_01_Review.md",
    "docs/140_Migration_Notes.md",
    "docs/150_Wave_01_Verification.md",
    "docs/160_Wave_01_Closeout.md",
    "docs/170_CI_Evidence_Guide.md",
    "docs/evidence/WAVE-01-MANUAL-TEST-RECORD-TEMPLATE.md",
    "scripts/backup-taskhost-data.ps1",
    "scripts/verify-wave-01.ps1",
    "scripts/finalize-wave-01.ps1",
    "WAVE-01-VERIFICATION-UPDATE-MANIFEST.md",
]

for relative_path in REQUIRED:
    if not (ROOT / relative_path).is_file():
        FAILURES.append(f"Missing required file: {relative_path}")

for xml_file in [
    ROOT / "Directory.Build.props",
    ROOT / "Directory.Packages.props",
    ROOT / "TaskHostLocal.WinForms/TaskHostLocal.WinForms.csproj",
    ROOT / "TaskHostLocal.Tests/TaskHostLocal.Tests.csproj",
]:
    try:
        ET.parse(xml_file)
    except Exception as exc:  # noqa: BLE001
        FAILURES.append(f"Invalid XML in {xml_file.relative_to(ROOT)}: {exc}")

try:
    global_json = json.loads((ROOT / "global.json").read_text(encoding="utf-8"))
    if "sdk" not in global_json or "version" not in global_json["sdk"]:
        FAILURES.append("global.json does not define sdk.version")
except Exception as exc:  # noqa: BLE001
    FAILURES.append(f"Invalid global.json: {exc}")

workflow_text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
if yaml is not None:
    try:
        yaml.safe_load(workflow_text)
    except Exception as exc:  # noqa: BLE001
        FAILURES.append(f"Invalid workflow YAML: {exc}")

for expected in [
    ".\\scripts\\verify-wave-01.ps1",
    "verification-results/ci",
    "actions/upload-artifact@v4",
]:
    if expected not in workflow_text:
        FAILURES.append(f"CI workflow misses expected verification marker: {expected}")

solution = (ROOT / "TaskHostLocal.sln").read_text(encoding="utf-8")
if "TaskHostLocal.Tests\\TaskHostLocal.Tests.csproj" not in solution:
    FAILURES.append("TaskHostLocal.Tests is not referenced by TaskHostLocal.sln")

product_project = (ROOT / "TaskHostLocal.WinForms/TaskHostLocal.WinForms.csproj").read_text(encoding="utf-8")
if 'InternalsVisibleTo Include="TaskHostLocal.Tests"' not in product_project:
    FAILURES.append("Product project does not expose internal verification classes to the test project")
if re.search(r'Microsoft\.Data\.Sqlite"\s+Version=', product_project):
    FAILURES.append("Microsoft.Data.Sqlite version must be managed centrally")

program = (ROOT / "TaskHostLocal.WinForms/Program.cs").read_text(encoding="utf-8")
for marker in ["private static int Main(string[] args)", "SelfCheckOptions.IsSelfCheckRequested", "SelfCheckRunner.Execute"]:
    if marker not in program:
        FAILURES.append(f"Program.cs misses self-check integration marker: {marker}")

runner = (ROOT / "TaskHostLocal.WinForms/Verification/SelfCheckRunner.cs").read_text(encoding="utf-8")
for marker in [
    "PRAGMA integrity_check",
    "PRAGMA foreign_key_check",
    "repository-and-service-crud",
    "VerifyBackup",
    "ComputeSha256",
]:
    if marker not in runner:
        FAILURES.append(f"SelfCheckRunner.cs misses expected check: {marker}")

verify_script = (ROOT / "scripts/verify-wave-01.ps1").read_text(encoding="utf-8")
for marker in ["dotnet", "publish", "--self-check", "verification-summary.json", "manualSmokeTestStatus = 'Pending'"]:
    if marker not in verify_script:
        FAILURES.append(f"verify-wave-01.ps1 misses expected marker: {marker}")

finalize_script = (ROOT / "scripts/finalize-wave-01.ps1").read_text(encoding="utf-8")
for marker in ["automatedVerificationStatus -ne 'Passed'", "repositoryDirty", "ManualTestRecord", "Overall result", "CiResult", "commit SHA"]:
    if marker not in finalize_script:
        FAILURES.append(f"finalize-wave-01.ps1 misses closeout guard: {marker}")

initializer = (ROOT / "TaskHostLocal.WinForms/Database/DatabaseInitializer.cs").read_text(encoding="utf-8")
schema_statements = re.findall(
    r'ExecuteNonQuery\(connection, transaction, """\s*(.*?)\s*"""\);',
    initializer,
    flags=re.DOTALL,
)

if len(schema_statements) < 5:
    FAILURES.append(f"Expected at least 5 embedded schema statements, found {len(schema_statements)}")
else:
    with tempfile.TemporaryDirectory(prefix="taskhost-wave01-") as directory:
        db_path = Path(directory) / "smoke.db"
        connection = sqlite3.connect(db_path)
        try:
            connection.execute("PRAGMA foreign_keys = ON;")
            for statement in schema_statements:
                connection.executescript(statement)
            connection.execute("PRAGMA user_version = 1;")
            connection.execute(
                "INSERT INTO task_lists (name, sort_order, created_at, updated_at) VALUES (?, ?, ?, ?)",
                ("Eingang", 0, "2026-07-24T00:00:00Z", "2026-07-24T00:00:00Z"),
            )
            list_id = connection.execute("SELECT id FROM task_lists LIMIT 1").fetchone()[0]
            connection.execute(
                """
                INSERT INTO tasks
                    (list_id, title, description, due_date, priority, is_completed, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (list_id, "Smoke task", "Wave 01", None, 1, 0, "2026-07-24T00:00:00Z", "2026-07-24T00:00:00Z"),
            )
            integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
            if integrity != "ok":
                FAILURES.append(f"Portable SQLite integrity check failed: {integrity}")
            connection.commit()
        except sqlite3.Error as exc:
            FAILURES.append(f"SQLite smoke validation failed: {exc}")
        finally:
            connection.close()

# Prevent documentation from claiming completion before generated evidence exists.
closeout = (ROOT / "docs/160_Wave_01_Closeout.md").read_text(encoding="utf-8")
if "**Current status:** Pending verification" not in closeout:
    FAILURES.append("Wave 01 closeout document must remain Pending verification in the prepared package")

if FAILURES:
    print("Wave 01 verification update validation failed:")
    for failure in FAILURES:
        print(f"- {failure}")
    sys.exit(1)

test_files = list((ROOT / "TaskHostLocal.Tests").rglob("*Tests.cs"))
test_methods = sum(
    len(re.findall(r"\[Fact\]\s+public void ", path.read_text(encoding="utf-8")))
    for path in test_files
)

print(f"Validated {len(REQUIRED)} required Wave 01 verification files.")
print("Parsed 4 MSBuild XML files and global.json.")
print(f"Found {len(test_files)} automated test files with {test_methods} test methods.")
print(f"Executed {len(schema_statements)} embedded schema statements with SQLite {sqlite3.sqlite_version}.")
print("Verified closeout guards and pending-status semantics.")
print("Wave 01 verification update static validation: OK")
