# Extract Favourites

A Python CLI tool for exporting Microsoft Edge bookmarks to CSV and Excel.

## Features

- Parse Microsoft Edge Chromium JSON bookmarks
- Preserve nested folder paths
- Export to CSV and Excel (`.xlsx`)
- Convert Chromium timestamps to readable UTC dates
- Sort bookmarks by folder, title, date added, or date last used
- Manage dependencies with `uv`

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
git clone https://github.com/kdjovanoski/extract-favourites.git
cd extract-favourites
uv sync
```

## Locating Microsoft Edge Bookmarks

Microsoft Edge stores bookmarks in a JSON file without a file extension.

**Windows:**

```text
C:\Users\<USERNAME>\AppData\Local\Microsoft\Edge\User Data\<PROFILE>\Bookmarks
```

Where:

- `<USERNAME>` is your Windows account username.
- `<PROFILE>` is your Edge profile directory, such as `Default`, `Profile 1`, or `Profile 2`.

**How to find the exact location:**

1. Open Microsoft Edge.
2. Navigate to `edge://version`.
3. Find the **Profile path** field.
4. Open that directory in File Explorer.
5. Locate the file named `Bookmarks` (without an extension).

**WSL (Windows Subsystem for Linux):**

The same file can be accessed using:

```text
/mnt/c/Users/<USERNAME>/AppData/Local/Microsoft/Edge/User Data/<PROFILE>/Bookmarks
```

Copy the file into the project's `data/` directory before processing it. This avoids modifying the original browser data.

## Usage

Export bookmarks to CSV and Excel:

```bash
uv run extract-favourites \
  --input data/Bookmarks \
  --format both \
  --sort added
```

Display available options:

```bash
uv run extract-favourites --help
```

## Output

By default, exported files are saved in the `output/` directory:

- `bookmarks.csv`
- `bookmarks.xlsx`

Each bookmark contains:

| Column | Description |
|---|---|
| Folder | Full folder hierarchy |
| Title | Bookmark title |
| URL | Website address |
| Date Added | Date the bookmark was created (UTC) |
| Date Last Used | Last recorded usage date (UTC), if available |

Note: The "Date Last Used" field may be unavailable for some bookmarks and should not be treated as a complete browsing history.

## Project Structure

```text
extract-favourites/
├── data/
├── output/
├── src/
│   └── extract_favourites/
│       ├── __init__.py
│       ├── cli.py
│       ├── parser.py
│       └── exporter.py
├── pyproject.toml
└── uv.lock
```

## Privacy

Bookmark data and generated exports are excluded from version control.

## License

This project is licensed under the MIT License.

## Version

0.1.0 — Initial release.