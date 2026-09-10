# Typing Speed Test

> Live: https://tools.stackfreeks.com/tools/typing-speed-test/

A code-focused typing speed test. Type real, syntactically valid snippets and get your WPM, raw WPM, and accuracy — a WPM test built for programmers, not prose.

## Features

- 7 languages: JavaScript, Python, Go, Rust, TypeScript, SQL, Bash (3-4 real snippets each)
- Per-character highlighting: untyped / correct / incorrect, with a live caret
- Live and final metrics: net WPM, raw WPM, accuracy %, elapsed time, error count
- Standard formula: `WPM = (correct chars / 5) / minutes`
- Timer starts on first keystroke; completion detected on the last character
- Tab inserts a real tab character (no focus jump); paste is blocked
- Best net WPM saved per language in `localStorage` (`typing-best-<lang>`)
- "Try again (same)" and "New snippet" controls
- EN/KO bilingual UI via `/shared/i18n.js`

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
