#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPOSITORY_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_DIRECTORY="${1:-artifacts/quality-gates/local}"

cd "$REPOSITORY_ROOT"
export PYTHONUTF8=1
python tooling/run-quality-gates.py --output-dir "$OUTPUT_DIRECTORY"
