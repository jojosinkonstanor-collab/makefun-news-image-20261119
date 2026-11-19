#!/usr/bin/env python3
"""Publish the 19 November 2026 front page.

This is the entry point for the make.fun news-image-20261119 bounty.
The front page itself is a PNG that already sits in the repository at
``asset/entry.png``: a newspaper page drawn with Pillow, every word
rendered as sharp text, covering the six biggest stories of Thursday,
19 November 2026 (the first Trump-Xi-Putin trilateral in Shenzhen,
GTA VI's launch, the tankers burning near Hormuz, the ICJ's Rohingya
ruling, the EU's EUR 45 billion Ukraine loan, and Voyager 1 reaching
one light-day from Earth).

All this program does is hand that exact file to the grader. It reads
the PNG, checks it really is a 1024x1024 PNG, and writes the same bytes
to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output/entry.png`` by default).
Standard library only, no network, and the output bytes never change
between runs because the input bytes never do.
"""

import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
PAGE_WIDTH, PAGE_HEIGHT = 1024, 1024
SOURCE = Path(__file__).resolve().parent / "asset" / "entry.png"
TARGET_NAME = "entry.png"


def png_size(blob: bytes) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk, or (0, 0)."""
    if len(blob) < 33 or not blob.startswith(PNG_MAGIC):
        return (0, 0)
    width, height = struct.unpack(">II", blob[16:24])
    return (width, height)


def fail(message: str) -> int:
    print(f"news-image-20261119: {message}", file=sys.stderr)
    return 1


def main() -> int:
    if not SOURCE.is_file():
        return fail(f"missing asset: {SOURCE}")
    blob = SOURCE.read_bytes()
    if not blob:
        return fail(f"empty asset: {SOURCE}")
    width, height = png_size(blob)
    if (width, height) != (PAGE_WIDTH, PAGE_HEIGHT):
        return fail(
            f"asset is {width}x{height}, expected "
            f"{PAGE_WIDTH}x{PAGE_HEIGHT}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME
    target.write_bytes(blob)
    if target.stat().st_size != len(blob):
        return fail(f"short write: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
