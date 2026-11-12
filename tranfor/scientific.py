"""TRANFOR/P1 typed NAT15 and REALIS dual-target compiler.

Numeric operations execute on both fictional CPU models. Float results are
compared separately against exact-rational, per-format expected values.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from fractions import Fraction

from machina_xxxvi.assembler import text_codes
from machina_xxxvi.cvl54 import PAD, pack_codes
from machina_xxxvi.floating import F36, F32, FloatFault
from machina_xxxvi.gateway import encode_cvl68, decode_cvl68
from machina_xxxvi.machine import Machine, encode_instruction as old_encode
from machina_nova.cpu import NovaCPU, encode_instruction as nova_encode
from .compiler import TranforError, _strip_comment, _identifier, NAT15_MAX

DECIMAL = re.compile(r'[+-]?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]{1,3})?\Z')


@dataclass(frozen=True)
class Action:
    kind: str
    name: str = ''
    left: str = ''
    right: str = ''
    operator: str = ''
    literal: Fraction = Fraction(0)


@dataclass(frozen=True)
class ScientificBuild:
    old_words: dict[int, int]
    nova_regions: dict[int, bytes]
    old_addresses: dict[str, int]
    nova_addresses: dict[str, int]
    kinds: dict[str, str]
    expected_integer: dict[str, int]
    expected_f36: dict[str, Fraction]
    expected_f32: dict[str, Fraction]
    expected_text: str


def parse_scientific(source: str) -> tuple[list[Action], dict[str, str], str]:
    items: list[Action] = []
    kinds: dict[str, str] = {}
    text_parts: list[str] = []
    in_text = False
    ended = False
    for line_no, original in enumerate(source.splitlines(), 1):
        line = _strip_comment(original).strip()
        if not line:
            continue
        if ended:
            raise TranforError(f'line {line_no}: statement after FINIS')
        if line == 'FINIS':
            ended = True
            continue
        if line.startswith('SCRIBE '):
            in_text = True
            try:
                txt = ast.literal_eval(line[7:].strip())
                if not isinstance(txt, str):
                    raise ValueError('SCRIBE requires a string')
                text_codes(txt)
                encode_cvl68(txt)
            except (SyntaxError, ValueError) as exc:
                raise TranforError(f'line {line_no}: invalid shared-alphabet string: {exc}') from exc
            text_parts.append(txt)
            continue
        if in_text:
            raise TranforError(f'line {line_no}: numeric statement after SCRIBE')
        declaration = re.fullmatch(r'(DATVM|REALIS)\s+(\S+)\s*=\s*(\S+)', line)
        expression = re.fullmatch(r'(CALCVLA|FORMVLA)\s+(\S+)\s*=\s*(\S+)\s*([+-])\s*(\S+)', line)
        if declaration:
            cmd, name, raw = declaration.groups()
            _identifier(name, line_no)
            if name in kinds:
                raise TranforError(f'line {line_no}: duplicate variable {name}')
            if cmd == 'DATVM':
                if not re.fullmatch(r'[0-9]+', raw) or int(raw) > NAT15_MAX:
                    raise TranforError(f'line {line_no}: DATVM requires decimal NAT15')
                value, kind = Fraction(int(raw)), 'NAT15'
            else:
                if not DECIMAL.fullmatch(raw) or len(raw) > 64:
                    raise TranforError(f'line {line_no}: REALIS requires a decimal literal')
                value, kind = Fraction(raw), 'REALIS'
                for fmt in (F36, F32):
                    try:
                        fmt.encode(value)
                    except FloatFault as exc:
                        raise TranforError(f'line {line_no}: {exc}') from exc
            kinds[name] = kind
            items.append(Action(cmd, name=name, literal=value))
        elif expression:
            cmd, name, left, operator, right = expression.groups()
            for ident in (name, left, right):
                _identifier(ident, line_no)
            if name in kinds:
                raise TranforError(f'line {line_no}: duplicate variable {name}')
            kind = 'NAT15' if cmd == 'CALCVLA' else 'REALIS'
            if kinds.get(left) != kind or kinds.get(right) != kind:
                raise TranforError(f'line {line_no}: undefined operands or mixed numeric types')
            kinds[name] = kind
            items.append(Action(cmd, name=name, left=left, right=right, operator=operator))
        else:
            raise TranforError(f'line {line_no}: unknown statement {line!r}')
    if not ended:
        raise TranforError('missing FINIS')
    return items, kinds, ''.join(text_parts)


def compile_scientific(source: str) -> ScientificBuild:
    actions, kinds, text = parse_scientific(source)
    ints: dict[str, int] = {}
    f36: dict[str, int] = {}
    f32: dict[str, int] = {}
    for item in actions:
        if item.kind == 'DATVM':
            ints[item.name] = int(item.literal)
        elif item.kind == 'CALCVLA':
            a, b = ints[item.left], ints[item.right]
            result = a + b if item.operator == '+' else a - b
            if not 0 <= result <= NAT15_MAX:
                raise TranforError(f'{item.name}: NAT15 result outside portable range')
            ints[item.name] = result
        elif item.kind == 'REALIS':
            f36[item.name], f32[item.name] = F36.encode(item.literal), F32.encode(item.literal)
        elif item.kind == 'FORMVLA':
            try:
                operation = 'add' if item.operator == '+' else 'subtract'
                f36[item.name] = getattr(F36, operation)(f36[item.left], f36[item.right])
                f32[item.name] = getattr(F32, operation)(f32[item.left], f32[item.right])
            except FloatFault as exc:
                raise TranforError(f'{item.name}: {exc}') from exc

    t54, t68 = text_codes(text), encode_cvl68(text)
    ntext = (len(t54) + 5) // 6
    old_count = sum(2 if s.kind in ('DATVM', 'REALIS') else 3 for s in actions) + ntext + 1
    nova_count = sum(2 if s.kind in ('DATVM', 'REALIS') else 3 for s in actions) + len(t68) + 1
    old_start, nova_start = max(0o100, old_count), max(0x100, 4 * nova_count)
    names = list(kinds)
    constants = [s.name for s in actions if s.kind == 'REALIS']
    old_addr = {name: old_start + i for i, name in enumerate(names)}
    nova_addr = {name: nova_start + 4 * i for i, name in enumerate(names)}
    old_const = {name: old_start + len(names) + i for i, name in enumerate(constants)}
    nova_const = {name: nova_start + 4 * (len(names) + i) for i, name in enumerate(constants)}
    old_text = old_start + len(names) + len(constants)
    nova_text = nova_start + 4 * (len(names) + len(constants))
    if old_text + ntext > 1 << 15:
        raise TranforError('XXXVI/P0 address space exhausted')
    if nova_text + len(t68) > 256 * 1024:
        raise TranforError('Nova-N1 default installed RAM exhausted')

    oi: list[int] = []
    ni: list[bytes] = []
    for s in actions:
        a = s.name
        if s.kind == 'DATVM':
            oi.extend((old_encode(9, int(s.literal)), old_encode(2, old_addr[a])))
            ni.extend((nova_encode(0x40, int(s.literal)), nova_encode(0x13, nova_addr[a])))
        elif s.kind == 'REALIS':
            oi.extend((old_encode(10, old_const[a]), old_encode(13, old_addr[a])))
            ni.extend((nova_encode(0x60, nova_const[a]), nova_encode(0x63, nova_addr[a])))
        elif s.kind == 'CALCVLA':
            oi.extend((old_encode(1, old_addr[s.left]),
                       old_encode(3 if s.operator == '+' else 4, old_addr[s.right]),
                       old_encode(2, old_addr[a])))
            ni.extend((nova_encode(0x11, nova_addr[s.left]),
                       nova_encode(0x20 if s.operator == '+' else 0x21, nova_addr[s.right]),
                       nova_encode(0x13, nova_addr[a])))
        else:
            oi.extend((old_encode(10, old_addr[s.left]),
                       old_encode(11 if s.operator == '+' else 12, old_addr[s.right]),
                       old_encode(13, old_addr[a])))
            ni.extend((nova_encode(0x60, nova_addr[s.left]),
                       nova_encode(0x61 if s.operator == '+' else 0x62, nova_addr[s.right]),
                       nova_encode(0x63, nova_addr[a])))
    oi.extend(old_encode(8, old_text + i) for i in range(ntext))
    ni.extend(nova_encode(0x50, nova_text + i) for i in range(len(t68)))
    oi.append(old_encode(0))
    ni.append(nova_encode(0))

    old_words = {i: word for i, word in enumerate(oi)}
    old_words.update({addr: 0 for addr in old_addr.values()})
    old_words.update({old_const[name]: f36[name] for name in constants})
    padded = t54 + [PAD] * (-len(t54) % 6)
    old_words.update({old_text + i: pack_codes(padded[6*i:6*i+6]) for i in range(ntext)})
    regions = {0: b''.join(ni)}
    if names:
        regions[nova_start] = bytes(4 * len(names))
    if constants:
        regions[nova_start + 4*len(names)] = b''.join(f32[name].to_bytes(4, 'big') for name in constants)
    if t68:
        regions[nova_text] = t68
    return ScientificBuild(old_words, regions, old_addr, nova_addr, kinds, ints,
                           {n: F36.decode(v) for n,v in f36.items()},
                           {n: F32.decode(v) for n,v in f32.items()}, text)


def execute_scientific(build: ScientificBuild, max_steps: int = 100000) -> dict[str, object]:
    old = Machine()
    old.load(build.old_words)
    old_text = old.run(max_steps)
    nova = NovaCPU()
    nova.load_regions(build.nova_regions)
    new_text = decode_cvl68(nova.run(max_steps))
    old_int = {n: old.memory[build.old_addresses[n]] for n,t in build.kinds.items() if t == 'NAT15'}
    new_int = {n: nova.memory.read_word32(build.nova_addresses[n]) for n,t in build.kinds.items() if t == 'NAT15'}
    old_real = {n: F36.decode(old.memory[build.old_addresses[n]]) for n,t in build.kinds.items() if t == 'REALIS'}
    new_real = {n: F32.decode(nova.memory.read_word32(build.nova_addresses[n])) for n,t in build.kinds.items() if t == 'REALIS'}
    if (old_text != new_text or old_text != build.expected_text or
        old_int != new_int or old_int != build.expected_integer or
        old_real != build.expected_f36 or new_real != build.expected_f32):
        raise RuntimeError('XXXVI/Nova scientific result differs from format-specific oracle')
    return {'text': old_text, 'integer': old_int, 'F36': old_real, 'F32': new_real}
