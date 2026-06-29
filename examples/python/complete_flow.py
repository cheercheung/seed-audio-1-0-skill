import json
import os
import time
import urllib.error
import urllib.request


API_KEY = os.environ.get("EVOLINK_API_KEY")
if not API_KEY:
    raise SystemExit("Set EVOLINK_API_KEY first")


def request_json(url, method="GET", payload=None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"{exc.code} {exc.reason}: {detail}") from exc


task = request_json(
    "https://api.evolink.ai/v1/audios/generations",
    method="POST",
    payload={
        "model": "doubao-seed-audio-1-0",
        "prompt": "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator.",
        "format": "mp3",
        "sample_rate": 24000,
    },
)

task_id = task.get("id")
if not task_id:
    raise SystemExit(f"Create task did not return id: {json.dumps(task, indent=2)}")

print(f"TASK_SUBMITTED: task_id={task_id}")

for _ in range(120):
    current = request_json(f"https://api.evolink.ai/v1/tasks/{task_id}")
    status = current.get("status")
    if status == "completed":
        print(json.dumps(current, indent=2))
        raise SystemExit(0)
    if status in {"failed", "cancelled"}:
        raise SystemExit(f"Task ended with {status}: {json.dumps(current, indent=2)}")
    print(f"STATUS_UPDATE: status={status} progress={current.get('progress', '')}")
    time.sleep(3)

raise SystemExit(f"Timed out waiting for task {task_id}")

