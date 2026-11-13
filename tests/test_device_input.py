"""Phase XIII: real native CAPTA input, cross-family record replay and failure cases."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from machina_xxxvi import Machine, MachineFault, encode_instruction as encode_old
from machina_xxxvi.cvl54 import pack_codes
from machina_xxxvi.gateway import encode_cvl68, decode_cvl68
from machina_nova import NovaCPU, NovaFault, encode_instruction as encode_nova
from ordo_operum.device import for_nova, for_xxxvi
from ordo_operum.monitor import Archives, Execution, OrdoError, parse_deck, run_deck, write_results

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
GREETING = "SALVE ΛΟΓΟΣ"
DATA = encode_cvl68(GREETING)


class InputInstructionTests(unittest.TestCase):
    def test_xxxvi_word_input_and_greek_page(self):
        cpu = Machine()
        cpu.load({0: encode_old(16, 0o100), 1: encode_old(8, 0o100),
                  2: encode_old(16, 0o101), 3: encode_old(8, 0o101),
                  4: encode_old(0)})
        words = for_xxxvi(DATA)
        self.assertEqual(len(words), 2)
        cpu.mount_input(words)
        self.assertEqual(cpu.run(), GREETING)
        self.assertEqual(cpu.input_position, 2)

    def test_nova_byte_input_and_output(self):
        cpu = NovaCPU()
        instructions = b"".join(encode_nova(op, 0x100+i)
                                for i in range(len(DATA)) for op in (0x66, 0x50))
        cpu.load_regions({0: instructions + encode_nova(0),
                          0x100: bytes(len(DATA))})
        cpu.mount_input(DATA)
        self.assertEqual(cpu.run(), DATA)
        self.assertEqual(cpu.input_position, len(DATA))

    def test_xxxvi_unmounted_and_exhausted_fault_is_atomic(self):
        cpu = Machine()
        instruction = encode_old(16, 0o100)
        cpu.load({0: instruction, 0o100: 0o123})
        with self.assertRaisesRegex(MachineFault, "without attached"):
            cpu.step()
        self.assertEqual((cpu.pc, cpu.steps, cpu.memory[0o100]), (0, 0, 0o123))
        cpu.mount_input(tuple())
        with self.assertRaisesRegex(MachineFault, "end of input"):
            cpu.step()
        self.assertEqual((cpu.pc, cpu.steps, cpu.input_position), (0, 0, 0))

    def test_nova_unmounted_and_exhausted_fault_is_atomic(self):
        cpu = NovaCPU()
        cpu.load_regions({0: encode_nova(0x66, 0x100), 0x100: b"\x7A"})
        with self.assertRaisesRegex(NovaFault, "without attached"):
            cpu.step()
        self.assertEqual((cpu.pc, cpu.steps, cpu.memory.read_byte(0x100)), (0, 0, 0x7A))
        cpu.mount_input(b"")
        with self.assertRaisesRegex(NovaFault, "end of input"):
            cpu.step()
        self.assertEqual((cpu.pc, cpu.steps, cpu.input_position), (0, 0, 0))

    def test_invalid_input_mount(self):
        cpu = Machine()
        with self.assertRaises(ValueError):
            cpu.mount_input((1 << 36,))
        cpu = NovaCPU()
        with self.assertRaises(ValueError):
            cpu.mount_input("SALVE")
        with self.assertRaises(ValueError):
            for_xxxvi(encode_cvl68("α"))  # lowercase unavailable in CVL-54
        self.assertEqual(for_nova(DATA), DATA)

    def test_existing_cpu_opcode_vectors_unchanged(self):
        self.assertEqual(encode_old(8, 0o100), 0o001000000100)
        self.assertEqual(encode_nova(0x50, 0x100), bytes.fromhex("50 00 01 00"))
        self.assertEqual(encode_old(16, 0o100), 0o002000000100)
        self.assertEqual(encode_nova(0x66, 0x100), bytes.fromhex("66 00 01 00"))


class SpoolInputTests(unittest.TestCase):
    def test_accipe_parse(self):
        deck = (EXAMPLES / "input_roundtrip.ord").read_text(encoding="utf-8")
        jobs = parse_deck(deck)
        self.assertEqual([j.input_spool for j in jobs], [None, None, "ACTA", "ACTA"])
        self.assertEqual([j.target for j in jobs], ["XXXVI", "NOVA", "NOVA", "XXXVI"])

    def test_four_actual_cpu_jobs(self):
        deck = (EXAMPLES / "input_roundtrip.ord").read_text(encoding="utf-8")
        results, archives = run_deck(deck, EXAMPLES)
        self.assertEqual([j.status for j in results], ["FINIS"] * 4,
                         [j.error for j in results])
        self.assertEqual([j.text for j in results], [GREETING] * 4)
        self.assertEqual(archives.records["ACTA"], [DATA, DATA])
        self.assertEqual(archives.records["PROBA"], [DATA, DATA])
        self.assertGreater(results[2].steps, 0)
        self.assertGreater(results[3].steps, 0)

    def test_queue_exhaustion_produces_error_and_continue(self):
        deck = (EXAMPLES / "input_roundtrip.ord").read_text(encoding="utf-8")
        deck += ("\nLABOR QVINTA NOVA IMAGE\nIMAGO echo_nova.nvi\n"
                 "ACCIPE ACTA\nEDE PROBA\nFINIS\n"
                 "LABOR SEXTA NOVA IMAGE\nIMAGO nova_salve_logos.nvi\n"
                 "EDE PROBA\nFINIS\n")
        result, archives = run_deck(deck, EXAMPLES)
        self.assertEqual([r.status for r in result][-2:], ["ERROR", "FINIS"])
        self.assertIn("no unread record", result[-2].error)
        self.assertEqual(len(archives.records["PROBA"]), 3)

    def test_failure_keeps_unread_record(self):
        base = ("LABOR PRIMA NOVA IMAGE\nIMAGO nova_salve_logos.nvi\n"
                "EDE ACTA\nFINIS\n")
        blocked = ("LABOR SECVN NOVA IMAGE\nIMAGO nova_salve_logos.nvi\n"
                   "ACCIPE ACTA\nEDE PROBA\nLIMES 1\nFINIS\n")
        consumer = ("LABOR TERTIA NOVA IMAGE\nIMAGO echo_nova.nvi\n"
                    "ACCIPE ACTA\nEDE PROBA\nFINIS\n")
        result, archives = run_deck(base + blocked + consumer, EXAMPLES)
        self.assertEqual([r.status for r in result], ["FINIS", "ERROR", "FINIS"])
        self.assertEqual(len(archives.records["PROBA"]), 1)
        self.assertEqual(archives.records["PROBA"][0], DATA)

    def test_missing_input_spool_is_job_error(self):
        deck = ("LABOR PRIMA NOVA IMAGE\nIMAGO echo_nova.nvi\n"
                "ACCIPE ACTA\nEDE PROBA\nFINIS\n"
                "LABOR SECVN NOVA IMAGE\nIMAGO nova_salve_logos.nvi\n"
                "EDE PROBA\nFINIS\n")
        result, archive = run_deck(deck, EXAMPLES)
        self.assertEqual([r.status for r in result], ["ERROR", "FINIS"])
        self.assertIn("no unread record", result[0].error)
        self.assertEqual(len(archive.records["PROBA"]), 1)

    def test_duplicate_input_card_rejected(self):
        source = ("LABOR PRIMA NOVA IMAGE\nIMAGO echo_nova.nvi\n"
                  "ACCIPE ACTA\nACCIPE PROBA\nEDE PROBA\nFINIS")
        with self.assertRaises(OrdoError):
            parse_deck(source)

    def test_file_archive_and_cli_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            run = subprocess.run([sys.executable, "-m", "ordo_operum", "run",
                                  str(EXAMPLES/"input_roundtrip.ord"), "--out-dir", td],
                                 cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
            report = json.loads((out/"report.json").read_text(encoding="utf-8"))
            self.assertEqual([j["status"] for j in report["jobs"]], ["FINIS"]*4)
            self.assertEqual(report["spools"]["ACTA"]["records"], 2)
            self.assertEqual(report["spools"]["PROBA"]["records"], 2)
            self.assertEqual(Archives.deserialize((out/"PROBA.omr").read_bytes()), (DATA, DATA))
            show = subprocess.run([sys.executable, "-m", "ordo_operum", "inspect",
                                   str(out/"PROBA.omr")], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(show.returncode, 0, show.stderr)
            self.assertEqual(show.stdout.count(GREETING), 2)


if __name__ == "__main__":
    unittest.main()
