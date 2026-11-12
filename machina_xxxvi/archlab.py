"""Phase VII candidate memory layouts: 36-bit retrofit versus byte-addressed Nova.

A present-day laboratory for fictional machine families, *not* a Nova CPU emulator.
"""
from __future__ import annotations

from dataclasses import dataclass

LEGACY_WORD_BITS = 36
LEGACY_WORDS = 1 << 15
RETROFIT_BYTES_PER_WORD = 4
RETROFIT_DATA_BITS = 32
NOVA_ARCH_ADDRESS_BITS = 24
NOVA_WORD_BITS = 32
DEFAULT_NOVA_INSTALLED_BYTES = 256 * 1024


@dataclass(frozen=True)
class RetrofitRecord:
    """The new text payload held in old 36-bit data words.

    Payload occupies bits 35..4. Bits 3..0 are zero in R0. Length is
    external record metadata, necessary to distinguish NUL from padding.
    """
    words: tuple[int, ...]
    logical_bytes: int

    def to_bytes(self) -> bytes:
        if not isinstance(self.logical_bytes, int) or isinstance(self.logical_bytes, bool):
            raise ValueError("logical_bytes must be an integer")
        if self.logical_bytes < 0 or self.logical_bytes > len(self.words) * 4:
            raise ValueError("logical byte count exceeds stored payload")
        if len(self.words) != (self.logical_bytes + 3) // 4:
            raise ValueError("non-canonical number of 36-bit words")
        raw = bytearray()
        for word in self.words:
            if type(word) is not int or not 0 <= word < (1 << LEGACY_WORD_BITS):
                raise ValueError("invalid 36-bit retrofit word")
            if word & 0xF:
                raise ValueError("nonzero reserved low nibble")
            raw.extend((word >> 4).to_bytes(4, "big"))
        if any(raw[self.logical_bytes:]):
            raise ValueError("nonzero trailing filler bytes")
        return bytes(raw[:self.logical_bytes])


def retrofit_pack(data: bytes) -> RetrofitRecord:
    """Pack arbitrary bytes, *not only* assigned CVL-68 characters, R0 policy."""
    if not isinstance(data, bytes):
        raise TypeError("retrofit_pack requires immutable bytes")
    if len(data) > LEGACY_WORDS * RETROFIT_BYTES_PER_WORD:
        raise ValueError("payload exceeds a full 32K-word retrofit memory")
    words = []
    for i in range(0, len(data), 4):
        chunk = data[i:i + 4].ljust(4, b"\0")
        words.append(int.from_bytes(chunk, "big") << 4)
    return RetrofitRecord(tuple(words), len(data))


class NovaMemory:
    """Nova-N0 *memory-only* proposal: 24-bit byte-address space, 32-bit words.

    N0 chooses big-endian word serialization and 4-byte aligned word accesses.
    These are research hypotheses, not historical necessities or an ISA.
    """

    def __init__(self, installed_bytes: int = DEFAULT_NOVA_INSTALLED_BYTES) -> None:
        if (type(installed_bytes) is not int or not 0 < installed_bytes <= (1 << NOVA_ARCH_ADDRESS_BITS)):
            raise ValueError("installed memory must fit 24-bit byte addresses")
        self.data = bytearray(installed_bytes)

    def _range(self, address: int, size: int) -> None:
        if type(address) is not int or type(size) is not int or size < 0:
            raise ValueError("address/size must be nonnegative integers")
        if address < 0 or address > len(self.data) or size > len(self.data) - address:
            raise ValueError("memory byte range is out of bounds")

    def load(self, address: int, data: bytes) -> None:
        if not isinstance(data, bytes):
            raise TypeError("load requires bytes")
        self._range(address, len(data))
        self.data[address:address + len(data)] = data

    def read_bytes(self, address: int, length: int) -> bytes:
        self._range(address, length)
        return bytes(self.data[address:address + length])

    def read_byte(self, address: int) -> int:
        self._range(address, 1)
        return self.data[address]

    def write_byte(self, address: int, value: int) -> None:
        self._range(address, 1)
        if type(value) is not int or not 0 <= value <= 255:
            raise ValueError("byte must be an integer from 0 to 255")
        self.data[address] = value

    def read_word32(self, address: int) -> int:
        if type(address) is not int or address % 4:
            raise ValueError("32-bit word access requires four-byte alignment")
        return int.from_bytes(self.read_bytes(address, 4), "big")

    def write_word32(self, address: int, value: int) -> None:
        if type(address) is not int or address % 4:
            raise ValueError("32-bit word access requires four-byte alignment")
        if type(value) is not int or not 0 <= value < (1 << NOVA_WORD_BITS):
            raise ValueError("invalid 32-bit unsigned word")
        self.load(address, value.to_bytes(4, "big"))


def demo() -> str:
    # Candidate CVL-68 bytes from the previously documented 2026 draft.
    data = bytes.fromhex("52 41 4B 54 45 20 8A 8E 82 8E 91")
    r = retrofit_pack(data)
    nova = NovaMemory()
    base = 0x100
    nova.load(base, r.to_bytes())
    assert nova.read_byte(base + 6) == 0x8A
    assert nova.read_bytes(base, len(data)) == data
    words = " ".join(f"{word:012o}" for word in r.words)
    return (f"CVL-68 candidate: {data.hex(' ').upper()}\n"
            f"XXXVI-R0 36-bit words (octal): {words}\n"
            f"Nova-N0 byte address 0x{base+6:06X}: 0x{nova.read_byte(base+6):02X}\n"
            f"Recovered bytes: {nova.read_bytes(base,len(data)).hex(' ').upper()}")


if __name__ == "__main__":
    print(demo())
