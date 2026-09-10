# Sequence Memory Test

> Live: https://tools.stackfreeks.com/tools/sequence-memory-test/

Remember the pattern of tiles that flash on a 3×3 grid, then repeat it back. Each level adds one more tile, so the test measures how long a visuospatial sequence you can recall.

## Features

- Human Benchmark style 3×3 grid, sequence grows by one tile per level
- Playback plays the full sequence, then adds one new random tile
- Input disabled during playback; tap feedback flash during your turn
- Wrong tile ends the run; game-over shows the level reached and context ("The average score is 6")
- Best level saved locally via `localStorage` (`seqmem-best`), with try/catch fallback
- Mouse + touch via `pointerdown`; all timers cleared on reset / game over
- EN/KO bilingual (shared i18n), how-to guide, FAQ, JSON-LD (WebApplication + FAQPage)

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
