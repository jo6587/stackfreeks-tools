# Verbal Memory Test

> Live: https://tools.stackfreeks.com/tools/verbal-memory-test/

Human Benchmark style verbal memory game: words appear one at a time and you mark each one SEEN or NEW. Three lives, score is how many words you correctly remember.

## Features

- Single-word prompt with SEEN / NEW judgement
- Pool of ~240 common English words, growing `seen` Set
- Weighted next-word pick (repeat probability ramps 30% → 60% as the seen list grows)
- 3 lives (♥♥♥), live score, game-over summary with context
- Best score saved in `localStorage` (`verbmem-best`), try/catch guarded
- Keyboard shortcuts: Left / K = NEW, Right / L = SEEN
- EN/KO bilingual UI (English word list by design — the standard test)
- Mobile responsive, no external libraries

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
