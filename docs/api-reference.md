# Doubao Seed-Audio 1.0 API Reference

## Create Audio Generation Task

```http
POST https://api.evolink.ai/v1/audios/generations
Authorization: Bearer ${EVOLINK_API_KEY}
Content-Type: application/json
```

## Required Parameters

| Parameter | Type | Description |
|---|---|---|
| `model` | string | Use `doubao-seed-audio-1-0` |
| `prompt` | string | Text prompt or synthesis instruction; maximum 1500 characters |

## Optional Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `audio_references` | string[] | omitted | Up to 3 preset voice IDs or reference-audio URLs |
| `image_urls` | string[] | omitted | One reference-image URL |
| `format` | string | `wav` | `wav`, `mp3`, `pcm`, or `ogg_opus` |
| `sample_rate` | integer | `24000` | `8000`, `16000`, `24000`, `32000`, `44100`, or `48000` |
| `speech_rate` | number | `1.0` | Speech speed from `0.5` to `2.0` |
| `loudness_rate` | number | `1.0` | Loudness multiplier from `0.5` to `2.0` |
| `pitch_rate` | integer | `0` | Pitch adjustment from `-12` to `12` semitones |
| `callback_url` | string | omitted | HTTPS URL invoked when task reaches a terminal state |

## Mode Selection

The API auto-detects generation mode from reference inputs:

- Text-to-audio: pass only `prompt`.
- Reference-audio / voice control: pass `audio_references`.
- Reference-image: pass `image_urls`.

`audio_references` and `image_urls` are mutually exclusive.

## Reference Audio

Each `audio_references` item can be:

- a preset voice ID from the voice list
- a reference-audio URL

Use `@audio1`, `@audio2`, and `@audio3` in the prompt to reference entries by array order.

Constraints:

- up to 3 items total
- each uploaded reference clip must be 30 seconds or shorter
- each uploaded reference clip must be 10 MB or smaller
- accepted reference-audio formats: `wav`, `mp3`, `pcm`, `ogg_opus`

## Reference Image

Constraints:

- up to 1 image URL
- image must be 10 MB or smaller
- accepted image formats: `jpeg`, `png`, `webp`

## Query Task Status

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
Authorization: Bearer ${EVOLINK_API_KEY}
```

Use this endpoint until the task status is `completed`, `failed`, or `cancelled`.

