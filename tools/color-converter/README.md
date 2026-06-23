# Color Converter

**Live URL:** https://tools.stackfreeks.com/tools/color-converter/

A free, browser-based color format converter that converts between HEX, RGB, and HSL in real time. No sign-up, no server — everything runs client-side.

## Features

- **Three-way live sync** — editing any field (HEX, RGB, or HSL) instantly updates the other two
- **Native color picker** — visual selection that stays in sync with all three formats
- **Color swatch preview** — large 160 px preview rectangle showing the current color with the HEX value centered
- **One-click copy** — copies the formatted string (`#rrggbb`, `rgb(r, g, b)`, or `hsl(h, s%, l%)`) to clipboard
- **8 preset swatches** — common web colors for quick loading
- **EN / KO bilingual** — full English and Korean UI via `/shared/i18n.js`
- **Mobile responsive** — works on all screen sizes

## Preset Colors

| Swatch | HEX |
|--------|-----|
| Red | `#ef4444` |
| Orange | `#f97316` |
| Yellow | `#eab308` |
| Green | `#22c55e` |
| Cyan | `#06b6d4` |
| Indigo | `#6366f1` |
| Purple | `#a855f7` |
| Pink | `#ec4899` |

## Conversion Math

- **HEX → RGB**: `parseInt(pair, 16)` for each channel pair
- **RGB → HEX**: `channel.toString(16).padStart(2, '0')`
- **RGB → HSL**: standard luminance formula with float rounding
- **HSL → RGB**: hue2rgb interpolation

HEX ↔ RGB is lossless. HSL may have ±1 rounding due to float math.

## Tech Stack

- Pure HTML / CSS / JS (no build step, no dependencies)
- Hosted on Cloudflare Pages (auto-deploy from `main` branch)
- Shared i18n: `/shared/i18n.js`

## Monetization

- Google AdSense slot reserved at top of page
- Vultr affiliate banner ($10/sign-up): `https://www.vultr.com/?ref=9907834-9J`
