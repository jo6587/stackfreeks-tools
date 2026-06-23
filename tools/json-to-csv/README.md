# JSON to CSV Converter

A free, browser-based tool to convert JSON arrays to CSV and CSV back to JSON — instantly, with no server or account required.

**Live:** https://tools.stackfreeks.com/tools/json-to-csv/

## Features

- **JSON → CSV**: Paste a JSON array of objects and get a properly formatted CSV with auto-detected headers.
- **CSV → JSON**: Paste CSV (with a header row) and get a formatted JSON array.
- Handles edge cases: nested objects (serialized as JSON string), null/undefined values (empty cell), arrays in values (semicolon-joined), quoted CSV fields containing commas.
- Row/column count info displayed after conversion.
- Copy to clipboard or download as `.csv` / `.json` file.
- Sample data buttons for quick testing.
- Bilingual UI: English + Korean (EN/KO toggle).

## Tech

Pure vanilla HTML/CSS/JavaScript — no dependencies, no build step, no server.

## Part of

[StackFreeks Tools](https://tools.stackfreeks.com) — a collection of free developer tools.
