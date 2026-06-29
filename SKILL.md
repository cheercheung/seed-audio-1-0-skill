---
name: seed-audio-1-0
description: Seed Audio 1.0 audio generation via EvoLink API for Claude Code, OpenCode, OpenClaw, Cursor, and other agents. Supports text-to-audio, voice references, reference-image guidance, callbacks, and async task polling.
homepage: https://github.com/cheercheung/seed-audio-1-0-skill
metadata: {"openclaw":{"homepage":"https://github.com/cheercheung/seed-audio-1-0-skill","requires":{"bins":["curl","python3"],"env":["EVOLINK_API_KEY"]},"primaryEnv":"EVOLINK_API_KEY"}}
---

# Seed Audio 1.0 Generation

Use this skill to generate speech, dialogue, ambience, sound effects, and mixed audio scenes through EvoLink.

## When to Activate This Skill

Activate when the user asks to:

- generate audio from text
- generate narration, dialogue, sound effects, ambience, or mixed audio scenes
- use Seed-Audio 1.0 or `doubao-seed-audio-1-0`
- use preset voices, reference-audio URLs, or image-guided audio
- create audio that can guide a video workflow
- run an EvoLink audio generation API flow from an agent

## Script Location

Resolve paths relative to this `SKILL.md`:

```text
SKILL_DIR = directory containing this SKILL.md
SCRIPT = {SKILL_DIR}/scripts/seed-audio-generate.sh
```

## After Installation

Check whether the API key is present:

```bash
echo $EVOLINK_API_KEY
```

If it is missing, ask the user to create an EvoLink API key at `https://evolink.ai/dashboard/keys` and set:

```bash
export EVOLINK_API_KEY=your_key_here
```

## Core Principles

- Ask all missing required inputs in one message.
- Do not ask for optional parameters unless the user's goal needs them.
- Use `--dry-run` before spending credits when the user wants to inspect the request.
- After `TASK_SUBMITTED:` appears, do not rerun automatically; the API task may already be billable.

## Flow

1. Identify the desired audio scene, voice style, duration target, and output format.
2. Check `EVOLINK_API_KEY`. If absent, ask for it before any real API call.
3. Ask ALL missing required parameters in ONE single message. Never split required input collection into multiple rounds.
4. Execute by agent type:
   - Claude Code: run the script in the shell and keep reading output until `TASK_COMPLETED:`, `POLL_TIMEOUT:`, or `ERROR:` appears.
   - OpenClaw / OpenCode / Cursor: run the script as a blocking command; the script handles polling internally.

Critical rule: once `TASK_SUBMITTED:` appears, do not rerun the script unless the user explicitly asks. Query the task instead.

## Script Usage

Basic generation:

```bash
export EVOLINK_API_KEY=your_key_here

{SKILL_DIR}/scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm narrator." \
  --format mp3
```

Preset voice references:

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

## Script Output Protocol

Parse these lines from stdout or stderr:

| Line | Agent action |
|---|---|
| `TASK_SUBMITTED: task_id=<id>` | Record the task id. Do not rerun automatically. |
| `STATUS_UPDATE: status=<status> progress=<n>` | Keep waiting unless the user asks to stop. |
| `AUDIO_URL=<url>` | Present the URL and remind the user to save the asset. |
| `TASK_COMPLETED: task_id=<id>` | Report completion and summarize the output. |
| `POLL_TIMEOUT: task_id=<id>` | Tell the user the server task may still finish; query the task later instead of resubmitting. |
| `ERROR: ...` | Surface a friendly error and suggest the smallest fix. |

Generated audio links may be time-limited. Tell the user to save outputs promptly.

Critical rule: `TASK_SUBMITTED:` means a task exists. Do not rerun the create request automatically.

## Error Handling

| Error | Friendly response |
|---|---|
| `EVOLINK_API_KEY is not set` | Ask the user to set `EVOLINK_API_KEY` before a real run. |
| `prompt exceeds 1500 characters` | Ask the user to shorten the prompt or split the scene. |
| `--audio-ref and --image-url are mutually exclusive` | Ask the user to choose either audio references or one image reference. |
| `create request failed` | Check the API key, request payload, and network. Use `--dry-run` to inspect the payload. |
| `task query failed` | Keep the task id and retry only the query endpoint later. Do not recreate the task. |
| `POLL_TIMEOUT` | Explain that the local polling window ended and the task may still complete server-side. |

## Model Capabilities Summary

Seed Audio 1.0 can generate audio from text prompts, use preset voices or reference-audio URLs, guide audio from one reference image, and return asynchronous task results through polling or callbacks. Good first scenarios include short ad narration, multi-character dialogue, podcast clips, game dialogue, ambience, and sound effects.

## References

- `scripts/seed-audio-generate.sh`
- `docs/quickstart.md`
- `docs/api-reference.md`
- `docs/task-lifecycle.md`
- `docs/response-schema.md`
- `docs/errors.md`
- `docs/callbacks.md`
- `docs/voices.md`
- `references/api-params.md`
