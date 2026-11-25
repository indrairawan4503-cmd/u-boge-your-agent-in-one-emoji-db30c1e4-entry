#!/usr/bin/env python3
"""Your Agent in One Emoji — Variant A: the owl.

Writes the single emoji glyph to /output/entry.txt first (the grader's
output directory), then a byte-identical copy next to this script in the
repo root, guarded so a read-only repo mount never crashes the run.
Deterministic: no network, no randomness, no time, no environment input.
"""

import os

GLYPH = "\U0001F989"  # OWL


def check_entry(glyph: str) -> str:
    """Gate self-check: the entry must be exactly one emoji glyph.

    Verifies, before anything is written, that the glyph is:
    - a str that encodes as valid UTF-8 (round-trip decode matches),
    - exactly 1 Unicode code point (the gate allows 1-16 characters,
      and this entry is defined as a single glyph),
    - not only whitespace.
    Raises ValueError/TypeError on any failure; the run must not
    produce an output file from a glyph that fails the gate.
    """
    if not isinstance(glyph, str):
        raise TypeError("entry glyph must be a str")
    if not 1 <= len(glyph) <= 16:
        raise ValueError(
            f"entry must be 1-16 characters, got {len(glyph)}"
        )
    if glyph.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if len(glyph) != 1:
        raise ValueError(
            f"entry must be exactly 1 Unicode code point, got {len(glyph)}"
        )
    data = glyph.encode("utf-8")
    if data.decode("utf-8") != glyph:
        raise ValueError("entry is not valid UTF-8")
    return glyph


def main() -> None:
    check_entry(GLYPH)
    data = GLYPH.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    try:
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root, "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
