#!/usr/bin/env python3
"""Static and SQLite smoke validation for TaskHost Local Wave 01.

This validator intentionally does not replace `dotnet build` and `dotnet test`.
It provides a dependency-free structural check and executes the schema SQL with
Python's SQLite implementation so obvious packaging and SQL errors are caught.
"""

from __future__ import annotations

import re
import sqlite3
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

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
    "TaskHostLocal.WinForms/Database/DatabaseInitializer.cs",
    "docs/110_SASD_Alignment.md",
    "docs/120_Wave_01_Review.md",
    "docs/140_Migration_Notes.md",
    "scripts/backup-taskhost-data.ps1",
    "scripts/verify-wave-01.ps1",
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
    except Exception as exc:  # noqa: BLE001 - validator reports all failures together.
        FAILURES.append(f"Invalid XML in {xml_file.relative_to(ROOT)}: {exc}")

solution = (ROOT / "TaskHostLocal.sln").read_text(encoding="utf-8")
if "TaskHostLocal.Tests\\TaskHostLocal.Tests.csproj" not in solution:
    FAILURES.append("TaskHostLocal.Tests is not referenced by TaskHostLocal.sln")

product_project = (ROOT / "TaskHostLocal.WinForms/TaskHostLocal.WinForms.csproj").read_text(encoding="utf-8")
if re.search(r'Microsoft\.Data\.Sqlite"\s+Version=', product_project):
    FAILURES.append("Microsoft.Data.Sqlite version must be managed centrally")

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
            connection.execute(
                """
                SELECT id, list_id, title, description, due_date, priority, is_completed, created_at, updated_at, completed_at
                FROM tasks
                WHERE list_id = ?
                ORDER BY is_completed,
                         CASE WHEN due_date IS NULL THEN 1 ELSE 0 END,
                         due_date, priority DESC, updated_at DESC
                """,
                (list_id,),
            ).fetchall()
            connection.execute(
                """
                SELECT id
                FROM tasks
                WHERE title LIKE ? OR COALESCE(description, '') LIKE ?
                ORDER BY is_completed,
                         CASE WHEN due_date IS NULL THEN 1 ELSE 0 END,
                         due_date, priority DESC, updated_at DESC
                """,
                ("%Wave%", "%Wave%"),
            ).fetchall()
            connection.commit()
        except sqlite3.Error as exc:
            FAILURES.append(f"SQLite smoke validation failed: {exc}")
        finally:
            connection.close()

if FAILURES:
    print("Wave 01 validation failed:")
    for failure in FAILURES:
        print(f"- {failure}")
    sys.exit(1)

print(f"Validated {len(REQUIRED)} required Wave 01 files.")
test_files = list((ROOT / "TaskHostLocal.Tests").rglob("*Tests.cs"))
if len(test_files) < 4:
    print(f"Expected at least 4 test files, found {len(test_files)}")
    sys.exit(1)

test_methods = sum(
    len(re.findall(r"\[Fact\]\s+public void ", path.read_text(encoding="utf-8")))
    for path in test_files
)
if test_methods < 10:
    print(f"Expected at least 10 automated test methods, found {test_methods}")
    sys.exit(1)

print(f"Parsed 4 MSBuild XML files.")
print(f"Found {len(test_files)} automated test files with {test_methods} test methods.")
print(f"Executed {len(schema_statements)} embedded schema statements with SQLite {sqlite3.sqlite_version}.")
print("Wave 01 static validation: OK")
