"""Parser for LeetCode master HTML artifact.

This module provides a minimal, dependency-light parser that can ingest
an HTML file (e.g., `master.html`) and emit normalized row dictionaries.

Design goals:
- No heavy dependencies (uses stdlib `html.parser`)
- Extensible hooks for site-specific structures
- Google-style docstrings and typing
"""

from __future__ import annotations

from html.parser import HTMLParser
from typing import Dict, List, Optional


class RowBuffer:
    """Mutable buffer to accumulate a single row.

    Attributes:
        cells: List of captured cell strings for the current row.
    """

    def __init__(self) -> None:
        self.cells: List[str] = []

    def add_cell(self, value: str) -> None:
        self.cells.append(value.strip())

    def to_record(self, headers: List[str]) -> Dict[str, str]:
        record: Dict[str, str] = {}
        for i, key in enumerate(headers):
            record[key] = self.cells[i] if i < len(self.cells) else ""
        return record


class TableParser(HTMLParser):
    """Very simple table-oriented HTML parser.

    This parser assumes the data is presented in <table> rows with <tr>, <th>, <td>.
    If your HTML uses cards/divs, extend the hooks accordingly.
    """

    def __init__(self) -> None:
        super().__init__()
        self.in_td = False
        self.in_th = False
        self.current_text: List[str] = []
        self.headers: List[str] = []
        self.rows: List[Dict[str, str]] = []
        self._row = RowBuffer()
        self._in_header_row = True

    # --- Tag hooks ---------------------------------------------------------

    def handle_starttag(self, tag: str, attrs):  # type: ignore[override]
        if tag in ("td", "th"):
            self.current_text = []
            if tag == "td":
                self.in_td = True
            else:
                self.in_th = True

        if tag == "tr":
            self._row = RowBuffer()

    def handle_endtag(self, tag: str) -> None:  # type: ignore[override]
        if tag == "td" and self.in_td:
            self._row.add_cell("".join(self.current_text))
            self.in_td = False

        if tag == "th" and self.in_th:
            self.headers.append("".join(self.current_text).strip())
            self.in_th = False

        if tag == "tr":
            # Finalize row if we have headers already
            if self.headers and self._row.cells:
                self.rows.append(self._row.to_record(self.headers))
                self._in_header_row = False

    def handle_data(self, data: str) -> None:  # type: ignore[override]
        if self.in_td or self.in_th:
            self.current_text.append(data)


# --- Public API ------------------------------------------------------------


def parse_html(html: str) -> List[Dict[str, str]]:
    """Parse HTML content into a list of row dictionaries.

    Args:
        html: Raw HTML string.

    Returns:
        A list of dictionaries mapping header -> cell value.
    """
    parser = TableParser()
    parser.feed(html)
    return parser.rows


if __name__ == "__main__":
    # Minimal CLI usage example
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parser.py <path_to_master.html>")
        raise SystemExit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    rows = parse_html(content)
    print(f"Parsed rows: {len(rows)}")
