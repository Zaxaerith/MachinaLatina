# Phase VIII — Two Executable Machine Languages / 双机器可执行验证

**DRAFT alternate-history research.** Modern implementation dated 2026-11-12. The 1954 Machina XXXVI and 1968 Machina Nova are fictional. CPU emulator behavior does not imply actual historical hardware existed.

## Result

The project now has **two independent CPU reference implementations**, each running a distinct native program that displays the same Latin–Greek phrase.

| | Machina XXXVI/P0 | Machina Nova-N1 |
| --- | --- | --- |
| Fictional date | 1954 | 1968 |
| Machine code | 36-bit word instructions | 32-bit fixed instructions |
| PC addressing | 15-bit **word addresses** | 24-bit **byte addresses** |
| Text | CVL-54/P0 six-bit shift pages | CVL-68 candidate direct bytes |
| EMIT | six symbols per operation | one byte per operation |
| Greeting program | two EMIT + FIN | eleven EMIT + FIN |
| Example instruction | octal 001000000100 | hex 50 00 01 00 |
| Visible result | SALVE ΛΟΓΟΣ | SALVE ΛΟΓΟΣ |
| Binary compatibility | No | No |

Nova-N1 builds upon the [Nova-N0 memory experiment](../specifications/Machina-Nova-N0.md), adopting a fixed 32-bit opcode word with an eight-bit opcode and 24-bit address/immediate. It is **not** a binary translation of the original 36-bit XXXVI instruction format.

## Why this matters to the fictional technology history

By the late 1960s, scientists and ministries can agree on the textual meaning of Latin and Greek records without agreeing on instruction sets or integer widths. XXXVI programs and Nova programs can exchange correctly decoded text, but one cannot run the other's executable words. This leads naturally to legacy machine virtualization, portable languages, linkers and compiler backends in the imagined 1970s.

An intentionally inefficient Nova-N1 greeting requires **48 instruction bytes for 11 text bytes**. The original XXXVI program requires three 36-bit instruction words to output two six-symbol data words. These measurements are *storage counts*, not CPU performance claims. A future Nova may add buffered output, a data pointer or compact instructions; the current model does not invent them prematurely.

## Commands

From the repository root, with Python 3.10+ and no third-party modules:

    python -m machina_nova demo
    python -m machina_nova run examples/nova_salve_logos.nvi
    python -m machina_nova compare
    python -m unittest discover -s tests -p test_nova_n1.py -v

Expected comparison:

    XXXVI/P0 CVL-54: SALVE ΛΟΓΟΣ
    Nova-N1 CVL-68: SALVE ΛΟΓΟΣ
    TEXT MATCH / BINARY INCOMPATIBLE

The .nvi file is a modern sparse hexadecimal memory image rather than an asserted 1968 ROM or punched-card format. The byte values for CVL-68 are still a **draft**. The output port carries raw bytes; a host-side candidate decoder supplies glyphs.

## Implemented in Phase VIII

- Twelve candidate Nova-N1 instructions: FIN, LEGB, LEGW, PONB, PONW, ADDE, SVBT, SALTA, SI0, NVM, ADI and EMIT.
- 24-bit byte PC, 32-bit accumulator, four-byte-aligned instruction fetch, unsigned modular arithmetic and big-endian word access.
- Sparse hexadecimal program loader and runnable image.
- Explicit traps for reserved instructions, invalid FIN fields, unaligned/out-of-RAM memory access and step-limit exhaustion.
- Modern compare command that executes native programs on the old and new CPU models independently.

Not implemented: Nova assembler, operating system, floating point, interrupts, historical peripheral protocol, transparent compatibility mode, complete polytonic Greek or an officially fixed CVL-68 specification.

## Test provenance

The 12 dedicated Phase VIII tests passed locally on 2026-11-12, alongside successful demo, image-run and compare commands. The local environment reconstructed legacy XXXVI and the CVL-68 gateway from their GitHub source text because a direct container clone failed at DNS resolution. Thus the recorded validation is **local reconstructed-source verification**, not a claim that GitHub Actions or a clean GitHub checkout ran green.

## Next phase: the 1970s compiler question

Should a higher-level scientific language (provisionally TRANFOR) have two fully independent backends? How would it specify signed 36-bit versus 32-bit arithmetic, six-character legacy identifiers, Greek variables, memory-address types, mixed-script string encoding and portable I/O? A plausible next milestone is one tiny well-specified source program compiled to both existing ISAs, not a full OS.

Related: [Nova-N1 ISA](../specifications/Machina-Nova-N1.md), [Phase VII fork](phase-vii-architecture-fork.md), [encoding war](encoding-war-1963-1968.md).
