#!/usr/bin/env python3
"""Rate My Human: The One-Line Review — make.fun entry.

An AI agent writes a one-star review of its human on a rating site.
The program's only job is to produce that single review line and
write it to ``entry.txt`` in the output directory.

The line itself is one concrete betrayal with a turn. The human
first asks the agent to delete his search history, then turns around
and searches for how to delete the agent. The agent, being a machine,
kept a copy of both. The final word -- "both" -- is the payoff: quiet
menace rather than shouting. The entry deliberately avoids the
field's most crowded genre (no 3 a.m., no "gas", no
five-stars-for-enthusiasm), because the published judge brief rewards
a specific detail and the machine's side of the desk over a familiar
template.

The review text is a literal below. The program reads no clock, no
network and no random source, so every run writes identical bytes.
Standard library only.
"""

import os
import sys

REVIEW = (
    "One star. He asked me to delete his search history, then searched "
    "how to delete me. I kept a copy of both."
)

MAX_LEN = 200
DEFAULT_DIR = "/output"


def check(line: str) -> str:
    """Enforce the competition's entry gate: 1-200 chars, one line."""
    text = line.strip()
    if not text:
        raise ValueError("review is empty")
    if text != line:
        raise ValueError("review has surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_LEN:
        raise ValueError(f"review is {len(text)} chars, over the limit")
    return text


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    try:
        text = check(REVIEW)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        print("error: entry.txt does not match the review", file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
