"""Phase XIV: record-status, EOF transitions and six real native-machine jobs."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from machina_xxxvi import Machine, MachineFault, encode_instruction as old_inst
from machina_nova import NovaCPU, NovaFault, encode_instruction as new_inst
from ordo_operum.monitor import Archives, OrdoError, parse_deck, run_deck

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
HELLO = "SALVE ΛΟΓΟΣ"


class StatusTests(unittest.TestCase):
    def test_xxxvi_status_offline_empty_eor_eof(self):
        offline = Machine()
        offline.load({0: old_inst(17)})
        offline.step()
        self.assertEqual(offline.a, 3)
        cpu = Machine()
        cpu.load({0: old_inst(17), 1: old_inst(18), 2: old_inst(17),
                  3: old_inst(18), 4: old_inst(17), 5: old_inst(0)})
        cpu.mount_records((tuple(), tuple()))
        self.assertEqual(cpu.input_status, 1)
        cpu.step()
        self.assertEqual(cpu.a, 1)
        cpu.step()
        self.assertEqual((cpu.input_status, cpu.input_record_index), (1, 1))
        cpu.step()
        self.assertEqual(cpu.a, 1)
        cpu.step()
        self.assertEqual(cpu.input_status, 2)
        cpu.step()
        self.assertEqual(cpu.a, 2)
        cpu.run()

    def test_nova_status_offline_empty_eor_eof(self):
        offline = NovaCPU()
        offline.load_regions({0: new_inst(0x67)})
        offline.step()
        self.assertEqual(offline.a, 3)
        cpu = NovaCPU()
        cpu.load_regions({0: b"".join(new_inst(op) for op in
                                       (0x67, 0x68, 0x67, 0x68, 0x67, 0))})
        cpu.mount_records((b"", b""))
        cpu.step()
        self.assertEqual(cpu.a, 1)
        cpu.step()
        self.assertEqual((cpu.input_status, cpu.input_record_index), (1, 1))
        cpu.step()
        self.assertEqual(cpu.a, 1)
        cpu.step()
        self.assertEqual(cpu.input_status, 2)
        cpu.step()
        self.assertEqual(cpu.a, 2)

    def test_data_status_then_eor_and_eof(self):
        for kind in ("old", "nova"):
            if kind == "old":
                cpu = Machine()
                cpu.load({0: old_inst(17), 1: old_inst(16, 0o100),
                          2: old_inst(17), 3: old_inst(18), 4: old_inst(17), 5: old_inst(0)})
                cpu.mount_records(((0o123456,),))
            else:
                cpu = NovaCPU()
                cpu.load_regions({0: b"".join([
                    new_inst(0x67), new_inst(0x66, 0x100), new_inst(0x67),
                    new_inst(0x68), new_inst(0x67), new_inst(0)]),
                                  0x100: b"\x00"})
                cpu.mount_records((b"X",))
            self.assertEqual(cpu.input_status, 0)
            cpu.step()
            self.assertEqual(cpu.a, 0)
            cpu.step()
            self.assertEqual(cpu.input_status, 1)
            cpu.step()
            self.assertEqual(cpu.a, 1)
            cpu.step()
            self.assertEqual(cpu.input_status, 2)
            cpu.step()
            self.assertEqual(cpu.a, 2)

    def test_early_prox_fails_atomically(self):
        old = Machine()
        old.load({0: old_inst(18)})
        old.mount_records(((42,),))
        with self.assertRaisesRegex(MachineFault, "before input record ends"):
            old.step()
        self.assertEqual((old.pc, old.steps, old.input_position, old.input_record_index), (0, 0, 0, 0))
        new = NovaCPU()
        new.load_regions({0: new_inst(0x68)})
        new.mount_records((b"X",))
        with self.assertRaisesRegex(NovaFault, "before input record ends"):
            new.step()
        self.assertEqual((new.pc, new.steps, new.input_position, new.input_record_index), (0, 0, 0, 0))

    def test_bad_zero_operand_rejected(self):
        old = Machine()
        old.load({0: old_inst(17, 1)})
        with self.assertRaisesRegex(MachineFault, "zero operand"):
            old.step()
        new = NovaCPU()
        new.load_regions({0: new_inst(0x67, 1)})
        with self.assertRaisesRegex(NovaFault, "zero operand"):
            new.step()
        self.assertEqual((old.pc, old.steps, new.pc, new.steps), (0, 0, 0, 0))

    def test_prox_at_eof_idempotent_and_offline_rejected(self):
        for kind in ("old", "nova"):
            if kind == "old":
                cpu = Machine()
                cpu.load({0: old_inst(18), 1: old_inst(0)})
                with self.assertRaisesRegex(MachineFault, "without attached records"):
                    cpu.step()
                cpu.mount_records(tuple())
            else:
                cpu = NovaCPU()
                cpu.load_regions({0: new_inst(0x68) + new_inst(0)})
                with self.assertRaisesRegex(NovaFault, "without attached records"):
                    cpu.step()
                cpu.mount_records(tuple())
            self.assertEqual(cpu.input_status, 2)
            cpu.step()
            self.assertEqual(cpu.input_status, 2)
            self.assertEqual(cpu.input_record_index, 0)

    def test_mount_validation_and_legacy_single_record(self):
        old = Machine()
        with self.assertRaises(ValueError):
            old.mount_records(((1, False),))
        old.mount_input((1,))
        self.assertEqual(old.input_status, 0)
        new = NovaCPU()
        with self.assertRaises(ValueError):
            new.mount_records((bytearray(b"X"),))
        new.mount_input(b"X")
        self.assertEqual(new.input_status, 0)


class MonitorSeriesTests(unittest.TestCase):
    def test_series_deck_parses_and_old_accipe_unchanged(self):
        deck = parse_deck((EXAMPLES/"input_series.ord").read_text(encoding="utf-8"))
        self.assertEqual(len(deck), 6)
        self.assertEqual(deck[2].series_spool, "ACTA")
        self.assertEqual(deck[2].series_count, 2)
        self.assertEqual(deck[5].series_spool, "ALTERA")
        self.assertEqual(deck[5].series_count, 2)
        old = parse_deck((EXAMPLES/"input_roundtrip.ord").read_text(encoding="utf-8"))
        self.assertEqual(old[2].input_spool, "ACTA")
        self.assertIsNone(old[2].series_spool)

    def test_six_real_native_jobs(self):
        results, archives = run_deck((EXAMPLES/"input_series.ord").read_text(encoding="utf-8"), EXAMPLES)
        self.assertEqual([j.status for j in results], ["FINIS"]*6, [j.error for j in results])
        self.assertEqual([j.text for j in results], ["SALVE ", "ΛΟΓΟΣ", HELLO,
                                                    "SALVE ", "ΛΟΓΟΣ", HELLO])
        self.assertEqual(len(archives.records["ACTA"]), 2)
        self.assertEqual(len(archives.records["ALTERA"]), 2)
        self.assertEqual(Archives.deserialize(archives.serialize("PROBA")),
                         tuple(archives.records["PROBA"]))
        self.assertEqual([len(x) for x in archives.records["PROBA"]], [11, 11])

    def test_series_partial_or_missing_is_error_without_consumption(self):
        base = """LABOR PRIMA NOVA TRANFOR
FONTE record_latin.trf
EDE ACTA
FINIS

"""
        bad = """LABOR SECVN NOVA IMAGE
IMAGO echo_series_nova.nvi
SERIES ACTA 2
EDE PROBA
FINIS

"""
        tail = """LABOR TERTIA NOVA IMAGE
IMAGO nova_salve_logos.nvi
ACCIPE ACTA
EDE PROBA
FINIS
"""
        results, archives = run_deck(base+bad+tail, EXAMPLES)
        self.assertEqual([r.status for r in results], ["FINIS", "ERROR", "FINIS"])
        self.assertIn("not enough unread records", results[1].error)
        self.assertEqual(len(archives.records["PROBA"]), 1)

    def test_series_failed_guest_does_not_consume(self):
        base = """LABOR PRIMA NOVA TRANFOR
FONTE record_latin.trf
EDE ACTA
FINIS

LABOR SECVN NOVA TRANFOR
FONTE record_greek.trf
EDE ACTA
FINIS

"""
        broken = """LABOR TERTIA NOVA IMAGE
IMAGO nova_salve_logos.nvi
SERIES ACTA 2
EDE PROBA
FINIS

"""
        valid = """LABOR QVARTA NOVA IMAGE
IMAGO echo_series_nova.nvi
SERIES ACTA 2
EDE PROBA
FINIS
"""
        results, archives = run_deck(base + broken + valid, EXAMPLES)
        self.assertEqual([r.status for r in results], ["FINIS", "FINIS", "ERROR", "FINIS"])
        self.assertIn("without reaching EOF", results[2].error)
        self.assertEqual(len(archives.records["PROBA"]), 1)

    def test_duplicate_and_conflicting_cards(self):
        head = "LABOR PRIMA NOVA IMAGE\nIMAGO echo_series_nova.nvi\n"
        for body in ("SERIES ACTA 0\n", "SERIES ACTA 33\n",
                     "SERIES ACTA 2\nSERIES ACTA 2\n",
                     "ACCIPE ACTA\nSERIES ACTA 2\n",
                     "SERIES ACTA 2\nACCIPE ACTA\n",
                     "SERIES JUICE 2\n", "SERIES ACTA z\n",
                     "SERIES ACTA\n"):
            with self.subTest(body=body), self.assertRaises(OrdoError):
                parse_deck(head + body + "EDE PROBA\nFINIS")

    def test_cli_six_jobs_and_archive_inspection(self):
        with tempfile.TemporaryDirectory() as temp:
            cmd = subprocess.run([sys.executable, "-m", "ordo_operum", "run",
                                  str(EXAMPLES/"input_series.ord"), "--out-dir", temp],
                                 cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(cmd.returncode, 0, cmd.stdout + cmd.stderr)
            meta = json.loads((Path(temp)/"report.json").read_text(encoding="utf-8"))
            self.assertEqual([r["status"] for r in meta["jobs"]], ["FINIS"]*6)
            self.assertEqual(meta["spools"]["PROBA"]["records"], 2)
            show = subprocess.run([sys.executable, "-m", "ordo_operum", "inspect",
                                   str(Path(temp)/"PROBA.omr")], cwd=ROOT,
                                  capture_output=True, text=True)
            self.assertEqual(show.returncode, 0, show.stderr)
            self.assertEqual(show.stdout.count(HELLO), 2)


if __name__ == "__main__":
    unittest.main()
