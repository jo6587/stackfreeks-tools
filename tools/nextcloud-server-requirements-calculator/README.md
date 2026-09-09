# Nextcloud Server Requirements Calculator

> Live: https://tools.stackfreeks.com/tools/nextcloud-server-requirements-calculator/

Estimate the server hardware a Nextcloud instance needs — vCPU, RAM, total storage with overhead, PHP-FPM worker count, and whether to add Redis or a dedicated database — from user count, concurrency, and workload profile. Sizing is keyed to peak concurrent PHP requests rather than raw user count, and the result is matched to a Vultr plan (rounded up for headroom).

## Features

- Inputs: total users, expected concurrent users (or auto = ~10% of total), average storage per user, workload profile (light file sync / office + groupware / media + heavy apps)
- Toggles for preview generation and full-text search (both affect RAM and CPU)
- Outputs: recommended vCPU, RAM (GB), total storage (GB/TB with overhead), PHP-FPM worker count
- Redis and dedicated-database recommendations based on concurrency and scale
- Matched Vultr plan, rounded up on both RAM and vCPU
- Transparent heuristic anchored to published Nextcloud sizing guidance (128 MB min / 512 MB recommended RAM per PHP process; 2-4 GB for <10 users, 8-16 GB for 10-100, 32 GB+ for 100+)
- All constants live in one clearly commented `NC` object in the page source
- EN / KO bilingual (shared `/shared/i18n.js` toggle)

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
