# Phase VII — Bifurcatio Machinarum: The 1968 Architecture Fork

> **DRAFT counterfactual research, 2026-11-12.** Machina XXXVI-R and Machina Nova are fictional architectural candidates, not real historical machines. Only memory layout experiments are implemented; there is **no Nova CPU, opcode set, or operating system**.

## Research question / 问题

The Machina XXXVI (fictional 1954, 36-bit word-addressed, CVL-54 six-bit shift pages) survives into an era of native CVL-68 eight-bit bilingual text. Should manufacturers preserve its legacy machine-code ABI, or introduce a new architecture built around directly addressable eight-bit characters?

Our chosen worldline (CANON) is that **CVL-68 wins as a major direct bilingual character standard**. This does **not** imply that a specific processor word length wins. The two computer families can coexist.

## Candidate A: Machina XXXVI-R0 — the legacy-compatible retrofit

- **CPU model:** keeps the Machina XXXVI/P0 36-bit word address space and existing instruction behavior; no byte-addressing instruction magically appears.
- **Adapter storage format:** place four CVL-68 bytes in the upper 32 bits of each 36-bit word, in stream order; four low bits **must be zero** in this R0 proposal.
- **Record metadata:** store the number of meaningful bytes *outside* the packed word sequence (so an actual zero byte is not confused with padding).
- **Text path:** software converts CVL-54 legacy records through their page-state machine; an output adapter can emit or accept CVL-68 data. This is an **extension proposal**, not a peripheral actually implemented by the original CPU emulator.
- **Failure costs:** 11 bytes occupy three 36-bit words = 108 raw memory bits rather than 88 payload bits. Without considering record-header overhead, 20 bits are unused (12 reserved nibbles + 8 trailing filler bits).
- **Access limitation:** the CPU loads a full 36-bit word. A character-specific read requires at least word selection, bit extraction, and controller/software logic. Even a direct byte adapter does not make the existing CPU byte-addressable.

Candidate full-memory text capacity: 32,768 × 4 = **131,072 bytes**, before reserving words for instructions, controllers, metadata and runtime. This is a theoretical upper bound, **not a real installed capacity or workload measurement**.

### R0 record rule

For each group of four bytes `b0 b1 b2 b3`, `W36 = (b0 << 28) | (b1 << 20) | (b2 << 12) | (b3 << 4)`.

Missing trailing bytes are filled with `00`; low four bits are `0000` and must be checked. A separate **logical byte count** tells a decoder how many original bytes to emit. This is not reversible from the words alone if trailing zeroes are valid data.

## Candidate B: Machina Nova-N0 — a clean byte-addressed generation

- **Address width:** 24-bit **byte** addresses (16 MiB architectural maximum, not installed RAM).
- **Installed memory for this experiment:** 256 KiB by default.
- **Word:** a candidate 32-bit general-purpose data word made of four bytes.
- **Byte operations:** direct load/store by byte address.
- **32-bit memory operations:** big-endian packing, 4-byte-aligned in N0. These conventions are **experimental**, not inevitable consequences of Latin or Greek.
- **Text:** CVL-68 core Latin and Greek codes are distinct and directly addressable; combining Greek diacritics may still occupy extra bytes and complicate grapheme indexing.
- **Compatibility strategy:** new software cannot execute existing XXXVI word instructions until a translator, emulator, or dedicated compatibility mode is defined. We currently provide none.

N0 is an **experimental memory interface**, not an instruction-set architecture or CPU emulator; the name `Machina Nova` does not denote a completed product.

## The same 11-byte greeting

The candidate CVL-68 encoding for `SALVE ΛΟΓΟΣ` is:

```text
52 41 4B 54 45 20 8A 8E 82 8E 91
```

R0 packs it in these **three 36-bit words**:

```text
0x52414B540
0x45208A8E0
0x828E91000
```

Their 12-digit octal equivalents, shown by `python -m machina_xxxvi.archlab`, are:

```text
244405132500 212202124340 405072210000
```

N0 can place the 11 bytes at address `0x100`, and directly read `0x8A` from byte address `0x106`, the Greek uppercase lambda (the seventh byte).

**The exact CVL-68 byte assignments remain DRAFT**; these examples test the memory arrangements independently of any finalized international character standard.

## Comparative matrix

| Dimension | XXXVI-R0 | Nova-N0 |
| --- | --- | --- |
| Native logical machine word | 36 bits | candidate 32 bits |
| Address unit | 36-bit word | 8-bit byte |
| Address field / range | 15 bits; 32K words | 24 bits; up to 16 MiB bytes |
| Eight-bit packing | 4 bytes + 4 spare bits per word | 4 bytes exactly per word |
| Direct character indexing | not native; requires shifts/masks or adapter | direct byte address for assigned code values |
| Previous P0 binary programs | intended to preserve CPU semantics | not executable without separate compatibility layer |
| CVL-54 source files | remain supported by old path | need transcoding |
| CVL-68 records | adapter/profile proposal | naturally stored as bytes |
| Polytonic Greek typography | external adapter/terminal still needed | direct bytes do not solve marks and glyph layout |

## An engineering consequence for the future

The winning **character** standard need not settle the competing **instruction sets**. This opens a plausible 1970s ecology: numerical research centers retain legacy 36-bit scientific applications, while newer public administration, business and communication systems adopt Nova byte-addressed machines. Institutions exchange *text* more easily than they exchange executable programs.

Thus the fictional industry's standards conflict shifts from **which alphabet can be stored?** to **which machine code can be executed?**

## Scope and validation

Committed prototype: `machina_xxxvi/archlab.py` and `tests/test_archlab.py`. The experiment checks packing, external logical lengths, reserved bits, arbitrary byte values, big-endian word reads, alignment and byte addressing. **Seven focused tests passed in a local lightweight lab** on 2026-11-12. This does not validate the full GitHub checkout or any CPU implementation. No CI result is claimed.

Run:

```sh
python -m machina_xxxvi.archlab
python -m unittest discover -s tests -p test_archlab.py -v
```

This phase's next decisions (not yet canon): Nova instruction format, software ABI, external conversion record format, historical standardization authority, and whether the XXXVI-R line gains native byte extraction instructions.

## Real-world analogies (not parts of fictional history)

- [IBM — System/360](https://www.ibm.com/history/system-360) (1964): standardized computer family and byte-oriented architectural decisions.
- [Columbia University — IBM 704](https://www1.columbia.edu/cu/computinghistory/704.html): period-specific 36-bit machine and packed six-bit text.
- [Computer History Museum — IBM 360](https://www.computerhistory.org/revolution/mainframe-computers/7/162): family design and software compatibility as technical and economic constraints.

The alternative machine model and specific 36/32/24-bit choices are **our proposals**, not historical conclusions.
