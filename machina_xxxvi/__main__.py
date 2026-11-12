"""CLI for the fictional Machina XXXVI/P0 architecture."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import Machine, MachineFault, encode_instruction, load_image, pack_codes
from .assembler import AssemblyError, assemble, format_image
from .cvl54 import CharacterFault
from .gateway import GatewayError, decode_cvl68, transcode_words


def demo_words() -> dict[int, int]:
    return {
        0: encode_instruction(8, 0o100),
        1: encode_instruction(8, 0o101),
        2: encode_instruction(0),
        0o100: pack_codes((0o22, 0o01, 0o13, 0o24, 0o05, 0o43)),
        0o101: pack_codes((0o61, 0o13, 0o17, 0o03, 0o17, 0o22)),
    }


def _octal_address(arg: str) -> int:
    try:
        if not arg or any(ch not in "01234567" for ch in arg):
            raise ValueError
        result = int(arg, 8)
        if not 0 <= result < 1 << 15:
            raise ValueError
        return result
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid 15-bit octal word address {arg!r}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Machina XXXVI/P0 (fictional)")
    sub = parser.add_subparsers(dest="action", required=True)
    demo = sub.add_parser("demo", help="run built-in SALVE ΛΟΓΟΣ program")
    run = sub.add_parser("run", help="run a P0 octal memory image")
    run.add_argument("image", type=Path)
    for p in (demo, run):
        p.add_argument("--trace", action="store_true", help="instruction trace on stderr")
        p.add_argument("--max-steps", type=int, default=100000)

    source = sub.add_parser("assemble", help="assemble P0 source into octal memory image")
    source.add_argument("source", type=Path)
    source.add_argument("--output", type=Path, help="write memory image instead of stdout")

    bridge = sub.add_parser("bridge", help="transcode selected CVL-54 word addresses to CVL-68 bytes")
    bridge.add_argument("image", type=Path)
    bridge.add_argument("addresses", metavar="OCTAL_ADDRESS", type=_octal_address, nargs="+")
    bridge.add_argument("--output", type=Path, help="save raw candidate CVL-68 bytes")

    args = parser.parse_args()
    try:
        if args.action == "assemble":
            words = assemble(args.source.read_text(encoding="utf-8"))
            result = format_image(words)
            if args.output is None:
                print(result, end="")
            else:
                args.output.write_text(result, encoding="utf-8")
            return 0
        if args.action == "bridge":
            words = load_image(args.image)
            absent = [addr for addr in args.addresses if addr not in words]
            if absent:
                raise ValueError(f"missing image word at {absent[0]:05o}")
            data = transcode_words(words[addr] for addr in args.addresses)
            if args.output is not None:
                args.output.write_bytes(data)
            print(data.hex(" ").upper())
            print(decode_cvl68(data))
            return 0
        machine = Machine()
        machine.load(demo_words() if args.action == "demo" else load_image(args.image))
        if args.trace:
            if args.max_steps < 1:
                raise ValueError("max_steps must be positive")
            for _ in range(args.max_steps):
                at, opcode = machine.step()
                print(f"PC={at:05o} {opcode:5s} A={machine.a:012o} OUT={machine.printer.text!r}", file=sys.stderr)
                if machine.halted:
                    break
            if not machine.halted:
                raise MachineFault(f"step limit {args.max_steps} reached")
        else:
            machine.run(args.max_steps)
        print(machine.printer.text)
        return 0
    except (ValueError, OSError, MachineFault, CharacterFault,
            GatewayError, AssemblyError) as exc:
        parser.exit(1, f"P0 fault: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
