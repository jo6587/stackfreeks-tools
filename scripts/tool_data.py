#!/usr/bin/env python3
"""Tool data for the tool-page rollout (guides/design-guide.md §7).

  py -3.10 scripts/tool_data.py            # JSON for all tools
  py -3.10 scripts/tool_data.py <slug>     # JSON for one tool
  py -3.10 scripts/tool_data.py --sprite   # rebuild /shared/icons.svg from lucide-static (after adding an icon)

Each tool: slug, EN/KO name, icon (Lucide name in /shared/icons.svg as #i-<icon>),
category (id, anchor, i18n key, EN/KO name, icon), prev/next in its category (or null).
Category order, tool order and names come from the home directory (index.html);
icons come from ICONS / CATEGORIES below — the single source for both.
"""
import json
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent

# category id -> (nav i18n key, Lucide icon)
CATEGORIES = {
    "cat-vps": ("cat_vps_server", "hard-drive"),
    "cat-devops": ("cat_devops", "wrench"),
    "cat-conv": ("cat_converters", "arrow-left-right"),
    "cat-text": ("cat_text_code", "type"),
    "cat-image": ("cat_image", "aperture"),
    "cat-fun": ("cat_fun", "puzzle"),
}

# tool slug -> Lucide icon (lucide.dev, ISC). Add a row for every new tool, then rebuild the sprite.
ICONS = {
    # VPS & Server
    "vps-cost-calculator": "server",
    "vps-bandwidth-calculator": "gauge",
    "vps-migration-checklist": "list-checks",
    "server-spec-recommender": "cpu",
    "sla-uptime-calculator": "activity",
    "object-storage-calculator": "archive",
    "linux-swap-calculator": "arrow-down-up",
    "docker-ram-calculator": "container",
    "game-server-cost-calculator": "gamepad-2",
    "minecraft-server-ram-calculator": "box",
    "game-server-ram-calculator": "memory-stick",
    "nextcloud-server-requirements-calculator": "cloud",
    "llm-gpu-cost-calculator": "brain-circuit",
    "redis-memory-estimator": "database-zap",
    "php-fpm-max-children-calculator": "layers",
    "managed-database-cost-calculator": "database",
    # DevOps & Config Generators
    "cron-builder": "calendar-clock",
    "curl-command-generator": "terminal",
    "dockerfile-generator": "file-code",
    "nginx-config-generator": "server-cog",
    "systemd-service-generator": "settings",
    "pm2-ecosystem-generator": "refresh-cw",
    "ssh-config-generator": "key-round",
    "fail2ban-jail-generator": "shield-ban",
    "firewall-rule-builder": "brick-wall",
    "mysql-backup-script-generator": "database-backup",
    "htpasswd-generator": "lock-keyhole",
    "postgresql-config-generator": "sliders-horizontal",
    "og-meta-generator": "share-2",
    # Converters & Encoders
    "timestamp-converter": "clock",
    "color-converter": "palette",
    "px-rem-converter": "ruler",
    "base-converter": "binary",
    "base64-encoder": "file-digit",
    "url-encoder": "link",
    "json-to-csv": "sheet",
    "hash-generator": "hash",
    "jwt-decoder": "ticket",
    "uuid-generator": "fingerprint",
    "chmod-calculator": "file-lock",
    "subnet-calculator": "network",
    "password-generator": "rectangle-ellipsis",
    # Text & Code
    "json-formatter": "braces",
    "diff-checker": "diff",
    "text-case-converter": "case-sensitive",
    "word-counter": "file-text",
    "lorem-ipsum": "pilcrow",
    "markdown-previewer": "notebook-pen",
    "regex-tester": "regex",
    # Image Tools
    "image-to-base64": "file-image",
    "qr-code-generator": "qr-code",
    "heic-to-jpg": "image",
    "webp-to-jpg": "images",
    "image-compressor": "shrink",
    "exif-remover": "eraser",
    "svg-to-png": "pen-tool",
    "css-filter-previewer": "contrast",
    # Fun & Tests
    "reaction-time-test": "zap",
    "click-speed-test": "mouse-pointer-click",
    "keyboard-tester": "keyboard",
    "typing-speed-test": "timer",
    "number-memory-test": "list-ordered",
    "sequence-memory-test": "grid-3x3",
    "verbal-memory-test": "message-square-text",
    "aim-trainer": "crosshair",
    "regex-golf": "flag",
    "guess-the-output": "circle-help",
    "http-status-code-quiz": "globe",
    "chimp-test": "brain",
}

# shell + in-tool UI icons (nav, search, trust strip, arrows, tool controls) — also in the sprite
UI_ICONS = ["search", "chevron-down", "arrow-left", "arrow-right", "arrow-up-right",
            "monitor", "cloud-off", "user-round-x", "circle-check", "sun", "moon",
            # tool controls (copy/upload/download buttons, drop zones, pass/fail marks, score)
            "copy", "upload", "download", "check", "x", "eye", "eye-off",
            "triangle-alert", "trophy", "heart", "circle-x", "info"]


def sprite_names():
    """Every icon id the sprite must contain."""
    return sorted(set(ICONS.values()) | {v[1] for v in CATEGORIES.values()} | set(UI_ICONS))


LUCIDE = "1.52.0"  # pinned lucide-static version


def build_sprite():
    """Fetch each icon from lucide-static and write /shared/icons.svg (one <symbol> per icon)."""
    import re
    import urllib.request
    out = ["<!-- Lucide icons v" + LUCIDE + " (https://lucide.dev), ISC License,",
           "     Copyright (c) Lucide Contributors 2022; portions Copyright (c) 2013-2022 Cole Bemis (Feather, MIT).",
           "     Generated by scripts/tool_data.py (sprite flag). Stroke width comes from CSS (.ico). -->",
           '<svg xmlns="http://www.w3.org/2000/svg">']
    for n in sprite_names():
        url = f"https://unpkg.com/lucide-static@{LUCIDE}/icons/{n}.svg"
        svg = urllib.request.urlopen(url, timeout=20).read().decode("utf-8")
        body = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
        body = " ".join(line.strip() for line in body.strip().splitlines())
        out.append(f'<symbol id="i-{n}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                   f'stroke-linecap="round" stroke-linejoin="round">{body}</symbol>')
    out.append("</svg>")
    (ROOT / "shared" / "icons.svg").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def tools():
    soup = BeautifulSoup((ROOT / "index.html").read_text(encoding="utf-8-sig"), "lxml")
    out = {}
    for sec in soup.select("section.tools-cat"):
        h2 = sec.select_one("h2")
        key, icon = CATEGORIES[sec["id"]]
        cat = {"id": sec["id"], "anchor": "/#" + sec["id"], "key": key, "icon": icon,
               "en": h2.select_one(".lang-en").get_text(strip=True),
               "ko": h2.select_one(".lang-ko").get_text(strip=True)}
        items = []
        for li in sec.select("li.tool-card"):
            slug = li.a["href"].strip("/").split("/")[1]
            items.append({"slug": slug, "icon": ICONS[slug],
                          "en": li.select_one(".lang-en .card-name").get_text(strip=True),
                          "ko": li.select_one(".lang-ko .card-name").get_text(strip=True)})
        for i, t in enumerate(items):
            near = lambda j: dict(items[j]) if 0 <= j < len(items) else None
            out[t["slug"]] = {**t, "category": cat, "prev": near(i - 1), "next": near(i + 1)}
    return out


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:] == ["--sprite"]:
        build_sprite()
        sys.exit(print(f"wrote shared/icons.svg ({len(sprite_names())} icons)"))
    assert len(set(ICONS.values())) == len(ICONS), "two tools share an icon"
    data = tools()
    on_disk = {p.parent.name for p in (ROOT / "tools").glob("*/index.html")}
    assert set(data) == on_disk == set(ICONS), "home directory, tools/ and ICONS disagree"
    sprite = (ROOT / "shared" / "icons.svg").read_text(encoding="utf-8")
    missing = [n for n in sprite_names() if f'id="i-{n}"' not in sprite]
    assert not missing, f"icons.svg lacks {missing}"
    assert data["word-counter"]["prev"]["slug"] == "text-case-converter" and data["word-counter"]["icon"] == "file-text"
    print(json.dumps(data[sys.argv[1]] if len(sys.argv) > 1 else data, ensure_ascii=False, indent=1))
