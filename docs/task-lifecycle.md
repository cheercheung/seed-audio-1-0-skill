# Task Lifecycle

Seed-Audio 1.0 generation is asynchronous.

## Create

Send a `POST /v1/audios/generations` request. A successful response creates an audio generation task and returns a task `id`.

Initial statuses can include:

- `pending`
- `processing`

## Poll

Poll:

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

Client behavior:

- keep the task ID from the create response
- poll with a fixed interval or backoff
- stop on terminal states
- add a timeout to avoid infinite waits

## Terminal States

| Status | Meaning | Client Action |
|---|---|---|
| `completed` | Generation finished | Read result URLs and save the audio promptly |
| `failed` | Generation failed | Inspect `error.code` and `error.message` |
| `cancelled` | Task was cancelled | Do not keep polling |

## URL Retention

Generated audio links are time-limited. Save completed outputs to durable storage promptly.

