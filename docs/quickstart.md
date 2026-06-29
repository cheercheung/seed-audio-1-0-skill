# Seed Audio 1.0 Quickstart

## 1. Set API Key

```bash
export EVOLINK_API_KEY="your_key_here"
```

## 2. Create A Task

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/audios/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "doubao-seed-audio-1-0",
    "prompt": "Create a 15-second calm product video audio bed with soft music, a clean studio ambience, and gentle narration.",
    "format": "mp3",
    "sample_rate": 24000
  }'
```

The response includes an `id`, for example:

```json
{
  "id": "task-unified-1775200000-abcd1234",
  "object": "audio.generation.task",
  "model": "doubao-seed-audio-1-0",
  "status": "pending",
  "progress": 0,
  "type": "audio"
}
```

## 3. Poll Task Status

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/task-unified-1775200000-abcd1234" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

Stop polling when `status` is `completed`, `failed`, or `cancelled`.

## 4. Run A Complete Example

```bash
node examples/javascript/complete-flow.mjs
```

## 5. Dry Run Without Credits

```bash
scripts/seed-audio-generate.sh --prompt "Short test" --dry-run
```

