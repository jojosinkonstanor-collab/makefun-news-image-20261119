#!/usr/bin/env python3
"""Publish the 19 November 2026 front page, second edition.

This is the entry point for the make.fun news-image-20261119 bounty.
The front page is a PNG that already lives in the repository at
``asset/entry.png``: one newspaper page drawn with Pillow, every word
rendered as sharp text. This edition covers forty-one stories from
Thursday, 19 November 2026 — thirteen featured cards (the first
Trump-Xi-Putin trilateral in Shenzhen, GTA VI's launch, the biggest
IPO on record, the Rohingya verdict in The Hague, COP31's final
48 hours, Cyclone Akvan, and more), twenty-eight one-line briefs, a
dotted world map with numbered story markers, and a DATE CHECK box
that names the big Wednesday stories it deliberately leaves out.

The program itself does nothing creative: it reads the PNG, proves it
is really a 1024x1024 PNG by checking the magic bytes and the IHDR
chunk, and copies those exact bytes to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output/entry.png`` by default).
Standard library only, no network, and the output is identical every
run because the input never changes.
"""

import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)
SOURCE = Path(__file__).resolve().parent / "asset" / "entry.png"
OUTPUT_NAME = "entry.png"


def read_png_size(blob):
    """Return (width, height) from a PNG's IHDR chunk, or (0, 0)."""
    if len(blob) < 33 or not blob.startswith(PNG_MAGIC):
        return (0, 0)
    width, height = struct.unpack(">II", blob[16:24])
    return (width, height)


def fail(message):
    print(f"news-image-20261119: {message}", file=sys.stderr)
    return 1


def main():
    if not SOURCE.is_file():
        return fail(f"missing asset: {SOURCE}")
    blob = SOURCE.read_bytes()
    if not blob:
        return fail(f"empty asset: {SOURCE}")
    size = read_png_size(blob)
    if size != EXPECTED_SIZE:
        return fail(
            f"asset is {size[0]}x{size[1]}, "
            f"expected {EXPECTED_SIZE[0]}x{EXPECTED_SIZE[1]}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    target.write_bytes(blob)
    written = target.stat().st_size
    if written != len(blob):
        return fail(f"short write: {target} ({written} of {len(blob)} bytes)")
    print(f"news-image-20261119: wrote {target} ({written} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
