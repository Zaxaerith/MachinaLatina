"""TRANFOR/P2: bounded vectors, lowered into genuine dual-target P1 code.

Each dot product evaluates products and additions left-to-right, rounding every
operation independently under XXXVI-F36 and Nova-F32.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from .compiler import TranforError, _strip_comment, _identifier
from .scientific import DECIMAL, ScientificBuild, compile_scientific, execute_scientific


@dataclass(frozen=True)
class VectorBuild:
    native: ScientificBuild
    vectors: dict[str, tuple[str, ...]]
    exposed: tuple[str, ...]
    lowered_source: str


def lower_vectors(source: str) -> tuple[str, dict[str, tuple[str, ...]], tuple[str, ...]]:
    lines = source.splitlines()
    # Reserve future user names too, preventing collisions with generated locals.
    reserved: set[str] = set()
    visible: list[str] = []
    for no, raw in enumerate(lines, 1):
        line = _strip_comment(raw).strip()
        found = re.match(r'(DATVM|REALIS|CALCVLA|FORMVLA|VECTOR|PRODVC)\s+(\S+)\s*=', line)
        if found:
            name = _identifier(found[2], no)
            if name in reserved:
                raise TranforError(f'line {no}: duplicate source identifier {name}')
            reserved.add(name)
            if found[1] != 'VECTOR':
                visible.append(name)
    counter = 0

    def fresh() -> str:
        nonlocal counter
        while counter <= 99999:
            candidate = f'Z{counter:05d}'
            counter += 1
            if candidate not in reserved:
                reserved.add(candidate)
                return candidate
        raise TranforError('internal symbol space exhausted')

    vectors: dict[str, tuple[str, ...]] = {}
    generated: list[str] = []
    for no, raw in enumerate(lines, 1):
        line = _strip_comment(raw).strip()
        if not line:
            continue
        v = re.fullmatch(r'VECTOR\s+(\S+)\s*=\s*\[(.*)\]', line)
        d = re.fullmatch(r'PRODVC\s+(\S+)\s*=\s*(\S+)\s*\*\s*(\S+)', line)
        if v:
            name = _identifier(v[1], no)
            parts = [p.strip() for p in v[2].split(',')]
            if not 1 <= len(parts) <= 8:
                raise TranforError(f'line {no}: VECTOR length must be 1..8')
            if any(len(p) > 64 or not DECIMAL.fullmatch(p) for p in parts):
                raise TranforError(f'line {no}: VECTOR entries must be decimal REALIS literals')
            names = tuple(fresh() for _ in parts)
            vectors[name] = names
            generated.extend(f'REALIS {symbol} = {literal}' for symbol, literal in zip(names, parts))
        elif d:
            name = _identifier(d[1], no)
            left, right = _identifier(d[2], no), _identifier(d[3], no)
            if left not in vectors or right not in vectors:
                raise TranforError(f'line {no}: PRODVC requires previously declared VECTOR operands')
            lvec, rvec = vectors[left], vectors[right]
            if len(lvec) != len(rvec):
                raise TranforError(f'line {no}: vector lengths differ')
            previous = ''
            for i, (lv, rv) in enumerate(zip(lvec, rvec)):
                product = name if len(lvec) == 1 else fresh()
                generated.append(f'FORMVLA {product} = {lv} * {rv}')
                if i == 0:
                    previous = product
                else:
                    summed = name if i == len(lvec)-1 else fresh()
                    generated.append(f'FORMVLA {summed} = {previous} + {product}')
                    previous = summed
        else:
            if line.startswith(('VECTOR ', 'PRODVC ')):
                raise TranforError(f'line {no}: invalid VECTOR/PRODVC syntax')
            generated.append(line)
    return '\n'.join(generated) + '\n', vectors, tuple(visible)


def compile_vectors(source: str) -> VectorBuild:
    lowered, vectors, visible = lower_vectors(source)
    native = compile_scientific(lowered)
    for name, elements in vectors.items():
        old = [native.old_addresses[n] for n in elements]
        nova = [native.nova_addresses[n] for n in elements]
        if any(b != a+1 for a,b in zip(old,old[1:])) or any(b != a+4 for a,b in zip(nova,nova[1:])):
            raise AssertionError(f'vector {name} was not allocated contiguously')
    return VectorBuild(native, vectors, visible, lowered)


def execute_vectors(build: VectorBuild) -> dict[str, object]:
    results = execute_scientific(build.native)
    return {
        'text': results['text'],
        'integer': {n: results['integer'][n] for n in build.exposed if n in results['integer']},
        'F36': {n: results['F36'][n] for n in build.exposed if n in results['F36']},
        'F32': {n: results['F32'][n] for n in build.exposed if n in results['F32']},
        'vectors_F36': {n: tuple(results['F36'][s] for s in symbols) for n,symbols in build.vectors.items()},
        'vectors_F32': {n: tuple(results['F32'][s] for s in symbols) for n,symbols in build.vectors.items()},
    }
