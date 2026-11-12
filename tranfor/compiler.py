"""TRANFOR/P0: tiny, straight-line, dual-target scientific language experiment.

All syntax and semantics are modern fictional research proposals, not historical
Latin or a real 1950s compiler. No I/O normalization or implicit transliteration.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass

from machina_xxxvi.assembler import text_codes
from machina_xxxvi.cvl54 import PAD, pack_codes
from machina_xxxvi.gateway import encode_cvl68, decode_cvl68
from machina_xxxvi.machine import Machine, encode_instruction as encode_old
from machina_nova.cpu import NovaCPU, encode_instruction as encode_nova

LATIN = "ABCDEFGHIKLMNOPQRSTVXYZ"
IDENT = re.compile(rf"[{LATIN}][{LATIN}0-9]{{0,5}}\Z")
NAT15_MAX = (1 << 15) - 1
OLD_MEM = 1 << 15
NOVA_INSTALLED = 256 * 1024


class TranforError(ValueError):
    """A source error with a source line or resource explanation."""


@dataclass(frozen=True)
class Statement:
    kind: str
    target: str = ""
    left: str = ""
    right: str = ""
    operator: str = ""
    value: int = 0
    text: str = ""


@dataclass(frozen=True)
class Compilation:
    old_words: dict[int, int]
    old_variables: dict[str, int]
    nova_regions: dict[int, bytes]
    nova_variables: dict[str, int]
    expected_values: dict[str, int]
    expected_text: str


def _strip_comment(line: str) -> str:
    """Remove ';' only outside quoted string; honor Python backslash escapes."""
    quote = ""
    escaped = False
    for index, char in enumerate(line):
        if escaped:
            escaped = False
            continue
        if quote and char == "\\":
            escaped = True
        elif quote and char == quote:
            quote = ""
        elif not quote and char in "\"'":
            quote = char
        elif not quote and char == ";":
            return line[:index]
    return line


def _identifier(name: str, line_number: int) -> str:
    if not IDENT.fullmatch(name):
        raise TranforError(f"line {line_number}: invalid Classical Latin identifier {name!r}")
    return name


def parse(source: str) -> tuple[list[Statement], dict[str, int], str]:
    statements: list[Statement] = []
    values: dict[str, int] = {}
    text_parts: list[str] = []
    in_text = False
    ended = False
    for lineno, raw in enumerate(source.splitlines(), 1):
        line = _strip_comment(raw).strip()
        if not line:
            continue
        if ended:
            raise TranforError(f"line {lineno}: statement after FINIS")
        if line == "FINIS":
            ended = True
            continue
        if line.startswith("SCRIBE "):
            in_text = True
            literal = line[len("SCRIBE "):].strip()
            try:
                text = ast.literal_eval(literal)
            except (SyntaxError, ValueError, TypeError) as exc:
                raise TranforError(f"line {lineno}: invalid SCRIBE string: {exc}") from exc
            if not isinstance(text, str):
                raise TranforError(f"line {lineno}: SCRIBE requires a quoted string")
            try:
                text_codes(text)
                encode_cvl68(text)
            except ValueError as exc:
                raise TranforError(f"line {lineno}: text outside shared CVL-54/P0 and CVL-68 subset: {exc}") from exc
            statements.append(Statement("SCRIBE", text=text))
            text_parts.append(text)
            continue
        if in_text:
            raise TranforError(f"line {lineno}: numeric work after SCRIBE is not in TRANFOR/P0")
        match = re.fullmatch(r"DATVM\s+(\S+)\s*=\s*([0-9]+)", line)
        if match:
            name = _identifier(match[1], lineno)
            if name in values:
                raise TranforError(f"line {lineno}: duplicate variable {name}")
            value = int(match[2], 10)
            if value > NAT15_MAX:
                raise TranforError(f"line {lineno}: NAT15 literal exceeds {NAT15_MAX}")
            values[name] = value
            statements.append(Statement("DATVM", target=name, value=value))
            continue
        match = re.fullmatch(r"CALCVLA\s+(\S+)\s*=\s*(\S+)\s*([+-])\s*(\S+)", line)
        if match:
            name = _identifier(match[1], lineno)
            left = _identifier(match[2], lineno)
            right = _identifier(match[4], lineno)
            if name in values:
                raise TranforError(f"line {lineno}: duplicate variable {name}")
            if left not in values or right not in values:
                raise TranforError(f"line {lineno}: operand must be a previously defined variable")
            op = match[3]
            result = values[left] + values[right] if op == "+" else values[left] - values[right]
            if not 0 <= result <= NAT15_MAX:
                raise TranforError(f"line {lineno}: expression outside portable NAT15 domain")
            values[name] = result
            statements.append(Statement("CALCVLA", target=name, left=left,
                                        right=right, operator=op))
            continue
        raise TranforError(f"line {lineno}: unknown TRANFOR/P0 statement {line!r}")
    if not ended:
        raise TranforError("missing FINIS")
    return statements, values, "".join(text_parts)


def compile_source(source: str) -> Compilation:
    statements, values, text = parse(source)
    numeric = [stmt for stmt in statements if stmt.kind != "SCRIBE"]
    old_codes = text_codes(text)
    new_codes = encode_cvl68(text)
    old_text_words = (len(old_codes) + 5) // 6
    old_steps = sum(2 if s.kind == "DATVM" else 3 for s in numeric) + old_text_words + 1
    nova_steps = sum(2 if s.kind == "DATVM" else 3 for s in numeric) + len(new_codes) + 1
    old_var_start = max(0o100, old_steps)
    nova_var_start = max(0x100, nova_steps * 4)
    if old_var_start + len(values) + old_text_words > OLD_MEM:
        raise TranforError("XXXVI word-memory limit exceeded")
    if nova_var_start + 4 * len(values) + len(new_codes) > NOVA_INSTALLED:
        raise TranforError("Nova-N1 reference RAM limit exceeded")
    old_vars = {name: old_var_start + i for i, name in enumerate(values)}
    nova_vars = {name: nova_var_start + 4*i for i, name in enumerate(values)}
    old_text_start = old_var_start + len(values)
    nova_text_start = nova_var_start + 4*len(values)

    old_instr: list[int] = []
    nova_instr: list[bytes] = []
    for stmt in numeric:
        if stmt.kind == "DATVM":
            old_instr.extend((encode_old(9, stmt.value), encode_old(2, old_vars[stmt.target])))
            nova_instr.extend((encode_nova(0x40, stmt.value), encode_nova(0x13, nova_vars[stmt.target])))
        else:
            old_instr.extend((encode_old(1, old_vars[stmt.left]),
                              encode_old(3 if stmt.operator == "+" else 4, old_vars[stmt.right]),
                              encode_old(2, old_vars[stmt.target])))
            nova_instr.extend((encode_nova(0x11, nova_vars[stmt.left]),
                               encode_nova(0x20 if stmt.operator == "+" else 0x21, nova_vars[stmt.right]),
                               encode_nova(0x13, nova_vars[stmt.target])))
    for index in range(old_text_words):
        old_instr.append(encode_old(8, old_text_start + index))
    for index in range(len(new_codes)):
        nova_instr.append(encode_nova(0x50, nova_text_start + index))
    old_instr.append(encode_old(0))
    nova_instr.append(encode_nova(0))

    old_words = {i: word for i, word in enumerate(old_instr)}
    old_words.update({location: 0 for location in old_vars.values()})
    packed = old_codes + [PAD] * ((-len(old_codes)) % 6)
    for index in range(old_text_words):
        old_words[old_text_start + index] = pack_codes(packed[6*index:6*(index+1)])
    nova_regions = {0: b"".join(nova_instr)}
    if values:
        nova_regions[nova_var_start] = bytes(4*len(values))
    if new_codes:
        nova_regions[nova_text_start] = new_codes
    return Compilation(old_words, old_vars, nova_regions, nova_vars, values, text)


def execute(compilation: Compilation, max_steps: int = 100_000) -> tuple[str, dict[str, int]]:
    """Execute independent machine programs and reject any output/value mismatch."""
    old = Machine()
    old.load(compilation.old_words)
    old_text = old.run(max_steps)
    nova = NovaCPU()
    nova.load_regions(compilation.nova_regions)
    raw = nova.run(max_steps)
    nova_text = decode_cvl68(raw)
    old_values = {name: old.memory[addr] for name, addr in compilation.old_variables.items()}
    nova_values = {name: nova.memory.read_word32(addr)
                   for name, addr in compilation.nova_variables.items()}
    if (old_text != nova_text or old_text != compilation.expected_text or
            old_values != nova_values or old_values != compilation.expected_values):
        raise RuntimeError(f"target divergence: old={old_text!r}/{old_values}, "
                           f"nova={nova_text!r}/{nova_values}")
    return old_text, old_values
