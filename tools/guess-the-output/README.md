# Guess the Output — JavaScript Quiz

> Live: https://tools.stackfreeks.com/tools/guess-the-output/

A short JavaScript quiz built from 18 famous "guess the output" gotchas — type
coercion, hoisting, the temporal dead zone, `var`-in-loop closures, `this`
binding, `typeof` quirks, `parseInt` radix and microtask ordering. Pick an
answer, see which rule produced it.

## Features

- 18 hand-verified snippets, one correct output out of four
- Instant feedback: correct answer green, wrong pick red, plus a 1–2 sentence explanation
- Live score, current streak and progress (Q n / 18)
- End screen with score/18, a result band, and a `localStorage` personal best (`gto-best`)
- Full EN / KO bilingual UI (dynamic text re-renders on language toggle)
- Snippets are shown as text only and never `eval()`'d — expected outputs are constants

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
