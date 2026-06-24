# Image to Base64 Encoder

**Live tool:** [tools.stackfreeks.com/tools/image-to-base64/](https://tools.stackfreeks.com/tools/image-to-base64/)

Convert images to Base64 strings for use in HTML, CSS, or JSON — instantly, in your browser.

## Features

- Drag & drop or click-to-upload (JPG, PNG, GIF, WebP, SVG, ICO)
- Image preview with file info (name, type, original size, Base64 size)
- Four output formats:
  - **Raw Base64** — just the encoded string
  - **Data URL** — `data:image/png;base64,...`
  - **HTML `<img>` tag** — ready to paste into HTML
  - **CSS** — `background-image: url("data:...")`
- One-click Copy to clipboard
- Warning when image exceeds 100 KB
- Clear / Reset button
- EN / KO bilingual UI

## Tech

- Pure HTML / CSS / JavaScript — no build step, no server
- Hosted on Cloudflare Pages
- Encoding via browser's native `FileReader` API

## Part of

[StackFreeks Tools](https://tools.stackfreeks.com) — free developer tools for server & VPS workflows.
