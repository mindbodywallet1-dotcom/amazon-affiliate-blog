#!/usr/bin/env python3
"""Build canonical Amazon affiliate URLs from ASINs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ASINS_DIR = ROOT / "affiliate" / "asins"
LINKS_DIR = ROOT / "affiliate" / "links"


def load_config() -> dict:
    for name in ("config.yaml", "config.example.yaml"):
        path = ROOT / "affiliate" / name
        if path.exists():
            return yaml.safe_load(path.read_text(encoding="utf-8"))
    raise SystemExit("Missing affiliate/config.yaml or config.example.yaml")


def build_url(asin: str, tag: str) -> str:
    return f"https://www.amazon.com/dp/{asin}?tag={tag}"


def update_asin_file(path: Path, url: str) -> None:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["affiliate_url"] = url
    path.write_text(yaml.dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def process_asin(asin: str, tag: str) -> str:
    url = build_url(asin, tag)
    asin_path = ASINS_DIR / f"{asin}.yaml"
    if asin_path.exists():
        update_asin_file(asin_path, url)

    LINKS_DIR.mkdir(parents=True, exist_ok=True)
    link_path = LINKS_DIR / f"{asin}.txt"
    link_path.write_text(url + "\n", encoding="utf-8")
    print(f"{asin} -> {url}")
    return url


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Amazon affiliate links")
    parser.add_argument("asin", nargs="?", help="Single ASIN to process")
    parser.add_argument("--all", action="store_true", help="Process all ASIN YAML files")
    args = parser.parse_args()

    config = load_config()
    tag = config.get("associate_tag", "").strip()
    if not tag or tag == "yourtag-20":
        print("Warning: using placeholder tag. Copy config.example.yaml to config.yaml and set your real tag.")

    if args.all:
        files = sorted(ASINS_DIR.glob("*.yaml"))
        if not files:
            print("No ASIN files found in affiliate/asins/")
            return 1
        for path in files:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            asin = data.get("asin") or path.stem
            process_asin(asin, tag)
        return 0

    if not args.asin:
        parser.print_help()
        return 1

    process_asin(args.asin.upper(), tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
