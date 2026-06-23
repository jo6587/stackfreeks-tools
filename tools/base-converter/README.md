# Number Base Converter — StackFreeks Tools

A free, instant four-way number base converter that runs entirely in the browser. No installs, no server, no dependencies beyond a single shared i18n script.

**Live URL:** https://tools.stackfreeks.com/tools/base-converter/

## Features

- **Four-way live conversion** — Binary ↔ Octal ↔ Decimal ↔ Hexadecimal
- Edit any field and all three others update instantly
- Hex input is case-insensitive; output is always uppercase
- **Copy button** on every field with "Copied!" feedback
- **Character count badge** showing current value length
- **Quick presets** — 0, 1, 8, 10, 16, 255, 256, 65535, 1048576
- **Bit-length analysis** — binary digit count, minimum bits needed, and which bit-width (8 / 16 / 32 / >32) the number fits in
- Real-time input validation per base (Binary: 0–1, Octal: 0–7, Decimal: 0–9, Hex: 0–9 A–F)
- Negative numbers not supported — shows inline error
- Clear-all on empty input

## Tech Stack

- Pure HTML/CSS/JS — zero build step, zero npm
- Hosted on Cloudflare Pages (auto-deploy from `main` branch)
- Multilingual EN/KO via `/shared/i18n.js` with `window.SF_PAGE_I18N` page overrides

## File Structure

```
tools/base-converter/
├── index.html   # Complete single-file tool
└── README.md    # This file
```

## Design Tokens

Uses the shared StackFreeks dark-theme token set (`--bg: #0a0a0b`, `--accent: #6366f1`, etc.).

## SEO

- Title: `Number Base Converter — Free Online Tool | StackFreeks`
- Meta description targets "binary octal decimal hexadecimal converter" keywords
- Canonical URL set; Open Graph tags included
- AdSense slot placeholder comment in `<head>`
