import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

EPOCH = datetime(1601, 1, 1, tzinfo=timezone.utc)


def chrome_time_to_dt(value):
    if not value:
        return None

    try:
        return EPOCH + timedelta(microseconds=int(value))
    except (ValueError, TypeError, OverflowError):
        return None


def parse_bookmarks(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []

    def walk(node, folders=None):
        if folders is None:
            folders = []

        if isinstance(node, list):
            for child in node:
                walk(child, folders)
            return

        if not isinstance(node, dict):
            return

        node_type = node.get("type")
        name = node.get("name", "")

        if node_type == "folder":
            new_folders = folders + [name]
            for child in node.get("children", []):
                walk(child, new_folders)

        elif node_type == "url":
            rows.append({
                "Folder": "/".join(folders),
                "Title": name,
                "URL": node.get("url", ""),
                "Date Added": chrome_time_to_dt(
                    node.get("date_added")
                ),
                "Date Last Used": chrome_time_to_dt(
                    node.get("date_last_used")
                ),
            })

    for root in data.get("roots", {}).values():
        walk(root)

    return rows
