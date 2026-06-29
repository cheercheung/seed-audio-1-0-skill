# Seed Audio 1.0 Skill

<p align="center">
  <strong>EvoLink를 통해 Seed Audio 1.0으로 음성, 대화, 앰비언스, 효과음, 혼합 오디오 장면을 생성합니다.</strong>
</p>

<p align="center">
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=banner">
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
- [문제 해결](#troubleshooting)
- [호환성](#compatibility)
- [라이선스](#license)

<a id="what-is-this"></a>

## 이것은 무엇인가요?

| 항목 | 값 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| 모델 | Seed Audio 1.0 |
| 유지 관리 영역 | `api-skill` |
| 사용자 진입점 | agent skill 설치 및 API 키 설정 |

다음이 필요할 때 이 저장소를 사용하세요.

- 생성 및 폴링까지 포함한 완전한 비동기 흐름으로 EvoLink Seed-Audio API 호출
- `npx evolink-seed-audio`로 에이전트 skill 설치
- 내레이션, 다중 인물 대화, 앰비언스, 효과음, 혼합 오디오 장면 생성
- 요청 파라미터, 응답 형식, 콜백, 오류, 음성 레퍼런스 확인

---

<a id="installation"></a>

## 설치

### 빠른 설치 (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
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
npx evolink-seed-audio -y --path ~/.codex/skills
```

### 수동 설치

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Agent 자동 설치

Codex:

```text
다음 명령으로 Seed Audio skill을 설치하세요:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

그다음 EVOLINK_API_KEY를 설정하고 다음 파일을 읽으세요:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
다음 명령으로 Seed Audio skill을 설치하세요:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

그다음 EVOLINK_API_KEY를 설정하고 다음 파일을 읽으세요:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
다음 명령으로 Seed Audio skill을 설치하세요:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

그다음 EVOLINK_API_KEY를 설정하고 다음 파일을 읽으세요:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

한 줄 명령:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
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
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | 지원 |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 지원 |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | 경로 설치로 지원 |
| Node.js | `>=16` | `package.json`에서 요구 |
| Shell | bash + curl + python3 | `scripts/seed-audio-generate.sh`에서 요구 |

---

<a id="license"></a>

## 라이선스

MIT. [LICENSE](LICENSE)를 참고하세요.

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
