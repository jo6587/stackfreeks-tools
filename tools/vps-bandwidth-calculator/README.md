# VPS Bandwidth Overage Calculator

**Live tool:** [tools.stackfreeks.com/tools/vps-bandwidth-calculator/](https://tools.stackfreeks.com/tools/vps-bandwidth-calculator/)

A free, browser-based tool that calculates whether your monthly traffic exceeds your VPS bandwidth allowance and shows estimated overage costs for **Vultr**, **Hetzner**, and **DigitalOcean**.

## Features

- **Two input modes** — enter your monthly traffic in GB directly, or estimate from visitor count + average page size + pages per visit
- **Per-provider results** — each cloud provider's included bandwidth and overage rate applied independently
- **Instant calculation** — results update live as you type, no submit button needed
- **EN / KO bilingual** — full English and Korean support via language toggle
- **Mobile responsive** — works on any screen size
- **No dependencies** — pure HTML, CSS, and vanilla JavaScript; no build tools, no frameworks

## Provider Data (as of 2025)

| Provider     | Included Bandwidth | Overage Rate     |
|-------------|-------------------|------------------|
| Vultr        | 1 TB / month      | $0.01 / GB       |
| Hetzner      | 20 TB / month     | ~$0.001 / GB     |
| DigitalOcean | 1 TB / month      | $0.01 / GB       |

> Hetzner overage rate is converted from €1 / TB. Prices are approximate; verify on provider websites.

## How It Works

**By Traffic (GB) tab:**
```
Enter monthly traffic (GB) → compare against each provider's included GB
```

**By Website tab:**
```
Total GB = monthly_visitors × pages_per_visit × (avg_page_size_KB / 1024 / 1024)
```
Example: 10,000 visitors × 3 pages × 500 KB = ~14.3 GB/month

**Overage cost:**
```
overage_GB = max(0, usage_GB - provider_included_GB)
overage_cost = overage_GB × provider_overage_rate
```

## Tech Stack

- Static HTML / CSS / JavaScript — no server required
- Hosted on **Cloudflare Pages** (auto-deploys from GitHub `main`)
- i18n via [`/shared/i18n.js`](../../shared/i18n.js)

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com) — a collection of free developer and server tools built for speed and simplicity.
