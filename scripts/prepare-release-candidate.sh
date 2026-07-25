#!/usr/bin/env bash
set -euo pipefail

mode="${1:-preview}"
output_directory="${2:-artifacts/release-candidate}"
if [[ "$mode" != "preview" && "$mode" != "release" ]]; then
  echo "Usage: $0 [preview|release] [output-directory]" >&2
  exit 2
fi

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"
python tooling/run-quality-gates.py
if [[ "$mode" == "release" ]]; then
  python tooling/generate-release-candidate-readiness.py --require-ready
fi
python tooling/build-release-candidate.py --mode "$mode" --output-dir "$output_directory"
python tooling/verify-release-candidate.py --directory "$output_directory"
