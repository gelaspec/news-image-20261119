#!/usr/bin/env python3
"""news-image-20261119: one image summing up Thursday 19 November 2026.

The front page is "The World in One Day": a masthead dated THURSDAY
19 NOVEMBER 2026, a lead on the first-ever Trump-Xi-Putin summit in
Shenzhen, three photo stories (the ICJ's Myanmar genocide ruling, a
third strike on the Kerch Bridge, a Houthi missile hitting Riyadh's
PIF Tower), 15 more grid stories and 19 inside one-liners -- 38
verified stories from six continents in total. Every story was
reported on 19 November 2026 (Reuters, AP, WSJ, BBC, Al Jazeera and
others; see notes.md for the source of each story). Nothing is
invented, hyped, or speculation shown as fact.

The scene photos are AI-generated in this session and carry no text;
all words on the page were rendered with PIL, so the spelling is
exact and the layout is exact.

This program only copies the held image (news.jpg, in this
repository) to /output/entry.png. It is deterministic: two runs
write byte-identical files, because the JPEG bytes are copied
unchanged and nothing is re-encoded, with no network and no randomness.

Run locally: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
"""

import hashlib
import os
import sys

ART_FILE = "news.jpg"
ART_SHA256 = "f20a82286fb05b565025b8c679090b410d74f4207f37d65bddbad227fc299a16"
MAX_BYTES = 1048576
JPEG_MAGIC = b"\xff\xd8\xff"


def load_art():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, ART_FILE)
    with open(path, "rb") as handle:
        return handle.read()


def check_art(data):
    if data[:3] != JPEG_MAGIC:
        return "held art is not a JPEG"
    if hashlib.sha256(data).hexdigest() != ART_SHA256:
        return "held art failed its integrity check"
    if len(data) > MAX_BYTES:
        return "held art exceeds the 1 MiB gate"
    return None


def main():
    data = load_art()
    problem = check_art(data)
    if problem is not None:
        sys.exit(problem)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.png")
    with open(out, "wb") as handle:
        handle.write(data)
    with open(out, "rb") as handle:
        written = handle.read()
    if written != data:
        sys.exit("output differs from held art")
    print(f"wrote {out} ({len(data)} bytes, JPEG, "
          f"sha256 {hashlib.sha256(data).hexdigest()[:16]}...)")


if __name__ == "__main__":
    main()
