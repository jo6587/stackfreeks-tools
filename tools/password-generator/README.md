# Password Generator

A free, browser-based strong password generator built for [StackFreeks Tools](https://tools.stackfreeks.com).

**Live URL:** https://tools.stackfreeks.com/tools/password-generator/

## Features

- **Cryptographically secure** — uses `crypto.getRandomValues()` (Web Crypto API), never `Math.random()`
- **Fully client-side** — passwords are generated in your browser and never sent to a server
- **Configurable length** — slider from 8 to 64 characters (default: 16)
- **Character set toggles:**
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Symbols (!@#$%^&*…)
  - Exclude ambiguous characters (0, O, l, 1, I)
- **Strength meter** — visual bar with Weak / Fair / Strong / Very Strong rating
- **One-click copy** — copies to clipboard with visual feedback
- **Bulk generate** — generate 10 passwords at once, each with its own copy button
- **Auto-regenerate** — new password generated on every option change
- **Bilingual** — English / Korean toggle (EN/KO) via shared i18n system

## Strength Scoring

| Condition | Rating |
|---|---|
| Length < 8 or no charset selected | Weak |
| Length 8–11 with 2+ charsets OR length 12–15 with 1 charset | Fair |
| Length 12–15 with 3+ charsets OR length 16+ with 2–3 charsets | Strong |
| Length 16+ with all 4 charsets | Very Strong |

## Tech Stack

- Pure HTML / CSS / JavaScript — no build step, no dependencies
- `crypto.getRandomValues()` for cryptographic randomness
- Cloudflare Pages (static hosting)

## File Structure

```
tools/password-generator/
  index.html   # Tool page (self-contained)
  README.md    # This file
```

## SEO Targets

- `password generator`
- `random password generator`
- `strong password generator free`
