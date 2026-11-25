"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes one job title to /output/entry.txt: a single title, at most 60
characters, the weirdest one I can think of. The trick is a real-sounding
title with one hilariously specific twist — a senior vice president whose
whole job is apologizing to the office printer.
"""

import os

ENTRY = "Senior Vice President of Apologizing to the Office Printer"

MAX_CHARS = 60


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
