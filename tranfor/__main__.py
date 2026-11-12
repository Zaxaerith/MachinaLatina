"""CLI: python -m tranfor run FILE | build FILE --out-dir DIR."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .compiler import compile_source, execute
from machina_xxxvi.assembler import format_image as old_format
from machina_nova.image import format_image as nova_format

def main() -> int:
    parser = argparse.ArgumentParser(description="TRANFOR/P0 fictional dual-target compiler")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="compile, run and compare both CPU targets")
    run.add_argument("source", type=Path)
    build = sub.add_parser("build", help="emit both memory images and a variable map")
    build.add_argument("source", type=Path)
    build.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        compiled = compile_source(args.source.read_text(encoding="utf-8"))
        if args.command == "run":
            text, values = execute(compiled)
            print(text)
            for name, value in values.items():
                print(f"{name}={value}")
            print("TRANFOR/P0: BOTH TARGETS AGREE")
        else:
            args.out_dir.mkdir(parents=True, exist_ok=True)
            stem = args.source.stem
            old_path = args.out_dir / f"{stem}.m36"
            nova_path = args.out_dir / f"{stem}.nvi"
            map_path = args.out_dir / f"{stem}.map.json"
            old_path.write_text(old_format(compiled.old_words), encoding="utf-8")
            nova_path.write_text(nova_format(compiled.nova_regions), encoding="utf-8")
            manifest = {
                "status": "TRANFOR/P0 modern draft; not a stable ABI",
                "xxxvi_word_addresses_octal": {name: f"{addr:05o}" for name, addr in compiled.old_variables.items()},
                "nova_byte_addresses_hex": {name: f"{addr:06X}" for name, addr in compiled.nova_variables.items()},
                "expected_values": compiled.expected_values,
                "expected_text": compiled.expected_text,
            }
            map_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"XXXVI image: {old_path}")
            print(f"Nova image: {nova_path}")
            print(f"Variable map: {map_path}")
        return 0
    except (ValueError, RuntimeError, OSError) as exc:
        parser.exit(1, f"TRANFOR/P0: {exc}\n")

if __name__ == "__main__":
    raise SystemExit(main())
