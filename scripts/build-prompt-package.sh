#!/usr/bin/env bash
set -euo pipefail
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output="${1:-artifacts/prompt-packages}"
cd "$repo"
python3 tooling/validate-prompt-packages.py
python3 tooling/build-prompt-package.py --output-dir "$output" --clean
python3 tooling/verify-prompt-package.py --directory "$output"
