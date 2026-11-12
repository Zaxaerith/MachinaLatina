"""Phase X floating formats, CPU instructions and TRANFOR/P1 cross-architecture tests."""
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from machina_xxxvi.floating import F36, F32, FloatFault
from machina_xxxvi.machine import Machine, MachineFault, encode_instruction as old_enc
from machina_nova.cpu import NovaCPU, NovaFault, encode_instruction as nova_enc
from machina_xxxvi.assembler import format_image as old_fmt
from machina_xxxvi.image import parse_image as old_parse
from machina_nova.image import format_image as nova_fmt, parse_image as nova_parse
from tranfor.scientific import compile_scientific, execute_scientific
from tranfor.compiler import TranforError

ROOT = Path(__file__).resolve().parents[1]
HALF = Fraction(1, 1 << 24)


class FloatingTests(unittest.TestCase):
    def test_finite_vectors(self):
        for fmt, one, negative, half in (
                (F36, 0x40C000000, 0xC0C000000, 0x40E000000),
                (F32, 0x41800000, 0xC1800000, 0x41C00000)):
            self.assertEqual(fmt.encode(0), 0)
            self.assertEqual(fmt.encode(1), one)
            self.assertEqual(fmt.encode(-1), negative)
            self.assertEqual(fmt.encode(Fraction(3, 2)), half)
            self.assertEqual(fmt.decode(one), 1)
            self.assertEqual(fmt.decode(negative), -1)
            self.assertEqual(fmt.decode(half), Fraction(3, 2))

    def test_ties_to_even_diverge(self):
        self.assertEqual(F36.decode(F36.encode(1 + HALF)), 1 + HALF)
        self.assertEqual(F32.decode(F32.encode(1 + HALF)), 1)
        self.assertEqual(F32.decode(F32.encode(1 + 3*HALF)), 1 + 4*HALF)
        self.assertEqual(F36.decode(F36.encode(-1 - HALF)), -1 - HALF)
        self.assertEqual(F32.decode(F32.encode(-1 - HALF)), -1)

    def test_finite_round_trip(self):
        for fmt in (F36, F32):
            for value in (Fraction(0), Fraction(1, 2), Fraction(3, 5),
                          Fraction(-7, 3), Fraction(2**12), Fraction(1, 2**12)):
                word = fmt.encode(value)
                self.assertEqual(fmt.encode(fmt.decode(word)), word)

    def test_exponent_and_reserved_codes(self):
        for fmt in (F36, F32):
            for word in (1, 1 << (fmt.bits-1), 1 << fmt.fraction_bits,
                         ((1 << fmt.exponent_bits)-1) << fmt.fraction_bits,
                         1 << fmt.bits):
                with self.subTest(fmt=fmt.name, word=word), self.assertRaises(FloatFault):
                    fmt.decode(word)
        with self.assertRaises(FloatFault):
            F32.encode(Fraction(1, 1 << 65))
        with self.assertRaises(FloatFault):
            F32.encode(1 << 62)

    def test_machine_float_instructions(self):
        for fmt, cpu_class, enc, ops, base, stride in (
                (F36, Machine, old_enc, (10, 11, 13), 0o100, 1),
                (F32, NovaCPU, nova_enc, (0x60, 0x61, 0x63), 0x100, 4)):
            data0, data1 = fmt.encode(1), fmt.encode(HALF)
            code = [enc(ops[0], base), enc(ops[1], base + stride),
                    enc(ops[2], base + 2*stride), enc(0)]
            cpu = cpu_class()
            if fmt == F36:
                cpu.load({**dict(enumerate(code)), base: data0,
                          base+1: data1, base+2: 0})
                cpu.run()
                stored = cpu.memory[base+2]
            else:
                cpu.load_regions({0: b"".join(code), base:
                                 data0.to_bytes(4, "big") +
                                 data1.to_bytes(4, "big") + b"\x00"*4})
                cpu.run()
                stored = cpu.memory.read_word32(base+8)
            self.assertEqual(fmt.decode(stored), 1+HALF if fmt == F36 else 1)
            self.assertEqual(cpu.steps, 4)

    def test_fault_atomicity_and_zero(self):
        old = Machine()
        old.load({0: old_enc(10, 0o100), 0o100: 1})
        with self.assertRaises(MachineFault):
            old.step()
        self.assertEqual((old.pc, old.a, old.steps), (0, 0, 0))
        new = NovaCPU()
        new.load_regions({0: nova_enc(0x60, 0x100), 0x100: b"\x00\x00\x00\x01"})
        with self.assertRaises(NovaFault):
            new.step()
        self.assertEqual((new.pc, new.a, new.steps), (0, 0, 0))
        self.assertEqual(F36.subtract(F36.encode(1), F36.encode(1)), 0)
        self.assertEqual(F32.subtract(F32.encode(1), F32.encode(1)), 0)

    def test_scientific_dual_execution(self):
        program = (ROOT / "examples/rounding.trf").read_text(encoding="utf-8")
        result = execute_scientific(compile_scientific(program))
        self.assertEqual(result["text"], "SALVE ΛΟΓΟΣ")
        self.assertEqual(result["integer"], {"A": 7, "B": 5, "C": 12})
        self.assertEqual(result["F36"]["Y"], 1+HALF)
        self.assertEqual(result["F32"]["Y"], 1)

    def test_p0_compatibility(self):
        source = 'DATVM A = 7\nDATVM B = 5\nCALCVLA C = A + B\nSCRIBE "SALVE ΛΟΓΟΣ"\nFINIS'
        result = execute_scientific(compile_scientific(source))
        self.assertEqual(result["integer"]["C"], 12)
        self.assertEqual(result["F36"], {})

    def test_reject_invalid_reals_and_types(self):
        sources = [
            "DATVM A = 1\nREALIS B = 1.0\nFORMVLA C = A + B\nFINIS",
            "REALIS A = 1.0\nREALIS B = 0.5\nCALCVLA C = A + B\nFINIS",
            "REALIS X = 1e100\nFINIS",
            "REALIS X = 1e-100\nFINIS",
            "REALIS X = hello\nFINIS",
            "REALIS X = 1.0\nREALIS X = 2.0\nFINIS",
            'SCRIBE "λόγος"\nFINIS',
            "REALIS U = 1.0\nFINIS",
        ]
        for source in sources:
            with self.subTest(source=source), self.assertRaises(TranforError):
                compile_scientific(source)

    def test_native_image_round_trip(self):
        compiled = compile_scientific((ROOT/"examples/rounding.trf").read_text(encoding="utf-8"))
        self.assertEqual(old_parse(old_fmt(compiled.old_words)), compiled.old_words)
        byte_map = lambda regions: {addr+i: byte for addr,data in regions.items()
                                    for i,byte in enumerate(data)}
        self.assertEqual(byte_map(nova_parse(nova_fmt(compiled.nova_regions))),
                         byte_map(compiled.nova_regions))

    def test_cli_and_exact_manifest(self):
        source = str(ROOT/"examples/rounding.trf")
        run = subprocess.run([sys.executable, "-m", "tranfor", "run-real", source],
                             cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("Y: XXXVI-F36=16777217/16777216 / Nova-F32=1 [DIFFERENT ROUNDING]", run.stdout)
        with tempfile.TemporaryDirectory() as folder:
            build = subprocess.run([sys.executable, "-m", "tranfor", "build-real",
                                    source, "--out-dir", folder], cwd=ROOT,
                                   capture_output=True, text=True)
            self.assertEqual(build.returncode, 0, build.stderr)
            obj = json.loads((Path(folder)/"rounding.map.json").read_text(encoding="utf-8"))
            self.assertEqual(obj["F36_exact_rational"]["Y"], "16777217/16777216")
            self.assertEqual(obj["F32_exact_rational"]["Y"], "1")
            self.assertTrue((Path(folder)/"rounding.m36").exists())
            self.assertTrue((Path(folder)/"rounding.nvi").exists())


if __name__ == "__main__":
    unittest.main()
