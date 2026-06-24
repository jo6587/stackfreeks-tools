# SLA Uptime Calculator

**Live tool:** [tools.stackfreeks.com/tools/sla-uptime-calculator/](https://tools.stackfreeks.com/tools/sla-uptime-calculator/)

Calculate allowed downtime for any SLA percentage — instantly see yearly, monthly, weekly, and daily downtime budgets.

## Features

- **Live calculation** — results update as you type or drag
- **Synced number input + slider** — range 90–99.999%, step 0.001
- **Preset buttons** — Two Nines (99%), Three Nines (99.9%), 99.95%, Four Nines (99.99%), Five Nines (99.999%)
- **Color-coded SLA display** — red below 99.9%, amber below 99.99%, green at 99.99%+
- **Downtime table** — per year, month, week, and day formatted as days/hours/minutes/seconds
- **EN / KO bilingual** — full i18n toggle via `/shared/i18n.js`

## Calculation

```
downtime = (1 − SLA/100) × period_in_seconds
```

| Period   | Seconds used             |
|----------|--------------------------|
| Per Year | 365.25 × 24 × 3600       |
| Per Month | 30.44 × 24 × 3600       |
| Per Week | 7 × 24 × 3600           |
| Per Day  | 24 × 3600               |

## Tech

- Pure HTML/CSS/JS — no build step, no dependencies
- Works entirely in the browser
- Hosted on Cloudflare Pages (auto-deploy from `main` branch)
