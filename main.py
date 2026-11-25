#!/usr/bin/env python3
"""Your Agent in One Emoji — Variant A: the owl.

Writes the single emoji glyph to /output/entry.txt first (the grader's
output directory), then a byte-identical copy next to this script in the
repo root, guarded so a read-only repo mount never crashes the run.
Deterministic: no network, no randomness, no time, no environment input.
"""

import os

GLYPH = "\U0001F989"  # OWL


def main() -> None:
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
