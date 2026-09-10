# Regex Golf

> Live: https://tools.stackfreeks.com/tools/regex-golf/

A browser regex golf game — write the shortest regular expression that matches every string in one list and rejects every string in the other, across 12 levels of increasing difficulty.

## Features

- 12 bundled levels: literal substrings → anchors → character classes → alternation → quantifiers → lookahead → backreferences
- Live pass/fail (✓ / ✗) feedback on every test string as you type
- Golf scoring: character count per solved level, total characters, average per level
- `i` / `m` / `g` flag toggles, with graceful "invalid regex" handling (never throws)
- End-of-run summary and a locally stored best run (`localStorage`, key `regexgolf-best`)
- Full EN / KO bilingual UI, Korean rendered from first paint on `/ko/` pages

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Uses the browser's native `RegExp` engine (JavaScript / ECMAScript flavor)
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
