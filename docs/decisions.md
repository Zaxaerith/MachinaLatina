# Architectural Decisions / 设计决策记录

This file is the project's lightweight decision log. It is not a final standard.

## D001 — Greco-Roman dual-script foundation
**State:** CANON (2026-10-25)

Latin is the common language of administrative and system engineering; Greek retains a prominent academic/scientific role. **Both writing systems** matter to computing from the outset. Neither script is merely a bitmap font added decades later.

**Rationale:** An institutional bilingual tradition creates a credible scientific demand for native Greek text.

**Limits:** This is fictional. Do not claim universal ancient Roman attitudes toward Greece.

## D002 — Latin orthographic core
**State:** CANON (2026-10-25)

Use a 23-letter Classical Latin base: `A B C D E F G H I K L M N O P Q R S T V X Y Z`. No separate J, U or W in the *core Latin alphabet*.

**Not implied:** Lack of lower case, modern punctuation, mathematical notation, other scripts or technical loanwords.

## D003 — 8-bit bilingual successor
**State:** CANON as design **direction**; mappings are DRAFT

Favor a direct, non-shifting 8-bit Latin–Greek character standard (CVL-68) in the late 1960s. Include both cases of the basic 23 Latin letters and 24 Greek letters, plus digits, common punctuation and controls.

**Constraint:** 46 Latin + 48 Greek + 10 digits = **104 positions before punctuation, spaces or controls**. A 7-bit code with a 33-position ASCII-like control budget cannot fit them directly.

**Migration:** Six-bit shift-page predecessors may exist; they are not the preferred long-term norm.

## D004 — Engineering before aesthetics
**State:** CANON

Prefer historically defensible compromises over conveniently modern design. Document unused codes, shifting state, copyable bit patterns, binary compatibility and conversion failures before inventing languages built on top of them.

## D005 — CVL-68 draft layout
**State:** DRAFT, intentionally not frozen

Reserve 0x00–0x1F for controls; consider retaining 0x20–0x7F as a hypothetical Latin/terminal-compatible region. Place Greek uppercase at 0x80–0x97, Greek lowercase at 0xA0–0xB7, leaving room for Greek variants and combining signs. The diagram is a **proposal**; not approved for implementation or long-term compatibility guarantees.

**Technical question:** Does the earlier Latin region put letters in continuous Classical Latin alphabetical order, and where are the freed J/U/W locations assigned?

## D013 — Licensing of original repository material
**State:** CANON (2026-10-25)

Original documentation and editorial encoding tables are offered under **CC BY 4.0**; source code and code examples under **MIT**. This does not relicense third-party source materials. See root LICENSE and LICENSE-CODE.

## D014 — Machina XXXVI experimental word-addressed ISA
**State:** DRAFT / P0 research proposal (2026-10-26)

A hypothetical 1954 scientific machine uses 36-bit words, 15-bit word addresses, a 12-bit opcode field, three index registers and six-bit CVL-54/P0 text with terminal-maintained LATINA/GRAECA shift state. Ten opcode semantics, bit encodings, and octal examples are proposed, but no emulator, floating-point format, tape protocol or hardware existence is claimed. See [ISA](../specifications/Machina-XXXVI.md) and [worked examples](machina-xxxvi-programs.md).

## D015 — The 1968 architecture fork
**State:** DRAFT (2026-11-12)

Two experimental families are proposed: [XXXVI-R0](../specifications/Machina-XXXVI-R0.md) retains word-addressed 36-bit execution, with CVL-68 byte records packed four per word plus four reserved bits; [Nova-N0](../specifications/Machina-Nova-N0.md) explores 24-bit byte addresses, candidate 32-bit words and big-endian memory. **Neither a Nova ISA nor native byte access in the XXXVI CPU has been canonized.** See [comparison](phase-vii-architecture-fork.md).

## D016 — Experimental Nova-N1 execution model
**State:** DRAFT / executable research profile (2026-11-12)

[Machina Nova-N1](../specifications/Machina-Nova-N1.md) proposes an independent **32-bit fixed-instruction ISA** using an 8-bit opcode and 24-bit unsigned byte-address operand, a 32-bit accumulator, twelve initial operations and native CVL-68 candidate byte output. The reference emulator and its own sparse memory-image format are working experiments, **not a canonized machine-code standard** or a binary-compatible extension of XXXVI. See [Phase VIII results](phase-viii-nova-n1.md).

## D017 — Portable TRANFOR/P0 NAT15 contract
**State:** DRAFT / executable research (2026-11-12)

[TRANFOR/P0](../specifications/TRANFOR-P0.md) specifies a single-assignment language with strictly range-checked unsigned **NAT15** numbers, a shared text repertoire and explicit compiler targets for XXXVI/P0 36-bit words and Nova-N1 32-bit instructions. Source portability does **not** mean binary compatibility, matching memory addresses or full ancient Greek orthography. No formal historical source-language standard is claimed. See [Phase IX report](phase-ix-tranfor.md).

## D018 — Distinct floating-point families and source-level numeric portability
**State:** DRAFT / executable research (2026-11-12)

Two experimental finite binary formats, [XXXVI-F36 and Nova-F32](../specifications/FLOAT-P0.md), use sign/exponent/explicit-normalized-fraction fields with different precision and exponent ranges. Both use exact rational evaluation followed by per-operation round-to-nearest ties-to-even, with invalid exponents and out-of-range results trapped. The [TRANFOR/P1](../specifications/TRANFOR-P1.md) extension keeps NAT15 integers, adds explicitly typed REALIS and deliberately **does not demand identical rounded floating values** on incompatible machines. IEEE 754 is not retroactively inserted into the fictional 1950s or 1960s.

## D019 — Dot-product reproducibility is an algorithmic property
**State:** DRAFT / executable research (2026-11-12)

[TRANFOR/P2](../specifications/TRANFOR-P2.md) adds bounded 1–8-element REALIS vectors and ordered dot products. [Phase XI](phase-xi-vectors.md) specifies **left-to-right multiply, round, add, round** semantics; F36/F32 can produce different yet valid answers. The dual compiler lowers each step to existing CPU instructions plus new FMVL/FDIV instructions, retaining native word/byte addressing differences. This is neither SIMD nor a stable matrix library or historical fact.

## D020 — Shared host-side batch job protocol, not a guest OS
**State:** DRAFT / laboratory research (2026-11-13)

[Ordo Operum/P0](../specifications/ORDO-P0.md) defines a bilingual-world **common job-control deck** that selects the existing XXXVI or Nova native emulator, with either TRANFOR/P2 compilation or a native machine image. Successful output becomes one independently length-framed CVL-68/P0 record in a named `OMR1` sequential spool; faults do not stop later jobs. This is a modern *host program* and **does not implement a guest kernel, guest file system, magnetic tape controller or privilege isolation**. See [Phase XII](phase-xii-batch.md).

## Open decisions

- [ ] D006: fixed table for CVL-54 and exact shift/reset behavior
- [ ] D007: whether CVL-63 genuinely deserves an independent standard
- [x] D008 exploration: inventory all 256 positions, including RESERVED entries in [draft ledger](../specifications/CVL-68-byte-ledger.md)
- [ ] D008 finalization: assign or deliberately reserve slots and establish normative semantics
- [ ] D009: accent marks, breathings, Greek final sigma and normalization
- [ ] D010: identifier security for Latin/Greek homoglyphs
- [ ] D011: byte order and packed text compatibility; *not* dictated by language
- [ ] D012: governance of post-1968 universal character encoding
- [x] D013: documentation CC BY 4.0 / code MIT