# Unix Timestamp Converter

**Live tool:** [tools.stackfreeks.com/tools/timestamp-converter/](https://tools.stackfreeks.com/tools/timestamp-converter/)

A free, browser-based Unix timestamp converter. No server, no account, no dependencies.

## Features

- **Live clock** — current Unix timestamp (seconds + milliseconds) updating every second
- **Timestamp → Date** — paste any Unix timestamp; auto-detects seconds vs. milliseconds (threshold: 1e10)
  - Outputs: local time with timezone name, UTC, ISO 8601, and relative time ("2 hours ago")
- **Date → Timestamp** — pick a date/time with the native browser picker
  - Outputs: Unix seconds, Unix milliseconds, ISO 8601
- One-click copy for every output field
- English / Korean (EN/KO) toggle via `/shared/i18n.js`
- Mobile responsive

## Tech

- Pure vanilla JS — `new Date()`, `Intl.DateTimeFormat`, `navigator.clipboard`
- No build step, no npm, no external libraries
- Cloudflare Pages static hosting

## SEO targets

- unix timestamp converter
- epoch to date
- timestamp to date online
- epoch converter
