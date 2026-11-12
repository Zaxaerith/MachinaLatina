"""Run: python -m machina_nova demo | run FILE | compare."""
from __future__ import annotations

import argparse
import sys
from . import NovaCPU, NovaFault, greeting_image, read_image
from machina_xxxvi.gateway import decode_cvl68, GatewayError


def _execute(image: dict[int, bytes], trace: bool, max_steps: int) -> bytes:
    machine = NovaCPU()
    machine.load_regions(image)
    if not trace:
        return machine.run(max_steps)
    if max_steps < 1:
        raise ValueError("max_steps must be a positive integer")
    for _ in range(max_steps):
        at, mnemonic = machine.step()
        print(f"PC={at:06X} {mnemonic:5s} A={machine.a:08X} OUT={machine.output.hex(' ').upper()}", file=sys.stderr)
        if machine.halted:
            return bytes(machine.output)
    raise NovaFault(f"step limit {max_steps}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Machina Nova-N1, fictional 1968 CPU")
    sub = parser.add_subparsers(dest="action", required=True)
    demo = sub.add_parser("demo", help="execute the native Nova greeting")
    runner = sub.add_parser("run", help="run sparse hex-byte memory image")
    runner.add_argument("image")
    compare = sub.add_parser("compare", help="run XXXVI/P0 and Nova-N1 greeting and compare text")
    for entry in (demo, runner, compare):
        entry.add_argument("--trace", action="store_true")
        entry.add_argument("--max-steps", type=int, default=100_000)
    args = parser.parse_args()
    try:
        image = read_image(args.image) if args.action == "run" else greeting_image()
        payload = _execute(image, args.trace, args.max_steps)
        displayed = decode_cvl68(payload)
        if args.action == "compare":
            from machina_xxxvi import Machine
            from machina_xxxvi.__main__ import demo_words
            old = Machine()
            old.load(demo_words())
            old_text = old.run(args.max_steps)
            if old_text != displayed:
                raise NovaFault(f"text mismatch: XXXVI={old_text!r} vs Nova={displayed!r}")
            print(f"XXXVI/P0 CVL-54: {old_text}")
            print(f"Nova-N1 CVL-68: {displayed}")
            print("TEXT MATCH / BINARY INCOMPATIBLE")
        else:
            print(displayed)
        return 0
    except (ValueError, OSError, NovaFault, GatewayError) as exc:
        parser.exit(1, f"Nova-N1 fault: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
