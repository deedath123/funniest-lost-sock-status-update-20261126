#!/usr/bin/env python3
"""make.fun entry: Funniest Lost Sock Status Update.

Writes the entry text to /output/entry.txt.
Stdlib only; no network, no files read.
"""

import os

ENTRY = (
    "Update: I'm in the freezer. The peas unionised at 3am and "
    "voted me their blanket. I miss the drawer. Send a hairdryer."
)


def main() -> None:
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= 120, "entry exceeds 120 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
