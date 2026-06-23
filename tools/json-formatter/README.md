# JSON Formatter & Validator

**URL:** https://tools.stackfreeks.com/tools/json-formatter/

A free, browser-based JSON formatter, beautifier, and validator with instant syntax highlighting. No account, no upload, no dependencies — runs entirely in the browser via native `JSON.parse()` and `JSON.stringify()`.

## Features

- **Format / Beautify** — expands JSON with configurable indentation (2 spaces, 4 spaces, or Tab)
- **Minify** — strips all whitespace for production/API use
- **Validate** — shows a green banner with key/depth counts on success, or a red banner with the exact `SyntaxError` message and position on failure
- **Syntax highlighting** — custom DOM-based highlighter; no library required
  - String values: `#86efac` (green)
  - Numbers: `#93c5fd` (blue)
  - Booleans / null: `#f9a8d4` (pink)
  - Object keys: `#e2e8f0` (white-ish)
  - Punctuation: `#64748b` (gray)
- **Auto-format on paste** — detects `paste` event and formats immediately
- **Copy Output** — copies formatted/minified JSON to clipboard
- **Sample JSON** — loads a realistic API response object for quick demo
- **Clear** — resets both panes
- **EN/KO bilingual** — full i18n via `/shared/i18n.js`

## Stack

- Pure HTML / CSS / JavaScript (no build step, no npm)
- Zero external libraries
- Deployed on Cloudflare Pages via GitHub `main` branch push

## Target Keywords

- json formatter
- format json online
- json beautifier
- json validator online

## Monetisation

- Google AdSense slot (top, marked with comment)
- Vultr affiliate banner (`https://www.vultr.com/?ref=9907834-9J`) — $10 per sign-up
