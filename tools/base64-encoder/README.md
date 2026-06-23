# Base64 Encoder / Decoder

**Live tool:** https://tools.stackfreeks.com/tools/base64-encoder/

A free, browser-only Base64 encoding and decoding tool. No server, no upload, no install — everything runs locally in your browser.

## Features

- **Text Encode / Decode** — Live two-panel layout: type plain text on the left, Base64 appears on the right (and vice versa). Handles Unicode correctly via `encodeURIComponent` + `escape` pattern.
- **File → Base64** — Drag and drop or click to select any file (image, PDF, binary). Outputs a Base64 data URL. Toggle between full data URL (`data:mime;base64,...`) and raw Base64 string. Shows file name, MIME type, and file size.
- **Base64 → File** — Paste a Base64 string (with or without the data URL prefix). Auto-detects MIME type from the prefix, or let the user choose from a dropdown. Decodes and triggers a browser download.

## Tech Stack

- Pure HTML / CSS / JavaScript — no frameworks, no build step
- Native browser APIs: `btoa()`, `atob()`, `FileReader`, `Blob`, `URL.createObjectURL()`
- Bilingual (EN / KO) via `/shared/i18n.js`

## File Structure

```
tools/base64-encoder/
├── index.html   # The tool — self-contained, no dependencies
└── README.md    # This file
```

## Keywords

base64 encode decode online, base64 encoder, base64 decoder, image to base64, file to base64, base64 data url
