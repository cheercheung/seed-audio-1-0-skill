# Seed Audio 1.0 Skill

<p align="center">
  <strong>Создавайте речь, диалоги, атмосферные звуки, звуковые эффекты и смешанные аудиосцены с Seed Audio 1.0 через EvoLink.</strong>
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
  <a href="#-menu">Меню</a> -
  <a href="#installation">Установка</a> -
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
- [Устранение неполадок](#troubleshooting)
- [Совместимость](#compatibility)
- [Лицензия](#license)

<a id="what-is-this"></a>

## Что это?

| Поле | Значение |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Модель | Seed Audio 1.0 |
| Поддерживаемая поверхность | `api-skill` |
| Входы для пользователя | установка agent skill и настройка API-ключа |

Используйте этот репозиторий, когда хотите:

- вызвать EvoLink Seed-Audio API с полным асинхронным циклом создания и опроса
- установить agent skill через `npx evolink-seed-audio`
- создавать дикторскую речь, диалоги нескольких персонажей, атмосферу, звуковые эффекты и смешанные аудиосцены
- изучать параметры запросов, формы ответов, callback, ошибки и голосовые референсы

---

<a id="installation"></a>

## Установка

### Быстрая установка (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
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
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Ручная установка

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Автоматическая установка для агентов

Codex:

```text
Установите Seed Audio skill командой:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

Затем задайте EVOLINK_API_KEY и прочитайте:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
Установите Seed Audio skill командой:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Затем задайте EVOLINK_API_KEY и прочитайте:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
Установите Seed Audio skill командой:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

Затем задайте EVOLINK_API_KEY и прочитайте:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

Одна команда:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
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
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | Поддерживается |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Поддерживается |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | Поддерживается через установку по пути |
| Node.js | `>=16` | Требуется `package.json` |
| Shell | bash + curl + python3 | Требуется `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Лицензия

MIT. См. [LICENSE](LICENSE).

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
