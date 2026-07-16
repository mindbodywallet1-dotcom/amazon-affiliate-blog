#!/usr/bin/env python3
"""Shared helpers for Wellthlab marketing scripts."""

from __future__ import annotations

import json
import os
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
BLOTATO_BASE = "https://backend.blotato.com/v2"


def load_api_key() -> str:
    key = os.environ.get("BLOTATO_API_KEY", "").strip()
    if key:
        return key

    mcp_paths = [
        ROOT / ".cursor" / "mcp.json",
        Path.home() / ".cursor" / "mcp.json",
    ]
    for path in mcp_paths:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        servers = data.get("mcpServers", {})
        blotato = servers.get("blotato", {})
        key = blotato.get("headers", {}).get("blotato-api-key", "").strip()
        if key:
            return key

    raise SystemExit(
        "No Blotato API key. Set BLOTATO_API_KEY or add to .cursor/mcp.json"
    )


def blotato_headers(api_key: str) -> dict[str, str]:
    return {"blotato-api-key": api_key, "Content-Type": "application/json"}


def blotato_request(method: str, path: str, api_key: str, **kwargs) -> dict:
    url = f"{BLOTATO_BASE}{path}"
    resp = requests.request(method, url, headers=blotato_headers(api_key), timeout=60, **kwargs)
    if resp.status_code >= 400:
        raise RuntimeError(f"Blotato {method} {path} failed ({resp.status_code}): {resp.text}")
    if resp.text.strip():
        return resp.json()
    return {}


def upload_local_video(api_key: str, file_path: Path) -> str:
    # Blotato presigned upload — same flow as blotato_create_presigned_upload_url MCP tool
    presign = blotato_request(
        "POST",
        "/uploads/presigned-url",
        api_key,
        json={"filename": file_path.name},
    )
    presigned_url = presign.get("presignedUrl") or presign.get("presigned_url")
    public_url = presign.get("publicUrl") or presign.get("public_url")
    if not presigned_url or not public_url:
        raise RuntimeError(f"Unexpected presign response: {presign}")

    with file_path.open("rb") as f:
        put = requests.put(presigned_url, data=f, timeout=300)
    if put.status_code >= 400:
        raise RuntimeError(f"Upload failed ({put.status_code}): {put.text[:500]}")

    return public_url
