"""Modern, sparse hex-byte memory image format; not a historical binary ABI."""
from __future__ import annotations

import re
from pathlib import Path

from .cpu import ADDRESS_MAX, encode_instruction

DATA_BASE = 0x100
GREETING = bytes.fromhex("52 41 4B 54 45 20 8A 8E 82 8E 91")
_HEX2 = re.compile(r"[0-9a-fA-F]{2}\Z")
_HEX6 = re.compile(r"[0-9a-fA-F]{6}\Z")


def greeting_image() -> dict[int, bytes]:
    """A distinct Nova program: eleven address-direct byte emits, then FIN."""
    instructions = b"".join(encode_instruction(0x50, DATA_BASE + i)
                            for i in range(len(GREETING))) + encode_instruction(0)
    return {0: instructions, DATA_BASE: GREETING}


def parse_image(text: str) -> dict[int, bytes]:
    """Hex-byte records: 000000: 50 00 01 00 ; comment. Overlaps fail."""
    regions: dict[int, bytes] = {}
    occupied: set[int] = set()
    for lineno, original in enumerate(text.splitlines(), 1):
        line = original.split(";", 1)[0].strip()
        if not line:
            continue
        if line.count(":") != 1:
            raise ValueError(f"line {lineno}: expected ADDRESS: HEXBYTES")
        address_text, tail = (p.strip() for p in line.split(":", 1))
        values = tail.split()
        if not _HEX6.fullmatch(address_text) or not values or any(not _HEX2.fullmatch(v) for v in values):
            raise ValueError(f"line {lineno}: invalid hex-byte memory-image row")
        address = int(address_text, 16)
        payload = bytes(int(v, 16) for v in values)
        if address > ADDRESS_MAX or len(payload) > ADDRESS_MAX + 1 - address:
            raise ValueError(f"line {lineno}: segment extends beyond 24-bit address space")
        keys = range(address, address + len(payload))
        if any(k in occupied for k in keys):
            raise ValueError(f"line {lineno}: overlapping memory-image data")
        occupied.update(keys)
        regions[address] = payload
    return regions


def format_image(regions: dict[int, bytes], row_width: int = 16) -> str:
    if type(row_width) is not int or row_width < 1:
        raise ValueError("row_width must be positive")
    rows: list[str] = []
    for address, data in sorted(regions.items()):
        if type(address) is not int or address < 0 or address > ADDRESS_MAX:
            raise ValueError("address out of bounds")
        if not isinstance(data, bytes) or not data or len(data) > ADDRESS_MAX + 1 - address:
            raise ValueError("invalid segment")
        for index in range(0, len(data), row_width):
            chunk = data[index:index + row_width]
            rows.append(f"{address + index:06X}: " + " ".join(f"{b:02X}" for b in chunk))
    return "\n".join(rows) + ("\n" if rows else "")


def read_image(path: str | Path) -> dict[int, bytes]:
    return parse_image(Path(path).read_text(encoding="utf-8"))
