"""Small two-pass P0 assembler; modern developer convenience, not a 1954 artifact."""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass

from .cvl54 import GREEK, LATIN, PAD, SHARED, SHIFT_GRC, SHIFT_LAT, pack_codes
from .machine import ADDRESS_MASK, MEMORY_WORDS, OPCODES, encode_instruction

LABEL = re.compile(r"^[ABCDEFGHIKLMNOPQRSTVXYZ][ABCDEFGHIKLMNOPQRSTVXYZ0-9]{0,5}$")
OCTAL = re.compile(r"^[0-7]+$")
LABEL_PREFIX = re.compile(r"^([A-Z0-9]+):(?:\s*|$)")
OP_NUM = {name: number for number, name in OPCODES.items()}
SHARED_CODE = {value: key for key, value in SHARED.items()}
INDEX_TAG = {"X1": 1, "X2": 2, "X3": 4}


class AssemblyError(ValueError):
    """Source-location-tagged error in P0 assembly."""


@dataclass(frozen=True)
class Entry:
    line: int
    address: int
    command: str
    operand: str
    size: int


def _fail(line: int, reason: str) -> None:
    raise AssemblyError(f"line {line}: {reason}")


def _octal(value: str, line: int, max_value: int) -> int:
    if not OCTAL.fullmatch(value):
        _fail(line, f"expected octal number: {value!r}")
    number = int(value, 8)
    if number > max_value:
        _fail(line, f"octal value out of range: {value!r}")
    return number


def _literal(text: str, line: int) -> str:
    try:
        value = ast.literal_eval(text)
    except (ValueError, SyntaxError, TypeError) as exc:
        _fail(line, f"invalid quoted TEX string: {exc}")
    if not isinstance(value, str) or not value:
        _fail(line, "TEX requires a nonempty quoted string")
    return value


def text_codes(text: str) -> list[int]:
    """Translate a single literal, assuming the output page initially LATINA.

    Does not prepend SHIFT_LAT or append EOT. Its caller must ensure the
    printer is in LATINA when the first word is emitted.
    """
    page = "LATINA"
    result: list[int] = []
    for char in text:
        if char in SHARED_CODE:
            result.append(SHARED_CODE[char])
        elif char in LATIN:
            if page != "LATINA":
                result.append(SHIFT_LAT)
                page = "LATINA"
            result.append(LATIN.index(char) + 1)
        elif char in GREEK:
            if page != "GRAECA":
                result.append(SHIFT_GRC)
                page = "GRAECA"
            result.append(GREEK.index(char) + 1)
        elif char == "\n":
            result.append(50)
        elif char == "\r":
            result.append(51)
        else:
            raise ValueError(f"unsupported CVL-54/P0 text character {char!r}")
    return result


def _resolve(token: str, symbols: dict[str, int], line: int) -> int:
    if OCTAL.fullmatch(token):
        return _octal(token, line, ADDRESS_MASK)
    if not LABEL.fullmatch(token):
        _fail(line, f"invalid address or label {token!r}")
    if token not in symbols:
        _fail(line, f"undefined label {token}")
    return symbols[token]


def _parse_operand(op: str, operand: str, symbols: dict[str, int], line: int) -> tuple[int, int]:
    if op == "FIN":
        if operand:
            _fail(line, "FIN takes no operands")
        return 0, 0
    if op == "PONX":
        fields = [v.strip() for v in operand.split(",")]
        if len(fields) != 2 or fields[0] not in INDEX_TAG:
            _fail(line, "PONX syntax is PONX X1,ADDRESS (or X2/X3)")
        return _resolve(fields[1], symbols, line), INDEX_TAG[fields[0]]
    if not operand:
        _fail(line, f"{op} requires an operand")
    if op == "NVM":
        if "+" in operand or "," in operand:
            _fail(line, "NVM takes an unindexed 15-bit literal")
        return _resolve(operand, symbols, line), 0
    indexed = re.fullmatch(r"(X[123])\+([A-Z0-9]+)", operand)
    if indexed:
        return _resolve(indexed.group(2), symbols, line), INDEX_TAG[indexed.group(1)]
    if "," in operand or "+" in operand:
        _fail(line, f"invalid indexed address: {operand!r}")
    return _resolve(operand, symbols, line), 0


def assemble(source: str) -> dict[int, int]:
    """Assemble ORG, VER, TEX and ten P0 opcodes into a sparse word image.

    Literals and ORG addresses are octal; labels are <=6 Classical Latin letters
    and decimal digits (starting with a letter). Returns a dict of word addresses
    to unsigned 36-bit words. Detects overlapping locations and invalid operands.
    """
    symbols: dict[str, int] = {}
    entries: list[Entry] = []
    position = 0
    for line_no, original in enumerate(source.splitlines(), 1):
        line = original.split(";", 1)[0].strip()
        if not line:
            continue
        labeled = LABEL_PREFIX.match(line)
        if labeled:
            name = labeled.group(1)
            if not LABEL.fullmatch(name):
                _fail(line_no, f"invalid label {name!r} (1–6 Classical Latin characters/digits)")
            if name in symbols:
                _fail(line_no, f"duplicate label {name}")
            symbols[name] = position
            line = line[labeled.end():].strip()
            if not line:
                continue
        fields = line.split(maxsplit=1)
        command = fields[0].upper()
        operand = fields[1].strip() if len(fields) > 1 else ""
        if command == "ORG":
            position = _octal(operand, line_no, ADDRESS_MASK)
            if labeled:
                _fail(line_no, "label must not precede ORG")
            continue
        if command == "VER":
            codes = [part.strip() for part in operand.split(",")]
            if len(codes) != 6:
                _fail(line_no, "VER requires exactly six octal codes")
            for c in codes:
                _octal(c, line_no, 63)
            size = 1
        elif command == "TEX":
            try:
                codes = text_codes(_literal(operand, line_no))
            except ValueError as exc:
                _fail(line_no, str(exc))
            size = (len(codes) + 5) // 6
        elif command in OP_NUM:
            size = 1
        else:
            _fail(line_no, f"unknown mnemonic/directive {command!r}")
        if position + size > MEMORY_WORDS:
            _fail(line_no, "statement crosses the end of addressable memory")
        entries.append(Entry(line_no, position, command, operand, size))
        position += size

    words: dict[int, int] = {}
    for item in entries:
        if item.command == "VER":
            values = [_octal(c.strip(), item.line, 63) for c in item.operand.split(",")]
            produced = [pack_codes(values)]
        elif item.command == "TEX":
            codes = text_codes(_literal(item.operand, item.line))
            padded = codes + [PAD] * (-len(codes) % 6)
            produced = [pack_codes(padded[i:i+6]) for i in range(0, len(padded), 6)]
        else:
            adr, tag = _parse_operand(item.command, item.operand, symbols, item.line)
            produced = [encode_instruction(OP_NUM[item.command], adr, tag)]
        for offset, word in enumerate(produced):
            addr = item.address + offset
            if addr in words:
                _fail(item.line, f"address {addr:05o} overlaps an earlier statement")
            words[addr] = word
    return words


def format_image(words: dict[int, int]) -> str:
    """Render the modern P0 textual memory-image format."""
    return "".join(f"{addr:05o} {word:012o}\n" for addr, word in sorted(words.items()))
