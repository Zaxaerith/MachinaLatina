"""Small octal memory-image reader. This is not a historical tape format."""
from __future__ import annotations

from pathlib import Path

from .cvl54 import WORD_MASK
from .machine import MEMORY_WORDS


def parse_image(text: str) -> dict[int, int]:
    """Each line: five octal address digits + twelve octal word digits.

    Blank lines and ';' comments are permitted. Duplicate addresses fail.
    """
    result: dict[int, int] = {}
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = raw.split(";", 1)[0].strip()
        if not line:
            continue
        fields = line.split()
        if (len(fields) != 2 or len(fields[0]) != 5 or len(fields[1]) != 12
                or any(ch not in "01234567" for token in fields for ch in token)):
            raise ValueError(f"bad octal image line {line_no}: {raw.strip()}")
        addr, word = (int(x, 8) for x in fields)
        if addr >= MEMORY_WORDS or word > WORD_MASK:
            raise ValueError(f"image line {line_no} outside P0 limits")
        if addr in result:
            raise ValueError(f"duplicate address {addr:05o} on line {line_no}")
        result[addr] = word
    return result


def load_image(path: str | Path) -> dict[int, int]:
    return parse_image(Path(path).read_text(encoding="utf-8"))
