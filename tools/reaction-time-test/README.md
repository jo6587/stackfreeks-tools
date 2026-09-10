# Reaction Time Test

> Live: https://tools.stackfreeks.com/tools/reaction-time-test/

A Human Benchmark style reaction time test — click when the box turns green and see how fast your reflexes are.

## Features

- Full-width click/tap area that turns red ("Wait for green…") then green ("Click!") after a random 1.2–4s delay
- Early-click detection with a "Too soon!" restart
- Millisecond timing via `performance.now()`
- 5 attempts, then average (big number), best attempt, per-attempt list, and a qualitative reflex band with context
- Remembers your best average in `localStorage` (`rt-best`), shown as "Your best"
- Works with mouse and touch (`pointerdown`), keyboard-activatable
- Bilingual EN/KO, how-to guide, FAQ, JSON-LD (WebApplication + FAQPage)

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
