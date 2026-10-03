#!/usr/bin/env python3
"""Step 1.5 QA — deterministic checks for a tool page (what a script judges better than an LLM).
The judgment part (acceptance criteria, real usefulness vs competitors) is agents/tool-critic.md.

  python scripts/qa_check.py <slug> [<slug> ...]   # exit 1 on any FAIL
  python scripts/qa_check.py --all                 # every tool (survey; old tools may predate rules)
  python scripts/qa_check.py --push                # pre-push gate: tools changed since origin/main

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
_post_urls = None


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


def check(slug: str) -> tuple[list[str], list[str]]:
    d = ROOT / "tools" / slug
    page = d / "index.html"
    if not page.exists():
        return [f"{page} missing"], []
    html = page.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
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
    page_i18n = html.find("SF_PAGE_I18N")
    need(page_i18n == -1 or page_i18n < i18n, "SF_PAGE_I18N defined after i18n.js loads")

    # SEO
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    need(" — " in title and title.endswith(" | StackFreeks"), f"title format: {title!r}")
    desc = soup.find("meta", attrs={"name": "description"})
    desc = desc.get("content", "") if desc else ""
    need(0 < len(desc) <= 160, f"meta description length {len(desc)} (Google truncates past ~160)")
    if len(desc) > 140:
        warns.append(f"meta description length {len(desc)} (target ≤140)")
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
    vultr = [a for a in soup.find_all("a", href=True) if "vultr.com" in a["href"]]
    need(vultr, "no Vultr affiliate link")
    for a in vultr:
        need(a["href"] == VULTR_REF, f"Vultr link {a['href']} != {VULTR_REF}")
        need({"nofollow", "sponsored"} <= set(a.get("rel") or []), "Vultr link missing rel=\"nofollow sponsored\"")
    for key in ("vultr_label", "vultr_title", "vultr_sub", "vultr_cta"):
        need(f'data-i18n="{key}"' in html, f'missing data-i18n="{key}"')

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


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
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
