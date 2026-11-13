"""Record-device adapters for fictional XXXVI word input and Nova byte input."""
from __future__ import annotations

from machina_xxxvi.assembler import text_codes
from machina_xxxvi.cvl54 import PAD, pack_codes
from machina_xxxvi.gateway import decode_cvl68


def for_xxxvi(record: bytes) -> tuple[int, ...]:
    """Translate one CVL-68/P0 record into 36-bit CVL-54/P0 words.

    Conversion is deliberately lossy for control/record metadata and rejects
    characters not representable by the legacy 6-bit printer. The caller
    mounts the resulting WORD stream; the old CPU still has word addresses.
    """
    if type(record) is not bytes:
        raise ValueError("record must contain CVL-68 bytes")
    codes = text_codes(decode_cvl68(record))
    padded = codes + [PAD] * (-len(codes) % 6)
    return tuple(pack_codes(padded[i:i+6]) for i in range(0, len(padded), 6))


def for_nova(record: bytes) -> bytes:
    """Preserve a CVL-68/P0 record byte-for-byte for Nova CAPTA."""
    if type(record) is not bytes:
        raise ValueError("record must contain CVL-68 bytes")
    decode_cvl68(record)  # strict assigned-character profile
    return record
