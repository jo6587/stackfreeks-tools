# QR Code Generator

**URL:** https://tools.stackfreeks.com/tools/qr-code-generator/

A free, no-watermark QR code generator that runs entirely in the browser. No account required, no usage limits, no hidden fees.

## Features

- **Live preview** — QR code regenerates as you type (300ms debounce)
- **Size options** — Small (256px) / Medium (512px) / Large (1024px)
- **Error correction levels** — L (7%) / M (15%) / Q (25%) / H (30%)
- **Custom colors** — Foreground and background color pickers
- **Download PNG** — Full-resolution canvas export via `canvas.toBlob()`
- **Download SVG** — Vector export via `QRCode.toString()` for infinite scaling
- **No watermark** — Clean output files, ready to use anywhere
- **Bilingual UI** — English / Korean toggle (EN/KO)
- **Fully static** — No server, no build step, pure HTML/CSS/JS

## Technology

- [qrcode.js v1.5.4](https://www.npmjs.com/package/qrcode) via jsDelivr CDN
- `/shared/i18n.js` for EN/KO language toggling
- Canvas API for PNG export
- Blob + object URL for file downloads

## Target Keywords

- qr code generator
- free qr code generator no watermark
- qr code maker online

## File Structure

```
tools/qr-code-generator/
├── index.html   # Tool page (all CSS/JS inline)
└── README.md    # This file
```

## Monetization

- Google AdSense slot reserved at top (`<!-- ADSENSE_SLOT_TOP -->`)
- Vultr affiliate banner at bottom (`https://www.vultr.com/?ref=9907834-9J`)
