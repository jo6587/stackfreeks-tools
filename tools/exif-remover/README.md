# EXIF Data Remover

**Live tool:** https://tools.stackfreeks.com/tools/exif-remover/

A free, browser-only tool that strips GPS location, camera metadata, and all EXIF data from JPEG, PNG, and WebP photos. No server upload required — all processing happens locally in the browser using the HTML5 Canvas API.

## How it works

When an image is drawn onto an HTML5 `<canvas>` element and exported via `canvas.toDataURL()`, the browser discards all EXIF metadata from the output. This is a reliable, zero-dependency technique that works in every modern browser.

**Processing pipeline:**

1. User selects one or more image files via click or drag & drop
2. `FileReader` reads each file as a Data URL
3. Image is loaded into a `new Image()` object
4. Image is drawn onto a `<canvas>` sized to match the original dimensions
5. Canvas is exported: `toDataURL('image/jpeg', 0.95)` for JPG inputs, `toDataURL('image/png')` for PNG inputs
6. The resulting Data URL contains zero EXIF metadata

## What gets removed

- GPS Location (latitude, longitude, altitude)
- Camera Model & Serial Number
- Date & Time taken
- Aperture, ISO, Shutter Speed
- Software Used
- Author / Copyright
- Embedded thumbnail preview

## Features

- Batch processing — multiple files at once
- "Download All" button for bulk export
- Before/after file size display
- EN / KO bilingual UI
- Mobile responsive
- Zero external dependencies

## Privacy

Photos are never uploaded to any server. All processing is done entirely within the user's browser using standard Web APIs.

## Tech stack

- Pure HTML / CSS / JavaScript
- HTML5 Canvas API for EXIF stripping
- FileReader API for file ingestion
- `<a download>` for file export
- `/shared/i18n.js` for EN/KO language toggle

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com) — free browser-based tools for developers and server admins.
