# Callback / Webhook

Pass `callback_url` to receive a server callback when the task reaches a terminal state.

```json
{
  "callback_url": "https://your-domain.com/webhooks/audio-completed"
}
```

Requirements:

- HTTPS only.
- Internal IP targets are not allowed.
- URL length must not exceed 2048 characters.
- The callback handler should return a 2xx response quickly.
- Callback timeout is 10 seconds.
- EvoLink retries failed callbacks up to 3 times, after about 1, 2, and 4 seconds.

The callback body has the same format as the task query response. Store the task ID and use `GET /v1/tasks/{task_id}` as a fallback.

Example callback payload:

```json
{
  "id": "task-unified-1775200000-abcd1234",
  "model": "doubao-seed-audio-1-0",
  "status": "completed",
  "progress": 100,
  "results": [
    "https://media.evolink.ai/example-audio.mp3"
  ]
}
```

