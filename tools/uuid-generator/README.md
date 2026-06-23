# UUID Generator

**Live tool:** [tools.stackfreeks.com/tools/uuid-generator/](https://tools.stackfreeks.com/tools/uuid-generator/)

A free, browser-based UUID v4 generator. No sign-up, no server round-trips — everything runs locally in your browser using the Web Crypto API.

## Features

- **Single generate** — one click to produce a fresh UUID v4 displayed in a large, readable box
- **Bulk generate** — generate 1–100 UUIDs at once with a scrollable list
- **Uppercase toggle** — switch between lowercase (default) and uppercase hex characters
- **Braces toggle** — wrap the UUID in `{...}` for compatibility with Microsoft tools (GUID format)
- **One-click copy** — copy individual UUIDs or the entire bulk list as newline-separated text
- **Bilingual UI** — English / 한국어 toggle (EN default, KO available)

## Technology

| Concern | Implementation |
|---|---|
| UUID generation | `crypto.randomUUID()` (Web Crypto API) |
| Clipboard | `navigator.clipboard.writeText()` |
| i18n | `/shared/i18n.js` + `window.SF_PAGE_I18N` |
| Styling | Pure CSS with design token variables |
| Build | None — static HTML/CSS/JS only |

## UUID v4 Primer

UUID v4 follows [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122) (updated by RFC 9562). Format:

```
xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
```

- Position 13 is always `4` (version indicator)
- Position 17 is `8`, `9`, `a`, or `b` (variant bits)
- The remaining **122 bits are cryptographically random**
- Collision probability ≈ 1 in 5.3 × 10³⁶

## File Structure

```
tools/uuid-generator/
├── index.html   # Complete tool (all HTML/CSS/JS inline)
└── README.md    # This file
```

## Part of StackFreeks Tools

Built as part of the [StackFreeks Tools](https://tools.stackfreeks.com) suite — free developer utilities focused on server, VPS, and infrastructure workflows.
