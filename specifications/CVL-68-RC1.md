# CVL-68/RC1 — Eight-Bit Latin–Greek Interchange
## 八位原生双文字标准：第一份可审阅的完整候选规范

> **REVIEW CANDIDATE / NOT CANON / NOT NORMATIVE** · editorial draft 2026-11-23, fictional origin 1968. The 1968 core and proposed early-1970s scholarly extension are distinct historical layers. The existing CVL-68 byte ledger is DRAFT; the fact that this proposal is complete does not ratify it. **No CPU emulator, codec, CI or historical hardware was modified.**

See the [full 256-entry RC1 byte ledger](CVL-68-RC1-ledger.md). This document supplies processing rules and compatibility contracts.

## 1. Core objectives

- Native direct Latin (23 uppercase + 23 lowercase) and Greek (24 uppercase + 24 lowercase), ten digits and common punctuation.
- One byte per basic letter, without CVL-54-style language-page shifts. Polytonic scholarly spelling may require one base byte and several post-base combining bytes.
- Stable distinct character identities for Latin A and Greek Α, even if they look alike in a font.
- Defined handling for unassigned bytes, controls, newlines, case conversion, malformed combining marks and legacy migration.
- Room for later historical extensions without inventing a fully international encoding in 1968.

**Capacity:** 46 Latin + 48 Greek + 10 digits = 104 essential characters even before punctuation, control codes, space and diacritics. The eight-bit choice is a plausible fictional engineering response, not proof that seven bits can never express two alphabets by other methods.

## 2. Complete allocation

| Range | Positions | Contents |
| --- | ---: | --- |
| 00–1F | 32 | Terminal and transmission controls |
| 20–40 | 33 | Space, decimal digits, punctuation including @ |
| 41–57 | 23 | Classical Latin uppercase: ABCDEFGHIKLMNOPQRSTVXYZ |
| 58–5A | 3 | RESERVED |
| 5B–60 | 6 | Brackets, slash, circumflex, underscore, backtick |
| 61–77 | 23 | Classical Latin lowercase |
| 78–7E | 7 | RESERVED |
| 7F | 1 | DEL control |
| 80–97 | 24 | Greek uppercase |
| 98–9A | 3 | Greek final sigma, ano teleia, Greek question mark |
| 9B–9F | 5 | RESERVED |
| A0–B7 | 24 | Greek lowercase |
| B8–BF | 8 | P1 combining Greek diacritics |
| C0–C2 | 3 | NEW P1 scholarly additions: breve, underdot, overline |
| C3–FF | 61 | RESERVED |

**Audit: 33 control + 136 separately printable glyph/space/punctuation slots + 11 combining + 76 RESERVED = 256/256.** A RESERVED code has no assigned identity and must not silently decode to an invented character. Leaving room unassigned is deliberate.

### Explicit scholarly extensions beyond Ledger A

| Byte | Meaning | Modern comparative transcription |
| --- | --- | --- |
| C0 | COMBINING BREVE | U+0306 |
| C1 | COMBINING DOT BELOW | U+0323 |
| C2 | COMBINING OVERLINE | U+0305 |

C0–C2 were RESERVED in Ledger A. They are proposals for an early-1970s scholarly profile, not a claim that every hypothetical 1968 terminal possessed their glyphs. Modern converters written for Ledger A may reject these bytes, so data using them needs an explicit profile identifier. The existing 256 entries outside these three positions remain unchanged.

Not assigned: separate coronis, archaic digamma/qoppa/sampi, every Greek editorial sign, all mathematical operators and the world's other scripts. RC1 is not full ancient Greek epigraphy or a Unicode competitor.

## 3. Exact compatibility vectors

| Text | CVL-68 hexadecimal bytes |
| --- | --- |
| Latin A | 41 |
| Greek Α | 80 |
| SALVE | 52 41 4B 54 45 |
| VERBVM | 54 45 51 42 54 4C |
| ΛΟΓΟΣ | 8A 8E 82 8E 91 |
| λόγος | AA AE B8 A2 AE 98 |
| ἄ | A0 BB B8 |
| ἆ | A0 BB BA |
| ἇ | A0 BC BA |
| ᾰ | A0 C0 |
| SALVE ΛΟΓΟΣ | 52 41 4B 54 45 20 8A 8E 82 8E 91 |

**SALVE is not ASCII-compatible:** under modern ASCII its CVL byte vector would be read as RAKTE. Modern Unicode values shown in the ledger are comparisons, not original fictional 1968 numbering.

## 4. Strict textual interchange profile RC1-L

A text record MUST declare its encoding/profile externally, or inherit an unambiguous record-layer declaration. A random binary stream MUST NOT be silently interpreted as RC1 text.

- Printable text uses assigned stand-alone graphic slots and valid P1 combining sequences. Latin and Greek alphabets require no shift.
- The only control bytes permitted **inside an RC1-L text record** are HT (09) and the consecutive pair CR LF (0D 0A). CR LF is the canonical line break for this interchange profile. In record-framed files, the external record boundary is independent and requires no CR LF.
- A lone CR or LF is malformed in RC1-L. Terminal-specific gateways may translate physical device line endings under a separately declared convention, never by guessing.
- The remaining C0 controls, including NUL (00), SO (0E), SI (0F), ESC (1B), and DEL (7F), are invalid in this strict in-band text profile. Their names are kept for independent terminal/control profiles; SO/SI do **not** switch Latin and Greek pages in CVL-68.
- Every RESERVED byte (58–5A, 78–7E, 9B–9F, C3–FF) is malformed in RC1-L. Do not emit a replacement glyph silently, reinterpret it as ASCII, or assign private characters by accident.
- Full-device printer control, file containers, binary payloads, checksums and error-recovery framing remain **outside** this text standard. File length is not inferred from NUL or DEL.

## 5. P1 Greek combining sequence grammar

The canonical representation uses base-first, zero-spacing marks. A strict cluster is one GREEK_BASE (80–97, 98, A0–B7) followed by up to one member of each category **in exactly this order**:

| Position after base | Allowed bytes | Rule |
| --- | --- | --- |
| BREATHING | BB smooth, BC rough | At most one; Greek vowels or rho only |
| QUANTITY_OR_DIAERESIS | BE diaeresis, BF macron, C0 breve | At most one; diaeresis only on iota/upsilon, macron or breve on vowels |
| ACCENT | B8 acute, B9 grave, BA perispomeni | At most one; vowels only; perispomeni only on alpha/eta/iota/upsilon/omega |
| IOTA_SUBSCRIPT | BD | At most one; only on alpha/eta/omega |
| EDITORIAL | C1 dot-below, C2 overline | At most one in strict profile; Greek letter bases only |

Diaeresis and a breathing may not appear on the same base under RC1-L; additional combinations require another approved scholarly profile. These rules intentionally specify a constrained interoperable grammar, **not complete philological spelling validation**. Capitals with iota subscript may display with adscript conventions; glyph placement is not a byte identity change.

A strict decoder rejects: leading unattached marks, marks after Latin/digits/punctuation, marks crossing line or record boundaries, duplicated categories, wrong category order, or prohibited base combinations. A presentation renderer MUST NOT treat each mark as a separate character cell. Caret movement and deletion should respect the base-plus-marks cluster.

## 6. Case and identity

- Latin basic uppercase A–Z *in the 23-letter sequence* and lowercase differ by hexadecimal 20; Greek basic uppercase/lowercase also differ by 20.
- Special final sigma is 98, medial sigma is B1, uppercase sigma is 91. These are distinct bytes. Case-insensitive comparison may group them semantically, **without modifying stored bytes**.
- Lowercasing uppercase Greek sigma needs word-boundary context to choose medial/final form. The exact word-segmentation algorithm is NOT finalized.
- Latin A (41) and Greek Alpha (80) remain distinct when indexing and comparing byte-exact text.
- Normalizing modern Unicode text is not automatically the same as canonical CVL mark ordering. Greek question mark and ano teleia have modern canonical-equivalence complications. A lossless Unicode gateway may require a source-byte sidecar or explicit escape metadata to reconstruct original CVL byte identity.

## 7. Historic migration and profiles

CVL-54 records consist of packed six-bit units under a LATINA/GRAECA shift-state machine. A correct 54→68 migration first unpacks physical words and statefully decodes the original characters; then, and only then, maps identities into RC1 bytes. PAD, redundant shifts, record framing and errors must be preserved separately for **bit-exact archival recovery**. Pure text transcoding cannot guarantee that recovery.

CVL-63 remains an unsettled seven-bit transmission design; no invented 63→68 byte-perfect converter is implied.

Proposed data labels:

| Label | Purpose |
| --- | --- |
| CVL-68/L-A | Earlier draft byte ledger; C0–FF unassigned |
| CVL-68/RC1-B | Base Latin/Greek punctuation/alphabet/code identities, no P1 assumptions |
| CVL-68/RC1-P1 | Base plus B8–C2 scholarly combining marks |
| CVL-68/RC1-L | Strict text record validity, controls and ordered marks |

These are proposed declaration labels, not actual wire-header bytes. **The 1968 date is fictional history; RC1 is a 2026 research revision.**

## 8. Alternatives considered, not silently copied

| Alternative | Reason not selected for primary profile |
| --- | --- |
| Real ASCII / ISO 8859-7 mapping | Our divergence starts with a 23-letter Latin order and a different historical standardization institution |
| Permanent six-bit shift pages | Shift-state loss complicates record damage recovery and arbitrary searching |
| Direct seven-bit all-characters | With terminal-style controls and useful punctuation/marks it is much less practical |
| Precomposed Greek vowel for every accent combination | Exhausts small byte repertoire quickly |
| Allocate all 256 positions to displayable glyphs | No extension room; unregistered meanings collide |
| Merge visually identical Latin and Greek glyphs | Breaks distinct character identities, scientific notation and source-code review |

## 9. Ratification blockers and references

**Completed as a written proposal:** complete accounting of 256 positions; no changing legacy assigned byte meanings; documented control and RESERVED rejection; post-base mark order; cross-encoding and record migration contracts.

**Still open before CANON:** philological review of polytonic corner cases; treatment of Greek punctuation during lossless Unicode conversion; exact CVL-54 tables and CVL-63 fate; whether C0–C2 should enter a later P1 profile; explicit sign-off in the decision log. No CI or software implementation is required merely because the proposal exists.

Real-world comparisons only: [Unicode Greek specification](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/), [Unicode Greek FAQ](https://www.unicode.org/faq/greek.html), [ISO 5428:1984 bibliographic Greek](https://www.iso.org/standard/11471.html), [ECMA-35:1971 shift techniques](https://www.ecma-international.org/wp-content/uploads/ECMA-35_1st_edition_december_1971.pdf).

Related: [full 256-row ledger](CVL-68-RC1-ledger.md), [original ledger](CVL-68-byte-ledger.md), [P1 profile](CVL-68-polytonic.md), [54→68 migration](CVL-54-to-68-migration.md).
