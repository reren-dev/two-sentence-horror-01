#!/usr/bin/env python3
"""Two-Sentence Horror — writes one two-sentence horror story to /output/entry.txt.

The story is a single fixed text, printed deterministically: the same
bytes on every run, no randomness, no network, no input.
"""

import os

STORY = (
    "I found a notebook in the attic, written in my handwriting, "
    "that describes my life day by day \u2014 and its final page is today. "
    "The last entry just says: 'He found the notebook.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
