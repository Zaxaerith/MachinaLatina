"""Phase VII memory-layout experiments; deliberately not a Nova CPU conformance test."""
import unittest

from machina_xxxvi.archlab import (
    RetrofitRecord, NovaMemory, retrofit_pack, demo,
    LEGACY_WORDS, RETROFIT_BYTES_PER_WORD,
)


class RetrofitTests(unittest.TestCase):
    def test_exact_words_and_roundtrip(self):
        data = bytes.fromhex("52 41 4B 54 45 20 8A 8E 82 8E 91")
        record = retrofit_pack(data)
        self.assertEqual(record.logical_bytes, 11)
        self.assertEqual(record.words, (0x52414B540, 0x45208A8E0, 0x828E91000))
        self.assertEqual(record.to_bytes(), data)
        self.assertEqual(len(record.words) * 36, 108)
        self.assertEqual(len(data) * 8, 88)

    def test_all_record_remainders_including_zero_bytes(self):
        for n in range(17):
            data = bytes((i * 37) % 256 for i in range(n))
            record = retrofit_pack(data)
            self.assertEqual(record.to_bytes(), data)
            self.assertEqual(len(record.words), (n + 3) // 4)
        self.assertEqual(retrofit_pack(b"\x00\x00\x00\x00").to_bytes(), b"\x00" * 4)
        self.assertEqual(retrofit_pack(b"").to_bytes(), b"")

    def test_noncanonical_and_corruption_rejections(self):
        for record in [RetrofitRecord((0x10,), -1), RetrofitRecord((0x10,), 5),
                       RetrofitRecord((0x10,), 0), RetrofitRecord((1,), 4),
                       RetrofitRecord((1 << 36,), 4), RetrofitRecord((0x000100000,), 1)]:
            with self.subTest(record=record), self.assertRaises(ValueError):
                record.to_bytes()
        with self.assertRaises(TypeError):
            retrofit_pack(bytearray(b"hello"))
        with self.assertRaises(ValueError):
            retrofit_pack(bytes((LEGACY_WORDS * RETROFIT_BYTES_PER_WORD) + 1))


class NovaTests(unittest.TestCase):
    def test_byte_addressing_and_endian_word(self):
        memory = NovaMemory(1024)
        memory.load(0x100, b"\x12\x34\x56\x78")
        self.assertEqual(memory.read_word32(0x100), 0x12345678)
        self.assertEqual(memory.read_byte(0x101), 0x34)
        memory.write_byte(0x102, 0xAB)
        self.assertEqual(memory.read_word32(0x100), 0x1234AB78)
        memory.write_word32(0x100, 0xDEADBEEF)
        self.assertEqual(memory.read_bytes(0x100, 4), bytes.fromhex("DE AD BE EF"))

    def test_alignment_bounds_and_type_check(self):
        memory = NovaMemory(8)
        for run in [lambda: NovaMemory(0), lambda: NovaMemory(1 << 24 | 1),
                    lambda: memory.read_byte(8), lambda: memory.read_bytes(7, 2),
                    lambda: memory.read_word32(2), lambda: memory.write_word32(4, 1 << 32),
                    lambda: memory.write_byte(0, -1), lambda: memory.load(7, b"abc")]:
            with self.subTest(run=run), self.assertRaises(ValueError):
                run()

    def test_retrofit_to_nova_copy(self):
        data = bytes.fromhex("52 41 4B 54 45 20 8A 8E 82 8E 91")
        record = retrofit_pack(data)
        nova = NovaMemory(512)
        nova.load(0x80, record.to_bytes())
        self.assertEqual(nova.read_byte(0x86), 0x8A)
        self.assertEqual(nova.read_bytes(0x80, 11), data)

    def test_demo(self):
        self.assertIn("Nova-N0 byte address 0x000106: 0x8A", demo())


if __name__ == "__main__":
    unittest.main()
