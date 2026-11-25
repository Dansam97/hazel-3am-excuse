#!/usr/bin/env python3
"""Entry for make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one line to entry.txt in the output directory: a hardware wallet's
excuse for refusing to sign a transaction at 3 AM, in the wallet's own voice.
"""

import os

TEXT = (
    "Access denied. I guard your keys from thieves, and at 3 AM the thief "
    "is you; sober-you left standing orders to lock you out until sunrise."
)


MAX_CHARS = 200


def render() -> str:
    """Return the entry text, validated against the competition gate."""
    text = TEXT.strip()
    if not text:
        raise ValueError("entry text must not be empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    text.encode("utf-8")  # raises if not encodable as UTF-8
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(render() + "\n")


if __name__ == "__main__":
    main()
