# StackFreeks Tools

Free browser-based tools — no account, no backend, no install.

Live at [tools.stackfreeks.com](https://tools.stackfreeks.com)

---

## What's here

Small, single-purpose tools that do one thing and get out of the way. Everything runs client-side, so nothing gets uploaded to a server.

**Image**
- [HEIC to JPG](https://tools.stackfreeks.com/tools/heic-to-jpg/) — batch convert iPhone photos
- [WebP to JPG](https://tools.stackfreeks.com/tools/webp-to-jpg/) — canvas API, no library
- [SVG to PNG](https://tools.stackfreeks.com/tools/svg-to-png/) — 1x / 2x / 4x export
- [Image Compressor](https://tools.stackfreeks.com/tools/image-compressor/) — no size limit, no watermark
- [EXIF Remover](https://tools.stackfreeks.com/tools/exif-remover/) — strips GPS + metadata via canvas

**Developer**
- [JSON Formatter](https://tools.stackfreeks.com/tools/json-formatter/) — format, minify, validate with syntax highlighting
- [JSON to CSV](https://tools.stackfreeks.com/tools/json-to-csv/) — two-way conversion
- [Base64 Encoder/Decoder](https://tools.stackfreeks.com/tools/base64-encoder/) — text and file support
- [Password Generator](https://tools.stackfreeks.com/tools/password-generator/) — crypto.getRandomValues(), strength meter
- [QR Code Generator](https://tools.stackfreeks.com/tools/qr-code-generator/) — PNG + SVG download, no watermark
- [Unix Timestamp Converter](https://tools.stackfreeks.com/tools/timestamp-converter/) — live clock, two-way
- [Cron Expression Builder](https://tools.stackfreeks.com/tools/cron-builder/) — visual + manual, next 5 runs preview
- [Word Counter](https://tools.stackfreeks.com/tools/word-counter/) — live stats, keyword density, reading time
- [Text Case Converter](https://tools.stackfreeks.com/tools/text-case-converter/) — 10 formats: camelCase, snake_case, kebab-case, etc.
- [Hash Generator](https://tools.stackfreeks.com/tools/hash-generator/) — MD5, SHA-1, SHA-256, SHA-512 from text or file
- [URL Encoder/Decoder](https://tools.stackfreeks.com/tools/url-encoder/) — encodeURI, encodeURIComponent, cheat sheet
- [Chmod Calculator](https://tools.stackfreeks.com/tools/chmod-calculator/) — interactive permission grid, presets, octal ↔ symbolic
- [JWT Decoder](https://tools.stackfreeks.com/tools/jwt-decoder/) — header/payload/expiry, claims table, no verification
- [.htpasswd Generator](https://tools.stackfreeks.com/tools/htpasswd-generator/) — bcrypt, MD5-APR, SHA1, client-side only
- [Diff Checker](https://tools.stackfreeks.com/tools/diff-checker/) — LCS-based line diff, side-by-side and unified view
- [IP Subnet Calculator](https://tools.stackfreeks.com/tools/subnet-calculator/) — CIDR, host range, broadcast, subnet split helper
- [OG Meta Tag Generator](https://tools.stackfreeks.com/tools/og-meta-generator/) — live Google/Facebook/Twitter previews
- [UUID Generator](https://tools.stackfreeks.com/tools/uuid-generator/) — crypto.randomUUID(), bulk up to 100, uppercase & braces options
- [Hex/RGB/HSL Color Converter](https://tools.stackfreeks.com/tools/color-converter/) — three-way live conversion, color picker, preset swatches
- [Number Base Converter](https://tools.stackfreeks.com/tools/base-converter/) — binary/octal/decimal/hex four-way conversion, bit-length info
- [Lorem Ipsum Generator](https://tools.stackfreeks.com/tools/lorem-ipsum/) — words/sentences/paragraphs, classic opening toggle
- [Markdown Previewer](https://tools.stackfreeks.com/tools/markdown-previewer/) — live split-pane, marked.js GFM, toolbar, copy HTML
- [px ↔ rem Converter](https://tools.stackfreeks.com/tools/px-rem-converter/) — adjustable base size, reference table, live text preview
- [Regex Tester](https://tools.stackfreeks.com/tools/regex-tester/) — live match highlighting, g/i/m/s flags, capture groups, cheat sheet

**Server / VPS**
- [VPS Cost Calculator](https://tools.stackfreeks.com/tools/vps-cost-calculator/) — Vultr / Hetzner / DigitalOcean
- [VPS Bandwidth Calculator](https://tools.stackfreeks.com/tools/vps-bandwidth-calculator/) — overage cost estimator

---

## Stack

Pure HTML/CSS/JS. No framework, no build step, no Node. Deployed on Cloudflare Pages — push to main and it's live.

External libraries are loaded from CDN only when needed (heic2any, qrcode.js, browser-image-compression). Everything else is vanilla.

---

## Structure

```
tools/[slug]/index.html   one file per tool
shared/i18n.js            EN/KO language toggle used across all pages
index.html                homepage with tool directory
sitemap.xml
```

---

Built with [Claude Code](https://claude.ai/code) — agentic coding from tool design to deployment.

---

Part of [stackfreeks.com](https://stackfreeks.com)
