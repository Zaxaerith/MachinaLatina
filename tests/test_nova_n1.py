"""Nova-N1 32-bit fixed instruction and byte-addressed CPU conformance checks."""
import subprocess
import sys
import unittest
from pathlib import Path

from machina_nova import (NovaCPU, NovaFault, decode_instruction,
                          encode_instruction, greeting_image, format_image,
                          parse_image, read_image, GREETING)
from machina_xxxvi import Machine
from machina_xxxvi.__main__ import demo_words
from machina_xxxvi.gateway import decode_cvl68, encode_cvl68

ROOT = Path(__file__).resolve().parents[1]


def flattened(regions):
    return {address + offset: value for address, payload in regions.items()
            for offset, value in enumerate(payload)}


def instructions(*items):
    """List (opcode, operand) pairs to native four-byte words."""
    return b"".join(encode_instruction(op, operand) for op, operand in items)


class NovaTests(unittest.TestCase):
    def machine(self, code, data=None, memory_size=1024):
        m = NovaCPU(memory_size)
        m.load_regions({0: code, **(data or {})})
        return m

    def test_instruction_encoding_is_not_legacy(self):
        self.assertEqual(encode_instruction(0x50, 0x100), bytes.fromhex("50 00 01 00"))
        self.assertEqual(decode_instruction(bytes.fromhex("41 AB CD EF")), (0x41, 0xABCDEF))
        self.assertEqual(encode_instruction(0), b"\x00" * 4)
        for op, operand in [(0xFF, 0), (0, 1), (0x10, 1 << 24)]:
            with self.subTest(op=op, operand=operand), self.assertRaises(ValueError):
                encode_instruction(op, operand)
        for word in [b"\x00\x00\x00\x01", b"\xFF\x00\x00\x00"]:
            with self.assertRaises(NovaFault):
                decode_instruction(word)

    def test_greeting_fixture_and_old_new_comparison(self):
        sample = read_image(ROOT / "examples/nova_salve_logos.nvi")
        m = NovaCPU()
        m.load_regions(sample)
        self.assertEqual(m.run(), GREETING)
        self.assertEqual(m.steps, 12)
        self.assertEqual(decode_cvl68(m.output), "SALVE ΛΟΓΟΣ")
        self.assertEqual(flattened(sample), flattened(greeting_image()))
        old = Machine()
        old.load(demo_words())
        self.assertEqual(old.run(), decode_cvl68(m.output))
        self.assertNotEqual(encode_instruction(0x50, 0x100),
                            (0o001000000100).to_bytes(5, "big"))

    def test_byte_read_write_and_low8_storage(self):
        code = instructions((0x40, 0x1234), (0x12, 0x100), (0x10, 0x100),
                            (0x50, 0x100), (0, 0))
        m = self.machine(code, {0x100: b"\x00"})
        self.assertEqual(m.run(), b"\x34")
        self.assertEqual(m.a, 0x34)
        self.assertEqual(m.memory.read_byte(0x100), 0x34)

    def test_word_memory_and_big_endian(self):
        code = instructions((0x11, 0x100), (0x13, 0x104), (0x10, 0x104), (0, 0))
        m = self.machine(code, {0x100: bytes.fromhex("12 34 56 78")})
        m.run()
        self.assertEqual(m.memory.read_bytes(0x104, 4), bytes.fromhex("12 34 56 78"))
        self.assertEqual(m.a, 0x12)

    def test_modular_arithmetic(self):
        code = instructions((0x11, 0x100), (0x20, 0x104), (0x13, 0x108),
                            (0x21, 0x104), (0x41, 3), (0, 0))
        m = self.machine(code, {0x100: bytes.fromhex("FF FF FF FE"),
                                0x104: bytes.fromhex("00 00 00 05")})
        m.run()
        self.assertEqual(m.memory.read_word32(0x108), 3)
        self.assertEqual(m.a, 1)

    def test_branches_taken_not_taken_and_halt(self):
        code = instructions((0x40, 0), (0x31, 16), (0x40, 42), (0x30, 20),
                            (0x40, 7), (0x00, 0))
        m = self.machine(code)
        m.run()
        self.assertEqual(m.a, 7)
        self.assertEqual(m.steps, 4)
        code2 = instructions((0x40, 5), (0x31, 16), (0x41, 2), (0, 0), (0x40, 99))
        m = self.machine(code2)
        m.run()
        self.assertEqual(m.a, 7)

    def test_atomic_fault_unknown_isa_and_invalid_fin(self):
        for word in [bytes.fromhex("FF 00 00 00"), bytes.fromhex("00 00 00 01")]:
            m = self.machine(word)
            with self.assertRaises(NovaFault):
                m.step()
            self.assertEqual((m.pc, m.steps, m.a, m.output), (0, 0, 0, bytearray()))

    def test_atomic_alignment_and_memory_bounds(self):
        for opcode, operand in [(0x11, 0x101), (0x13, 0x101),
                                (0x20, 0x101), (0x21, 0x101),
                                (0x10, 0x1000), (0x12, 0x1000),
                                (0x50, 0x1000), (0x30, 0x000003)]:
            with self.subTest(op=opcode, addr=operand):
                m = self.machine(instructions((opcode, operand)))
                with self.assertRaises(NovaFault):
                    m.step()
                self.assertEqual((m.pc, m.steps, m.a, bytes(m.output)), (0, 0, 0, b""))
        m = self.machine(instructions((0x40, 1), (0x31, 13), (0, 0)))
        self.assertEqual(m.run(), b"")

    def test_pc_alignment_and_limits(self):
        m = self.machine(instructions((0x30, 0)))
        with self.assertRaisesRegex(NovaFault, "step limit"):
            m.run(3)
        self.assertEqual(m.steps, 3)
        m.pc = 1
        with self.assertRaises(NovaFault):
            m.step()
        with self.assertRaises(ValueError):
            m.run(0)
        with self.assertRaises(ValueError):
            NovaCPU(0)

    def test_atomic_region_overlap_and_overrun(self):
        m = NovaCPU(512)
        for regions in [{0:b"\x01\x02", 1:b"\x03"}, {511:b"\x01\x02"},
                        {1 << 24:b"\x00"}, {0:b""}]:
            with self.subTest(regions=regions), self.assertRaises(ValueError):
                m.load_regions(regions)
        self.assertEqual(m.memory.read_bytes(0, 4), b"\x00" * 4)

    def test_image_format_roundtrip_and_errors(self):
        raw = greeting_image()
        self.assertEqual(flattened(parse_image(format_image(raw))), flattened(raw))
        for bad in ["000000: GG", "000000 00", "0: 00", "000000: 00\n000000: 00",
                    "FFFFFF: 00 00", "000000:"]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                parse_image(bad)

    def test_cli_both_nova_and_compare(self):
        for args in [["demo"], ["run", "examples/nova_salve_logos.nvi"]]:
            process = subprocess.run([sys.executable, "-m", "machina_nova", *args],
                                     cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(process.stdout.strip(), "SALVE ΛΟΓΟΣ")
        process = subprocess.run([sys.executable, "-m", "machina_nova", "compare"],
                                 cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertIn("TEXT MATCH / BINARY INCOMPATIBLE", process.stdout)
        self.assertEqual(encode_cvl68("SALVE ΛΟΓΟΣ"), GREETING)


if __name__ == "__main__":
    unittest.main()
