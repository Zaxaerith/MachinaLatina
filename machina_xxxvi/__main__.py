"""Run: python -m machina_xxxvi demo | run FILE [--trace]."""
from __future__ import annotations

import argparse
from pathlib import Path

from . import Machine, MachineFault, encode_instruction, load_image, pack_codes
from .cvl54 import CharacterFault


def demo_words() -> dict[int, int]:
    return {
        0: encode_instruction(8, 0o100),
        1: encode_instruction(8, 0o101),
        2: encode_instruction(0),
        0o100: pack_codes((0o22, 0o01, 0o13, 0o24, 0o05, 0o43)),
        0o101: pack_codes((0o61, 0o13, 0o17, 0o03, 0o17, 0o22)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Machina XXXVI/P0 emulator (fictional)")
    sub = parser.add_subparsers(dest="action", required=True)
    example = sub.add_parser("demo", help="run built-in SALVE ΛΟΓΟΣ program")
    runner = sub.add_parser("run", help="run octal memory-image text")
    runner.add_argument("image", type=Path)
    for p in (example, runner):
        p.add_argument("--trace", action="store_true", help="show instruction trace on stderr")
        p.add_argument("--max-steps", type=int, default=100000)
    args = parser.parse_args()
    machine = Machine()
    machine.load(demo_words() if args.action == "demo" else load_image(args.image))
    try:
        if args.trace:
            import sys
            for _ in range(args.max_steps):
                at, opcode = machine.step()
                print(f"PC={at:05o} {opcode:5s} A={machine.a:012o} OUT={machine.printer.text!r}", file=sys.stderr)
                if machine.halted:
                    break
            if not machine.halted:
                raise MachineFault(f"step limit {args.max_steps} reached")
        else:
            machine.run(args.max_steps)
    except (MachineFault, CharacterFault) as exc:
        parser.exit(1, f"P0 fault: {exc}\n")
    print(machine.printer.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
