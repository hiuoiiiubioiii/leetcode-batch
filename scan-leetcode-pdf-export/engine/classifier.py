"""Pattern classifier scaffold for LeetCode problems.

Takes normalized row dictionaries and assigns:
- primary pattern
- secondary pattern(s)
- composite patterns
- bucket
"""

from __future__ import annotations

from typing import Dict, List


# --- Simple rule-based seeds (extend later) -------------------------------

PATTERN_KEYWORDS = {
    "two_pointer": ["two pointer", "pair", "sorted array"],
    "sliding_window": ["substring", "window", "longest"],
    "binary_search": ["sorted", "search", "log n"],
    "dfs": ["dfs", "depth", "tree", "graph"],
    "bfs": ["bfs", "level order", "queue"],
    "dp": ["dp", "dynamic", "subproblem"],
}

BUCKET_MAP = {
    "two_pointer": "search",
    "sliding_window": "optimization",
    "binary_search": "search",
    "dfs": "traversal",
    "bfs": "traversal",
    "dp": "optimization",
}


# --- Core API -------------------------------------------------------------


def classify_row(row: Dict[str, str]) -> Dict[str, object]:
    """Classify a single problem row.

    Args:
        row: Normalized row dict.

    Returns:
        Enriched row with pattern annotations.
    """
    text = " ".join(row.values()).lower()

    matched: List[str] = []
    for pattern, keys in PATTERN_KEYWORDS.items():
        if any(k in text for k in keys):
            matched.append(pattern)

    primary = matched[0] if matched else "unknown"
    bucket = BUCKET_MAP.get(primary, "unknown")

    return {
        **row,
        "primary_pattern": primary,
        "secondary_patterns": matched[1:],
        "composite_patterns": matched,
        "bucket": bucket,
    }


def classify(rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    """Classify multiple rows."""
    return [classify_row(r) for r in rows]
