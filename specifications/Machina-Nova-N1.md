# Machina Nova-N1 — First Byte-Addressed ISA (fictional 1968)

**Status: DRAFT, experimental executable profile — not a real historical computer or a standardized ABI.** N1 extends the Nova-N0 memory proposal and is intentionally incompatible with the earlier 36-bit XXXVI ISA.

## Architecture

| Item | Nova-N1 |
| --- | --- |
| Address | Unsigned 24-bit **byte** address, 16 MiB architecture limit |
| RAM | 256 KiB default in emulator |
| Word | 32-bit big-endian, aligned on four-byte boundaries |
| Instruction | Four bytes: **8-bit opcode + 24-bit operand**, big-endian |
| Registers | 32-bit unsigned accumulator A; 24-bit byte-addressed PC |
| Z flag | Derived from A == 0 |
| Output | Raw CVL-68 candidate 8-bit bytes (not UTF-8) |

On reset A and PC are zero; the Python test harness zero-initializes RAM. Fetch requires PC divisible by four and within installed RAM. Normal PC increments by four modulo 2^24. Taken branches replace PC. Integer arithmetic wraps modulo 2^32. Invalid instructions or accesses raise faults.

## Twelve candidate operations

| Opcode (hex) | Mnemonic | Operand | Behavior |
| --- | --- | --- | --- |
| 00 | FIN | exactly zero | halt |
| 10 | LEGB | byte address | A = zero-extended byte |
| 11 | LEGW | aligned address | A = 32-bit word |
| 12 | PONB | byte address | store low byte of A |
| 13 | PONW | aligned address | store A as 32-bit big-endian word |
| 20 | ADDE | aligned address | A = A + word modulo 2^32 |
| 21 | SVBT | aligned address | A = A - word modulo 2^32 |
| 30 | SALTA | aligned instruction address | jump |
| 31 | SI0 | aligned instruction address | jump if A = 0 |
| 40 | NVM | 24-bit immediate | load immediate into A |
| 41 | ADI | 24-bit immediate | add immediate modulo 2^32 |
| 50 | EMIT | byte address | send one raw byte to terminal |

The original N1 profile reserved the other 244 opcodes; Phase X additionally assigns 0x60–0x63 in its experimental floating extension (see below). FIN requires a zero operand. The SI0 operand is checked only when its branch is actually taken. Latin mnemonics are fictional technical coinages; this is an accumulator ISA, not a transplanted IBM or PDP-10 instruction set.

## First native bilingual program

The CVL-68 candidate bytes representing SALVE ΛΟΓΟΣ are:

    52 41 4B 54 45 20 8A 8E 82 8E 91

The sample image stores text beginning at byte address 000100 (hex). Eleven EMIT instructions output consecutive byte addresses, followed by FIN, for 48 code bytes in all.

    000000: 50 00 01 00   ; EMIT 000100
    000004: 50 00 01 01   ; EMIT 000101
    000018: 50 00 01 06   ; Greek Lambda byte = 8A
    00002C: 00 00 00 00   ; FIN

An EMIT opcode outputs an uninterpreted eight-bit byte. A modern CVL-68 draft decoder produces the visible text. Latin A (41 hex) and Greek Α (80 hex) have different identities.

## Experiment / commands

    python -m machina_nova demo
    python -m machina_nova run examples/nova_salve_logos.nvi
    python -m machina_nova compare
    python -m unittest discover -s tests -p test_nova_n1.py -v

The .nvi format is a **modern sparse hex-byte memory listing**, not a vintage binary/ROM standard. One line is a six-digit hexadecimal address, a colon and hexadecimal byte pairs; comments use semicolons. The reference loader rejects overlap, invalid hex and out-of-range data.

## Phase X floating extension

Four more opcodes are now specified for research: `60 FLEG` (load a validated F32 word), `61 FADD`, `62 FSVB`, and `63 FPON` (validate and store). They operate on the existing accumulator, use aligned four-byte words and perform the exact [Nova-F32](FLOAT-P0.md) round-to-nearest ties-to-even finite semantics. The original twelve N1 opcodes remain unchanged. This extension is not IEEE 754. Phase XI further adds `64 FMVL` and `65 FDIV` (hexadecimal) for finite multiply/divide with exact-rational operation and one F32 rounding, and traps division by zero. See [Phase XI](../docs/phase-xi-vectors.md). See [Phase X report](../docs/phase-x-floating.md).

## Phase XIII extension: native byte-record input

The new experimental opcode `66 CAPTA` (hexadecimal) transfers **one eight-bit value** from a host-mounted CVL-68/P0 record to the addressed memory byte and advances the record cursor. A missing/exhausted record or invalid destination traps without advancing PC or cursor or updating memory. This complements `50 EMIT` and does not give the CPU a full filesystem, terminal driver, interrupt system or EOF status register. See [Ordo P1](ORDO-P1-DEVICE.md).

## What is still missing

N1 has no assembler, signed integer arithmetic, floating multiply/divide, interrupts, DMA, protection, real terminal timing, file system or system-call ABI. CVL-68 is not frozen and does not define complete Unicode-equivalent polytonic Greek text. Textual output equivalence with XXXVI does not imply executable compatibility or equal efficiency: this deliberately naive Nova greeting uses 48 code bytes to emit 11 text bytes.

More context: [Phase VIII](../docs/phase-viii-nova-n1.md), [Nova-N0](Machina-Nova-N0.md), [Phase VII](../docs/phase-vii-architecture-fork.md).
