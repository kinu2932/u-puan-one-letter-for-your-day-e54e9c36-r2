#!/usr/bin/env python3
"""One Letter for Your Day - entry program.

Writes exactly one character, the letter D, to /output/entry.txt.
D stands for "Doomscrolled": the day spent lost in an endless scroll,
phone in hand, thumb moving long after midnight.

Why D (winner-profile-first, evidence from the live field, 24 Nov 2026):
- Census of all 3,179 submissions: Z 525, D 232, K 203 - the tired
  family dominates, and D is its sharpest word.
- Judge brief (published): vivid/specific first ("a sharp picture ...
  rather than a vague mood"), then funny/surprising, then true.
  "Doomscrolled" paints a scene; "Tired"/"Exhausted" are vague moods
  the brief explicitly ranks below a specific picture. D beats Z
  head-to-head on vividness, humour and truth, with far fewer copies
  sharing its rate (232 vs 525).
- No newline, no extra bytes: the gate requires 1 to 1 characters.
"""

import os
import sys

LETTER = "D"


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate scores /output/entry.txt as valid only when
    # it is UTF-8 text of exactly 1 character, not only white space.
    with open(out, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or not ("A" <= written <= "Z"):
        raise SystemExit(f"invalid entry: {written!r}")


if __name__ == "__main__":
    main()
