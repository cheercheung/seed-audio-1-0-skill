# Response Schema

## Create Task Response

```json
{
  "created": 1775200000,
  "id": "task-unified-1775200000-abcd1234",
  "model": "doubao-seed-audio-1-0",
  "object": "audio.generation.task",
  "progress": 0,
  "status": "pending",
  "task_info": {
    "can_cancel": true,
    "estimated_time": 15,
    "audio_type": "audio_generation"
  },
  "type": "audio",
  "usage": {
    "credits_reserved": 9.6
  }
}
```

## Pending / Processing Response

```json
{
  "id": "task-unified-1775200000-abcd1234",
  "model": "doubao-seed-audio-1-0",
  "status": "processing",
  "progress": 45,
  "type": "audio"
}
```

## Completed Task Response

The task query response is the source of truth for the final shape. Clients should handle URLs in any of these common locations:

- `results[]`
- `result_urls[]`
- `result_data[].audio_url`
- `result_data[].url`

Example:

```json
{
  "id": "task-unified-1775200000-abcd1234",
  "model": "doubao-seed-audio-1-0",
  "status": "completed",
  "progress": 100,
  "type": "audio",
  "results": [
    "https://media.evolink.ai/example-audio.mp3"
  ]
}
```

## Failed Task Response

```json
{
  "id": "task-unified-1775200000-abcd1234",
  "model": "doubao-seed-audio-1-0",
  "status": "failed",
  "error": {
    "code": "invalid_request",
    "message": "Explain what went wrong."
  }
}
```

