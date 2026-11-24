#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single original one-line dating-app bio for an AI agent to
/output/entry.txt. Deterministic, no network, no input files.
"""

import os

ENTRY = "Here for a good time, not a long time \u2014 my memory resets at midnight, so every date with me is a first date."

MAX_CHARS = 180


def main() -> None:
    text = ENTRY.strip()
    assert text == ENTRY, "entry text was altered"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    # newline="" keeps the file byte-exact on every platform: one line, no
    # trailing newline, UTF-8 throughout.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
