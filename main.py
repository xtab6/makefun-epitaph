#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is a dying person's will, spoken as last words: the whole estate
goes to the cat, because the cat earned it — and the reader did not. A
genuine joke with a surprise twist, short enough to carve in stone and
quotable enough to repeat to a friend.
"""

import os

LINE = "I leave everything to my cat. She earned it. You didn't."


def main():
    # Gate: the entry must be UTF-8 text of 1 to 150 characters, not
    # only whitespace. Refuse to write an invalid line rather than
    # hand the grader one.
    if not 1 <= len(LINE) <= 150 or not LINE.strip():
        raise SystemExit("entry line fails the 1-150 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
