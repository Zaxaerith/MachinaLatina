"""Conformance tests for the fictional Machina XXXVI/P0 reference machine."""
import unittest

from machina_xxxvi import Machine, MachineFault, encode_instruction, pack_codes, unpack_codes
from machina_xxxvi.cvl54 import CharacterFault, Printer
from machina_xxxvi.image import parse_image
from machina_xxxvi.__main__ import demo_words


class MachineTests(unittest.TestCase):
    def run_words(self, instructions, data=None, max_steps=100):
        m = Machine()
        m.load({**{i: w for i, w in enumerate(instructions)}, **(data or {})})
        m.run(max_steps)
        return m

    def test_word_vectors(self):
        self.assertEqual(encode_instruction(8, 0o100), 0o001000000100)
        self.assertEqual(encode_instruction(8, 0o101), 0o001000000101)
        self.assertEqual(pack_codes([0o22, 0o01, 0o13, 0o24, 0o05, 0o43]), 0o220113240543)
        self.assertEqual(pack_codes([0o61, 0o13, 0o17, 0o03, 0o17, 0o22]), 0o611317031722)
        self.assertEqual(unpack_codes(0o611317031722), (0o61, 0o13, 0o17, 0o03, 0o17, 0o22))

    def test_hello_demo(self):
        m = Machine()
        m.load(demo_words())
        self.assertEqual(m.run(), "SALVE ΛΟΓΟΣ")
        self.assertEqual(m.steps, 3)
        self.assertTrue(m.halted)

    def test_arithmetic_example(self):
        instructions = [encode_instruction(9, 7), encode_instruction(2, 0o102),
                        encode_instruction(9, 5), encode_instruction(3, 0o102),
                        encode_instruction(2, 0o103), encode_instruction(0)]
        m = self.run_words(instructions)
        self.assertEqual((m.a, m.memory[0o103]), (12, 12))

    def test_all_arithmetic_memory_and_branch(self):
        instructions = [encode_instruction(9, 10), encode_instruction(2, 0o100),
                        encode_instruction(1, 0o100), encode_instruction(4, 0o100),
                        encode_instruction(6, 7), encode_instruction(9, 2),
                        encode_instruction(5, 8), encode_instruction(9, 3),
                        encode_instruction(0)]
        m = self.run_words(instructions)
        self.assertEqual(m.a, 3)
        self.assertTrue(m.z is False)

    def test_index_registers_and_address_wrap(self):
        for tag, index in [(1, 0), (2, 1), (4, 2)]:
            m = self.run_words([encode_instruction(7, 5, tag),
                                encode_instruction(1, 0o100, tag),
                                encode_instruction(0)], {0o105: 17})
            self.assertEqual(m.a, 17)
            self.assertEqual(m.x[index], 5)
        m = self.run_words([encode_instruction(7, 1, 1),
                            encode_instruction(1, 0o77777, 1),
                            encode_instruction(0)], {0: encode_instruction(7, 1, 1)})
        self.assertEqual(m.a, encode_instruction(7, 1, 1))

    def test_modulo_wrap(self):
        m = self.run_words([encode_instruction(1, 0o100),
                            encode_instruction(3, 0o101), encode_instruction(0)],
                           {0o100: (1 << 36) - 1, 0o101: 2})
        self.assertEqual(m.a, 1)
        m = self.run_words([encode_instruction(9, 0), encode_instruction(4, 0o100),
                            encode_instruction(0)], {0o100: 1})
        self.assertEqual(m.a, (1 << 36) - 1)

    def test_greek_state_persists_between_words(self):
        p = Printer()
        p.feed_word(pack_codes([49, 1, 2, 3, 4, 5]))
        p.feed_word(pack_codes([6, 7, 8, 9, 10, 11]))
        self.assertEqual(p.text, "ΑΒΓΔΕΖΗΘΙΚΛ")
        self.assertEqual(p.page, "GRAECA")

    def test_eot_reset_and_padding(self):
        p = Printer()
        p.feed_word(pack_codes([49, 1, 52, 1, 0, 0]))
        self.assertEqual(p.text, "ΑA")
        self.assertEqual(p.page, "LATINA")
        with self.assertRaises(CharacterFault):
            p.feed_word(pack_codes([1] * 6))

    def test_printer_atomic_on_fault(self):
        p = Printer()
        with self.assertRaises(CharacterFault):
            p.feed_word(pack_codes([1, 2, 0, 3, 0, 0]))
        self.assertEqual((p.text, p.page, p.padded), ("", "LATINA", False))
        with self.assertRaises(CharacterFault):
            p.feed_word(pack_codes([1, 2, 24, 0, 0, 0]))
        self.assertEqual(p.text, "")

    def test_reject_reserved_instruction_fields(self):
        bad = [encode_instruction(10), encode_instruction(1, indirect=1),
               encode_instruction(1, aux=1), encode_instruction(1, tag=3),
               encode_instruction(0, adr=1), encode_instruction(9, tag=1),
               encode_instruction(7, tag=0)]
        for instruction in bad:
            with self.subTest(word=instruction):
                m = Machine()
                m.load({0: instruction})
                with self.assertRaises(MachineFault):
                    m.step()
                self.assertEqual((m.pc, m.steps), (0, 0))

    def test_invalid_inputs_and_atomic_load(self):
        for bad in [-1, 1 << 36, True]:
            with self.assertRaises(ValueError):
                pack_codes([bad, 0, 0, 0, 0, 0])
        m = Machine()
        with self.assertRaises(ValueError):
            m.load({0: 1, 1 << 15: 2})
        self.assertEqual(m.memory[0], 0)
        with self.assertRaises(ValueError):
            m.run(0)

    def test_infinite_loop_guard(self):
        m = Machine()
        m.load({0: encode_instruction(5, 0)})
        with self.assertRaisesRegex(MachineFault, "step limit"):
            m.run(3)
        self.assertEqual(m.steps, 3)

    def test_image_parser(self):
        image = """; example
00000 001000000100
00001 001000000101 ; comment
00100 220113240543
"""
        self.assertEqual(parse_image(image)[0o100], 0o220113240543)
        for bad in ("00000 123", "00000 000000000000\n00000 000000000000",
                    "88888 000000000000", "100000 000000000000"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                parse_image(bad)


if __name__ == "__main__":
    unittest.main()
