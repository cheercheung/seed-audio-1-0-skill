# Doubao Seed-Audio 1.0 API & Agent Skill

<p align="center">
  <strong>Generate speech, dialogue, ambience, sound effects, and mixed audio scenes with Seed-Audio 1.0 through EvoLink.</strong>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/evolink-seed-audio"><img src="https://img.shields.io/npm/v/evolink-seed-audio?color=cb3837&label=npm" alt="NPM version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/EvoLinkAI/doubao-seed-audio-api-skill/stargazers"><img src="https://img.shields.io/github/stars/EvoLinkAI/doubao-seed-audio-api-skill?style=flat" alt="GitHub stars"></a>
  <a href="https://github.com/EvoLinkAI/doubao-seed-audio-api-skill/commits/main/"><img src="https://img.shields.io/github/last-commit/EvoLinkAI/doubao-seed-audio-api-skill" alt="Last commit"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> -
  <a href="#complete-first-run-flow">First Run</a> -
  <a href="#agent-skill-install">Agent Skill</a> -
  <a href="#api-reference">API Reference</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=doubao-seed-audio-api-skill&utm_content=readme-top">Try on EvoLink</a>
</p>

> **AI Agent?** Skip the README and read [llms-install.md](llms-install.md) for step-by-step installation instructions.

## Menu

- [Quick Start](#quick-start)
- [Complete First-Run Flow](#complete-first-run-flow)
- [What Is Seed-Audio 1.0?](#what-is-seed-audio-10)
- [Generation Modes](#generation-modes)
- [Agent Skill Install](#agent-skill-install)
- [API Reference](#api-reference)
- [Runnable Examples](#runnable-examples)
- [Docs](#docs)
- [Release Status](#release-status)

## Quick Start

Set your EvoLink API key:

```bash
export EVOLINK_API_KEY="your_key_here"
```

Create an audio generation task:

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/audios/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "doubao-seed-audio-1-0",
    "prompt": "Create a 20-second premium product video audio bed: soft electronic music, subtle camera whoosh, a glass bottle placed on marble, calm female narration, clean studio ambience.",
    "format": "mp3",
    "sample_rate": 24000
  }'
```

The API is asynchronous. The create request returns a task `id`. Poll the task endpoint until it is `completed` or `failed`:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

## Complete First-Run Flow

Run a complete local flow that creates a task, polls status, and prints the completed task JSON:

```bash
node examples/javascript/complete-flow.mjs
```

Or use the packaged script:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

Use `--dry-run` to inspect the request payload without spending API credits:

```bash
scripts/seed-audio-generate.sh --prompt "Short test" --dry-run
```

## What Is Seed-Audio 1.0?

Seed-Audio 1.0 is an audio generation model exposed through EvoLink as `doubao-seed-audio-1-0`. It can generate audio directly from text and can also use preset voice IDs, reference-audio URLs, or one reference image to guide the output.

Good first tests:

- narration for short video ads
- multi-character dialogue
- podcast or audiobook clips
- game character dialogue
- sound effects and ambience
- audio references for video generation workflows

## Generation Modes

### Text To Audio

Pass only `prompt` to generate audio from text.

### Reference Audio / Voice Control

Pass `audio_references` with up to 3 items. Each item can be a preset `voice_type` or a reference-audio URL. In the prompt, refer to entries as `@audio1`, `@audio2`, and `@audio3`.

```json
{
  "model": "doubao-seed-audio-1-0",
  "prompt": "@audio1 gives a calm documentary narration. @audio2 replies with a bright and excited delivery.",
  "audio_references": [
    "ICL_uranus_en_male_noah_tob",
    "ICL_uranus_en_female_charlie_tob"
  ],
  "format": "mp3"
}
```

### Reference Image

Pass `image_urls` with one image URL when the audio should match the mood of a visual. `audio_references` and `image_urls` are mutually exclusive.

## Agent Skill Install

Install the agent skill silently:

```bash
npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

Print the agent installation guide:

```bash
npx evolink-seed-audio@latest --llms
```

Print the skill definition:

```bash
npx evolink-seed-audio@latest --skill
```

## API Reference

Primary endpoint:

```text
POST https://api.evolink.ai/v1/audios/generations
```

Task query endpoint:

```text
GET https://api.evolink.ai/v1/tasks/{task_id}
```

Core parameters:

| Parameter | Required | Notes |
|---|---:|---|
| `model` | yes | Use `doubao-seed-audio-1-0` |
| `prompt` | yes | Up to 1500 characters |
| `audio_references` | no | Up to 3 preset voices or reference-audio URLs |
| `image_urls` | no | One reference image URL |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; default `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5` to `2.0` |
| `loudness_rate` | no | `0.5` to `2.0` |
| `pitch_rate` | no | `-12` to `12` semitones |
| `callback_url` | no | HTTPS callback URL for terminal task states |

See [docs/api-reference.md](docs/api-reference.md) and [references/api-params.md](references/api-params.md).

## Runnable Examples

- [examples/curl/complete-flow.sh](examples/curl/complete-flow.sh)
- [examples/javascript/complete-flow.mjs](examples/javascript/complete-flow.mjs)
- [examples/python/complete_flow.py](examples/python/complete_flow.py)

## Docs

- [Quickstart](docs/quickstart.md)
- [API reference](docs/api-reference.md)
- [Task lifecycle](docs/task-lifecycle.md)
- [Response schema](docs/response-schema.md)
- [Error handling](docs/errors.md)
- [Callbacks](docs/callbacks.md)
- [Voice guide](docs/voices.md)

Official EvoLink docs:

- [Seed-Audio 1.0 API](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0)
- [Seed-Audio 1.0 voice list](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices)

## Release Status

This repository is scaffolded and locally verified for static correctness. Public release is blocked until:

- `_meta.json.ownerId` is replaced with the real EvoLink owner ID.
- A real API smoke test is approved and run with `EVOLINK_API_KEY`.
- The owner approves GitHub publication and npm publish.

