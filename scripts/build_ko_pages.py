#!/usr/bin/env python3
"""Prerender standalone Korean (/ko/) sibling pages for every tool + the home page.

For each tools/<slug>/index.html -> tools/<slug>/ko/index.html
and index.html -> ko/index.html

Also patches the English originals' hreflang alternate block to be reciprocal,
and regenerates the Tools section of sitemap.xml with EN + KO entries.

Usage:  python scripts/build_ko_pages.py
Re-run this whenever a new tool is added.
"""
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://tools.stackfreeks.com"
KO_TITLE_SUFFIX = " — 무료 온라인 도구 | StackFreeks"
EN_TITLE_SUFFIX = " — Free Online Tool | StackFreeks"

warnings = []


def make_soup(html):
    return BeautifulSoup(html, "lxml")


def serialize(soup):
    out = soup.decode(formatter="html5")
    if not out.lstrip().lower().startswith("<!doctype"):
        out = "<!DOCTYPE html>\n" + out
    return out


def hreflang_links(soup, en_url, ko_url):
    """Return list of new <link rel=alternate> tags (en, ko, x-default)."""
    tags = []
    for hl, href in (("en", en_url), ("ko", ko_url), ("x-default", en_url)):
        t = soup.new_tag("link", rel="alternate", href=href)
        t["hreflang"] = hl
        tags.append(t)
    return tags


def replace_hreflang(soup, en_url, ko_url):
    existing = soup.find_all("link", rel="alternate")
    existing = [t for t in existing if t.get("hreflang")]
    new_tags = hreflang_links(soup, en_url, ko_url)
    if existing:
        first = existing[0]
        for nt in new_tags:
            first.insert_before(nt)
            first.insert_before("\n  ")
        for t in existing:
            t.decompose()
    else:
        ref = soup.find("link", rel="canonical") or soup.find("title")
        if ref is None:
            head = soup.find("head")
            for nt in new_tags:
                head.append(nt)
                head.append("\n")
        else:
            for nt in new_tags:
                ref.insert_after(nt)
                ref.insert_after("\n  ")
                ref = nt


def rewrite_internal_links(soup):
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href == "/":
            a["href"] = "/ko/"
        elif re.match(r"^/tools/[^/]+/$", href):
            a["href"] = href + "ko/"


def set_meta(soup, selector_attr, value):
    tag = soup.find("meta", attrs=selector_attr)
    if tag is not None and value:
        tag["content"] = value


def build_faq_mainentity(soup):
    items = soup.select(".lang-ko .faq-item")
    entities = []
    for it in items:
        q_btn = it.select_one(".faq-q")
        a_el = it.select_one(".faq-a")
        if not q_btn or not a_el:
            continue
        # question = first span text, excluding .faq-icon
        q_text = None
        for span in q_btn.find_all("span"):
            if "faq-icon" in (span.get("class") or []):
                continue
            q_text = span.get_text(" ", strip=True)
            break
        if q_text is None:
            q_text = q_btn.get_text(" ", strip=True).rstrip("+").strip()
        a_text = a_el.get_text(" ", strip=True)
        if q_text and a_text:
            entities.append({
                "@type": "Question",
                "name": q_text,
                "acceptedAnswer": {"@type": "Answer", "text": a_text},
            })
    return entities


def process_jsonld(soup, ko_url, slug):
    for sc in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = sc.string or sc.get_text()
        if not raw or not raw.strip():
            continue
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            warnings.append(f"{slug}: could not parse a JSON-LD block, left unchanged")
            continue

        def fix(obj):
            if isinstance(obj, list):
                for x in obj:
                    fix(x)
                return
            if not isinstance(obj, dict):
                return
            if obj.get("@type") == "FAQPage":
                ents = build_faq_mainentity(soup)
                if ents:
                    obj["mainEntity"] = ents
                else:
                    warnings.append(f"{slug}: no Korean FAQ items found; kept English FAQPage")
            else:
                if "url" in obj:
                    obj["url"] = ko_url
                if "@id" in obj:
                    obj["@id"] = ko_url
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    fix(v)

        fix(data)
        sc.string = json.dumps(data, ensure_ascii=False)


def replace_lang_toggle(soup, en_url):
    btn = soup.find(class_="lang-toggle")
    if btn is None:
        return
    a = soup.new_tag("a", href=en_url)
    a["class"] = "lang-toggle"
    a.string = "English"
    btn.replace_with(a)


def build_ko_page(src_path, en_url, ko_url, slug, is_home):
    soup = make_soup(src_path.read_text(encoding="utf-8"))

    html_tag = soup.find("html")
    html_tag["lang"] = "ko"
    html_tag["data-force-lang"] = "ko"

    # Remove English prose
    for el in soup.select(".lang-en"):
        el.decompose()

    # Korean title
    ko_h1 = soup.select_one(".lang-ko h1")
    if ko_h1 and ko_h1.get_text(strip=True):
        ko_name = ko_h1.get_text(strip=True)
    else:
        t = soup.find("title")
        ko_name = (t.get_text() if t else slug)
        for suf in (EN_TITLE_SUFFIX, " — Free Online Tools, No Account Required"):
            if ko_name.endswith(suf):
                ko_name = ko_name[: -len(suf)]
        ko_name = ko_name.strip()

    ko_title = ko_name + KO_TITLE_SUFFIX
    if soup.find("title"):
        soup.find("title").string = ko_title

    # Korean description from KO hero <p>
    hero = soup.select_one(".hero .lang-ko p") or soup.select_one(".lang-ko p")
    ko_desc = hero.get_text(" ", strip=True) if hero else ko_name

    set_meta(soup, {"name": "description"}, ko_desc)
    set_meta(soup, {"property": "og:title"}, ko_title)
    set_meta(soup, {"property": "og:description"}, ko_desc)
    set_meta(soup, {"name": "twitter:title"}, ko_title)
    set_meta(soup, {"name": "twitter:description"}, ko_desc)
    set_meta(soup, {"property": "og:url"}, ko_url)

    can = soup.find("link", rel="canonical")
    if can:
        can["href"] = ko_url

    replace_hreflang(soup, en_url, ko_url)
    rewrite_internal_links(soup)
    replace_lang_toggle(soup, en_url)
    process_jsonld(soup, ko_url, slug)

    out_path = src_path.parent / "ko" / "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(serialize(soup), encoding="utf-8")
    return out_path


def patch_english_original(src_path, en_url, ko_url):
    """Targeted text edit: replace ONLY the hreflang alternate block. Nothing else."""
    text = src_path.read_text(encoding="utf-8")
    triple = (
        f'  <link rel="alternate" hreflang="en" href="{en_url}" />\n'
        f'  <link rel="alternate" hreflang="ko" href="{ko_url}" />\n'
        f'  <link rel="alternate" hreflang="x-default" href="{en_url}" />\n'
    )
    # Drop any existing alternate hreflang links (and the leading indentation/newline).
    new_text, n = re.subn(r'[ \t]*<link[^>]*rel="alternate"[^>]*>[ \t]*\n?', '', text)
    if n == 0:
        new_text, n = re.subn(r'[ \t]*<link[^>]*hreflang="[^"]*"[^>]*>[ \t]*\n?', '', text)

    m = re.search(r'<link rel="canonical"[^>]*>[ \t]*\n', new_text)
    if m:
        pos = m.end()
    else:
        m = re.search(r'</title>[ \t]*\n', new_text)
        pos = m.end()
    new_text = new_text[:pos] + triple + new_text[pos:]
    src_path.write_text(new_text, encoding="utf-8", newline="")


def update_sitemap(slugs):
    sm_path = ROOT / "sitemap.xml"
    text = sm_path.read_text(encoding="utf-8")

    lines = ["", "  <!-- Homepage KO -->", "  <url>",
             f"    <loc>{BASE}/ko/</loc>", "    <changefreq>weekly</changefreq>",
             "    <priority>0.9</priority>", "  </url>", "", "  <!-- Tools -->"]
    for s in slugs:
        lines.append("  <url>")
        lines.append(f"    <loc>{BASE}/tools/{s}/</loc>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append("    <priority>0.8</priority>")
        lines.append("  </url>")
        lines.append("  <url>")
        lines.append(f"    <loc>{BASE}/tools/{s}/ko/</loc>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append("    <priority>0.7</priority>")
        lines.append("  </url>")
    block = "\n".join(lines) + "\n\n"

    # Replace everything from the KO-homepage / Tools section to just before </urlset>
    # (idempotent across re-runs).
    if "  <!-- Homepage KO -->" in text:
        start = text.index("  <!-- Homepage KO -->")
    else:
        start = text.index("  <!-- Tools -->")
    end = text.index("</urlset>")
    new_text = text[:start] + block.lstrip("\n") + text[end:]
    sm_path.write_text(new_text, encoding="utf-8")


def main():
    tool_dirs = sorted(p for p in (ROOT / "tools").iterdir() if (p / "index.html").exists())
    slugs = [p.name for p in tool_dirs]

    generated = 0

    # Home
    home = ROOT / "index.html"
    build_ko_page(home, f"{BASE}/", f"{BASE}/ko/", "index.html", True)
    patch_english_original(home, f"{BASE}/", f"{BASE}/ko/")
    generated += 1
    print(f"  home -> ko/index.html")

    for d in tool_dirs:
        slug = d.name
        en_url = f"{BASE}/tools/{slug}/"
        ko_url = f"{BASE}/tools/{slug}/ko/"
        src = d / "index.html"
        build_ko_page(src, en_url, ko_url, slug, False)
        patch_english_original(src, en_url, ko_url)
        generated += 1

    update_sitemap(slugs)

    print(f"\nGenerated {generated} KO pages ({len(slugs)} tools + 1 home).")
    print(f"Patched {generated} English originals' hreflang blocks.")
    print(f"Updated sitemap.xml ({len(slugs)} EN tools + {len(slugs)} KO tools + 2 homes).")
    if warnings:
        print(f"\n{len(warnings)} WARNING(s):")
        for w in warnings:
            print(f"  WARNING: {w}")
    else:
        print("\nNo warnings.")


if __name__ == "__main__":
    sys.exit(main())
