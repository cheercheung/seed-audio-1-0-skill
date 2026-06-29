#!/usr/bin/env bash
set -euo pipefail

API_BASE="${EVOLINK_API_BASE:-https://api.evolink.ai}"
MODEL="doubao-seed-audio-1-0"
PROMPT=""
FORMAT="mp3"
SAMPLE_RATE="24000"
SPEECH_RATE="1.0"
LOUDNESS_RATE="1.0"
PITCH_RATE="0"
CALLBACK_URL=""
IMAGE_URL=""
DRY_RUN="0"
MAX_POLLS="${EVOLINK_SEED_AUDIO_MAX_POLLS:-120}"
POLL_INTERVAL="${EVOLINK_SEED_AUDIO_POLL_INTERVAL:-3}"
AUDIO_REFS=()

usage() {
  cat <<'EOF'
Usage:
  seed-audio-generate.sh --prompt <text> [options]

Options:
  --prompt <text>          Required prompt, max 1500 characters
  --audio-ref <value>      Preset voice_type or reference-audio URL; repeat up to 3
  --image-url <url>        One reference image URL; mutually exclusive with --audio-ref
  --format <fmt>           wav | mp3 | pcm | ogg_opus (default: mp3)
  --sample-rate <hz>       8000 | 16000 | 24000 | 32000 | 44100 | 48000
  --speech-rate <num>      0.5 to 2.0
  --loudness-rate <num>    0.5 to 2.0
  --pitch-rate <int>       -12 to 12
  --callback-url <url>     HTTPS callback URL
  --dry-run                Print payload and exit without calling the API
  --help                   Show help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prompt) PROMPT="${2:-}"; shift 2 ;;
    --audio-ref) AUDIO_REFS+=("${2:-}"); shift 2 ;;
    --image-url) IMAGE_URL="${2:-}"; shift 2 ;;
    --format) FORMAT="${2:-}"; shift 2 ;;
    --sample-rate) SAMPLE_RATE="${2:-}"; shift 2 ;;
    --speech-rate) SPEECH_RATE="${2:-}"; shift 2 ;;
    --loudness-rate) LOUDNESS_RATE="${2:-}"; shift 2 ;;
    --pitch-rate) PITCH_RATE="${2:-}"; shift 2 ;;
    --callback-url) CALLBACK_URL="${2:-}"; shift 2 ;;
    --dry-run) DRY_RUN="1"; shift ;;
    --help|-h) usage; exit 0 ;;
    *) echo "ERROR: unknown option $1" >&2; usage; exit 2 ;;
  esac
done

if [[ -z "$PROMPT" ]]; then
  echo "ERROR: --prompt is required" >&2
  exit 2
fi
if [[ ${#PROMPT} -gt 1500 ]]; then
  echo "ERROR: prompt exceeds 1500 characters" >&2
  exit 2
fi
if [[ ${#AUDIO_REFS[@]} -gt 3 ]]; then
  echo "ERROR: --audio-ref supports at most 3 items" >&2
  exit 2
fi
if [[ ${#AUDIO_REFS[@]} -gt 0 && -n "$IMAGE_URL" ]]; then
  echo "ERROR: --audio-ref and --image-url are mutually exclusive" >&2
  exit 2
fi

PY_ARGS=("$MODEL" "$PROMPT" "$FORMAT" "$SAMPLE_RATE" "$SPEECH_RATE" "$LOUDNESS_RATE" "$PITCH_RATE" "$CALLBACK_URL" "$IMAGE_URL")
if [[ ${#AUDIO_REFS[@]} -gt 0 ]]; then
  PY_ARGS+=("${AUDIO_REFS[@]}")
fi

PAYLOAD="$(python3 - "${PY_ARGS[@]}" <<'PY'
import json
import sys

model, prompt, fmt, sample_rate, speech_rate, loudness_rate, pitch_rate, callback_url, image_url, *audio_refs = sys.argv[1:]
payload = {
    "model": model,
    "prompt": prompt,
    "format": fmt,
    "sample_rate": int(sample_rate),
    "speech_rate": float(speech_rate),
    "loudness_rate": float(loudness_rate),
    "pitch_rate": int(pitch_rate),
}
if callback_url:
    payload["callback_url"] = callback_url
if image_url:
    payload["image_urls"] = [image_url]
if audio_refs:
    payload["audio_references"] = audio_refs
print(json.dumps(payload, ensure_ascii=False, indent=2))
PY
)"

if [[ "$DRY_RUN" == "1" ]]; then
  printf '%s\n' "$PAYLOAD"
  exit 0
fi

if [[ -z "${EVOLINK_API_KEY:-}" ]]; then
  echo "ERROR: EVOLINK_API_KEY is not set" >&2
  exit 2
fi

CREATE_RESPONSE="$(curl --silent --show-error --fail-with-body \
  --request POST \
  --url "${API_BASE}/v1/audios/generations" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header "Content-Type: application/json" \
  --data "$PAYLOAD")" || {
    echo "ERROR: create request failed" >&2
    exit 1
  }

TASK_ID="$(python3 -c '
import json, sys
data = json.loads(sys.argv[1])
print(data.get("id", ""))
' "$CREATE_RESPONSE")"

if [[ -z "$TASK_ID" ]]; then
  echo "ERROR: create response did not include id" >&2
  printf '%s\n' "$CREATE_RESPONSE" >&2
  exit 1
fi

echo "TASK_SUBMITTED: task_id=${TASK_ID}"

for ((i=1; i<=MAX_POLLS; i++)); do
  TASK_RESPONSE="$(curl --silent --show-error --fail-with-body \
    --request GET \
    --url "${API_BASE}/v1/tasks/${TASK_ID}" \
    --header "Authorization: Bearer ${EVOLINK_API_KEY}")" || {
      echo "ERROR: task query failed" >&2
      exit 1
    }

  STATUS="$(python3 -c '
import json, sys
data = json.loads(sys.argv[1])
print(data.get("status", "unknown"))
' "$TASK_RESPONSE")"
  PROGRESS="$(python3 -c '
import json, sys
data = json.loads(sys.argv[1])
print(data.get("progress", ""))
' "$TASK_RESPONSE")"

  if [[ "$STATUS" == "completed" ]]; then
    python3 -c '
import json, sys
data = json.loads(sys.argv[1])
urls = []
for key in ("results", "result_urls"):
    value = data.get(key)
    if isinstance(value, list):
        urls.extend(str(item) for item in value if isinstance(item, str))
for item in data.get("result_data", []) or []:
    if isinstance(item, dict):
        for key in ("audio_url", "url"):
            if item.get(key):
                urls.append(str(item[key]))
for url in dict.fromkeys(urls):
    print(f"AUDIO_URL={url}")
print(json.dumps(data, ensure_ascii=False, indent=2))
' "$TASK_RESPONSE"
    echo "TASK_COMPLETED: task_id=${TASK_ID}"
    exit 0
  fi

  if [[ "$STATUS" == "failed" || "$STATUS" == "cancelled" ]]; then
    echo "ERROR: task ended with status=${STATUS}" >&2
    printf '%s\n' "$TASK_RESPONSE" >&2
    exit 1
  fi

  echo "STATUS_UPDATE: status=${STATUS} progress=${PROGRESS}"
  sleep "$POLL_INTERVAL"
done

echo "POLL_TIMEOUT: task_id=${TASK_ID}" >&2
exit 1
