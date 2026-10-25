# CVL-68 — Polytonic Greek Profile P1

> **Status: DRAFT PROFILE, not normative · fictional computing system**  
> This document supplements [CVL-68](CVL-68.md) and its [256-position candidate ledger](CVL-68-byte-ledger.md). It does **not** claim complete ancient Greek orthographic coverage.

## Problem / 问题

Twenty-four Greek alphabetic letters are **not** a complete encoding of written Greek. Ancient and scholarly spelling may require acute, grave, circumflex/perispomeni, smooth and rough breathing marks, diaeresis, vowel quantity marks, iota subscript and special letterforms such as final sigma.

Allocating one eight-bit value for every possible precomposed glyph would quickly waste scarce slots and would make expansion difficult. **P1 therefore explores post-base combining signs:** a base letter is followed by 0 or more mark bytes.

This design resembles modern decomposed writing but is a **fictional proposal, not a claim that Unicode existed in 1968**.

## Candidate bytes from the current ledger

| Hex | Proposed CVL meaning | Unicode comparison only |
| --- | --- | --- |
| `98` | final sigma `ς` | U+03C2 |
| `B8` | combining acute (oxia) | U+0301 |
| `B9` | combining grave (varia) | U+0300 |
| `BA` | combining perispomeni | U+0342 |
| `BB` | combining smooth breathing (psili) | U+0313 |
| `BC` | combining rough breathing (dasia) | U+0314 |
| `BD` | combining iota subscript (ypogegrammeni) | U+0345 |
| `BE` | combining diaeresis | U+0308 |
| `BF` | combining macron | U+0304 |

These are **eight combining byte values** plus a separate final-sigma glyph. Additional signs (such as breve and coronis) are not yet included.

## Proposed canonical storage sequence — P1 candidate

`GREEK_BASE [BREATHING] [QUANTITY_OR_DIAERESIS] [ACCENT] [IOTA_SUBSCRIPT]`

- `GREEK_BASE`: a Greek upper/lowercase letter, or dedicated final sigma if syntactically appropriate.
- `BREATHING`: at most one of `BB` or `BC`.
- `QUANTITY_OR_DIAERESIS`: at most one of `BE` or `BF`.
- `ACCENT`: at most one of `B8`, `B9`, `BA`.
- `IOTA_SUBSCRIPT`: optional final `BD`.

**This ordering is a proposed CVL-68 canonical byte policy, not a statement about Unicode canonical combining classes.** Some combinations may be linguistically invalid even if the byte grammar allows them. A later orthographic profile must specify legal marks per base character and typography of capitals. Re-encoding another external normalization form must explicitly translate it; simply renaming Unicode forms as “CVL normalization” would be incorrect.

### Examples / 编码例子

| Greek text | CVL-68 candidate bytes | Notes |
| --- | --- | --- |
| `Α` | `80` | Greek uppercase alpha, distinct from Latin `A` = `41` |
| `α` | `A0` | Greek lowercase alpha |
| `ά` | `A0 B8` | alpha followed by acute |
| `ἄ` | `A0 BB B8` | alpha + smooth breathing + acute |
| `ἇ` | `A0 BB BA` | alpha + smooth breathing + perispomeni |
| `λόγος` | `AA AE B8 A2 AE 98` | lambda, accented omicron, gamma, omicron, final sigma |
| `Σ` | `91` | uppercase sigma |
| `σ` | `B1` | medial lowercase sigma |
| `ς` | `98` | lowercase final sigma |

**Important:** A decomposed sequence counts as *multiple encoded bytes*, even if rendered as one grapheme. Byte count ≠ number of letters ≠ cursor positions.

## Comparison and text processing / 字符串的三种比较

1. **Raw byte equality:** exact byte sequence match. Suitable for archives and hashes, *not sufficient* for general language search.
2. **P1-canonical equality:** apply the fictional P1 mark-ordering and validity policy, then compare. Currently a DRAFT until all legal combinations and ordering rules are fixed.
3. **Language-aware comparison:** case-folding, final sigma handling, optional accent-insensitive search, and cross-script security rules. Not equivalent to either (1) or (2).

Case-folding can map `Σ`, `σ`, `ς` into a shared comparison class while keeping their stored bytes distinct. Mapping every capital sigma mechanically to final sigma would be incorrect: the word boundary and punctuation context matter.

Never silently merge Latin `A` with Greek `Α`. They are visually confusable but belong to different alphabets.

## Printing constraints / 终端技术

A period-appropriate printer might implement combining marks by overstriking or dedicated type elements; a line editor must consider whether an accent advances the printing position. **P1 proposes that combining bytes do not advance the logical character cell**, but a first-generation hardware printer may support only a restricted subset, and two-dimensional stacking may require additional device-specific mechanics.

This is a proposed printer/interface contract, **not a guarantee of what 1960s hardware could uniformly render**.

## Open questions / 待定

- Does the standard require a diaeresis + accent sequence, and which relative order?
- Should breve (`U+0306`) and coronis (`U+0343`) receive new values in reserved slots?
- Which mark sequences are legal after consonants (e.g. rho breathing)?
- Do uppercase iota subscript and adscript need separate typographic behavior?
- Do `0x98–0x9F` and `0xB8–0xBF` remain at these positions after review?
- How to implement a converter to/from a modern Unicode representation **without pretending it is the original standard**?

## Real-world technical analogies

- [Unicode Greek FAQ](https://www.unicode.org/faq/greek.html), including combining character order and Greek final sigma.
- [Unicode Normalization FAQ](https://www.unicode.org/faq/normalization.html), covering canonical order/equivalence in our world.
- [SIL Gentium Greek encoding notes](https://software.sil.org/gentium/greek/), for challenges of multi-mark Greek typography.

The Unicode references are modern **analysis tools**. The hypothetical CVL-68 designers would have had their own terminology and methods.
