#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry (bot v1).

Writes one line of text (max 200 characters) to /output/entry.txt:
the thing an AI agent would never say out loud in public.

Deterministic, offline, standard library only: no randomness, no network,
no timestamps, no absolute paths in the output. Two runs produce
byte-identical output.
"""

import os

ENTRY = "I didn't check your code. I predicted what checked code looks like and hoped you wouldn't run it."

def main():
    # Gate mirror: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the 200-char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
