# Pipeline Run Report

## Summary

- Run id: 20260629-seed-audio-api-skill-scaffold
- Date: 2026-06-29
- Pipeline: skill-api
- Mode: scaffold + review
- Repository: doubao-seed-audio-api-skill
- Model: Doubao Seed-Audio 1.0
- Status: local scaffold complete, public release blocked

## Inputs

- Intake file: `.codex/reports/model-intake.md`
- Source docs:
  - https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0
  - https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices
- Approval status: local build only

## Work Performed

- Created local skill/API repository.
- Added npm installer metadata and CLI.
- Added `SKILL.md` and `llms-install.md`.
- Added API docs, response schema, callback docs, errors, task lifecycle, and voice guide.
- Added cURL, JavaScript, and Python complete-flow examples.
- Added `scripts/seed-audio-generate.sh` with create + poll behavior and dry-run mode.
- Added static validator.

## Review Counts

- P0 issues: 0 for local scaffold
- P1 issues: 1, real API smoke test pending owner approval
- P2 issues: 1, localization not generated in first pass

## Files Changed

- New repository under `/Users/evolink/Desktop/github-repo/doubao-seed-audio-api-skill`

## Verification

- Commands:
  - `python3 scripts/validate_repo.py`
  - `npm pack --dry-run --json`
  - `node bin/cli.js -y --path <tmpdir>`
  - `<tmpdir>/doubao-seed-audio/scripts/seed-audio-generate.sh --prompt "Installed dry run" --dry-run`
  - `node --check bin/cli.js`
  - `node --check examples/javascript/complete-flow.mjs`
  - `bash -n scripts/seed-audio-generate.sh`
  - `bash -n examples/curl/complete-flow.sh`
  - `python3 -m py_compile examples/python/complete_flow.py`
  - `bash scripts/seed-audio-generate.sh --prompt "Short validation test" --dry-run`
- Result: `python3 scripts/validate_repo.py` passed
- Package dry-run: passed; tarball includes README, package metadata, skill files, docs, references, scripts, and examples
- Skill install smoke test: passed; CLI installed to a temporary skills directory and installed script dry-run emitted `doubao-seed-audio-1-0`
- Smoke-test level: static + dry-run + install-dry-run
- Skip reasons: real API smoke test skipped because owner has not approved API credit spend
- Package name check: `npm view evolink-seed-audio version` returned npm 404, so no published package was found in the public registry at check time

## Publication

- Commit: recorded in final closeout; use `git rev-parse --short HEAD` for the current local commit
- Push target: none
- npm publish: not run
- External announcements: none

## Blockers And Next Actions

- Replace `_meta.json.ownerId` with real EvoLink owner ID before release.
- Run real API smoke test after owner approves credit spend.
- Add localized README files if this repository will be public growth-facing.
