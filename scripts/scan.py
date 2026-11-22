#!/usr/bin/env python3
"""Weekly scan of Microsoft Learn Fabric IQ docs.

Detects pages whose "Last updated on" date changed, refreshes the stored
snapshot, and writes a "What's new" report (docs/reports/YYYY-MM-DD.md).
"""
import argparse
import datetime as dt
import difflib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
SNAP = ROOT / "snapshots"
MANIFEST = SNAP / "manifest.json"
DOCS = ROOT / "docs"
REPORTS = DOCS / "reports"

BASE = "https://learn.microsoft.com/en-us/fabric/iq/"
TOC = BASE + "toc.json"
HEADERS = {"User-Agent": "fabric-iq-learn-tracker (+https://github.com/david-pizzi-msft/fabric-iq-learn-tracker)"}


def get(url, retries=3):
    for i in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.text
        except requests.RequestException:
            if i == retries - 1:
                raise


def walk_toc(items, out):
    for it in items:
        href = it.get("href")
        if href and not href.startswith(("http://", "https://")) and href not in ("./", ""):
            out.append(href.split("#")[0].split("?")[0])
        walk_toc(it.get("children", []), out)


def discover():
    toc = json.loads(get(TOC))
    hrefs = []
    walk_toc(toc["items"], hrefs)
    seen, pages = set(), []
    for h in hrefs:
        url = urljoin(BASE, h).rstrip("/")
        if url.startswith(BASE.rstrip("/")) and url not in seen:
            seen.add(url)
            pages.append(url)
    return pages


def slug(url):
    return url[len(BASE):].strip("/") or "index"


def parse(url, html):
    soup = BeautifulSoup(html, "html.parser")
    lt = soup.select_one("ul[aria-label='page info'] local-time, local-time[datetime]")
    updated = lt["datetime"][:10] if lt and lt.get("datetime") else None
    if not updated:
        meta = soup.find("meta", attrs={"name": "updated_at"}) or soup.find("meta", attrs={"name": "ms.date"})
        updated = meta["content"][:10] if meta else None
    title = (soup.find("h1").get_text(" ", strip=True) if soup.find("h1") else slug(url))
    body = soup.select_one("div.content[data-bi-name='content']") or soup.select_one("main") or soup
    for sel in ["nav", "script", "style", "[data-bi-name='feedback']", ".feedback-section",
                "[data-bi-name='article-header']", "ul[aria-label='page info']", ".page-metadata-container",
                "[data-bi-name='rating']", "#article-header", ".contributors-holder", "[data-bi-name='pageactions']"]:
        for t in body.select(sel):
            t.decompose()
    md = markdownify(str(body), heading_style="ATX", bullets="-")
    md = re.sub(r"^\s*(Table of contents\s*|Exit editor mode\s*|---\s*|Note\s+Access to this page requires authorization\.?\s*)+", "", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    dm = soup.find("meta", attrs={"name": "description"})
    description = dm["content"].strip() if dm and dm.get("content") else ""
    # Heading anchors for linking
    anchors = {}
    for h in body.select("h2[id], h3[id]"):
        anchors[h.get_text(" ", strip=True)] = h["id"]
    return {"url": url, "title": title, "updated": updated, "markdown": md, "anchors": anchors, "description": description}


def split_sections(md):
    sections, cur, lines = {}, "Introduction", []
    for line in md.splitlines():
        m = re.match(r"^(#{2,3})\s+(.*)", line)
        if m:
            sections[cur] = "\n".join(lines).strip()
            cur, lines = m.group(2).strip(), []
        else:
            lines.append(line)
    sections[cur] = "\n".join(lines).strip()
    return sections


def first_sentence(text, limit=170):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`>#|]", "", text).strip()
    text = re.sub(r"\s+", " ", text)
    s = re.split(r"(?<=[.!?])\s", text)[0] if text else ""
    return (s[:limit].rstrip() + "…") if len(s) > limit else s


def summarize(old_md, new_md, page):
    """Return bullet strings describing section-level changes, each linked to Learn."""
    old, new = split_sections(old_md), split_sections(new_md)
    anchors, url, bullets = page["anchors"], page["url"], []
    for name, text in new.items():
        link = f"{url}#{anchors[name]}" if name in anchors else url
        label = f"[{name}]({link})" if name != "Introduction" else f"[Introduction]({url})"
        if name not in old:
            bullets.append(f"**New section** {label}: {first_sentence(text)}")
        elif old[name] != text:
            added = [l[2:] for l in difflib.ndiff(old[name].splitlines(), text.splitlines())
                     if l.startswith("+ ") and l[2:].strip()]
            removed = [l for l in difflib.ndiff(old[name].splitlines(), text.splitlines()) if l.startswith("- ")]
            sample = first_sentence(" ".join(added)) if added else "content removed or reworded"
            bullets.append(f"**Updated** {label} (+{len(added)}/−{len(removed)} lines): {sample}")
    for name in old:
        if name not in new:
            bullets.append(f"**Removed section** “{name}”")
    return bullets


META_END = "<!-- /meta -->\n"


def read_snap(f):
    if not f.exists():
        return ""
    s = f.read_text("utf-8")
    return s.split(META_END, 1)[1] if META_END in s else s


def render_snap(page):
    head = (f"---\ntitle: \"{page['title'].replace(chr(34), chr(39))}\"\n---\n\n"
            f"!!! info \"Snapshot\"\n    Source: [{page['url']}]({page['url']}) · Last updated on **{page['updated']}**\n\n")
    return head + META_END + page["markdown"]


def load_manifest():
    return json.loads(MANIFEST.read_text("utf-8")) if MANIFEST.exists() else {"pages": {}}


BASELINE_DAYS = 14
SERVICES = {"plan": "Planning", "ontology": "Ontology", "connectors": "Connectors"}


def service(url):
    seg = slug(url).split("/")
    return SERVICES.get(seg[0], seg[0].replace("-", " ").title()) if len(seg) > 1 else "Fabric IQ"


def write_report(today, new_pages, updated, removed, baseline, total):
    cutoff = (dt.date.fromisoformat(today) - dt.timedelta(days=BASELINE_DAYS)).isoformat()
    REPORTS.mkdir(parents=True, exist_ok=True)
    if not baseline and not (new_pages or updated or removed) and (REPORTS / f"{today}.md").exists():
        return
    lines = ["---", f"title: \"Fabric IQ What's New: week of {today}\"", f"date: {today}", "---", "",
             f"# Fabric IQ What's New: {today}", ""]
    if baseline:
        recent = sorted((p for p in new_pages if p["updated"] and p["updated"] >= cutoff),
                        key=lambda p: p["updated"], reverse=True)
        lines += [f"Baseline captured: **{total} pages** snapshotted. Below are the **{len(recent)} pages** "
                  f"updated on Microsoft Learn in the last {BASELINE_DAYS} days. Later reports show changes since the previous scan.", ""]
        for p in recent:
            lines += [f"### {service(p['url'])} – [{p['title']}]({p['url']})", f"_Last updated {p['updated']}_", ""]
            intro = p.get("description") or first_sentence(split_sections(p["markdown"]).get("Introduction", ""), 220)
            if intro:
                lines += [intro, ""]
            heads = list(p["anchors"].items())[:8]
            lines += [f"- [{t}]({p['url']}#{a})" for t, a in heads] + [""]
    elif not (new_pages or updated or removed):
        lines += ["No documentation changes detected this week.", ""]
    else:
        lines += [f"**{len(updated)} updated · {len(new_pages)} new · {len(removed)} removed** (of {total} pages)", ""]
        if updated:
            lines += ["## Updated pages", ""]
            for p, old_date, bullets in updated:
                lines += [f"### {service(p['url'])} – [{p['title']}]({p['url']})", f"_Last updated {old_date} → {p['updated']}_", ""]
                lines += [f"- {b}" for b in bullets] or ["- Page metadata updated (no visible content change)"]
                lines.append("")
        if new_pages:
            lines += ["## New pages", ""]
            lines += [f"- **{service(p['url'])}** – [{p['title']}]({p['url']}) · {p['updated']}" for p in new_pages] + [""]
        if removed:
            lines += ["## Removed pages", ""]
            lines += [f"- **{service(r['url'])}** – {r['title']} ({r['url']})" for r in removed] + [""]
    lines += ["---", "Source: [Microsoft Learn – Fabric IQ](https://learn.microsoft.com/en-us/fabric/iq/). "
              "Content © Microsoft, CC BY 4.0."]
    (REPORTS / f"{today}.md").write_text("\n".join(lines) + "\n", "utf-8")


def write_index():
    reports = sorted(REPORTS.glob("20*.md"), reverse=True)
    lines = ["---", "title: What's new", "---", "", "# Fabric IQ: What's new", "",
             "Changes to the [Microsoft Fabric IQ documentation](https://learn.microsoft.com/en-us/fabric/iq/), "
             "detected from each page's *Last updated on* date. Use the search box to look through the documentation history. "
             "Earlier reports are in the [Archive](reports/index.md).", ""]
    if reports:
        body = reports[0].read_text("utf-8").split("---\n", 2)[-1]
        body = re.sub(r"^# .*\n", "", body.lstrip(), count=1)
        lines += [f"## Report: {reports[0].stem}", "", body]
    (DOCS / "index.md").write_text("\n".join(lines) + "\n", "utf-8")
    arch = ["---", "title: Archive", "---", "", "# Archive", "",
            "Past scan reports, newest first.", ""]
    arch += [f"- [{r.stem}]({r.stem}.md)" for r in reports]
    (REPORTS / "index.md").write_text("\n".join(arch) + "\n", "utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--silent-edits", action="store_true",
                    help="also treat body changes without a date change as updates")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    args = ap.parse_args()

    manifest = load_manifest()
    baseline = not manifest["pages"]
    urls = discover()
    print(f"Discovered {len(urls)} pages")

    def fetch(u):
        html = get(u)
        return u, (parse(u, html) if html else None)

    with ThreadPoolExecutor(8) as ex:
        results = dict(ex.map(fetch, urls))

    new_pages, updated = [], []
    for url, page in results.items():
        if page is None:
            continue
        key, snap_file = slug(url), SNAP / (slug(url) + ".md")
        prev = manifest["pages"].get(key)
        changed = prev is None or (page["updated"] or "") != (prev["updated"] or "")
        if prev and not changed and args.silent_edits and snap_file.exists() \
                and read_snap(snap_file) != page["markdown"]:
            changed = True
        if prev is None:
            new_pages.append(page)
        elif changed:
            old_md = read_snap(snap_file)
            updated.append((page, prev["updated"], summarize(old_md, page["markdown"], page)))
        if changed:
            snap_file.parent.mkdir(parents=True, exist_ok=True)
            snap_file.write_text(render_snap(page), "utf-8")
        manifest["pages"][key] = {"url": url, "title": page["title"], "updated": page["updated"],
                                  "checked": args.date}

    removed = []
    for key in list(manifest["pages"]):
        if manifest["pages"][key]["url"] not in results or results[manifest["pages"][key]["url"]] is None:
            removed.append(manifest["pages"].pop(key))
            f = SNAP / (key + ".md")
            if f.exists():
                f.unlink()

    manifest["lastScan"] = args.date
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True), "utf-8")
    write_report(args.date, new_pages, [u for u in updated], removed, baseline, len(manifest["pages"]))
    write_index()
    print(f"updated={len(updated)} new={len(new_pages)} removed={len(removed)} baseline={baseline}")
    return 0


if __name__ == "__main__":
    sys.exit(main())


