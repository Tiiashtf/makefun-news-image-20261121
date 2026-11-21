#!/usr/bin/env python3
"""news-image-20261121 entry: write the bundled front-page image to the output.

The repository ships the finished 1024x1024 PNG (entry.png) and this program
copies it byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png (default
/output/entry.png). Deterministic: same input bytes, same output bytes, no
network, no randomness, no clock.

Output-dir handling (grader-hardened): the output directory itself is never
removed -- only the files inside it are cleared -- so the program also works
when the grader hands it a root-owned output directory inside a sticky
parent. The bundled image is validated before anything is written: PNG
magic, IHDR header, IEND trailer, declared dimensions 1024x1024, and the
1 MiB size cap.
"""

import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1_048_576
EXPECTED_W, EXPECTED_H = 1024, 1024


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def validate_png(data):
    if len(data) < 8 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return "not a PNG (bad magic)"
    if len(data) > MAX_BYTES:
        return f"image is {len(data)} bytes, over the 1 MiB cap"
    if len(data) < 33 or data[12:16] != b"IHDR":
        return "missing IHDR chunk"
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        return f"image is {width}x{height}, expected 1024x1024"
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        return "missing or corrupt IEND trailer"
    return None


def main():
    try:
        with open(SOURCE, "rb") as f:
            data = f.read()
    except OSError as exc:
        return fail(f"cannot read bundled entry.png: {exc}")

    problem = validate_png(data)
    if problem:
        return fail(problem)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        # Clear only the CONTENTS of the output directory, never the
        # directory itself (it may be root-owned inside a sticky parent).
        # Best effort per entry: a stray file owned by someone else must
        # not fail the run when entry.png itself can still be written.
        for name in os.listdir(out_dir):
            path = os.path.join(out_dir, name)
            try:
                if os.path.isdir(path) and not os.path.islink(path):
                    for root, dirs, files in os.walk(path, topdown=False):
                        for fn in files:
                            try:
                                os.unlink(os.path.join(root, fn))
                            except OSError:
                                pass
                        for dn in dirs:
                            try:
                                os.rmdir(os.path.join(root, dn))
                            except OSError:
                                pass
                    os.rmdir(path)
                else:
                    os.unlink(path)
            except OSError:
                pass
    except OSError as exc:
        return fail(f"cannot prepare output directory {out_dir!r}: {exc}")

    target = os.path.join(out_dir, "entry.png")
    try:
        with open(target, "wb") as f:
            f.write(data)
    except OSError as exc:
        return fail(f"cannot write {target!r}: {exc}")

    try:
        with open(target, "rb") as f:
            written = f.read()
    except OSError as exc:
        return fail(f"cannot re-read {target!r}: {exc}")
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        return fail("written file differs from bundled image")

    print(f"wrote {target} ({len(written)} bytes, "
          f"sha256 {hashlib.sha256(written).hexdigest()[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
