"""Experimental CVL-54/P0 -> CVL-68 direct-byte gateway (lossy metadata)."""
from __future__ import annotations
from collections.abc import Iterable
from .cvl54 import GREEK, LATIN, Printer

PUNCTUATION = " .,:;+-*/=()?"
DIACRITICS = {
    "\u0301": 0xB8, "\u0300": 0xB9, "\u0342": 0xBA,
    "\u0313": 0xBB, "\u0314": 0xBC, "\u0345": 0xBD,
    "\u0308": 0xBE, "\u0304": 0xBF,
}
CHAR_TO_BYTE: dict[str,int] = {
    **{c: 0x41+i for i,c in enumerate(LATIN)},
    **{c: 0x61+i for i,c in enumerate(LATIN.lower())},
    **{c: 0x80+i for i,c in enumerate(GREEK)},
    **{c: 0xA0+i for i,c in enumerate(GREEK.lower())},
    **{c:ord(c) for c in "0123456789"+PUNCTUATION},
    **DIACRITICS,
    "ς":0x98, "\n":0x0A, "\r":0x0D,
}
BYTE_TO_CHAR = {value:key for key,value in CHAR_TO_BYTE.items()}
assert len(BYTE_TO_CHAR) == len(CHAR_TO_BYTE), "duplicate CVL-68 candidate code"

class GatewayError(ValueError):
    """Character unrepresentable in the assigned CVL-68/P0 subset."""

def encode_cvl68(text:str)->bytes:
    """Encode exact, already-decomposed characters; no Unicode normalization."""
    out=bytearray()
    for position,c in enumerate(text):
        try:out.append(CHAR_TO_BYTE[c])
        except KeyError as exc:
            raise GatewayError(f"unrepresentable CVL-68/P0 character at {position}: {c!r}") from exc
    return bytes(out)

def decode_cvl68(data:bytes)->str:
    """Decode only the subset assigned above; RESERVED/control bytes are errors."""
    try:return "".join(BYTE_TO_CHAR[c] for c in data)
    except KeyError as exc:
        raise GatewayError(f"unassigned CVL-68/P0 byte: {exc.args[0]:02X}") from exc

def transcode_words(words:Iterable[int])->bytes:
    """Decode one CVL-54/P0 logical record and produce CVL-68/P0 bytes.

    Drops shift events, PAD and EOT/record-boundary information; it does NOT
    preserve original 36-bit packing or distinguish old terminal controls.
    """
    terminal=Printer()
    for word in words:
        terminal.feed_word(word)
    return encode_cvl68(terminal.text)
