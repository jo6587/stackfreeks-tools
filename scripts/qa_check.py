#!/usr/bin/env python3
"""Step 1.5 QA — deterministic checks for a tool page (what a script judges better than an LLM).
The judgment part (acceptance criteria, real usefulness vs competitors) is agents/tool-critic.md.

  python scripts/qa_check.py <slug> [<slug> ...]   # exit 1 on any FAIL
  python scripts/qa_check.py --all                 # every tool (survey; old tools may predate rules)
  python scripts/qa_check.py --push                # pre-push gate: tools changed since origin/main
  python scripts/qa_check.py --selftest            # the parser-backed rules check themselves

--push also requires output/<slug>/qa-report.md starting with "QA: PASS" and newer than
tools/<slug>/index.html for every tool *added* in the push. Installed as .git/hooks/pre-push.
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://tools.stackfreeks.com"
VULTR_REF = "https://www.vultr.com/?ref=9907834-9J"
HANGUL = re.compile(r"[가-힣]")
# anchor on the ASSIGNMENT: pages also read window.SF_PAGE_I18N inside guards
PAGE_I18N_ASSIGN = re.compile(r"SF_PAGE_I18N\s*=\s*\{")
_post_urls = None

# tokens that name a background/surface — never legal as a text colour (design-guide §2)
SURFACE_TOKENS = ("--success", "--danger-bg", "--warning-bg", "--accent-soft", "--accent-soft-2",
                  "--surface", "--surface-2", "--bg", "--border", "--border-2")
COLOR_DECL = re.compile(r"(?<![-\w])color\s*:\s*var\((--[\w-]+)\)")

# design-guide §8: no emoji / unicode-symbol icons.
# EMOJI_ANY — emoji presentation, banned anywhere in <body> (never body wording here).
# MARK_SCOPED — plain marks, banned only as an element's sole content or inside a button/label,
#   so "✓ Valid JSON — 3 keys" and "6 × 1024" in a sentence stay legal (see §8 for the limits).
EMOJI_ANY = re.compile(r"[\U0001F000-\U0001FAFFℹ⏰✅⚠⚡❌]")
MARK_SCOPED = re.compile(r"[✓✕✖✗✎▲▼★☆♥]")
CONTROLISH = re.compile(r"\b(btn|button|tab|label|chip|toggle|pill|remove|close)\b")


def blog_post_urls():
    """stackfreeks.com post URLs, or None if the sitemap can't be fetched."""
    global _post_urls
    if _post_urls is None:
        try:
            req = urllib.request.Request("https://stackfreeks.com/post-sitemap.xml", headers={"User-Agent": "sf-qa"})
            xml = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
            _post_urls = {u.rstrip("/") for u in re.findall(r"<loc>(.*?)</loc>", xml)}
        except Exception:
            _post_urls = set()
    return _post_urls or None


def contrast(a: str, b: str) -> float:
    """WCAG contrast ratio of two #rrggbb colors."""
    def lum(h):
        c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def _scan_js(s: str, i: int):
    """Walk JS source from i, yielding (index, nesting depth) for chars OUTSIDE string
    literals only. Stops when nesting falls below the starting level (the closing brace)."""
    q, depth = None, 0
    while i < len(s):
        c = s[i]
        if q:
            if c == "\\":
                i += 2
                continue
            if c == q:
                q = None
            i += 1
            continue
        if c in "\"'`":
            q = c
            yield i, depth  # a quoted object key starts here
        elif c in "{[(":
            depth += 1
        elif c in "}])":
            depth -= 1
            if depth < 0:
                return
        else:
            yield i, depth
        i += 1


def _obj_keys(src: str, open_brace: int) -> list[str]:
    """Top-level keys of the object literal whose '{' is at open_brace."""
    keys = []
    for i, depth in _scan_js(src, open_brace + 1):
        if depth:
            continue
        m = re.match(r"([A-Za-z_$][\w$]*|\"[^\"]*\"|'[^']*')\s*:", src[i:])
        if m and (i == 0 or not re.match(r"[\w$.]", src[i - 1])):
            keys.append(m.group(1).strip("\"'"))
    return keys


def page_i18n_halves(html: str):
    """{'en': [keys], 'ko': [keys]} from SF_PAGE_I18N, or None if the page has none."""
    m = PAGE_I18N_ASSIGN.search(html)
    if not m:
        return None
    outer = m.end() - 1
    out = {}
    for j, depth in _scan_js(html, outer + 1):
        if depth:
            continue
        m = re.match(r"(en|ko)\s*:\s*\{", html[j:])
        if m and not re.match(r"[\w$]", html[j - 1]):
            out[m.group(1)] = _obj_keys(html, html.index("{", j))
    return out


def glyph_fails(soup) -> list[str]:
    """design-guide §8: emoji anywhere, plain marks as an icon (sole content / in a control)."""
    body = soup.body
    out = []
    if not body:
        return out
    for el in body.find_all(True):
        own = "".join(c for c in el.children if isinstance(c, str))
        label = f"<{el.name}{'.' + '.'.join(el.get('class')) if el.get('class') else ''}>"
        for m in set(EMOJI_ANY.findall(own)):
            out.append(f"emoji {m!r} in {label} — use a /shared/icons.svg sprite icon (design-guide §8)")
        marks = set(MARK_SCOPED.findall(own))
        if not marks:
            continue
        sole = not MARK_SCOPED.sub("", el.get_text()).strip()
        control = el.name in ("button", "label") or CONTROLISH.search(" ".join(el.get("class") or []))
        if sole or control:
            where = "sole content of" if sole else "control"
            out.append(f"symbol icon {''.join(sorted(marks))!r} as {where} {label} — "
                       f"use a sprite icon (design-guide §8)")
    return out


def check(slug: str) -> tuple[list[str], list[str]]:
    d = ROOT / "tools" / slug
    page = d / "index.html"
    if not page.exists():
        return [f"{page} missing"], []
    html = page.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    # design checks below also cover linked local stylesheets (/shared/sf.css), read as if inline
    for link in soup.find_all("link", rel="stylesheet", href=True):
        sheet = ROOT / link["href"].lstrip("/")
        if link["href"].startswith("/") and sheet.is_file():
            html += f"\n<style>{sheet.read_text(encoding='utf-8')}</style>"
    url = f"{BASE}/tools/{slug}/"
    fails, warns = [], []

    def need(ok, msg):
        if not ok:
            fails.append(msg)

    # structure
    need(soup.select_one('a[data-i18n="nav_back"]'), 'no <a data-i18n="nav_back">')
    need(not re.search(r"\.nav-back\s*\{[^}]*var\(--text-3\)", html), ".nav-back uses var(--text-3) (unreadable)")
    need("<!-- ADSENSE_SLOT_TOP -->" in html, "no <!-- ADSENSE_SLOT_TOP --> comment")
    need(soup.select_one(".lang-en") and soup.select_one(".lang-ko"), "hero missing .lang-en / .lang-ko block")
    i18n = html.find('<script src="/shared/i18n.js"></script>')
    need(i18n != -1, 'no <script src="/shared/i18n.js"></script>')
    pm = PAGE_I18N_ASSIGN.search(html)
    page_i18n = pm.start() if pm else -1
    need(page_i18n == -1 or page_i18n < i18n, "SF_PAGE_I18N defined after i18n.js loads")

    # SF_PAGE_I18N EN/KO parity — a key missing from one half leaves that language untranslated
    halves = page_i18n_halves(html)
    if halves is not None:
        need("en" in halves and "ko" in halves,
             f"SF_PAGE_I18N needs both en: and ko: halves (have {sorted(halves)})")
        if {"en", "ko"} <= set(halves):
            for a, b in (("en", "ko"), ("ko", "en")):
                gone = sorted(set(halves[a]) - set(halves[b]))
                need(not gone, f"SF_PAGE_I18N {b}: missing keys present in {a}: {gone}")
            for lang in ("en", "ko"):
                dup = sorted({k for k in halves[lang] if halves[lang].count(k) > 1})
                need(not dup, f"SF_PAGE_I18N {lang}: duplicate keys {dup}")

    # SEO
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    need(" — " in title and title.endswith(" | StackFreeks"), f"title format: {title!r}")
    desc = soup.find("meta", attrs={"name": "description"})
    desc = desc.get("content", "") if desc else ""
    need(0 < len(desc) <= 160, f"meta description length {len(desc)} (Google truncates past ~160)")
    if len(desc) > 140:
        warns.append(f"meta description length {len(desc)} (target ≤140)")
    for attrs in ({"property": "og:description"}, {"name": "twitter:description"}):
        m = soup.find("meta", attrs=attrs)
        n = len(m.get("content", "")) if m else 0
        need(n <= 160, f"{next(iter(attrs.values()))} length {n} (>160)")
        if n > 140:
            warns.append(f"{next(iter(attrs.values()))} length {n} (target ≤140)")
    canon = soup.find("link", rel="canonical")
    need(canon and canon.get("href") == url, f"canonical != {url}")
    langs = {l.get("hreflang") for l in soup.find_all("link", rel="alternate") if l.get("hreflang")}
    need({"en", "ko", "x-default"} <= langs, f"hreflang en/ko/x-default missing (have {sorted(langs)})")
    types = set()
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
        except ValueError:
            fails.append("JSON-LD does not parse")
            continue
        for item in data if isinstance(data, list) else [data]:
            types.add(item.get("@type"))
            if item.get("@type") == "FAQPage" and HANGUL.search(json.dumps(item, ensure_ascii=False)):
                fails.append("FAQPage JSON-LD contains Korean")
    need({"WebApplication", "FAQPage"} <= types, f"JSON-LD needs WebApplication + FAQPage (have {sorted(t for t in types if t)})")
    need("cloudflareinsights.com/beacon" in str(soup.head), "no Cloudflare Web Analytics beacon in <head>")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    need(f"<loc>{url}</loc>" in sitemap, "not in sitemap.xml (run scripts/build_ko_pages.py)")
    need(f"<loc>{url}ko/</loc>" in sitemap and (d / "ko" / "index.html").exists(),
         "no /ko/ page or sitemap entry (run scripts/build_ko_pages.py)")

    # Vultr affiliate
    # plain vultr.com links (pricing citations) are fine; anything carrying a ref must be ours + sponsored
    vultr = [a for a in soup.find_all("a", href=True) if "vultr.com" in a["href"] and "ref=" in a["href"]]
    need(vultr, "no Vultr affiliate link")
    for a in vultr:
        need(a["href"] == VULTR_REF, f"Vultr link {a['href']} != {VULTR_REF}")
        need({"nofollow", "sponsored"} <= set(a.get("rel") or []), "Vultr link missing rel=\"nofollow sponsored\"")
    for key in ("vultr_label", "vultr_title", "vultr_sub", "vultr_cta"):
        need(f'data-i18n="{key}"' in html, f'missing data-i18n="{key}"')

    # design (guides/design-guide.md §2, §5-4)
    t3, bg = re.search(r"--text-3:\s*(#[0-9a-fA-F]{6})", html), re.search(r"--bg:\s*(#[0-9a-fA-F]{6})", html)
    if t3 and bg:
        cr = contrast(t3.group(1), bg.group(1))
        need(cr >= 4.5, f"--text-3 {t3.group(1)} contrast {cr:.2f}:1 on --bg (needs >= 4.5; design-guide §2)")
    fields = [e for e in soup.find_all(["input", "select", "textarea"])
              if (e.get("type") or "text").lower() not in {"checkbox", "radio", "range", "file", "color", "hidden"}]
    need(not fields or re.search(r"@media\s*\(max-width:\s*768px\)\s*\{\s*input,\s*select,\s*textarea\s*\{\s*font-size:\s*max\(16px",
                                 html), "text inputs but no mobile 16px input rule (iOS zoom; design-guide §5-4)")
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        sel = " ".join(sel.split())
        col = re.search(r"(?<![-\w])color\s*:\s*([^;}]+)", body)
        col = col.group(1).strip().lower() if col else ""
        white = re.fullmatch(r"#fff(fff)?|white|var\(--accent-fg\)", col)
        if white and re.search(r"background(-color)?\s*:\s*(var\(--success\)|#22c55e)", body, re.I):
            fails.append(f"white text on green {sel!r} (2.28:1) — use var(--success-fg) (design-guide §5-5)")
        if white and re.search(r"background(-color)?\s*:\s*(var\(--accent\)|#6366f1)", body, re.I):
            fails.append(f"white text on --accent {sel!r} (4.47:1) — use var(--accent-strong) (design-guide §2)")
    need(not re.search(r"(?<![-\w])color\s*:\s*(var\(--accent\)|#6366f1)", html),
         "color: var(--accent) as text (4.22:1 on surface) — use var(--accent-text) (design-guide §2)")
    for tok, against, low in (("--accent-text", "--surface-2", 4.5), ("--success-fg", "--success", 7.0)):
        m, b = re.search(tok + r":\s*(#[0-9a-fA-F]{6})", html), re.search(against + r":\s*(#[0-9a-fA-F]{6})", html)
        if f"var({tok})" in html:
            need(m, f"uses var({tok}) but never defines it")
        if m and b:
            need(contrast(m.group(1), b.group(1)) >= low, f"{tok} {m.group(1)} < {low}:1 on {against}")
    need(re.search(r"width:\s*max\(100%,\s*40px\);\s*height:\s*max\(100%,\s*40px\)", html),
         "no 40px touch-target rule (sf-touch-40; .lang-toggle/nav/buttons; design-guide §5-5)")
    need(re.search(r"@media\s*\(max-width:\s*480px\)\s*\{[^{}]*\{[^}]*\}[^{}]*\{[^}]*\}\s*nav\s*:is\(a,\s*button\)\s*\{\s*white-space:\s*nowrap", html),
         "no sf-nav-compact block (nav must stay one row at 375/320; design-guide §5-1)")
    need(not re.search(r"\.(nav-back|back-link)\s*\{\s*display:\s*none", html),
         ".nav-back/.back-link hidden — the back link must stay visible at every width (design-guide §5-1)")
    need(not re.search(r"(?<![-\w])color\s*:\s*#818cf8", html),
         "hardcoded #818cf8 — use var(--accent-text) (design-guide §2)")

    # surface/background token used as a text colour — invisible or near-invisible in one theme.
    # CSS blocks, plus every style="" attribute in the file (so JS template literals count too).
    for sel, body in re.findall(r"([^{}@]+)\{([^{}]*)\}", css):
        for m in COLOR_DECL.finditer(body):
            if m.group(1) in SURFACE_TOKENS:
                fails.append(f"color: var({m.group(1)}) is a surface token, not a text colour, "
                             f"in {' '.join(sel.split())[:60]!r} (design-guide §2)")
    for m in re.finditer(r"""style\s*=\s*(\\?["'])(.*?)\1""", html, re.S):
        for mm in COLOR_DECL.finditer(m.group(2)):
            if mm.group(1) in SURFACE_TOKENS:
                fails.append(f"color: var({mm.group(1)}) is a surface token, not a text colour, "
                             f"in inline style {m.group(2)[:70]!r} (design-guide §2)")

    # emoji / unicode-symbol icons (design-guide §8)
    fails += glyph_fails(soup)

    # mobile + content
    need(re.search(r"@media\s*\(max-width:\s*768px\)", html), "no @media (max-width: 768px)")
    need(soup.select_one(".guide-grid"), "no How-to section (.guide-grid)")
    need(len(soup.select(".faq-item")) >= 3, "FAQ (.faq-item) needs 3+ items")
    related = soup.select_one(".sf-related")
    rel_links = {a["href"] for a in related.find_all("a", href=True)
                 if re.fullmatch(r"/tools/[a-z0-9-]+/", a["href"]) and a["href"] != f"/tools/{slug}/"} if related else set()
    need(len(rel_links) >= 3, f".sf-related needs 3+ internal tool links (have {len(rel_links)})")
    for href in rel_links:
        need((ROOT / href.strip("/") / "index.html").exists(), f"related link {href} points to a missing tool")
    footer = soup.find("footer")
    fhrefs = " ".join(a["href"] for a in footer.find_all("a", href=True)) if footer else ""
    need("/about" in fhrefs and "/privacy" in fhrefs, "footer missing About / Privacy links")
    need((d / "README.md").exists(), "tools/<slug>/README.md missing")

    blog = {a["href"].split("#")[0].rstrip("/") for a in soup.find_all("a", href=True)
            if re.match(r"https://stackfreeks\.com/[^?#]+", a["href"])}
    posts = blog_post_urls()
    if posts is None:
        warns.append("could not fetch stackfreeks.com/post-sitemap.xml — blog links unchecked")
    else:
        need(not blog - posts, f"blog links not in post-sitemap: {sorted(blog - posts)}")
    return fails, warns


def changed_slugs():
    def git(*a):
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.split()
    slug = lambda p: p.split("/")[1]
    tool_files = lambda files: [p for p in files if re.match(r"tools/[^/]+/", p)]
    changed = {slug(p) for p in tool_files(git("diff", "--name-only", "origin/main..HEAD"))}
    added = {slug(p) for p in tool_files(git("diff", "--name-only", "--diff-filter=A", "origin/main..HEAD"))
             if p.endswith("/index.html") and p.count("/") == 2}
    return sorted(s for s in changed if (ROOT / "tools" / s / "index.html").exists()), added


def selftest():
    """The three rules that need a parser rather than a regex — keep them honest."""
    src = """<script>window.SF_PAGE_I18N = {
      en: { a: 'x: not a key', b: "}", c: { nested: 1 }, "d": 2, only_en: 3 },
      ko: { a: '1', b: '2', c: { nested: 1 }, "d": 2 }
    };</script>"""
    h = page_i18n_halves(src)
    assert h["en"] == ["a", "b", "c", "d", "only_en"], h
    assert h["ko"] == ["a", "b", "c", "d"], h
    assert set(h["en"]) - set(h["ko"]) == {"only_en"}
    assert page_i18n_halves("<p>no i18n here</p>") is None

    ok = BeautifulSoup("<body><p>Result: 6 × 1024 ✓ done, 50 ÷ 2 → fine</p>"
                       "<a href='/'>All tools →</a></body>", "lxml")
    assert glyph_fails(ok) == [], glyph_fails(ok)
    bad = BeautifulSoup("<body><button class='btn'>📋</button><span>✕</span>"
                        "<p>fine ✓ here too</p></body>", "lxml")
    assert len(glyph_fails(bad)) == 2, glyph_fails(bad)

    assert COLOR_DECL.search("color: var(--surface-2)").group(1) in SURFACE_TOKENS
    assert COLOR_DECL.search("background-color: var(--surface-2)") is None
    print("selftest OK")
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if args == ["--selftest"]:
        return selftest()
    added = set()
    if args == ["--all"]:
        slugs = sorted(p.parent.name for p in (ROOT / "tools").glob("*/index.html"))
    elif args == ["--push"]:
        slugs, added = changed_slugs()
    else:
        slugs = args
    if not slugs:
        print("qa_check: no tools to check")
        return 0
    bad = 0
    for s in slugs:
        fails, warns = check(s)
        if s in added:  # new tool: also needs the critic's verdict (Step 1.5), fresher than the page
            rep = ROOT / "output" / s / "qa-report.md"
            if not rep.exists() or not rep.read_text(encoding="utf-8").startswith("QA: PASS"):
                fails.append(f"{rep.relative_to(ROOT)} missing or not 'QA: PASS' — run Step 1.5 (agents/tool-critic.md)")
            elif rep.stat().st_mtime < (ROOT / "tools" / s / "index.html").stat().st_mtime:
                fails.append("qa-report.md is older than index.html — re-run Step 1.5")
        print(f"{'FAIL' if fails else 'PASS'}  {s}")
        for m in fails:
            print(f"   FAIL {m}")
        for m in warns:
            print(f"   WARN {m}")
        bad += bool(fails)
    if args == ["--push"] and bad:
        print("[blocked] push refused — fix the FAILs above (no override)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
