# CVL-63/TP1 — Migration and Parity Ledger
## 六位数据、七位校验传输、八位原生文本之间的实际区别

> **DRAFT, documentary worked examples.** This worksheet computes examples from the existing [CVL-54/P0 profile](../specifications/CVL-54-P0.md), the new [CVL-63/TP1 proposal](../specifications/CVL-63-TP1.md) and [CVL-68/RC1](../specifications/CVL-68-RC1.md). The three codebooks are not declared CANON by this document. No executable converter or CI was added.

## A complete small mixed-script record

As originally documented for CVL-54/P0:

    SALVE ΛΟΓΟΣ

The 36-bit XXXVI records contain **two consecutive 36-bit words**, each holding six 6-bit codes. The first word contains a trailing space and the second contains the Greek page-switch unit and five uppercase Greek letters.

    36-bit word 1: 220113240543 (octal)
    36-bit word 2: 611317031722 (octal)

Do **not** reset Latin/Greek state between these two words; they are in the same logical record.

| Index | Source code (octal, six bits) | Interpretation | Popcount parity p | TP1 7-bit t (hex editorial) | Seven-bit binary |
| ---: | ---: | --- | ---: | --- | --- |
| 0 | 22 | LATINA S | 0 | 12 | 0010010 |
| 1 | 01 | LATINA A | 1 | 41 | 1000001 |
| 2 | 13 | LATINA L | 1 | 4B | 1001011 |
| 3 | 24 | LATINA V | 0 | 14 | 0010100 |
| 4 | 05 | LATINA E | 0 | 05 | 0000101 |
| 5 | 43 | SPACE | 1 | 63 | 1100011 |
| 6 | 61 | SHIFT-GRC; no displayed character | 1 | 71 | 1110001 |
| 7 | 13 | GRAECA Λ | 1 | 4B | 1001011 |
| 8 | 17 | GRAECA Ο | 0 | 0F | 0001111 |
| 9 | 03 | GRAECA Γ | 0 | 03 | 0000011 |
| 10 | 17 | GRAECA Ο | 0 | 0F | 0001111 |
| 11 | 22 | GRAECA Σ | 0 | 12 | 0010010 |

The seven-bit TP1 units in transmission order (shown as two-digit hex numbers for **human reading**, not as eight-bit file bytes):

    12 41 4B 14 05 63 71 4B 0F 03 0F 12

Every seven-bit slot contains even parity. The underlying six-bit unit is recovered by masking to the low six bits **only after parity validation**. Latin S and Greek Σ can both have original six-bit code 22, so the page state remains essential.

## Text transcoding into 1968 direct CVL-68/RC1

The TP1 receiver removes the parity layer (not a character), then decodes the 12 six-bit units with the state machine. One of those units is the SHIFT, so the rendered output contains **11 characters**. Under the candidate CVL-68/RC1 direct byte encoding:

    52 41 4B 54 45 20 8A 8E 82 8E 91

This is a **new encoding of the same abstract text**, not the result of appending a bit to each old six-bit code. It is also not the direct bytes of reality's ASCII or UTF-8.

| Representation | Symbols/bytes | Payload bits | Caveat |
| --- | ---: | ---: | --- |
| Packed XXXVI text | 12 six-bit source units (two words) | 72 | Preserves local shift state if record boundary known |
| CVL-63/TP1 logical link payload | 12 seven-bit slots | 84 | **+16⅔%** over six-bit payload, excluding link framing |
| CVL-68/RC1 direct text | 11 eight-bit bytes | 88 | **+4.76%** over TP1 *for this one phrase*, no shift byte |

These figures are a **single sample**, not a universal compression comparison. A Latin-only message gains no benefit from dropping Greek shifts; a shift-heavy mixed scientific document might have a different bit-cost tradeoff. Real serial framing and parity/checksum cost may change the comparison dramatically.

## A parity failure that can be detected

SHIFT-GRC c=61 octal (49 decimal) → TP1 71 hex. A one-bit flip in its parity bit produces 31 hex, now odd parity, rejected. The strict receiver **must not** feed an unchecked SHIFT command to the page decoder.

## A two-bit failure that passes parity

The same 71 hex with two lower-bit flips becomes 72 hex. The resulting even-parity word carries low-six-bit code 62 octal (LF) instead of code 61 (SHIFT-GRC). The text can now be corrupted despite parity passing; TP1 cannot detect this error in isolation.

Physical record-length checking may catch some dropped units, but cannot detect all equal-count substitutions. A separate checksum or retransmission method remains an open item.

## Migration risk matrix

| Input | Proper action | Bad shortcut |
| --- | --- | --- |
| Raw XXXVI 36-bit packed word | Unpack according to P0 ordering and known record/page state | Read the word as four or five arbitrary bytes |
| CVL-63 TP1 link slot | Check parity, extract six-bit original, interpret under P0 | Treat t=41 as Latin A ASCII/CVL-68 |
| CVL-54 SHIFT-GRC | Update current language page only | Print the shift or treat its high bit as a new Greek letter |
| CVL-54 PAD | Preserve original machine word/padding in archival metadata | Emit PAD as an additional text glyph |
| CVL-54 EOT | Respect logical end-of-record and reset semantics | Guess that an EOT corresponds to printable newline |
| CVL-68 base bytes | Produce 1968 direct byte codes after *character* decoding | Pad/extend six-bit integers to byte values |
| Source with accents/lowercase absent from P0 | Reject or annotate lost information explicitly | Add historically unknowable Greek accent marks |
| Lost raw tape framing | Preserve available provenance and report loss | Promise a bit-exact archive reconstruction |

## Practical editorial conclusion

CVL-63/TP1 can **reliably detect certain transmission errors without creating new text identities**. It explains why 1963 telecommunications equipment might improve while XXXVI files and word size remain unchanged. CVL-68's 1968 eight-bit direct alphabet is then a genuine break in representation, not merely a wider tape with a parity bit.

See [history](de-transmissione-codicum-1963-1968.md), [source profile](../specifications/CVL-54-P0.md), [TP1](../specifications/CVL-63-TP1.md) and [RC1 direct encoding](../specifications/CVL-68-RC1.md).
