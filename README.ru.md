# Seed Audio 1.0 Skill

<p align="center">
  <strong>Создавайте речь, диалоги, атмосферные звуки, звуковые эффекты и смешанные аудиосцены с Seed Audio 1.0 через EvoLink.</strong>
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
  <a href="#-menu">Меню</a> -
  <a href="#installation">Установка</a> -
  <a href="#seed-audio-10-api-quick-start">Быстрый старт API</a> -
  <a href="#getting-an-api-key">API-ключ</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Попробовать в EvoLink</a>
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

> **AI-агент?** Пропустите README и откройте [**llms-install.md**](llms-install.md) с пошаговыми инструкциями установки для агентов.

---

## 📑 Меню

- [Что это?](#what-is-this)
- [Установка](#installation)
- [Получение API-ключа](#getting-an-api-key)
- [Быстрый старт API Seed Audio 1.0](#seed-audio-10-api-quick-start)
- [Структура файлов](#file-structure)
- [Устранение неполадок](#troubleshooting)
- [Совместимость](#compatibility)
- [Лицензия](#license)
- [Сообщество](#community)
- [История звезд](#star-history)

<a id="what-is-this"></a>

## Что это?

| Поле | Значение |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Модель | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| Поддерживаемая поверхность | `api-skill` |
| Входы для пользователя | быстрый старт API и установка agent skill |

Используйте этот репозиторий, когда хотите:

- вызвать EvoLink Seed-Audio API с полным асинхронным циклом создания и опроса
- установить agent skill через `npx evolink-seed-audio`
- создавать дикторскую речь, диалоги нескольких персонажей, атмосферу, звуковые эффекты и смешанные аудиосцены
- изучать параметры запросов, формы ответов, callback, ошибки и голосовые референсы

---

<a id="installation"></a>

## Установка

### Быстрая установка (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### Установка через npm (рекомендуется)

```bash
npx evolink-seed-audio
```

Тихая установка для агентов:

```bash
npx evolink-seed-audio -y
```

Установка в указанный каталог skills:

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### Ручная установка

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Автоустановка для агентов

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Затем задайте EVOLINK_API_KEY и прочитайте:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

Затем задайте EVOLINK_API_KEY и прочитайте:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

Затем задайте EVOLINK_API_KEY и прочитайте:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

Одна команда:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## Получение API-ключа

1. Откройте [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Создайте или скопируйте API-ключ.
3. Экспортируйте его в shell:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Запустите задачу генерации:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Быстрый старт API Seed Audio 1.0

### Быстрый API-запрос

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

API работает асинхронно. Запрос создания возвращает `id` задачи; опрашивайте статус, пока задача не станет `completed`, `failed` или `cancelled`:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### Полный первый запуск

```bash
node examples/javascript/complete-flow.mjs
```

Или используйте входящий в пакет скрипт:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### Режимы генерации

| Режим | Как использовать |
|---|---|
| Текст в аудио | Передайте только `prompt`. |
| Голосовой референс | Передайте до 3 `audio_references`; ссылайтесь на них в prompt как `@audio1`, `@audio2` и `@audio3`. |
| Референсное изображение | Передайте один элемент `image_urls`. Не совмещайте `image_urls` с `audio_references`. |
| Callback | Передайте `callback_url`, чтобы получать финальные состояния задачи. |

### Справка по скрипту

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### Параметры API

| Параметр | Обязательно | Примечания |
|---|---:|---|
| `model` | да | Используйте `doubao-seed-audio-1-0` |
| `prompt` | да | До 1500 символов |
| `audio_references` | no | До 3 preset-голосов или URL референсного аудио |
| `image_urls` | no | Один URL референсного изображения |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; по умолчанию `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | от `0.5` до `2.0` |
| `loudness_rate` | no | от `0.5` до `2.0` |
| `pitch_rate` | no | от `-12` до `12` полутонов |
| `callback_url` | no | HTTPS callback URL для финальных состояний задачи |

См. [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md) и [references/api-params.md](references/api-params.md).

---

<a id="file-structure"></a>

## Структура файлов

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

## Устранение неполадок

| Проблема | Вероятная причина | Действие |
|---|---|---|
| `EVOLINK_API_KEY is not set` | Нет API-ключа | Экспортируйте `EVOLINK_API_KEY` и повторите попытку. |
| `create request failed` | Неверный ключ, тело запроса или сбой сети | Запустите с `--dry-run`, затем проверьте `docs/errors.md`. |
| `POLL_TIMEOUT` | Задача не завершилась до окончания локального опроса | Позже запросите `GET /v1/tasks/{task_id}`. Не отправляйте задачу повторно автоматически. |
| URL аудио не найден | Форма ответа изменилась или у задачи еще нет созданного ресурса | Сохраните полный JSON задачи и сравните с `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Совместимость

| Агент или runtime | Способ установки | Статус |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Поддерживается |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | Поддерживается через установку по пути |
| OpenClaw | `openclaw skills add` или `npx ... --path ~/.openclaw/skills` | Поддерживается |
| Cursor | `npx ... --path ~/.cursor/skills` или проектный `.cursor/skills` | Поддерживается |
| Node.js | `>=16` | Требуется `package.json` |
| Shell | bash + curl + python3 | Требуется `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Лицензия

MIT. См. [LICENSE](LICENSE).

---

<a id="community"></a>

## Сообщество

- [Попробовать Seed-Audio в EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [Создать API-ключ EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [Открыть официальную документацию API](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [Открыть официальный список голосов](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## История звезд

```text
История звезд станет доступна после публикации репозитория.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
