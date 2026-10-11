from pathlib import Path
import pandas as pd


def export_bookmarks(
    rows,
    output: Path,
    fmt="both",
    sort_by="folder",
):
    output.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(rows)

    if df.empty:
        print("No bookmarks found.")
        return

    sort_columns = {
        "folder": ["Folder", "Title", "URL"],
        "added": ["Date Added"],
        "used": ["Date Last Used"],
        "title": ["Title"],
    }

    column = sort_columns[sort_by]

    df = df.sort_values(
        column,
        ascending=(sort_by not in ("added", "used")),
        kind="stable",
        na_position="last",
    )

    # Excel requires timezone-naive datetimes.
    for col in ("Date Added", "Date Last Used"):
        df[col] = pd.to_datetime(
            df[col], utc=True
        ).dt.tz_localize(None)

    if fmt in ("csv", "both"):
        df.to_csv(
            output / "bookmarks.csv",
            index=False,
            encoding="utf-8-sig",
        )

    if fmt in ("xlsx", "both"):
        df.to_excel(
            output / "bookmarks.xlsx",
            index=False,
        )

    print(f"Exported {len(df)} bookmarks.")
