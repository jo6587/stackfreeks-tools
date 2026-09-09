# Game Server RAM Calculator

> Live: https://tools.stackfreeks.com/tools/game-server-ram-calculator/

Estimate dedicated game server RAM for Palworld, Valheim, ARK: Survival Ascended, Rust, Counter-Strike 2, and Project Zomboid from player slots, mods, and world scale — with a matched Vultr plan.

## Features

- Per-game heuristic: each game carries its own base RAM, per-player cost, and mod weighting
- Inputs: game, player slots, mods on/off + mod count, world/map scale
- Output: recommended RAM (GB), breakdown (base + per-player + mods), recommended CPU cores, matched Vultr Cloud Compute plan (rounded up)
- Transparent, single well-commented constants object keyed by game
- EN / KO bilingual (i18n toggle)

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
