# Markdown Previewer

A live, split-pane Markdown previewer that runs entirely in the browser. No install, no server, no dependencies beyond a single CDN script.

**Live tool:** [tools.stackfreeks.com/tools/markdown-previewer/](https://tools.stackfreeks.com/tools/markdown-previewer/)

## Features

- **Live preview** — rendered output updates on every keystroke
- **Split-pane layout** — editor on the left, preview on the right (stacked on mobile)
- **Quick-insert toolbar** — one-click buttons for Bold, Italic, Code, H1–H3, Link, Image, Blockquote, UL, OL, HR
- **Copy HTML** — copies the rendered HTML output to clipboard
- **Clear** — resets editor and preview in one click
- **Stats bar** — live word count and character count
- **EN / KO toggle** — full bilingual UI (English + Korean)
- **Dark theme** — matches the StackFreeks design system
- **GFM support** — GitHub Flavored Markdown via [marked.js](https://marked.js.org/)

## Tech Stack

- Pure HTML / CSS / JavaScript — zero build step
- [marked.js](https://cdn.jsdelivr.net/npm/marked/marked.min.js) via jsDelivr CDN
- `/shared/i18n.js` for EN/KO language toggle

## File Structure

```
tools/markdown-previewer/
├── index.html   # Tool page (self-contained)
└── README.md    # This file
```

## Local Development

Open `index.html` directly in a browser, or serve from the repo root:

```bash
npx serve .
# then visit http://localhost:3000/tools/markdown-previewer/
```

## License

Part of the [StackFreeks Tools](https://tools.stackfreeks.com) open portfolio.
