# Seed Audio 1.0 Skill

<p align="center">
  <strong>Genera voz, diálogos, ambientes, efectos de sonido y escenas de audio mixtas con Seed Audio 1.0 a través de EvoLink.</strong>
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
  <a href="#-menu">Menú</a> -
  <a href="#installation">Instalar</a> -
  <a href="#getting-an-api-key">Clave API</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Probar en EvoLink</a>
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

> **¿Agente de IA?** Salta el README y ve directamente a [**llms-install.md**](llms-install.md), con instrucciones de instalación paso a paso diseñadas para ti.

---

## 📑 Menú

- [¿Qué es esto?](#what-is-this)
- [Instalación](#installation)
- [Obtener una clave API](#getting-an-api-key)
- [Solución de problemas](#troubleshooting)
- [Compatibilidad](#compatibility)
- [Licencia](#license)

<a id="what-is-this"></a>

## ¿Qué es esto?

| Campo | Valor |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modelo | Seed Audio 1.0 |
| Superficie mantenida | `api-skill` |
| Entradas de usuario | instalación del skill para agentes y configuración de clave API |

Usa este repositorio cuando quieras:

- llamar a la API Seed-Audio de EvoLink con un flujo asíncrono completo de creación y consulta
- instalar un skill de agente con `npx evolink-seed-audio`
- generar narración, diálogo de varios personajes, ambientes, efectos de sonido y escenas de audio mixtas
- revisar parámetros de solicitud, formatos de respuesta, callbacks, errores y referencias de voz

---

<a id="installation"></a>

## Instalación

### Instalación rápida (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Instalar con npm (recomendado)

```bash
npx evolink-seed-audio
```

Instalación silenciosa para agentes:

```bash
npx evolink-seed-audio -y
```

Instalar en un directorio de skills específico:

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Instalación manual

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Instalación automática para agentes

Codex:

```text
Instala el skill de Seed Audio ejecutando:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

Luego configura EVOLINK_API_KEY y lee:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
Instala el skill de Seed Audio ejecutando:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Luego configura EVOLINK_API_KEY y lee:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
Instala el skill de Seed Audio ejecutando:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

Luego configura EVOLINK_API_KEY y lee:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

Una línea:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
```

---

<a id="getting-an-api-key"></a>

## Obtener una clave API

1. Abre [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Crea o copia una clave API.
3. Expórtala en tu shell:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Inicia una tarea de generación:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

<a id="troubleshooting"></a>

## Solución de problemas

| Problema | Causa probable | Acción |
|---|---|---|
| `EVOLINK_API_KEY is not set` | Falta la clave API | Exporta `EVOLINK_API_KEY` y vuelve a intentarlo. |
| `create request failed` | Clave no válida, cuerpo de solicitud incorrecto o fallo de red | Ejecuta con `--dry-run` y revisa `docs/errors.md`. |
| `POLL_TIMEOUT` | La tarea no terminó antes de que finalizara el sondeo local | Consulta `GET /v1/tasks/{task_id}` más tarde. No la vuelvas a enviar automáticamente. |
| No se encontró URL de audio | La forma de la respuesta cambió o la tarea aún no tiene recurso generado | Guarda el JSON completo de la tarea y compáralo con `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Compatibilidad

| Agente o runtime | Método de instalación | Estado |
|---|---|---|
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | Compatible |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Compatible |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | Compatible mediante instalación por ruta |
| Node.js | `>=16` | Requerido por `package.json` |
| Shell | bash + curl + python3 | Requerido por `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Licencia

MIT. Consulta [LICENSE](LICENSE).

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
