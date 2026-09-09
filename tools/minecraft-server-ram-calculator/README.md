# Minecraft Server RAM Calculator

> Live: https://tools.stackfreeks.com/tools/minecraft-server-ram-calculator/

Estimate how much RAM a self-hosted Minecraft server needs from server type, peak
players, plugin/mod count, and view distance. Outputs a memory breakdown, a
recommended `-Xms`/`-Xmx` pair, and a matching Vultr plan (rounded up for OS + JVM
headroom).

## Features

- Five server profiles: Vanilla, Paper/Spigot, Forge, Fabric, modpack-heavy
- Transparent heuristic with all tunable constants in one commented `TUNABLE` object
- Breakdown: base JVM + server, per-player, per-plugin/mod, world cache, OS headroom
- Recommended `-Xms`/`-Xmx` flags you can paste into a start script
- Suggested Vultr Cloud Compute tier with vCPU and price
- EN / KO bilingual (shared `/shared/i18n.js`)
- WebApplication + FAQPage JSON-LD

## Heuristic (GB, tunable)

| Component        | Value                                                              |
| ---------------- | ----------------------------------------------------------------- |
| Base heap        | vanilla 2.0, paper 1.5, forge 3.0, fabric 2.5, modpack 6.0        |
| Per player       | 0.1 (~1 GB per 10 players)                                        |
| Per plugin       | 0.05 (Paper/Spigot)                                               |
| Per mod          | 0.125 (Forge/Fabric), 0.15 (modpack)                             |
| World cache      | 0.5 base + 0.12 per view-distance chunk above 10                  |
| OS + JVM headroom| 1.0, or 2.0 once heap >= 6 GB (added outside the Java heap)        |

Heap is rounded up to the nearest 0.5 GB; recommended RAM is heap + headroom,
matched up to the next Vultr tier.

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
