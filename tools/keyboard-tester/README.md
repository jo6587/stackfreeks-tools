# Keyboard Tester

> Live: https://tools.stackfreeks.com/tools/keyboard-tester/

Test every key on your keyboard online. Press keys to light up an on-screen
layout, track which keys you've tested, and check for a stuck key, chatter, or
ghosting — all in the browser.

## Features

- On-screen keyboard rendered from a JS layout array, matched on `event.code`
  (physical position, layout-language independent)
- Layout presets: Full (104), TKL (87), 75%, 65%, 60%
- Live `event.key` / `event.code` / `event.keyCode` readout
- Persistent "tested" highlight + coverage counter (`42 / 104 keys tested`)
- Multi-key / rollover support — held keys stay active, so you can test ghosting
- `preventDefault()` on scroll/navigation keys while the tester is focused
- Stuck-key hint (held-too-long heuristic) and a mobile "use a physical keyboard"
  note
- Reset button clears tested state
- EN/KO bilingual UI via `/shared/i18n.js`

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
