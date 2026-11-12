# Machina Nova-N0 — Byte-Addressed Memory Research Profile

**Status: DRAFT; memory subsystem only, NOT an ISA or full CPU.**

We are testing one plausible late-1960s alternative to the existing 36-bit Machina XXXVI family.

| Field | N0 design choice |
| --- | --- |
| Data address | 24-bit, **byte-addressed**, 0x000000–0xFFFFFF |
| Architectural address space | 16 MiB (does not imply 16 MiB installed memory) |
| Default RAM in present-day test program | 256 KiB |
| Candidate data word | 32 bits, four 8-bit bytes |
| Byte access | 8-bit read/write at any installed byte address |
| Word access | 32-bit unsigned, big-endian |
| Alignment | 4-byte aligned word reads/writes required by N0 |
| Native text | CVL-68 candidate byte stream; no page-shift required for base alphabets |

**Explicitly not specified:** program counter, processor registers, opcode format, execution semantics, operating system, interrupts, cache, privilege, linkage or binary compatibility with XXXVI.

### Example of byte access

With `52 41 4B 54` at byte address `0x100`:

- `READ_BYTE(0x101)` returns `0x41`.
- `READ_WORD32(0x100)` returns `0x52414B54`.
- `READ_WORD32(0x101)` is rejected as unaligned in this specific draft.
- Storing candidate `SALVE ΛΟΓΟΣ` at `0x100` makes its Greek lambda code `0x8A` directly available at `0x106`.

A code byte is not automatically a complete grapheme: polytonic Greek accents and breathing marks may follow a base letter as extra bytes.

### Portability and migration

Copying CVL-68 bytes from the R0 adapter to Nova-N0 is a **data conversion** operation. Copying 36-bit XXXVI machine instructions would not produce executable Nova instructions; an emulator or binary translator would be a separate, future system.

The N0 memory model is implemented for experiments in `machina_xxxvi.archlab.NovaMemory` (a modern Python prototype). No time-per-instruction or comparative performance claims are made.

See [Phase VII comparison](../docs/phase-vii-architecture-fork.md).
