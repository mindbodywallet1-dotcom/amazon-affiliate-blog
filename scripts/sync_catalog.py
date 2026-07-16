#!/usr/bin/env python3
"""Pull product list from wellthlab.shop into products/catalog-summary.yaml"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
STORE = "https://wellthlab.shop"
OUT = ROOT / "products" / "catalog-summary.yaml"


def fetch_json(path: str) -> dict:
    r = requests.get(f"{STORE}{path}", timeout=30)
    r.raise_for_status()
    return r.json()


def load_handles() -> list[str]:
    catalog = ROOT / "products" / "catalog.yaml"
    if not catalog.exists():
        return []
    text = catalog.read_text(encoding="utf-8")
    return re.findall(r"handle:\s+(\S+)", text)


def fetch_product(handle: str) -> dict | None:
    r = requests.get(f"{STORE}/products/{handle}", timeout=30)
    if r.status_code >= 400:
        return None
    html = r.text
    name = (
        re.search(r'"name"\s*:\s*"([^"]+)"', html)
        or re.search(r'property="og:title"\s+content="([^"]+)"', html)
        or re.search(r"<title>([^<|]+)", html, re.I)
    )
    price = re.search(r"\$\s*([\d.]+)", html)
    sold_out = "sold out" in html.lower() or "Sold out" in html
    if not name:
        return None
    return {
        "handle": handle,
        "name": name.group(1).strip(),
        "price": float(price.group(1)) if price else None,
        "sold_out": sold_out,
        "url": f"{STORE}/products/{handle}",
    }


def fetch_page_products() -> list[dict]:
    products = []
    for handle in load_handles():
        item = fetch_product(handle)
        if item:
            products.append(item)
    return products


def main() -> int:
    synced_at = datetime.now(timezone.utc).isoformat()
    collections = []
    try:
        collections = fetch_json("/collections.json").get("collections", [])
    except Exception as e:
        print(f"collections.json warning: {e}")

    products = fetch_page_products()
    if not products:
        print("No products found — check store URL")
        return 1

    payload = {
        "store": STORE,
        "synced_at": synced_at,
        "product_count": len(products),
        "collections": [
            {"title": c.get("title"), "handle": c.get("handle"), "count": c.get("products_count")}
            for c in collections
        ],
        "products": sorted(products, key=lambda p: p["name"]),
    }

    OUT.write_text(yaml.dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Synced {len(products)} products -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
