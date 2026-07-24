#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required_markers=(
  "README.md"
  "docs/00-foundation/PROJECT-CHARTER.md"
  "docs/40-governance/NORMATIVE-LANGUAGE.md"
  "tooling/run-quality-gates.py"
)
for marker in "${required_markers[@]}"; do
  [[ -e "$marker" ]] || { echo "Missing canonical marker: $marker" >&2; exit 1; }
done

if remote="$(git config --get remote.origin.url 2>/dev/null)"; then
  if [[ ! "$remote" =~ Robin-Goerlach[/:]SASD-Development-Standard(\.git)?$ ]]; then
    echo "Unexpected origin remote: $remote" >&2
    exit 1
  fi
fi

foreign_paths=(
  "SASD-Development-Standard"
  "TaskHostLocal.Tests"
  "TaskHostLocal.WinForms"
  "TaskHostLocal.sln"
  "WAVE-01-UPDATE-MANIFEST.md"
  "WAVE-01-VERIFICATION-UPDATE-MANIFEST.md"
  "Directory.Build.props"
  "Directory.Packages.props"
  "global.json"
  ".github/workflows/ci.yml"
  "docs/080_Known_Issues.md"
  "docs/100_Manual_Test_Plan.md"
  "docs/110_SASD_Alignment.md"
  "docs/120_Wave_01_Review.md"
  "docs/130_Build_and_Test.md"
  "docs/140_Migration_Notes.md"
  "docs/150_Wave_01_Verification.md"
  "docs/160_Wave_01_Closeout.md"
  "docs/170_CI_Evidence_Guide.md"
  "docs/adr"
  "docs/evidence"
  "scripts/backup-taskhost-data.ps1"
  "scripts/finalize-wave-01.ps1"
  "scripts/verify-wave-01.ps1"
  "tooling/validate-wave-01.py"
)

removed=0
for path in "${foreign_paths[@]}"; do
  if [[ -e "$path" || -L "$path" ]]; then
    rm -rf -- "$path"
    printf 'Removed: %s\n' "$path"
    removed=$((removed + 1))
  fi
done
printf 'Removed %d misplaced paths.\n' "$removed"

python tooling/generate-repository-manifest.py --write
python tooling/run-quality-gates.py --output-dir artifacts/quality-gates/boundary-repair

echo
printf '%s\n' 'Repository boundary repair completed.'
printf '%s\n' 'Review the deletions with: git status --short'
printf '%s\n' 'Commit deletions and additions with: git add -A'
