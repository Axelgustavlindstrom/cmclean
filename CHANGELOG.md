# Changelog

## 0.1.0 — 2026-08-20

- Initial release.
- Detect TODO-like debris (`TODO`, `FIXME`, `HACK`, `XXX`).
- Detect author plaques (`@author`, `@created by`, `@written by`).
- Detect blocker-style remarks (`@blame`, `@debugger`, `@temp`, `@workaround`).
- Detect suspicious debris (`@#\$%` patterns).
- Detect excessively long comments (>240 chars).
- Multi-language support: `.py`, `.js`, `.ts`, `.tsx`, `.md`, `.yaml`, `.yml`, `.json`, `.toml`.
- JSON and human-friendly text output.
- CLI via `cmclean` and `python -m cmclean`.
