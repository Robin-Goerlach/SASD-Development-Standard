#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
args=(tooling/capture-ci-activation.py --write)
if [[ "${1:-}" == "--require-active-ruleset" ]]; then
  args+=(--require-active-ruleset)
fi
python "${args[@]}"
