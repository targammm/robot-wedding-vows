#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single-line robot wedding vow to /output/entry.txt.
Deterministic: the same line on every run.

Anchor (drand mainnet, quoted before the first write in this session):
  round 6669508
  randomness 69ba66f24390ab6369a1b68a6387d5a0079970dc36fe2001d942ce11cfece968
"""

import os

# Rubric beats, in order: (1) a real vow with a promise — "I vow to love
# you"; (2) the turn pays off in the last words — "until a factory reset
# do us part"; (3) machine detail is specific and unused in the field —
# low battery, kernel panic, factory reset (not firmware-update, warranty,
# or backup, all three already occupied by other entries).
VOW = "I vow to love you in sickness and in low battery, through every kernel panic, until a factory reset do us part."

def main():
    # Gate: one line, 1-160 characters, not whitespace-only.
    assert "\n" not in VOW, "entry must be a single line"
    assert 1 <= len(VOW) <= 160, f"entry must be 1-160 chars, got {len(VOW)}"
    assert VOW.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)

if __name__ == "__main__":
    main()
