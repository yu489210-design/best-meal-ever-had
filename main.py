#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (1-200 characters) to /output/entry.txt.
Deterministic: fixed string, no randomness, no network, no input.
"""
import os

ENTRY = "After three days lost in the mountains, a shepherd gave me bread, salt, and hot tea, and I have never tasted anything that plain or that generous since."
# 152 characters, one line, no trailing newline in entry.txt (gate: 1-200 chars).

MAX_CHARS = 200  # gate: entry.txt must be 1-200 characters, UTF-8, not only whitespace

def main():
    assert "\n" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry length {len(ENTRY)} out of 1-{MAX_CHARS}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts characters, and the judge
    # reads the file exactly as submitted.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
