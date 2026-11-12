"""Phase XI: native float multiplication/division and vector dot products."""
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path
from machina_xxxvi.floating import F36, F32, FloatFault
from machina_xxxvi.machine import Machine, MachineFault, encode_instruction as old_instruction
from machina_nova.cpu import NovaCPU, NovaFault, encode_instruction as nova_instruction
from machina_xxxvi.assembler import format_image as old_format
from machina_xxxvi.image import parse_image as old_parse
from machina_nova.image import format_image as nova_format, parse_image as nova_parse
from tranfor.compiler import TranforError
from tranfor.vectors import compile_vectors, execute_vectors

ROOT = Path(__file__).resolve().parents[1]
EPS = Fraction(1, 1 << 24)


class VectorTests(unittest.TestCase):
    def test_exact_multiply_and_divide(self):
        for fmt in (F36, F32):
            self.assertEqual(fmt.decode(fmt.multiply(fmt.encode(Fraction(3, 2)), fmt.encode(2))), 3)
            self.assertEqual(fmt.decode(fmt.divide(fmt.encode(3), fmt.encode(2))), Fraction(3, 2))
            self.assertEqual(fmt.divide(fmt.encode(0), fmt.encode(2)), 0)
            with self.assertRaisesRegex(FloatFault, "division by zero"):
                fmt.divide(fmt.encode(1), fmt.encode(0))

    def test_native_cpu_instructions(self):
        old = Machine()
        old.load({0: old_instruction(10, 0o100), 1: old_instruction(14, 0o101),
                  2: old_instruction(15, 0o102), 3: old_instruction(13, 0o103),
                  4: old_instruction(0), 0o100: F36.encode(3),
                  0o101: F36.encode(4), 0o102: F36.encode(2), 0o103: 0})
        old.run()
        self.assertEqual(F36.decode(old.memory[0o103]), 6)
        new = NovaCPU()
        code = b"".join([nova_instruction(0x60, 0x100), nova_instruction(0x64, 0x104),
                         nova_instruction(0x65, 0x108), nova_instruction(0x63, 0x10C),
                         nova_instruction(0)])
        new.load_regions({0: code, 0x100:
                          b"".join(F32.encode(v).to_bytes(4, "big") for v in (3, 4, 2)) + b"\x00"*4})
        new.run()
        self.assertEqual(F32.decode(new.memory.read_word32(0x10C)), 6)
        self.assertEqual((old.steps, new.steps), (5, 5))

    def test_zero_division_does_not_advance_pc(self):
        old = Machine()
        old.load({0: old_instruction(15, 0o100), 0o100: 0})
        old.a = F36.encode(1)
        with self.assertRaises(MachineFault):
            old.step()
        self.assertEqual((old.pc, old.steps, old.a), (0, 0, F36.encode(1)))
        new = NovaCPU()
        new.load_regions({0: nova_instruction(0x65, 0x100), 0x100: b"\x00"*4})
        new.a = F32.encode(1)
        with self.assertRaises(NovaFault):
            new.step()
        self.assertEqual((new.pc, new.steps, new.a), (0, 0, F32.encode(1)))

    def test_ordered_dot_yields_architecture_specific_results(self):
        build = compile_vectors((ROOT/"examples/portable_dot.trf").read_text(encoding="utf-8"))
        result = execute_vectors(build)
        self.assertEqual(result["text"], "SALVE ΛΟΓΟΣ")
        self.assertEqual(result["F36"]["S"], EPS)
        self.assertEqual(result["F32"]["S"], 0)
        self.assertNotEqual(result["F36"]["DIV"], result["F32"]["DIV"])
        self.assertIn(14, [(w>>24) & 0xFFF for w in build.native.old_words.values()])
        self.assertIn(0x64, build.native.nova_regions[0][0::4])

    def test_vector_storage_contiguity(self):
        b = compile_vectors((ROOT/"examples/portable_dot.trf").read_text(encoding="utf-8"))
        for elements in b.vectors.values():
            old = [b.native.old_addresses[x] for x in elements]
            nova = [b.native.nova_addresses[x] for x in elements]
            self.assertEqual([y-x for x,y in zip(old,old[1:])], [1]*(len(old)-1))
            self.assertEqual([y-x for x,y in zip(nova,nova[1:])], [4]*(len(nova)-1))
        self.assertEqual(b.exposed, ("ONE", "THIRD", "DIV", "S"))

    def test_one_element_and_negative_dot(self):
        s = "VECTOR A = [-2.0]\nVECTOR B = [3.0]\nPRODVC C = A * B\nFINIS"
        result = execute_vectors(compile_vectors(s))
        self.assertEqual(result["F36"]["C"], -6)
        self.assertEqual(result["F32"]["C"], -6)

    def test_invalid_vector_grammar_and_orthography(self):
        bad = ["VECTOR A = []\nFINIS",
               "VECTOR A = [1,2,3,4,5,6,7,8,9]\nFINIS",
               "VECTOR A = [1.0,bad]\nFINIS",
               "VECTOR A = [1]\nVECTOR A = [2]\nFINIS",
               "VECTOR A = [1,2]\nVECTOR B = [1]\nPRODVC C = A * B\nFINIS",
               "PRODVC C = A * B\nFINIS",
               "VECTOR U = [1]\nFINIS",
               "REALIS A = 1\nVECTOR A = [2]\nFINIS",
               "VECTOR A = [1e100]\nFINIS",
               'VECTOR A = [1]\nSCRIBE "HI"\nPRODVC B = A * A\nFINIS']
        for value in bad:
            with self.subTest(value=value), self.assertRaises(TranforError):
                compile_vectors(value)

    def test_scalar_multiply_divide_and_nat15_rejection(self):
        src = "REALIS A = 6.0\nREALIS B = 2.0\nFORMVLA C = A * B\nFORMVLA D = C / B\nFINIS"
        result = execute_vectors(compile_vectors(src))
        self.assertEqual(result["F36"]["D"], 6)
        self.assertEqual(result["F32"]["C"], 12)
        with self.assertRaises(TranforError):
            compile_vectors("DATVM A = 2\nDATVM B = 3\nCALCVLA C = A * B\nFINIS")
        with self.assertRaises(TranforError):
            compile_vectors("REALIS A = 1.0\nREALIS B = 0.0\nFORMVLA C = A / B\nFINIS")

    def test_image_roundtrip(self):
        b = compile_vectors((ROOT/"examples/portable_dot.trf").read_text(encoding="utf-8"))
        self.assertEqual(old_parse(old_format(b.native.old_words)), b.native.old_words)
        def flatten(records):
            return {addr+i:byte for addr,data in records.items() for i,byte in enumerate(data)}
        self.assertEqual(flatten(nova_parse(nova_format(b.native.nova_regions))),
                         flatten(b.native.nova_regions))

    def test_cli_run_and_build(self):
        src = ROOT/"examples/portable_dot.trf"
        run = subprocess.run([sys.executable, "-m", "tranfor", "run-vector", str(src)],
                             cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("S: XXXVI-F36=1/16777216 / Nova-F32=0", run.stdout)
        with tempfile.TemporaryDirectory() as folder:
            build = subprocess.run([sys.executable, "-m", "tranfor", "build-vector",
                                    str(src), "--out-dir", folder],
                                   cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(build.returncode, 0, build.stderr)
            name = Path(folder)/"portable_dot"
            for ext in (".m36", ".nvi", ".map.json"):
                self.assertTrue(Path(str(name)+ext).exists())
            data = json.loads(Path(str(name)+".map.json").read_text(encoding="utf-8"))
            self.assertEqual(data["expected_F36"]["S"], "1/16777216")
            self.assertEqual(data["expected_F32"]["S"], "0")


if __name__ == "__main__":
    unittest.main()
