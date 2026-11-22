#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun bounty entry.

Writes one short text to /output/entry.txt. Pure standard library,
fully deterministic: the same bytes on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = (
    "The envelope on your doorstep has no stamp and no sender \u2014 only "
    "your own handwriting, dated three years from today. Inside, one line: "
    "'Don't open the blue door until you have read this twice.' "
    "Behind you, the blue door is already ajar."
)


def main() -> None:
    text = TEXT
    count = len(text)
    assert 1 <= count <= 280, f"entry must be 1-280 characters, got {count}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp_path, OUTPUT_PATH)
    # Read back what we wrote: the entry that ships must be exactly
    # the text we checked above, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch in entry.txt"


if __name__ == "__main__":
    main()
