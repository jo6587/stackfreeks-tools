# Number Memory Test

> Live: https://tools.stackfreeks.com/tools/number-memory-test/

A Human Benchmark style number memory test. A number flashes on screen, then you type it
back from memory. Each level adds one more digit, so your final level equals the number of
digits you can hold in short-term memory (your digit span).

## Features

- Level N shows an N-digit number (level 1 = 1 digit, level 2 = 2 digits, …)
- Visible countdown bar; display time scales with level (`2000 + level * 1000` ms, tunable)
- Type-back input with `inputmode="numeric"`, submit on Enter or button
- One wrong digit ends the run; game-over screen shows the target number vs. what you typed
- Context line: "The average person remembers 7 digits — Miller's Law (7 ± 2)"
- Best level persisted in `localStorage` (`nummem-best`), shown as "Your best: level N"
- Bilingual EN / KO via `/shared/i18n.js`
- How-to guide + 5-question FAQ + JSON-LD (WebApplication + FAQPage)

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
