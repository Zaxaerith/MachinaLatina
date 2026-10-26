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