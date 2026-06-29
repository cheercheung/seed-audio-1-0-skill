# Doubao Seed-Audio API Skill Review

Review date: 2026-06-29

## Verdict

Local scaffold is complete for a first-pass Skill + API repository. It is not ready for npm/public release until owner ID and real API smoke-test gates are closed.

## Checklist

| Area | Status | Evidence |
|---|---|---|
| README first screen | Pass | API and agent skill entrances are visible |
| API quickstart | Pass | Uses `EVOLINK_API_KEY` |
| Async first-run flow | Pass | Script and examples create task, poll task, stop on terminal states |
| Response docs | Pass | `docs/response-schema.md` |
| Error docs | Pass | `docs/errors.md` |
| Callback docs | Pass | `docs/callbacks.md` |
| Voice docs | Pass | `docs/voices.md` |
| Skill files | Pass | `SKILL.md`, `llms-install.md`, `_meta.json`, package, CLI |
| Metadata consistency | Partial | Version and slug match; `ownerId` is placeholder |
| Static validation | Pass after `python3 scripts/validate_repo.py` |
| npm pack dry-run | Pass | Tarball includes docs, scripts, references, skill files, and examples |
| install dry-run | Pass | CLI installs to a temporary skills dir and installed script dry-run works |
| Package name | Pass | `npm view evolink-seed-audio version` returned 404, no package found |
| Real API smoke test | Skipped | Needs owner approval for credit spend |
| npm publish | Blocked | Owner approval and real ownerId required |

## Required Before Release

1. Replace `_meta.json.ownerId`.
2. Run a real API smoke test with a low-cost prompt.
3. Confirm package name availability.
4. Add release notes and owner approval for npm publish.
