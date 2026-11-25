# Sextaria-S0 — A 48-bit Scientific Computer, Not Yet an ISA
## 48 位科学计算机：设计候选与硬件成本

> **Status: DRAFT / design study only, 2026-11-23.** Sextaria is a provisional coinage, not certified Classical Latin, not an attested machine, and **not** an implemented CPU. This profile does not overwrite or silently extend the 1954 XXXVI or 1968 Nova standards.

## 1. Why consider 48 bits?

A recurring record convention on 36-bit machines packs six six-bit symbols in one word. After CVL-68 establishes eight-bit Latin–Greek characters as a design direction, one natural but **non-inevitable** successor is 6 × 8 = 48 bits. This permits six CVL-68 code units in a single wide word.

The real-world [Burroughs B5000](https://www.cs.uaf.edu/2010/fall/cs441/proj1/b5000/) establishes that a 48-bit data word was not fantastical in the 1960s. Its actual character layout and architecture are **not** this design; historical plausibility is not a license to copy its ISA.

## 2. Three alternative address models

| Option | Memory abstraction | Advantage | Cost |
| --- | --- | --- | --- |
| W — **word-addressed** | address = 48-bit word | suits legacy scientific software mental model | text indexing requires extract/insert |
| B — **byte-addressed** | 8-bit byte address; aligned 6-byte word ops | direct CVL-68 character access | six-byte word alignment and address decomposition are awkward |
| H — **hybrid proposal** | word address + 0–5 byte-lane selector for text | honest about six-character record heritage | two kinds of pointers; ABI and compiler complexity |

**Suggested working candidate: H.** Word-valued scientific loads use 48-bit word addresses; character access requires a separate (word_index, lane_index 0..5) pair, or a precisely specified encoded byte pointer. The textual data is still eight-bit CVL-68. This is a **research preference**, not a committed ISA or a fictional historical fact.

## 3. Raw data layout and independent addressing

Physical word concept:

    MSB                                                LSB
    | 8-bit C0 | 8-bit C1 | 8-bit C2 | 8-bit C3 | 8-bit C4 | 8-bit C5 |
        47:40      39:32      31:24      23:16       15:8       7:0

For a byte sequence of length n, the bare number of 48-bit storage words is ceil(n/6); on 32-bit Nova it is ceil(n/4) **if deliberately packed into full 32-bit words**. In *byte-addressed* Nova memory the bytes themselves are individually addressable, and a length-n string uses exactly n data bytes before headers and alignment.

**Do not claim better raw textual density:** 48/6 = 32/4 = 8 bits per character; the 48-bit design merely changes grouping and potential burst access.

For equal counts of machine words, 48-bit data needs 1.5 × as many stored bits as 32-bit words. For equal byte capacity, 48- and 32-bit data architectures can have the same bare data-bit requirement. Silicon area, bus pins and real machine bill of materials cannot be determined from word width alone.

## 4. A realistic 1976 construction, rather than magic silicon

Early models could be **multi-board or bit-sliced** systems, using several smaller memory banks and ALU elements in parallel. A conceptual 48-bit word can be assembled from **three 16-bit lanes or six 8-bit lanes**, but extra logic is needed for carries, parity/error detection, address decoding and coordinated writes.

Possible costs:
- wider wiring, connectors and memory datapaths;
- awkward partial writes and byte-lane enabling;
- more complex physical memory organization than regular 32-bit designs;
- expensive low-volume peripherals and compiler toolchains;
- a risk of losing performance to memory bandwidth or control overhead despite wide arithmetic.

A wide accumulator alone does not guarantee faster matrix multiplication, more clock speed or better scientific results.

## 5. Numeric format: open research, no fake precision

A **candidate** 48-bit floating profile might devote more bits to a significand than the current XXXVI-F36 or Nova-F32 research encodings. One mathematically possible split is sign 1 + exponent 9 + fraction 38 = 48. That sum is only a **budget example**: the normalization convention, exponent bias, subnormals, rounding, error semantics, NaNs, and cross-format conversion rules are **not defined**.

The old F36 and new F32 prototypes are separate fictional formats with well-documented numerical differences. They must not be silently reinterpreted as Sextaria F48 words; that would fabricate binary compatibility.

## 6. Software migration

Proposed options:
1. **Source recompilation:** TRANFOR library source can acquire a third backend only after type sizes, I/O, record layout and floating semantics are defined.
2. **Archival gateway:** CVL-54 six-bit records and CVL-68 documents can be converted, with explicit warnings about unsupported characters and physical packing.
3. **Software emulation:** a later Sextaria installation might run XXXVI machine-code binaries in an interpreter; not assumed or delivered.
4. **Shared calling conventions:** future MODVLA modules could define portable symbols and data records, but executable object files remain architecture-specific.

Source compatibility ≠ numeric reproducibility ≠ byte-format compatibility ≠ binary execution.

## 7. Decisions intentionally deferred

- Hardware pointer layout for the hybrid word/lane address model.
- Register count, privilege modes, instruction format, interrupts and device selection.
- Fixed- or variable-length instructions; no reason to inherit the Nova 8+24 instruction template.
- A coherent F48 numeric and scientific exception model.
- Terminal typing and full polytonic Greek typography.
- The cost and market share necessary for Sextaria survival beyond 1985.

See [the 1973–1985 architecture war](../docs/de-bello-verborum-et-machinarum-1973-1985.md) and [existing XXXVI/Nova split](../docs/phase-vii-architecture-fork.md).

## 2026-11-25 Sextaria follow-up

[S1/R1](Sextaria-S1-R1.md) and [F48/R1](Sextaria-F48-R1.md) are subsequent paper candidates, not CANON or implementation. Earlier statements about undefined F48 describe the original study. Existing F32/F36 and RATIO-I accepted execution formats remain unchanged.
