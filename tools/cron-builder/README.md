# Cron Expression Builder

A free, browser-based visual cron expression builder and validator with real-time next-run previews.

**Live tool:** [tools.stackfreeks.com/tools/cron-builder/](https://tools.stackfreeks.com/tools/cron-builder/)

## Features

- **Visual Builder** — configure each cron field (minute, hour, day-of-month, month, day-of-week) using dropdowns with common presets, or enter custom values
- **Manual Input** — paste any cron expression to validate and preview it instantly
- **Human-readable description** — converts `0 9 * * 1-5` to "At 9:00 AM, Monday through Friday"
- **Next 5 run times** — calculated client-side in the user's local timezone using a pure JS cron parser
- **Quick presets** — one-click chips for the 6 most common schedules
- **Copy to clipboard** — copies the expression with a single click
- **EN/KO bilingual** — full English and Korean interface with toggle

## Cron Syntax Supported

| Syntax    | Example     | Meaning                |
|-----------|-------------|------------------------|
| `*`       | `*`         | Every unit             |
| `n`       | `5`         | Specific value         |
| `*/n`     | `*/15`      | Every n units          |
| `n-m`     | `1-5`       | Range                  |
| `n,m`     | `0,30`      | List                   |
| `n-m/s`   | `0-12/2`    | Range with step        |

## Quick Presets

| Expression    | Schedule               |
|---------------|------------------------|
| `* * * * *`   | Every minute           |
| `0 * * * *`   | Every hour             |
| `0 9 * * 1-5` | Weekdays at 9 AM       |
| `0 0 * * *`   | Daily at midnight      |
| `0 0 * * 0`   | Weekly on Sunday       |
| `0 0 1 * *`   | Monthly on the 1st     |

## Tech Stack

- Pure HTML, CSS, JavaScript — no frameworks, no build tools
- Cron parser implemented from scratch in vanilla JS
- Runs entirely in the browser — no server, no API calls
- Deployed on Cloudflare Pages

## Related

- [StackFreeks Blog](https://stackfreeks.com) — server, VPS, and developer guides
- [VPS Cost Calculator](https://tools.stackfreeks.com/tools/vps-cost-calculator/) — compare Vultr, Hetzner, DigitalOcean pricing
- [VPS Bandwidth Calculator](https://tools.stackfreeks.com/tools/vps-bandwidth-calculator/) — estimate bandwidth overage costs
