# SVG to PNG Converter

A free, browser-based tool that converts SVG files to PNG at custom export resolutions (1x, 2x, 4x). No account, no upload — everything runs locally in the browser using the Canvas API.

**Live:** https://tools.stackfreeks.com/tools/svg-to-png/

## Features

- **Custom scale** — export at 1x, 2x, or 4x the SVG's native dimensions
- **Transparent or white background** — choose per export
- **Batch support** — drag and drop multiple SVG files at once
- **Preview thumbnails** — checkered background shows transparency clearly
- **Dimension display** — shows original SVG size → output PNG size in pixels
- **Download All** — one click to grab all converted files
- **Bilingual** — English / Korean (EN/KO toggle)

## How It Works

1. User selects one or more `.svg` files (click or drag & drop)
2. `FileReader` reads each SVG as text
3. The tool parses `width`/`height` attributes or `viewBox` from the SVG source
4. Creates a `Blob` URL → loads into `new Image()` → draws onto `<canvas>` at the chosen scale
5. `canvas.toDataURL('image/png')` produces the final PNG
6. Download link is generated per file; white background is applied via `ctx.fillRect` before drawing if selected

## Tech Stack

- Pure vanilla JavaScript — no dependencies
- HTML5 Canvas API for raster rendering
- FileReader API for local file access
- DOMParser for SVG dimension extraction
- Blob URL + `<a download>` for file downloads

## SEO Keywords

- svg to png
- convert svg to png online
- svg to png free
- svg to png transparent background
- svg to png high resolution

## Part of StackFreeks Tools

This tool is part of the [StackFreeks Tools](https://tools.stackfreeks.com) collection — free developer utilities for server, VPS, and web workflows.
