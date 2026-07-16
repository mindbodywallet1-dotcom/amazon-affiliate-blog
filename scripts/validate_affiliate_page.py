#!/usr/bin/env python3
"""Validate Amazon affiliate pages for compliance and SEO basics."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "site" / "src" / "content" / "affiliate"
CONFIG_PATHS = [
    ROOT / "affiliate" / "config.yaml",
    ROOT / "affiliate" / "config.example.yaml",
]

BANNED_PATTERNS = [
    (r"lowest price guaranteed", "Price guarantee claim"),
    (r"click here to buy", "Generic 'click here to buy' copy"),
    (r"amazon recommends", "Implied Amazon endorsement"),
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def load_config() -> dict:
    for path in CONFIG_PATHS:
        if path.exists():
            return yaml.safe_load(path.read_text(encoding="utf-8"))
    raise SystemExit("Missing affiliate config")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta = yaml.safe_load(match.group(1)) or {}
    body = text[match.end() :]
    return meta, body


def validate_page(path: Path, tag: str) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    title = meta.get("title", "")
    description = meta.get("description", "")
    slug = path.stem
    published = meta.get("published", False)

    if not published:
        return errors

    if not title:
        errors.append(f"{slug}: missing title")
    elif len(title) > 70:
        errors.append(f"{slug}: title too long ({len(title)} chars)")

    if not description:
        errors.append(f"{slug}: missing description")
    elif len(description) < 50 or len(description) > 170:
        errors.append(f"{slug}: description length out of range ({len(description)} chars)")

    if not meta.get("primary_keyword"):
        errors.append(f"{slug}: missing primary_keyword")

    if not meta.get("asins"):
        errors.append(f"{slug}: missing asins")

    h1_count = len(re.findall(r"^#\s+", body, re.MULTILINE))
    if h1_count > 0:
        errors.append(f"{slug}: markdown body should not contain H1 (layout provides it)")

    for pattern, message in BANNED_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"{slug}: {message}")

    amazon_links = re.findall(r"https?://(?:www\.)?amazon\.com[^\s\)]*", text)
    for link in amazon_links:
        if f"tag={tag}" not in link:
            errors.append(f"{slug}: Amazon link missing tag={tag}: {link}")

    return errors


def validate_site_components(tag: str) -> list[str]:
    errors: list[str] = []
    cta_path = ROOT / "site" / "src" / "components" / "AmazonCTA.astro"
    disclosure_path = ROOT / "site" / "src" / "components" / "DisclosureBanner.astro"

    if not cta_path.exists():
        errors.append("Missing AmazonCTA.astro component")
    else:
        cta_text = cta_path.read_text(encoding="utf-8")
        if 'rel="nofollow sponsored"' not in cta_text:
            errors.append("AmazonCTA.astro missing rel='nofollow sponsored'")

    if not disclosure_path.exists():
        errors.append("Missing DisclosureBanner.astro component")

    layout_path = ROOT / "site" / "src" / "layouts" / "AffiliateLayout.astro"
    if layout_path.exists():
        layout_text = layout_path.read_text(encoding="utf-8")
        if "DisclosureBanner" not in layout_text:
            errors.append("AffiliateLayout.astro missing DisclosureBanner")
    else:
        errors.append("Missing AffiliateLayout.astro")

    return errors


def main() -> int:
    config = load_config()
    tag = config.get("associate_tag", "yourtag-20")

    errors: list[str] = []
    errors.extend(validate_site_components(tag))

    if not CONTENT_DIR.exists():
        errors.append(f"Content directory missing: {CONTENT_DIR}")
    else:
        pages = sorted(CONTENT_DIR.glob("*.md"))
        published = 0
        for path in pages:
            meta, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
            if meta.get("published"):
                published += 1
                errors.extend(validate_page(path, tag))

        if published == 0:
            errors.append("No published pages found in site/src/content/affiliate/")

    if errors:
        print("Validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Validation OK — all published pages passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
