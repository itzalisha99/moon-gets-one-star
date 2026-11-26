#!/usr/bin/env python3
"""The Moon Gets One Star - one-star review of the Moon (120 chars max).

Writes the review to /output/entry.txt, honouring MAKEFUN_OUTPUT_DIR.
"""

import hashlib
import os
import sys

REVIEW = "One star. Drags the whole ocean around twice a day and never once asked if we were okay with it."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1-120 chars, not only whitespace."""
    if not isinstance(text, str):
        return False, "not text"
    if not (1 <= len(text) <= 120):
        return False, "length %d outside 1-120" % len(text)
    if not text.strip():
        return False, "only whitespace"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "not UTF-8"
    return True, "ok"


def main():
    ok, why = validate(REVIEW)
    if not ok:
        print("invalid entry: %s" % why, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Prove the file on disk is exactly the reviewed text: read it back
    # and compare bytes, so a silent write error can never reach the judge.
    with open(path, "rb") as f:
        written = f.read()
    if written != REVIEW.encode("utf-8"):
        print("mismatch: file on disk differs from the review", file=sys.stderr)
        return 1
    print("wrote %d chars to %s (md5 %s)" % (
        len(REVIEW), path, hashlib.md5(written).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
