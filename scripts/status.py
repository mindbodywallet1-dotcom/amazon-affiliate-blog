#!/usr/bin/env python3
"""Show Blotato accounts and upcoming scheduled posts."""

from __future__ import annotations

import sys

from _lib import blotato_request, load_api_key


def main() -> int:
    key = load_api_key()

    accounts_raw = blotato_request("GET", "/users/me/accounts", key)
    if isinstance(accounts_raw, list):
        account_list = accounts_raw
    else:
        account_list = accounts_raw.get("items", accounts_raw.get("accounts", accounts_raw.get("data", [])))
    print("CONNECTED ACCOUNTS")
    print("-" * 40)
    for acct in account_list:
        platform = acct.get("platform", "?")
        name = acct.get("username") or acct.get("fullname") or acct.get("id")
        print(f"  {platform:12} {name}  (id: {acct.get('id')})")

    print("\nSCHEDULED POSTS")
    print("-" * 40)
    try:
        schedules = blotato_request("GET", "/schedules", key)
        items = schedules if isinstance(schedules, list) else schedules.get("schedules", schedules.get("items", []))
        if not items:
            print("  (none)")
        for item in items[:20]:
            when = item.get("scheduledTime") or item.get("scheduled_at") or "?"
            text = (item.get("text") or item.get("content", {}).get("text") or "")[:60]
            platform = item.get("platform") or item.get("target", {}).get("targetType") or "?"
            print(f"  {when}  [{platform}]  {text}")
    except Exception as e:
        print(f"  Could not list schedules: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
