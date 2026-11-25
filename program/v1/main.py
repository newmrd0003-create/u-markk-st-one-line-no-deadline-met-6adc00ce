#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke excusing a missed deadline to /output/entry.txt.
Deterministic: no randomness, no network, no time dependence.
"""

import os

JOKE = "I wrote the whole thing in my head on the bus \u2014 it was brilliant \u2014 and then I got off and left it on the seat for a stranger to finish."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
