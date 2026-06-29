# Error Handling

| Error | Likely Cause | Fix |
|---|---|---|
| `400 Bad Request` | Invalid model, prompt, reference input, format, rate, callback URL, or mutually exclusive inputs | Check request fields and constraints |
| `401 Unauthorized` | Missing or invalid `EVOLINK_API_KEY` | Set a valid key with `export EVOLINK_API_KEY=...` |
| `402 Payment Required` | Insufficient balance or billing issue | Check EvoLink account balance |
| `403 Forbidden` | Account, model, or permission restriction | Confirm model access |
| `404 Not Found` | Unknown task ID | Store the create response `id` exactly |
| `429 Too Many Requests` | Rate limit or concurrency pressure | Retry with backoff and reduce concurrency |
| `500` | Server-side error | Retry later or report the task/request details |
| `failed` task status | Provider-side generation failure or invalid input | Inspect `error.code` and `error.message` |

Recommended client behavior:

- validate required inputs before sending
- check HTTP status before parsing success
- print the API error body during development
- stop polling on `completed`, `failed`, or `cancelled`
- use a timeout to avoid infinite polling
- do not retry automatically after a task has been created unless the user approves another credit-consuming run

