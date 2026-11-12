"""Phase VI assembler and text gateway conformance tests."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from machina_xxxvi import Machine, pack_codes
from machina_xxxvi.assembler import AssemblyError, assemble, format_image, text_codes
from machina_xxxvi.gateway import GatewayError, decode_cvl68, encode_cvl68, transcode_words
from machina_xxxvi.image import load_image, parse_image

ROOT = Path(__file__).resolve().parents[1]

class AssemblerTests(unittest.TestCase):
    def test_exact_legacy_example(self):
        source = (ROOT/'examples/salve_logos.mxa').read_text(encoding='utf-8')
        words = assemble(source)
        self.assertEqual(words, load_image(ROOT/'examples/salve_logos.m36'))
        self.assertEqual(parse_image(format_image(words)), words)
        m = Machine()
        m.load(words)
        self.assertEqual(m.run(), 'SALVE ΛΟΓΟΣ')

    def test_text_directive(self):
        words = assemble('ORG 00000\nEMIT SCRIP\nEMIT 00101\nFIN\nORG 00100\nSCRIP: TEX "SALVE ΛΟΓΟΣ"')
        self.assertEqual([words[0o100],words[0o101]],
                         [pack_codes([0o22,0o01,0o13,0o24,0o05,0o43]),
                          pack_codes([0o61,0o13,0o17,0o03,0o17,0o22])])

    def test_forward_labels_and_indexing(self):
        words = assemble('ORG 00000\nPONX X2,00005\nLEGE X2+DATA\nFIN\nORG 00100\nDATA: VER 01,02,03,04,05,06')
        self.assertEqual(words[1], 0o000100200100)
        self.assertEqual(words[0], 0o000700200005)

    def test_typed_errors(self):
        bad = [
            'ORG 80000\nFIN', 'FIN 00001', 'LEGE UNKNOWN',
            'ABC: FIN\nABC: FIN', 'TEX "καλημέρα"',
            'ORG 00000\nFIN\nORG 00000\nFIN',
            'VER 01,02', 'VER 01,02,03,04,05,88',
            'PONX X4,00001', 'NVM X1+00001',
            'ORG 77777\nTEX "SALVE ΛΟΓΟΣ"',
        ]
        for source in bad:
            with self.subTest(source=source), self.assertRaises(AssemblyError):
                assemble(source)
        self.assertEqual(text_codes('SALVE ΛΟΓΟΣ'),
                         [0o22,0o01,0o13,0o24,0o05,0o43,0o61,0o13,0o17,0o03,0o17,0o22])

    def test_cli_assemble(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td)/'demo.m36'
            ret = subprocess.run([sys.executable,'-m','machina_xxxvi','assemble',
                                  str(ROOT/'examples/salve_logos.mxa'),'--output',str(output)],
                                 cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(ret.returncode,0,ret.stderr)
            self.assertEqual(load_image(output),load_image(ROOT/'examples/salve_logos.m36'))
            run = subprocess.run([sys.executable,'-m','machina_xxxvi','run',str(output)],
                                 cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(run.stdout.strip(),'SALVE ΛΟΓΟΣ')

class GatewayTests(unittest.TestCase):
    def test_direct_translation(self):
        words = load_image(ROOT/'examples/salve_logos.m36')
        raw = transcode_words([words[0o100],words[0o101]])
        self.assertEqual(raw,bytes.fromhex('52 41 4B 54 45 20 8A 8E 82 8E 91'))
        self.assertEqual(decode_cvl68(raw),'SALVE ΛΟΓΟΣ')
        self.assertEqual(encode_cvl68('SALVE ΛΟΓΟΣ'),raw)
        self.assertNotEqual(encode_cvl68('A'),encode_cvl68('Α'))

    def test_polytonic_byte_subset_and_rejection(self):
        self.assertEqual(encode_cvl68('α\u0313\u0301'),b'\xa0\xbb\xb8')
        self.assertEqual(decode_cvl68(b'\xa0\xbb\xb8'),'α\u0313\u0301')
        with self.assertRaises(GatewayError):
            encode_cvl68('ἄ')  # no implicit Unicode normalization
        with self.assertRaises(GatewayError):
            decode_cvl68(b'\xff')  # reserved position

    def test_greek_page_omega_and_errors(self):
        self.assertEqual(transcode_words([pack_codes([49,24,0,0,0,0])]),b'\x97')
        with self.assertRaises(ValueError):
            transcode_words([pack_codes([24,0,0,0,0,0])])

    def test_cli_bridge(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td)/'out.cvl'
            ret = subprocess.run([sys.executable,'-m','machina_xxxvi','bridge',
                                  str(ROOT/'examples/salve_logos.m36'),'00100','00101',
                                  '--output',str(output)],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(ret.returncode,0,ret.stderr)
            self.assertEqual(output.read_bytes(),bytes.fromhex('52 41 4B 54 45 20 8A 8E 82 8E 91'))
            self.assertIn('SALVE ΛΟΓΟΣ',ret.stdout)
            bad = subprocess.run([sys.executable,'-m','machina_xxxvi','bridge',
                                  str(ROOT/'examples/salve_logos.m36'),'00500'],
                                 cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(bad.returncode,1)
            self.assertIn('missing image word',bad.stderr)

if __name__=='__main__':
    unittest.main()
