# PX ↔ REM Converter

A free, browser-only tool for converting between CSS `px` and `rem` units — live, with no server required.

**Live URL:** https://tools.stackfreeks.com/tools/px-rem-converter/

## Features

- **Two-way conversion** — type px to get rem, or type rem to get px; updates on every keystroke
- **Adjustable base font size** — slider + number input, range 10–32px, default 16px
- **Live text preview** — renders "The quick brown fox…" at the current px size so you can see the scale visually
- **Common values table** — 19 common px sizes (8–96px) with their rem equivalents, recalculated instantly when the base changes
- **Copy button** — copies the rem value (with unit suffix) to clipboard
- **EN / KO bilingual** — full English and Korean UI via `/shared/i18n.js`
- **Responsive** — works on mobile and desktop
- **No build step** — pure static HTML/CSS/JS

## How it works

```
rem = px / base
px  = rem × base
```

Where `base` is the root font size (default: 16px).

## File structure

```
tools/px-rem-converter/
  index.html   — complete tool page
  README.md    — this file
```

## Part of StackFreeks Tools

Built for developers who work with responsive CSS and need a fast, no-friction unit converter.  
Site: https://tools.stackfreeks.com
