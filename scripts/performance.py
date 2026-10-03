#!/usr/bin/env python3
"""Pull Google Search Console results for tools.stackfreeks.com into output/performance.md,
so past tools feed back into planning (tool-picker) and lessons (retro).

  python scripts/performance.py

One-time setup:
  1. pip install google-auth google-auth-oauthlib
  2. Nothing else if the WordPress pipeline already has gsc-token.json — same Google account and
     scope, so its token is shared (refreshes are written back there). Otherwise a browser opens to consent.
Same desktop OAuth app as 04_Ops_Briefing and the WordPress pipeline (only client_secret.json is read).
Env overrides: GSC_CLIENT_SECRET, GSC_TOKEN (paths), GSC_SITE (default sc-domain:tools.stackfreeks.com)
"""
import os
import subprocess
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import quote

from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

ROOT = Path(__file__).resolve().parent.parent
CLIENT_SECRET = Path(os.getenv("GSC_CLIENT_SECRET", r"F:\02_PipeLineWork\04_Ops_Briefing\_config\client_secret.json"))
TOKEN_FILE = Path(os.getenv("GSC_TOKEN", ROOT.parent / "02_Autoblog_StackFreeks_Wordpress" / "gsc-token.json"))
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE = os.getenv("GSC_SITE", "sc-domain:tools.stackfreeks.com")
BASE = "https://tools.stackfreeks.com/tools/"
DAYS = 28
LAG = 3  # GSC data is ~2-3 days behind


def query(session, start, end, dims, limit):
    url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{quote(SITE, safe='')}/searchAnalytics/query"
    resp = session.post(url, json={"startDate": start.isoformat(), "endDate": end.isoformat(),
                                   "dimensions": dims, "rowLimit": limit})
    if resp.status_code != 200:
        sys.exit(f"[error] GSC {resp.status_code}: {resp.text[:300]}")
    return resp.json().get("rows", [])


def credentials():
    creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES) if TOKEN_FILE.exists() else None
    if creds and not creds.valid and creds.refresh_token:
        try:
            creds.refresh(Request())
        except Exception:
            creds = None  # revoked refresh token → consent again
    if not creds or not creds.valid:
        if not CLIENT_SECRET.exists():
            sys.exit(f"[error] {CLIENT_SECRET} not found — set GSC_CLIENT_SECRET")
        creds = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES).run_local_server(port=0)
    TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")
    return creds


def launched(slug):
    out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%as", "--", f"tools/{slug}/index.html"],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    return out[-1] if out else str(date.today())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    session = AuthorizedSession(credentials())
    end = date.today() - timedelta(days=LAG)
    start = end - timedelta(days=DAYS - 1)

    # EN + /ko/ pages roll up into one row per tool
    agg = defaultdict(lambda: [0.0, 0.0, 0.0])  # impressions, clicks, impression-weighted position
    for r in query(session, start, end, ["page"], 1000):
        url = r["keys"][0].split("#")[0]
        if url.startswith(BASE):
            a = agg[url[len(BASE):].split("/")[0]]
            a[0] += r["impressions"]; a[1] += r["clicks"]; a[2] += r["position"] * r["impressions"]
    # API orders by clicks; with few clicks that is ~alphabetical, so rank by impressions ourselves
    queries = sorted(query(session, start, end, ["query"], 1000), key=lambda q: -q["impressions"])[:50]

    slugs = sorted(p.parent.name for p in (ROOT / "tools").glob("*/index.html"))
    rows, dead = [], []
    for s in slugs:
        imp, clicks, wpos = agg.get(s, (0, 0, 0))
        pub = launched(s)
        rows.append((imp, clicks, wpos / imp if imp else 0, s, pub))
        if imp == 0 and (date.today() - date.fromisoformat(pub)).days > 30:
            dead.append(f"- {s} ({pub})")
    rows.sort(reverse=True)

    out = ["# Performance — Google Search Console (tools)", "",
           f"Pulled: {date.today()} | Window: {start} → {end} ({DAYS} days) | Property: {SITE}",
           f"Tools: {len(slugs)} | With impressions: {sum(1 for r in rows if r[0])} | "
           f"Total clicks: {sum(r[1] for r in rows):.0f} | Total impressions: {sum(r[0] for r in rows):.0f}",
           "", "## Tools by impressions (EN + KO)", "",
           "| Impr | Clicks | Avg pos | Tool | Launched |", "|---:|---:|---:|---|---|"]
    out += [f"| {i:.0f} | {c:.0f} | {p:.1f} | {s} | {pub} |" for i, c, p, s, pub in rows]
    out += ["", f"## Zero impressions after 30+ days ({len(dead)})", ""] + (dead or ["- none"])
    out += ["", "## Top search queries (what Google already shows us for)", "",
            "| Query | Impr | Clicks | Avg pos |", "|---|---:|---:|---:|"]
    out += [f"| {q['keys'][0]} | {q['impressions']:.0f} | {q['clicks']:.0f} | {q['position']:.1f} |" for q in queries]

    target = ROOT / "output" / "performance.md"
    target.parent.mkdir(exist_ok=True)
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Saved {target} ({len(slugs)} tools, {len(agg)} with data)")


if __name__ == "__main__":
    main()
