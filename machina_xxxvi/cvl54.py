"""Provisional six-bit CVL-54/P0 printer and word packing.

Not a real ancient standard. See specifications/CVL-54-P0.md.
"""
from __future__ import annotations

LATIN = "ABCDEFGHIKLMNOPQRSTVXYZ"
GREEK = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
SHARED = {**{25 + i: c for i, c in enumerate("0123456789")},
          **dict(enumerate(" ., :;+ -*/=()?".replace(" ", ""), start=999))}
# Fixed assignments from CVL-54/P0; avoid relying on dictionary insertion order.
SHARED = {
    **{25 + i: c for i, c in enumerate("0123456789")},
    **{35 + i: c for i, c in enumerate(" .,:;+-*/=()?")},
}
PAD, SHIFT_LAT, SHIFT_GRC, LF, CR, EOT = 0, 48, 49, 50, 51, 52
WORD_MASK = (1 << 36) - 1


class CharacterFault(ValueError):
    """Undefined or ill-formed CVL-54/P0 code stream."""


def pack_codes(codes: list[int] | tuple[int, ...]) -> int:
    """Pack exactly six 0..63 six-bit symbols, first symbol in top six bits."""
    if len(codes) != 6 or any(type(c) is not int or not 0 <= c < 64 for c in codes):
        raise ValueError("expected exactly six 6-bit integer symbols")
    result = 0
    for code in codes:
        result = (result << 6) | code
    return result


def unpack_codes(word: int) -> tuple[int, ...]:
    if type(word) is not int or not 0 <= word <= WORD_MASK:
        raise ValueError("word must be an unsigned 36-bit integer")
    return tuple((word >> shift) & 63 for shift in range(30, -1, -6))


class Printer:
    """Stateful Latin/Greek terminal; one EMIT sends six code symbols.

    PAD is allowed only as a suffix in the final emitted word of the run.
    A further EMIT after padding is a CharacterFault. This deliberately
    restricts the provisional P0 profile; no tape record framing is implied.
    """

    def __init__(self) -> None:
        self.page = "LATINA"
        self.parts: list[str] = []
        self.padded = False

    @property
    def text(self) -> str:
        return "".join(self.parts)

    def feed_word(self, word: int) -> None:
        codes = unpack_codes(word)
        if self.padded:
            raise CharacterFault("text after final-word PAD")
        page = self.page
        local: list[str] = []
        padding = False
        for c in codes:
            if c == PAD:
                padding = True
                continue
            if padding:
                raise CharacterFault("non-padding code after PAD within a word")
            if c == SHIFT_LAT:
                page = "LATINA"
            elif c == SHIFT_GRC:
                page = "GRAECA"
            elif c == LF:
                local.append("\n")
            elif c == CR:
                local.append("\r")
            elif c == EOT:
                page = "LATINA"
            elif c in SHARED:
                local.append(SHARED[c])
            elif 1 <= c <= 23:
                local.append((LATIN if page == "LATINA" else GREEK)[c - 1])
            elif c == 24 and page == "GRAECA":
                local.append("Ω")
            else:
                raise CharacterFault(f"undefined CVL-54 symbol {c:02o} in {page}")
        self.page = page
        self.padded = padding
        self.parts.extend(local)
