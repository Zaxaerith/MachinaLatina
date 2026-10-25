# CVL-68 — Eight-Bit Native Latin–Greek Encoding

**Status: PRIMARY DIRECTION, MAPPING DRAFT · fictional**

CVL-68 is the planned mainstream eight-bit bilingual character set of Machina Latina's late-1960s computing world. The **decision to adopt direct 8-bit bilingual encoding is canon**; no complete mapping is canon yet.

## Capacity calculation

| Set | Code positions |
| --- | ---: |
| Classical Latin uppercase and lowercase: 23 × 2 | 46 |
| Greek uppercase and lowercase: 24 × 2 | 48 |
| Decimal digits | 10 |
| **Subtotal** | **104** |
| Remaining of 256 (for control, space, punctuation, variants and marks) | **152** |

This is a minimum estimate. Real Greek text also needs final sigma ς, accents/breathings and different historical orthographic practices; the alphabet alone does not specify the whole character repertoire.

## Proposed broad allocation (NON-NORMATIVE)

| Hexadecimal range | Count | Provisional role |
| --- | ---: | --- |
| 00–1F | 32 | Controls |
| 20–7F | 96 | Latin + digits + common punctuation + possible DEL |
| 80–97 | 24 | Greek uppercase |
| 98–9F | 8 | Reserved / controls / variants |
| A0–B7 | 24 | Greek lowercase |
| B8–FF | 72 | Accents, breathings, final sigma, math symbols, extension |

**Counts cover all 256 values.** A separate 0x7F delete value would live inside the Latin-compatible range, not constitute an extra slot.

The 0x20 separation between proposed Greek upper and lower blocks might simplify case conversion, but it is only a design convenience. No assumption about accent composition or Unicode compatibility follows.

## Character identity vs glyph appearance

Latin `A` and Greek `Α` must remain distinct code points even if a font makes them visually identical. An identifier policy should define warnings or restrictions for mixed-script confusables rather than silently merging characters.

## Unknowns before first implementation

1. Is the Latin section a direct successor of CVL-63 or a break in compatibility?
2. How do word spacing, DEL, line endings, and terminal control functions work?
3. Which ancient Greek diacritics are **combining marks** vs precomposed characters, and how does ordering/normalization work?
4. Does the system support proper lowercase final sigma handling?
5. What is the canonical byte-to-glyph mapping for all 256 positions?
6. Can a text file be round-tripped across CVL-54, CVL-63 and CVL-68 without loss?
7. How can non-Greek and non-Latin scripts be exchanged before a later universal standard?

## Supplementary draft profiles

- [Polytonic Greek Profile P1](CVL-68-polytonic.md) — combining marks, final sigma and comparison semantics.
- [CVL-54 to CVL-68 migration](CVL-54-to-68-migration.md) — stateful decoding and legacy data limitations.

## Current research artifact

A [full 256-position candidate ledger](CVL-68-byte-ledger.md) now exists, with 79 explicitly RESERVED positions, eight proposed combining diacritics and sample byte vectors. The inventory is **not yet normative**. In particular, CVL-68 is **not ASCII compatible** even where some punctuation and digits share numeric positions.

## First milestone

Review the candidate 256-position map, refine test vectors, and document rejected alternatives **before treating any profile as interoperable**. Do not claim ASCII compatibility: our hypothetical Latin region may differ from ASCII despite a superficially similar 0x20–0x7F allocation.