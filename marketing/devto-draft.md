---
title: I built 47 free static dev tools with no backend — lessons learned
published: true
tags: webdev, showdev, devops, sideproject
---

<!-- dev.to 에디터에 이 파일 전체를 붙여넣으면 됨 (frontmatter 포함) -->

Over the past few weeks I shipped [47 free browser-based tools](https://tools.stackfreeks.com) for developers and sysadmins — cost calculators, config generators, converters. No backend, no build step, no framework. Just static HTML/CSS/JS on Cloudflare Pages.

Here's what I learned.

## Why static-only

Every "free online tool" site I used had the same problems: slow, ad-stuffed, and quietly shipping my input to a server somewhere. For 90% of dev utilities that's absurd — a chmod calculator does not need a database.

So I set one constraint: **everything runs client-side.** If a tool can't work with the network tab empty, it doesn't get built. Paste a JWT into the [JWT decoder](https://tools.stackfreeks.com/tools/jwt-decoder/) and nothing leaves your browser. Load a tool once and it works offline.

That constraint turned out to be a feature, not a limitation:

- **Hosting costs $0.** Cloudflare Pages serves static files for free, with a CDN included.
- **Nothing to maintain.** No server to patch, no dependencies to bump, no 3am pages.
- **Deploys are `git push`.** Build pipeline: none.

## Lesson 1: one HTML file per tool beats a framework

Each tool is a single self-contained `index.html` — inline CSS, inline JS. I expected this to get painful around tool #10. It never did.

What I gained: zero shared state, zero build config, and any tool can be rewritten from scratch in an afternoon without touching the others. What I lost: some duplication (design tokens are copy-pasted into every file). I'll take that trade every time for a project like this — duplication is cheaper than the wrong abstraction.

## Lesson 2: niche tools beat generic tools

My JSON formatter and password generator will never rank on Google — they compete with a hundred DR-90 sites. The tools that actually get found are the weirdly specific ones:

- [Game Server Cost Calculator](https://tools.stackfreeks.com/tools/game-server-cost-calculator/) — RAM and VPS cost by player count for Minecraft, Valheim, Rust
- [Fail2ban Jail Generator](https://tools.stackfreeks.com/tools/fail2ban-jail-generator/) — pick services, get a ready `jail.local`
- [Docker RAM Calculator](https://tools.stackfreeks.com/tools/docker-ram-calculator/) — size containers before picking a VPS plan

If I started over, I'd skip the generic utilities entirely and build only tools where I can name the exact person searching for it.

## Lesson 3: static doesn't mean SEO-exempt

Pure-JS tool pages look "thin" to crawlers. What moved the needle:

- Real written content on every page: a how-to section and an FAQ, not just the widget
- `FAQPage` + `WebApplication` JSON-LD on every tool
- Aggressive internal cross-linking — every tool links 3 related tools, so there are no orphan pages
- Pairing each niche tool with a matching blog article that targets the informational version of the query

## Lesson 4: i18n in ~60 lines of vanilla JS

The site is bilingual (EN/KO). I almost reached for a library, then wrote a tiny shared script instead: `data-i18n` attributes for short strings, `.lang-en` / `.lang-ko` blocks for long content, a toggle that flips a class on `<html>` and persists to `localStorage`. Sixty lines, no dependencies, works on every page.

## The stack, in full

- HTML/CSS/JS (vanilla, no build)
- Cloudflare Pages (free tier) + Cloudflare Web Analytics (free, no cookies)
- GitHub for deploys — push to `main`, live in ~1 minute

That's it. That's the whole stack.

## What's next

More long-tail calculators, and following the search data to decide what to build instead of guessing. The full collection is at [tools.stackfreeks.com](https://tools.stackfreeks.com) — all free, no signup, nothing tracked beyond a page-view counter.

If you've built something similar (or think static-only is a mistake), I'd love to hear about it in the comments. And if there's a niche dev tool you wish existed — tell me, I might just build it.
