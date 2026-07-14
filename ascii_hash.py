#!/usr/bin/env python3
import sys
import hashlib

FILLED = "#"
EMPTY = " "

def tar_identicon(path, out_path, size=17):
    with open(path, "rb") as f:
        data = f.read()

    digest = hashlib.sha256(data).digest()

    bits = []
    for b in digest:
        for i in range(8):
            bits.append((b >> i) & 1)

    half = size // 2 + size % 2
    idx = 0
    lines = []

    for _ in range(size):
        row_half = []
        for _ in range(half):
            bit = bits[idx % len(bits)]
            idx += 1
            row_half.append(FILLED if bit else EMPTY)

        if size % 2:
            row = row_half + row_half[:-1][::-1]
        else:
            row = row_half + row_half[::-1]

        lines.append("".join(row))

    with open(out_path, "w") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    if len(sys.argv) < 3:
        print("usage: tar_identicon.py archive.tar output.txt [size]")
        sys.exit(1)

    tar_path = sys.argv[1]
    out_path = sys.argv[2]
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 17

    tar_identicon(tar_path, out_path, size)

if __name__ == "__main__":
    main()
