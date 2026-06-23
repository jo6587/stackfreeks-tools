# WebP to JPG Converter

**Live:** https://tools.stackfreeks.com/tools/webp-to-jpg/

A free, browser-based tool that converts WebP images to JPG instantly — no upload, no account, no server required.

## Features

- **Batch conversion** — select or drag multiple `.webp` files at once
- **Quality slider** — adjust JPG quality from 70% to 100% (default: 92%)
- **Live preview** — thumbnail shown alongside original vs. converted file size in KB
- **Download All** — one-click download when 2+ files are ready
- **EN / KO bilingual UI** — language toggle with localStorage persistence
- **Privacy-first** — all processing happens in your browser via Canvas API

## How it works

1. Files are read with `FileReader` as data URLs
2. Each WebP is drawn into a hidden `<canvas>` element (with white background fill for transparency)
3. `canvas.toDataURL('image/jpeg', quality)` produces the JPG output
4. A download link is generated client-side — nothing is sent to any server

## Tech stack

- Pure HTML / CSS / JavaScript (no frameworks, no build step)
- Canvas API for image conversion
- Cloudflare Pages (static hosting)

## SEO targets

- `webp to jpg`
- `convert webp to jpg online free`
- `webp to jpeg`
