# Regex Tester — StackFreeks Tools

A free, browser-based regular expression tester with live match highlighting, flag toggles, capture group inspection, and a built-in cheat sheet. No signup, no server — runs entirely in the browser.

**Live:** [tools.stackfreeks.com/tools/regex-tester/](https://tools.stackfreeks.com/tools/regex-tester/)

## Features

- **Live matching** — matches update on every keystroke in the pattern or test string
- **Match highlighting** — matched text is highlighted inline with accent color
- **Flag toggles** — pill buttons for `g` (global), `i` (ignore case), `m` (multiline), `s` (dotall)
- **Match list panel** — shows each match with index, matched text, position, length, and any capture groups
- **Copy Pattern** — copies `/pattern/flags` format to clipboard
- **Regex cheat sheet** — collapsible panel with 8 common patterns; click "Use" to load any pattern instantly
- **EN / KO bilingual** — full English and Korean UI via `/shared/i18n.js`

## Cheat Sheet Patterns

| Name         | Pattern                                          |
|--------------|--------------------------------------------------|
| Email        | `[\w.-]+@[\w.-]+\.\w+`                          |
| URL          | `https?:\/\/[^\s]+`                              |
| Phone (US)   | `\d{3}[-.\s]\d{3}[-.\s]\d{4}`                   |
| IPv4         | `\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`        |
| Date         | `\d{4}-\d{2}-\d{2}`                              |
| Hex Color    | `#[0-9a-fA-F]{3,6}`                              |
| Numbers Only | `\d+`                                            |
| Words        | `\b\w+\b`                                        |

## Tech

- Pure HTML / CSS / JS — zero dependencies, zero build step
- JavaScript `RegExp` engine (ES2018+)
- Shared i18n system: `/shared/i18n.js`
- Deployed via Cloudflare Pages on push to `main`

## Part of StackFreeks Tools

A collection of free developer utilities at [tools.stackfreeks.com](https://tools.stackfreeks.com).
