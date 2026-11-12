"""TRANFOR/P0 and TRANFOR/P1 dual-target tools, modern experimental drafts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .compiler import compile_source, execute
from .scientific import compile_scientific, execute_scientific
from .vectors import compile_vectors, execute_vectors
from machina_xxxvi.assembler import format_image as old_format
from machina_nova.image import format_image as nova_format


def main() -> int:
    parser = argparse.ArgumentParser(description="Machina Latina experimental TRANFOR compiler")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("run", "run-real", "build", "build-real"):
        cmd = sub.add_parser(name)
        cmd.add_argument("source", type=Path)
        if name.startswith("build"):
            cmd.add_argument("--out-dir", type=Path, required=True)
    for name in ("run-vector", "build-vector"):
        cmd = sub.add_parser(name, help="TRANFOR/P2 bounded vector dot-product experiment")
        cmd.add_argument("source", type=Path)
        if name.startswith("build"):
            cmd.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command in ("run-vector", "build-vector"):
            project = compile_vectors(args.source.read_text(encoding="utf-8"))
            native = project.native
            if args.command == "run-vector":
                result = execute_vectors(project)
                print(result["text"])
                for name in project.exposed:
                    if name in result["integer"]:
                        print(f"{name}={result['integer'][name]}")
                    else:
                        f36, f32 = result["F36"][name], result["F32"][name]
                        print(f"{name}: XXXVI-F36={f36} / Nova-F32={f32}" +
                              (" [DIFFERENT ROUNDING]" if f36 != f32 else ""))
                print("TRANFOR/P2: BOTH TARGETS MATCH THEIR DEFINED FORMATS")
            else:
                args.out_dir.mkdir(parents=True, exist_ok=True)
                stem = args.source.stem
                old = args.out_dir / f"{stem}.m36"
                nova = args.out_dir / f"{stem}.nvi"
                path = args.out_dir / f"{stem}.map.json"
                old.write_text(old_format(native.old_words), encoding="utf-8")
                nova.write_text(nova_format(native.nova_regions), encoding="utf-8")
                manifest = {
                    "status": "TRANFOR/P2 experimental fixed vectors; no stable ABI",
                    "variables": list(project.exposed),
                    "vector_elements": {n: list(names) for n,names in project.vectors.items()},
                    "xxxvi_word_addresses_octal": {n:f"{a:05o}" for n,a in native.old_addresses.items()},
                    "nova_byte_addresses_hex": {n:f"{a:06X}" for n,a in native.nova_addresses.items()},
                    "expected_F36": {n:str(v) for n,v in native.expected_f36.items()},
                    "expected_F32": {n:str(v) for n,v in native.expected_f32.items()},
                    "expected_text": native.expected_text,
                }
                path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                print(f"XXXVI image: {old}\nNova image: {nova}\nVariable map: {path}")
            return 0
        scientific = args.command.endswith("-real")
        source = args.source.read_text(encoding="utf-8")
        compiled = compile_scientific(source) if scientific else compile_source(source)
        if args.command == "run":
            result_text, values = execute(compiled)
            print(result_text)
            for key, value in values.items():
                print(f"{key}={value}")
            print("TRANFOR/P0: BOTH TARGETS AGREE")
        elif args.command == "run-real":
            result = execute_scientific(compiled)
            print(result["text"])
            for name, kind in compiled.kinds.items():
                if kind == "NAT15":
                    print(f"{name}={result['integer'][name]}")
                else:
                    f36, f32 = result["F36"][name], result["F32"][name]
                    print(f"{name}: XXXVI-F36={f36} / Nova-F32={f32}" +
                          (" [DIFFERENT ROUNDING]" if f36 != f32 else ""))
            print("TRANFOR/P1: BOTH TARGETS MATCH THEIR DEFINED FORMATS")
        else:
            args.out_dir.mkdir(parents=True, exist_ok=True)
            stem = args.source.stem
            old_path = args.out_dir / f"{stem}.m36"
            nova_path = args.out_dir / f"{stem}.nvi"
            map_path = args.out_dir / f"{stem}.map.json"
            old_path.write_text(old_format(compiled.old_words), encoding="utf-8")
            nova_path.write_text(nova_format(compiled.nova_regions), encoding="utf-8")
            if scientific:
                manifest = {
                    "status": "TRANFOR/P1 floating research draft, not a stable ABI",
                    "xxxvi_word_addresses_octal": {n: f"{a:05o}" for n,a in compiled.old_addresses.items()},
                    "nova_byte_addresses_hex": {n: f"{a:06X}" for n,a in compiled.nova_addresses.items()},
                    "types": compiled.kinds,
                    "NAT15": compiled.expected_integer,
                    "F36_exact_rational": {n: str(v) for n,v in compiled.expected_f36.items()},
                    "F32_exact_rational": {n: str(v) for n,v in compiled.expected_f32.items()},
                    "expected_text": compiled.expected_text,
                }
            else:
                manifest = {
                    "status": "TRANFOR/P0 modern draft; not a stable ABI",
                    "xxxvi_word_addresses_octal": {n: f"{a:05o}" for n,a in compiled.old_variables.items()},
                    "nova_byte_addresses_hex": {n: f"{a:06X}" for n,a in compiled.nova_variables.items()},
                    "expected_values": compiled.expected_values,
                    "expected_text": compiled.expected_text,
                }
            map_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"XXXVI image: {old_path}")
            print(f"Nova image: {nova_path}")
            print(f"Variable map: {map_path}")
        return 0
    except (ValueError, RuntimeError, OSError) as exc:
        parser.exit(1, f"TRANFOR error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
