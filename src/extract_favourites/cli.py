import argparse
from pathlib import Path

from .parser import parse_bookmarks
from .exporter import export_bookmarks


def main():
    parser = argparse.ArgumentParser(
        description="Export Microsoft Edge bookmarks"
    )

    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help=(
            "Path to the Edge Bookmarks JSON file. "
            "Find its location at edge://version "
            "(Profile path)."
        ),
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
    )

    parser.add_argument(
        "--format",
        choices=["csv", "xlsx", "both"],
        default="both",
    )

    parser.add_argument(
        "--sort",
        choices=["folder", "added", "used", "title"],
        default="folder",
    )

    args = parser.parse_args()

    rows = parse_bookmarks(args.input)

    export_bookmarks(
        rows,
        args.output,
        args.format,
        args.sort,
    )


if __name__ == "__main__":
    main()
