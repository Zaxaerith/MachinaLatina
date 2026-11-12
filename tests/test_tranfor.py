"""TRANFOR/P0 dual-backend conformance tests."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tranfor import TranforError, compile_source, execute, parse
from machina_xxxvi.image import parse_image as parse_old
from machina_nova.image import parse_image as parse_nova

ROOT = Path(__file__).resolve().parents[1]


class TranforTests(unittest.TestCase):
    def test_both_targets_greeting_and_variables(self):
        c = compile_source((ROOT / "examples/portable_greeting.trf").read_text(encoding="utf-8"))
        self.assertEqual(execute(c), ("SALVE ΛΟΓΟΣ", {"A": 7, "B": 5, "C": 12, "D": 5}))
        self.assertNotEqual(c.old_words[0], int.from_bytes(c.nova_regions[0][:4], "big"))

    def test_padding_and_multiple_strings(self):
        c = compile_source('DATVM A = 1\nSCRIBE "SAL"\nSCRIBE "VE; ΛΟΓΟΣ"\nFINIS')
        self.assertEqual(execute(c), ("SALVE; ΛΟΓΟΣ", {"A": 1}))
        self.assertEqual(execute(compile_source('SCRIBE "SALVE"\nFINIS')), ("SALVE", {}))

    def test_numeric_extremes(self):
        c = compile_source('DATVM A = 32767\nDATVM B = 32767\nCALCVLA C = A - B\nFINIS')
        self.assertEqual(execute(c), ("", {"A": 32767, "B": 32767, "C": 0}))
        self.assertEqual(execute(compile_source("FINIS")), ("", {}))

    def test_reject_nonportable_text_and_orthography(self):
        bad = [
            'SCRIBE "λόγος"\nFINIS', 'SCRIBE "SALVE U"\nFINIS',
            'SCRIBE "ἄ"\nFINIS', 'DATVM JUL = 1\nFINIS',
            'DATVM LONGNAME = 1\nFINIS', 'DATVM A = 32768\nFINIS',
            'DATVM A = 1\nDATVM A = 2\nFINIS',
            'DATVM A = 1\nCALCVLA B = A - A\nCALCVLA C = B - A\nFINIS',
            'DATVM A = 32767\nCALCVLA B = A + A\nFINIS',
            'CALCVLA A = B + C\nFINIS',
            'SCRIBE "A"\nDATVM B = 1\nFINIS',
            'FINIS\nSCRIBE "X"', 'DATVM A = 7',
        ]
        for source in bad:
            with self.subTest(source=source), self.assertRaises(TranforError):
                compile_source(source)

    def test_quoted_semicolon_and_comment(self):
        statements, values, displayed = parse('DATVM A = 1 ; comment\nSCRIBE "A;B" ; comment\nFINIS')
        self.assertEqual(values, {"A": 1})
        self.assertEqual(displayed, "A;B")
        self.assertEqual(len(statements), 2)

    def test_images_load_on_both_machine_families(self):
        from machina_xxxvi.assembler import format_image as old_format
        from machina_nova.image import format_image as nova_format
        from machina_xxxvi import Machine
        from machina_nova import NovaCPU
        c = compile_source('DATVM A = 7\nDATVM B = 5\nCALCVLA C = A + B\nSCRIBE "SALVE ΛΟΓΟΣ"\nFINIS')
        old = Machine()
        old.load(parse_old(old_format(c.old_words)))
        self.assertEqual(old.run(), "SALVE ΛΟΓΟΣ")
        new = NovaCPU()
        new.load_regions(parse_nova(nova_format(c.nova_regions)))
        self.assertEqual(new.run(), bytes.fromhex("52 41 4B 54 45 20 8A 8E 82 8E 91"))
        self.assertEqual(old.memory[c.old_variables["C"]], new.memory.read_word32(c.nova_variables["C"]))

    def test_cli_run_and_build(self):
        source = ROOT / "examples/portable_greeting.trf"
        run = subprocess.run([sys.executable, "-m", "tranfor", "run", str(source)],
                             cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("TRANFOR/P0: BOTH TARGETS AGREE", run.stdout)
        self.assertIn("C=12", run.stdout)
        with tempfile.TemporaryDirectory() as folder:
            built = subprocess.run([sys.executable, "-m", "tranfor", "build", str(source), "--out-dir", folder],
                                   cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(built.returncode, 0, built.stderr)
            stem = Path(folder) / "portable_greeting"
            manifest = json.loads((Path(str(stem) + ".map.json")).read_text(encoding="utf-8"))
            self.assertEqual(manifest["expected_values"]["C"], 12)
            self.assertEqual(manifest["expected_text"], "SALVE ΛΟΓΟΣ")
            self.assertTrue(parse_old(Path(str(stem) + ".m36").read_text(encoding="utf-8")))
            self.assertTrue(parse_nova(Path(str(stem) + ".nvi").read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
