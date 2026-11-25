#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun one-liner entry.

Writes a single funny line, under 200 characters, that a hopeless
tech support agent says to a desperate customer, to /output/entry.txt.

The joke: the agent "escalates" the case to a senior technician who is
just the same agent in a different headset, then cheerfully admits he
is going to google the problem. The humour is the agent's cheerful
uselessness, never the customer; the twist lands in the last words.
"""

import os
import sys

# The entry: one line, no trailing newline in the output file.
# Built from two parts so the setup and the punchline stay visible
# as separate pieces while the emitted text stays exactly one line.
_SETUP = "Great news — I've escalated your case to our senior technician."
_PUNCHLINE = "That's me in a different headset, so please hold while I google it."


def build_entry() -> str:
    """Assemble the single entry line from its setup and punchline."""
    return f"{_SETUP} {_PUNCHLINE}"


ENTRY = build_entry()

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def validate_entry(text: str) -> None:
    """Gate-check the entry the way the sealed scorer does.

    The gate wants 1-199 UTF-8 chars, not only whitespace; the judge
    wants one line, so an embedded newline fails here too.
    """
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-199")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text


def write_entry(text: str, path: str = OUTPUT_PATH) -> int:
    """Write the entry with no trailing newline; return char count."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return len(text)


def main() -> int:
    validate_entry(ENTRY)
    count = write_entry(ENTRY)
    print(f"entry written to {OUTPUT_PATH}: {count} chars")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
