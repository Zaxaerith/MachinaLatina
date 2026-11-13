"""Ordo Operum/P0 job deck, spool and failure-isolation tests.

A host-only suite: external CPU integration is a separate acceptance step.
"""
import json
import tempfile
import unittest
from pathlib import Path
from ordo_operum.monitor import (Archives, Execution, OrdoError,
                                  parse_deck, run_deck, write_results, _source_path)

ONE = ("LABOR PRIMA XXXVI TRANFOR\nFONTE portable_dot.trf\n"
       "EDE ACTA\nLIMES 100\nFINIS\n")
TWO = ONE + ("LABOR SECVN NOVA TRANFOR\nFONTE portable_dot.trf\n"
             "EDE ACTA\nFINIS\n")


class DeckTests(unittest.TestCase):
    def test_two_jobs(self):
        jobs = parse_deck(TWO)
        self.assertEqual([(j.name, j.target, j.limit) for j in jobs],
                         [("PRIMA", "XXXVI", 100), ("SECVN", "NOVA", 10000)])

    def test_empty_bad_and_unterminated(self):
        for source in ("", "; comment", ONE.removesuffix("FINIS\n"),
                       "FINIS", "FONTE foo.trf",
                       "LABOR PRIMA NOVA TRANFOR\nFINIS"):
            with self.subTest(source=source), self.assertRaises(OrdoError):
                parse_deck(source)

    def test_duplicate_names_cards_and_limit(self):
        for source in (
            TWO.replace("SECVN", "PRIMA"),
            ONE.replace("FINIS", "EDE ACTA\nFINIS"),
            ONE.replace("FINIS", "FONTE other.trf\nFINIS"),
            ONE.replace("LIMES 100", "LIMES 0"),
            ONE.replace("LIMES 100", "LIMES 100001")
        ):
            with self.subTest(source=source), self.assertRaises(OrdoError):
                parse_deck(source)

    def test_invalid_targets_cards_and_identifiers(self):
        for source in (
            ONE.replace("XXXVI", "UNIX"),
            ONE.replace("PRIMA", "JUICE"),
            ONE.replace("EDE ACTA", "EDE UPPER"),
            ONE.replace("LIMES 100", "SHELL exit"),
            ONE.replace("FONTE", "IMAGO")
        ):
            with self.subTest(source=source), self.assertRaises(OrdoError):
                parse_deck(source)

    def test_comments_and_order(self):
        source = ("; comment\n" + ONE.replace(
            "EDE ACTA\nLIMES 100", "LIMES 100 ; max instructions\nEDE ACTA"))
        self.assertEqual(parse_deck(source)[0].spool, "ACTA")

    def test_path_confinement(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "prog.trf").write_text("FINIS", encoding="utf-8")
            job = parse_deck(ONE.replace("portable_dot.trf", "prog.trf"))[0]
            self.assertEqual(_source_path(job, root), root / "prog.trf")
            for name in ("../outside.trf", "/tmp/secret.trf", "prog.m36",
                         "C:\\evil.trf", "missing.trf"):
                bad = parse_deck(ONE.replace("portable_dot.trf", name))[0]
                with self.subTest(name=name), self.assertRaises((OrdoError, FileNotFoundError)):
                    _source_path(bad, root)

    def test_image_suffix(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "prog.m36").write_text("00000 000000000000")
            job = parse_deck("LABOR TEST XXXVI IMAGE\nIMAGO prog.m36\nEDE ACTA\nFINIS")[0]
            self.assertEqual(_source_path(job, root).suffix, ".m36")


class ArchiveTests(unittest.TestCase):
    def test_two_records_and_empty_record(self):
        archive = Archives()
        archive.append("ACTA", bytes.fromhex("52 41 4B 54 45 20 8A 8E 82 8E 91"))
        archive.append("ACTA", b"")
        self.assertEqual(Archives.deserialize(archive.serialize("ACTA")),
                         tuple(archive.records["ACTA"]))

    def test_reject_truncated_and_unknown_bytes(self):
        a = Archives()
        a.append("ACTA", b"ABC")
        cases = (b"", b"OMR2", b"OMR1\x00", a.serialize("ACTA")[:-1],
                 b"OMR1\x00\x00\x00\x01\xff")
        for content in cases:
            with self.subTest(content=content), self.assertRaises((ValueError, KeyError)):
                Archives.deserialize(content)

    def test_invalid_spool(self):
        a = Archives()
        with self.assertRaises(OrdoError):
            a.append("JUICE", b"X")
        with self.assertRaises((ValueError, KeyError)):
            a.append("ACTA", b"\xff")
        with self.assertRaises(OrdoError):
            a.append("ACTA", b"a" * (1024*1024+1))

    def test_record_count_not_newlines(self):
        a = Archives()
        a.append("ACTA", b"ABC")
        a.append("ACTA", b"DEF")
        self.assertEqual(len(Archives.deserialize(a.serialize("ACTA"))), 2)


class MonitorTests(unittest.TestCase):
    def test_two_targets_one_spool(self):
        seen = []
        def fake(job, root):
            seen.append(job.target)
            return Execution("SALVE ΛΟΓΟΣ", 12, {"S": "0"})
        results, archives = run_deck(TWO, Path("."), fake)
        self.assertEqual([j.status for j in results], ["FINIS", "FINIS"])
        self.assertEqual(seen, ["XXXVI", "NOVA"])
        self.assertEqual(len(archives.records["ACTA"]), 2)

    def test_fail_job_continue(self):
        def fake(job, root):
            if job.name == "PRIMA":
                raise RuntimeError("synthetic failure")
            return Execution("OK", 3, {})
        results, archive = run_deck(TWO, Path("."), fake)
        self.assertEqual([j.status for j in results], ["ERROR", "FINIS"])
        self.assertEqual(len(archive.records["ACTA"]), 1)

    def test_step_budget(self):
        results, archive = run_deck(
            ONE, Path("."), lambda job, root: Execution("HI", job.limit+1, {}))
        self.assertEqual(results[0].status, "ERROR")
        self.assertFalse(archive.records)

    def test_output_manifest(self):
        results, archive = run_deck(
            TWO, Path("."), lambda job, root: Execution("SALVE", 3, {}))
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            write_results(root, results, archive)
            manifest = json.loads((root / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["spools"]["ACTA"]["records"], 2)
            self.assertEqual(len(Archives.deserialize((root / "ACTA.omr").read_bytes())), 2)


if __name__ == "__main__":
    unittest.main()
