#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${EVOLINK_API_KEY:-}" ]]; then
  echo "Set EVOLINK_API_KEY first" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"

"${ROOT_DIR}/scripts/seed-audio-generate.sh" \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3 \
  --sample-rate 24000

