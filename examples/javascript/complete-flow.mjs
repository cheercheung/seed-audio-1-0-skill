const apiKey = process.env.EVOLINK_API_KEY;
if (!apiKey) {
  throw new Error("Set EVOLINK_API_KEY first");
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const text = await response.text();
  let data = {};
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    throw new Error(`Non-JSON response: ${text}`);
  }
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}: ${JSON.stringify(data)}`);
  }
  return data;
}

const task = await requestJson("https://api.evolink.ai/v1/audios/generations", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "doubao-seed-audio-1-0",
    prompt: "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator.",
    format: "mp3",
    sample_rate: 24000
  })
});

if (!task.id) {
  throw new Error(`Create task did not return id: ${JSON.stringify(task)}`);
}

console.log(`TASK_SUBMITTED: task_id=${task.id}`);

for (let attempt = 0; attempt < 120; attempt += 1) {
  const current = await requestJson(`https://api.evolink.ai/v1/tasks/${task.id}`, {
    headers: { Authorization: `Bearer ${apiKey}` }
  });

  if (current.status === "completed") {
    console.log(JSON.stringify(current, null, 2));
    process.exit(0);
  }
  if (current.status === "failed" || current.status === "cancelled") {
    throw new Error(`Task ended with ${current.status}: ${JSON.stringify(current)}`);
  }
  console.log(`STATUS_UPDATE: status=${current.status} progress=${current.progress ?? ""}`);
  await new Promise((resolve) => setTimeout(resolve, 3000));
}

throw new Error(`Timed out waiting for task ${task.id}`);

