---
name: doubao-seed-audio
description: Doubao Seed-Audio 1.0 audio generation via EvoLink API. Supports text-to-audio, preset voices, reference-audio voice control, reference-image audio generation, and mixed audio scenes.
homepage: https://github.com/EvoLinkAI/doubao-seed-audio-api-skill
metadata: {"openclaw":{"homepage":"https://github.com/EvoLinkAI/doubao-seed-audio-api-skill","requires":{"bins":["curl","python3"],"env":["EVOLINK_API_KEY"]},"primaryEnv":"EVOLINK_API_KEY"}}
---

# Doubao Seed-Audio 1.0 Generation

Use this skill to generate speech, dialogue, ambience, sound effects, and mixed audio scenes through EvoLink.

## When To Activate

Activate when the user asks to:

- generate audio from text
- generate narration or dialogue
- create sound effects, ambience, or mixed audio scenes
- use Seed-Audio 1.0 or `doubao-seed-audio-1-0`
- use a preset voice or reference audio
- create audio to guide a video workflow

## Script Location

Resolve paths relative to this `SKILL.md`:

```text
SKILL_DIR = directory containing this SKILL.md
SCRIPT = {SKILL_DIR}/scripts/seed-audio-generate.sh
```

## Setup

Check for the API key:

```bash
echo $EVOLINK_API_KEY
```

If it is missing, ask the user to get an EvoLink API key from `https://evolink.ai/dashboard/keys`.

## Required User Inputs

- `prompt`: what audio to generate, up to 1500 characters.

Optional inputs:

- `format`: `wav`, `mp3`, `pcm`, or `ogg_opus`; default `mp3`.
- `sample_rate`: default `24000`.
- `speech_rate`: `0.5` to `2.0`.
- `loudness_rate`: `0.5` to `2.0`.
- `pitch_rate`: `-12` to `12`.
- `audio_references`: up to 3 preset voices or reference-audio URLs.
- `image_url`: one image URL; mutually exclusive with `audio_references`.
- `callback_url`: HTTPS callback URL.

## Generation Rules

- Ask all missing required information in one message.
- Do not ask for optional parameters unless the user's goal needs them.
- Use `mp3`, `24000`, `speech_rate=1.0`, `loudness_rate=1.0`, and `pitch_rate=0` as defaults.
- `audio_references` and `image_url` cannot be used together.
- If using reference voices, tell the user to reference them in the prompt as `@audio1`, `@audio2`, and `@audio3`.
- Run the script once. Once a task is submitted, do not retry unless the user explicitly asks.

## Script Usage

```bash
export EVOLINK_API_KEY=your_key_here

{SKILL_DIR}/scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm narrator." \
  --format mp3
```

Preset voice example:

```bash
{SKILL_DIR}/scripts/seed-audio-generate.sh \
  --prompt "@audio1 gives a calm documentary narration. @audio2 replies with a brighter delivery." \
  --audio-ref ICL_uranus_en_male_noah_tob \
  --audio-ref ICL_uranus_en_female_charlie_tob \
  --format mp3
```

Dry run:

```bash
{SKILL_DIR}/scripts/seed-audio-generate.sh --prompt "Short test" --dry-run
```

## Output Protocol

Parse these lines from stdout:

| Line | Meaning |
|---|---|
| `TASK_SUBMITTED: task_id=<id>` | The task was created. Do not retry automatically. |
| `STATUS_UPDATE: status=<status> progress=<n>` | The task is still running. |
| `AUDIO_URL=<url>` | A generated audio URL was found. Present it to the user and remind them to save it. |
| `TASK_COMPLETED: task_id=<id>` | The task completed. |
| `POLL_TIMEOUT: task_id=<id>` | The local poll timed out; the server task may still finish later. |
| `ERROR: ...` | Surface the error to the user. |

Generated audio links are time-limited. Tell the user to save outputs promptly.

## References

- `docs/api-reference.md`
- `docs/task-lifecycle.md`
- `docs/voices.md`
- `references/api-params.md`

