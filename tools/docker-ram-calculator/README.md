# Docker RAM Calculator

**URL:** https://tools.stackfreeks.com/tools/docker-ram-calculator/

Estimate the total RAM needed for a set of Docker containers and get a recommended Vultr VPS plan — no sign-up, no server, pure browser.

## What it does

- Add containers one by one with the "Add Container" button
- Each row: name, image preset (or custom MB), and replica count
- Live calculation including OS overhead (+512 MB), Docker daemon overhead (+256 MB), and a 20% safety buffer
- Total recommended RAM is rounded up to the nearest power-of-2 GB (1 / 2 / 4 / 8 / 16 / 32 GB)
- Vultr Cloud Compute plans table with the matching plan highlighted in green
- "Get this plan on Vultr" CTA with affiliate link

## Image presets

| Image          | RAM estimate |
|----------------|-------------|
| nginx          | 50 MB       |
| Apache         | 100 MB      |
| MySQL          | 400 MB      |
| PostgreSQL     | 200 MB      |
| Redis          | 50 MB       |
| MongoDB        | 300 MB      |
| Node.js app    | 150 MB      |
| Python app     | 120 MB      |
| WordPress      | 200 MB      |
| Elasticsearch  | 1000 MB     |
| Custom         | user input  |

## Calculation formula

```
Container RAM  = Σ (image_mb × replicas)
Buffer         = (Container RAM + 512 + 256) × 0.20
Raw total      = Container RAM + 512 + 256 + Buffer
Recommended GB = next power of 2 ≥ (Raw total / 1024)
```

## Tech

- Pure HTML / CSS / JavaScript — no build step, no dependencies
- Hosted on Cloudflare Pages (auto-deploy from `main` branch)
- EN / KO bilingual via `/shared/i18n.js`

## Monetization

- Vultr affiliate CTA ($10 commission per sign-up): `https://www.vultr.com/?ref=9907834-9J`
- AdSense slot placeholder at the top of the page
