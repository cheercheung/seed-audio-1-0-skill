# Seed Audio 1.0 Skill

<p align="center">
  <strong>EvoLink를 통해 Seed Audio 1.0으로 음성, 대화, 앰비언스, 효과음, 혼합 오디오 장면을 생성합니다.</strong>
</p>

<p align="center">
  <a href="https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=banner">
    <img src="assets/banner.jpg" alt="seed-audio-1-0-agent-skill" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/evolink-seed-audio"><img src="https://img.shields.io/npm/v/evolink-seed-audio?color=cb3837&label=npm" alt="NPM version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/cheercheung/seed-audio-1-0-skill/stargazers"><img src="https://img.shields.io/github/stars/cheercheung/seed-audio-1-0-skill?style=flat" alt="GitHub stars"></a>
  <a href="https://github.com/cheercheung/seed-audio-1-0-skill/commits/main/"><img src="https://img.shields.io/github/last-commit/cheercheung/seed-audio-1-0-skill" alt="Last commit"></a>
</p>

<p align="center">
  <a href="#-menu">메뉴</a> -
  <a href="#installation">설치</a> -
  <a href="#seed-audio-10-api-quick-start">API 빠른 시작</a> -
  <a href="#getting-an-api-key">API 키</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">EvoLink에서 사용해보기</a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸_English-Read-111111" alt="English"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703" alt="Español"></a>
  <a href="README.pt.md"><img src="https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f" alt="Português"></a>
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵_日本語-表示-52b788" alt="日本語"></a>
  <a href="README.ko.md"><img src="https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de" alt="한국어"></a>
  <a href="README.de.md"><img src="https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261" alt="Deutsch"></a>
  <a href="README.fr.md"><img src="https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51" alt="Français"></a>
  <a href="README.tr.md"><img src="https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828" alt="Türkçe"></a>
  <a href="README.zh-TW.md"><img src="https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec" alt="繁體中文"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f" alt="简体中文"></a>
  <a href="README.ru.md"><img src="https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590" alt="Русский"></a>
</p>

> **AI 에이전트인가요?** README 대신 에이전트용 단계별 설치 안내인 [**llms-install.md**](llms-install.md)로 바로 이동하세요.

---

## 📑 메뉴

- [이것은 무엇인가요?](#what-is-this)
- [설치](#installation)
- [API 키 받기](#getting-an-api-key)
- [Seed Audio 1.0 API 빠른 시작](#seed-audio-10-api-quick-start)
- [파일 구조](#file-structure)
- [문제 해결](#troubleshooting)
- [호환성](#compatibility)
- [라이선스](#license)
- [커뮤니티](#community)
- [스타 기록](#star-history)

<a id="what-is-this"></a>

## 이것은 무엇인가요?

| 항목 | 값 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| 모델 | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| 유지 관리 영역 | `api-skill` |
| 사용자 진입점 | API 빠른 시작 및 에이전트 skill 설치 |

다음이 필요할 때 이 저장소를 사용하세요.

- 생성 및 폴링까지 포함한 완전한 비동기 흐름으로 EvoLink Seed-Audio API 호출
- `npx evolink-seed-audio`로 에이전트 skill 설치
- 내레이션, 다중 인물 대화, 앰비언스, 효과음, 혼합 오디오 장면 생성
- 요청 파라미터, 응답 형식, 콜백, 오류, 음성 레퍼런스 확인

---

<a id="installation"></a>

## 설치

### 빠른 설치 (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### npm으로 설치 (권장)

```bash
npx evolink-seed-audio
```

에이전트용 자동 설치:

```bash
npx evolink-seed-audio -y
```

특정 skills 디렉터리에 설치:

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### 수동 설치

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### 에이전트 자동 설치

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

그다음 EVOLINK_API_KEY를 설정하고 다음 파일을 읽으세요:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

그다음 EVOLINK_API_KEY를 설정하고 다음 파일을 읽으세요:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

그다음 EVOLINK_API_KEY를 설정하고 다음 파일을 읽으세요:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

원라이너:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## API 키 받기

1. [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key)를 엽니다.
2. API 키를 만들거나 복사합니다.
3. 셸에서 내보냅니다:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. 생성 작업을 시작합니다:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Seed Audio 1.0 API 빠른 시작

### 빠른 API 요청

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

API는 비동기 방식입니다. 생성 요청은 작업 `id`를 반환합니다. 작업이 `completed`, `failed`, `cancelled` 중 하나가 될 때까지 폴링하세요:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### 첫 실행 전체 흐름

```bash
node examples/javascript/complete-flow.mjs
```

또는 포함된 스크립트를 사용하세요:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### 생성 모드

| 모드 | 사용 방법 |
|---|---|
| 텍스트를 오디오로 | `prompt`만 전달합니다. |
| 음성 레퍼런스 | 최대 3개의 `audio_references`를 전달하고 prompt 안에서 `@audio1`, `@audio2`, `@audio3`로 참조합니다. |
| 참조 이미지 | `image_urls` 항목 하나를 전달합니다. `image_urls`와 `audio_references`를 함께 사용하지 마세요. |
| Callback | 최종 작업 상태를 받으려면 `callback_url`을 전달합니다. |

### 스크립트 참조

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### API 파라미터

| 파라미터 | 필수 | 설명 |
|---|---:|---|
| `model` | 예 | `doubao-seed-audio-1-0` 사용 |
| `prompt` | 예 | 최대 1500자 |
| `audio_references` | no | 최대 3개의 프리셋 음성 또는 참조 오디오 URL |
| `image_urls` | no | 참조 이미지 URL 하나 |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; 기본값 `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5`에서 `2.0` |
| `loudness_rate` | no | `0.5`에서 `2.0` |
| `pitch_rate` | no | `-12`에서 `12` 반음 |
| `callback_url` | no | 최종 작업 상태를 받는 HTTPS callback URL |

자세한 내용은 [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md), [references/api-params.md](references/api-params.md)를 참고하세요.

---

<a id="file-structure"></a>

## 파일 구조

```text
.
├── README.md
├── README.es.md ... README.ru.md
├── SKILL.md
├── llms-install.md
├── _meta.json
├── package.json
├── bin/cli.js
├── scripts/seed-audio-generate.sh
├── docs/
├── examples/
├── references/
└── assets/banner.jpg
```

---

<a id="troubleshooting"></a>

## 문제 해결

| 문제 | 가능한 원인 | 조치 |
|---|---|---|
| `EVOLINK_API_KEY is not set` | API 키가 없음 | `EVOLINK_API_KEY`를 export한 뒤 다시 시도하세요. |
| `create request failed` | 키, 요청 본문 또는 네트워크 문제 | `--dry-run`으로 실행한 뒤 `docs/errors.md`를 확인하세요. |
| `POLL_TIMEOUT` | 로컬 폴링 시간이 끝나기 전에 작업이 완료되지 않음 | 나중에 `GET /v1/tasks/{task_id}`를 조회하세요. 자동으로 다시 제출하지 마세요. |
| 오디오 URL을 찾을 수 없음 | 응답 형식이 바뀌었거나 작업에 아직 생성된 자산이 없음 | 전체 작업 JSON을 저장하고 `docs/response-schema.md`와 비교하세요. |

---

<a id="compatibility"></a>

## 호환성

| 에이전트 또는 런타임 | 설치 방법 | 상태 |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 지원 |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | 경로 설치로 지원 |
| OpenClaw | `openclaw skills add` 또는 `npx ... --path ~/.openclaw/skills` | 지원 |
| Cursor | `npx ... --path ~/.cursor/skills` 또는 프로젝트 `.cursor/skills` | 지원 |
| Node.js | `>=16` | `package.json`에서 요구 |
| Shell | bash + curl + python3 | `scripts/seed-audio-generate.sh`에서 요구 |

---

<a id="license"></a>

## 라이선스

MIT. [LICENSE](LICENSE)를 참고하세요.

---

<a id="community"></a>

## 커뮤니티

- [EvoLink에서 Seed-Audio 사용해보기](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [EvoLink API 키 만들기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [공식 API 문서 읽기](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [공식 음성 목록 읽기](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## 스타 기록

```text
저장소가 공개되면 스타 기록을 사용할 수 있습니다.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
