# Seed-Audio 1.0 API Parameters

Source docs:

- https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0
- https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices

## Model

Use:

```text
doubao-seed-audio-1-0
```

## Prompt

- Required.
- Maximum 1500 characters.
- For reference audio, use `@audio1`, `@audio2`, and `@audio3`.

## audio_references

- Optional.
- Up to 3 items.
- Each item can be a preset `voice_type` or a reference-audio URL.
- Reference audio and reference image are mutually exclusive.
- Reference-audio URL constraints: up to 30 seconds, up to 10 MB, `wav`, `mp3`, `pcm`, or `ogg_opus`.

## image_urls

- Optional.
- Up to 1 item.
- Mutually exclusive with `audio_references`.
- Image URL constraints: up to 10 MB, `jpeg`, `png`, or `webp`.

## Output

| Parameter | Values |
|---|---|
| `format` | `wav`, `mp3`, `pcm`, `ogg_opus` |
| `sample_rate` | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | `0.5` to `2.0`, step `0.01` |
| `loudness_rate` | `0.5` to `2.0`, step `0.01` |
| `pitch_rate` | `-12` to `12` semitones |

## Callback

- `callback_url` must be HTTPS.
- Internal IP addresses are forbidden.
- Maximum URL length is 2048 characters.
- Callback timeout is 10 seconds.
- Failed callbacks retry up to 3 times.

