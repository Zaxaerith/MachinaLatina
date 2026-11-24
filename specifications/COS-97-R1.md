# COS-97/R1 — Codex Omnium Scripturarum
## 24 位全球字符身份与第一代交换格式候选

> **REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-24.** Fictional design window 1997–2005. This is a fully described candidate numbering and serialization framework, **not a complete world-character repertoire**, not a deployed codec, and not a CSM vote or approved international standard. The historical CVL-68/RC1 source ledger also remains a candidate.

## 1. Why 24 bits?

The proposed CSM registry uses unsigned 24-bit abstract identities (CID), independent of glyphs, encoding bytes, language, font, tokenization and sorting. There are 2^24 = 16,777,216 positions. Two CIDs fit in a proposed Sextaria 48-bit data word; a Nova-derived 32-bit processor can hold one CID in a register. Neither observation mandates a CPU ISA or memory ABI.

A 16-bit registry offers only 65,536 positions before exclusions; 32 bits make alignment convenient but are not required for a character namespace. We choose 24-bit as an editorial engineering compromise, **not a proof that all future textual entities fit**, nor a claim that 1997 hardware uniformly used 24-bit pointers.

## 2. Registry allocation and stability

All ranges are hexadecimal, inclusive. A numerical position is not an assigned character unless it has a published registry entry.

| CID range | Positions | R1 purpose |
| --- | ---: | --- |
| 000000 | 1 | permanently invalid sentinel |
| 000001–00FFFF | 65,535 | general registry, no automatic assignments |
| 010000–0100FF | 256 | frozen legacy-mapping window: 150 candidate IDs, 106 permanent holes |
| 010100–01FFFF | 65,280 | general registry |
| 020000–021FFF | 8,192 | compact international bank, two-byte wire representation |
| 022000–02FFFF | 57,344 | general registry |
| 030000–03FFFF | 65,536 | expanded international bank, three-byte wire representation |
| 040000–FFFFFE | 16,515,071 | general registry |
| FFFFFF | 1 | permanently invalid sentinel |

Total positions = 16,777,216. Excluding the two sentinels and 106 legacy holes leaves 16,777,108 potential character IDs, **not assigned characters**. There is no UTF-16 surrogate range, Unicode-derived code-point equality, or private-use promise. No ranges imply script ownership, collation order or cultural rank.

The 150 legacy IDs are derived from the preserved CVL-68/RC1 source ledger: all 136 graphic slots, all 11 combining marks, and HT/LF/CR (09/0A/0D). For each such source byte b, assign CID = 0x010000 + b. All other positions in the 256-slot legacy window are permanently unavailable in R1. This is an explicit compatibility mapping, not an assertion that old CVL bytes were already COS IDs.

The compact banks are **capacity reservations, not completed character allocations**. CSM would consult affected communities, publish proposal evidence, distinguish characters from glyph variants, and prioritize multiple scripts for short encodings by documented usage and implementation constraints. Early Latin/Greek users benefit disproportionately from the existing 150 direct positions. That is an explicit transitional compromise, not proof of cultural neutrality. No assigned stable CID may be moved to a shorter bank later merely to improve compression. A different future wire format may optimize byte lengths without renumbering IDs.

Each registry release must state its version and each entry's CID, stable name, status, script/usage properties, source evidence, relevant combining or equivalence rules, and changes from the prior release. Deprecated assigned IDs retain their historical meaning; do not silently recycle IDs. Full Unicode-like normalization, casefolding, segmentation and bidi algorithms are **not** delivered here.

## 3. C24 — fixed-width exchange/storage

Proposed label: COS-97/C24-R1. Each CID is serialized into exactly three octets, most significant first:

    b0 = (CID >> 16) & FF
    b1 = (CID >> 8) & FF
    b2 = CID & FF

For example, Latin A (CID 010041) is 01 00 41; Greek Α (CID 010080) is 01 00 80. No byte-order mark, implicit padding, termination byte or automatic endian guessing. Input length must be divisible by 3. The external record declares the profile and registry release. The permanent sentinels and legacy holes are invalid. An otherwise usable but unknown ID is structurally readable, not an accepted registered character.

C24 is useful for fixed-offset indexing and packed 48-bit scientific records, but a 32-bit aligned in-memory representation may be faster on Nova. Neither is prescribed as the universal memory layout.

## 4. W1 — CVL-compatible variable-width exchange

Proposed label: COS-97/W1-R1. At a known symbol boundary, read the first octet. These cases are exhaustive and mutually exclusive:

| First octet | Length | Decoded CID |
| --- | ---: | --- |
| one of the 150 mapped legacy bytes | 1 | 010000 + byte |
| D0–EF | 2 | 020000 + ((first − D0) × 256) + second |
| F0 | 3 | 030000 + (second × 256) + third |
| F1 | 4 | second × 65536 + third × 256 + fourth |
| all other byte values | invalid at boundary | reject |

Payload octets may be **any** 00–FF. Their values do not start new symbols while the decoder is consuming a known prefix. Byte order within the payload is high first. The canonical encoding is exactly the shortest designated form above. F1 MUST NOT encode a legacy mapped identity, a legacy hole, a sentinel or an ID in either shorter bank. No alternate escape, overlong form, page-shift state or BOM is allowed.

An encoder emits 1 byte for a mapped legacy ID; 2 for 020000–021FFF; 3 for 030000–03FFFF; 4 for other permitted IDs. An unknown/unassigned ID is not publishable as registered text, even if the numeric syntax is valid. A preservation tool MAY retain the original unassigned ID with an explicit diagnostic; it must not silently assign it a character.

A decoder distinguishes malformed (bad boundary byte, truncated sequence, noncanonical F1, invalid ID) from unsupported registry version/unknown ID. Strict interchange rejects both before presenting a validated text record. It may report byte offset and original payload for recovery. A font missing a known character is a separate display limitation, not malformed encoding.

**Important tradeoff:** W1 is prefix-decodable at a known boundary but is **not self-synchronizing**. For example D0 41 represents one bank ID, not D0 followed by Latin A. A dropped byte or a seek into arbitrary payload may create plausible but incorrect text. Parse from the record start or a verified boundary/index; use independent record length, integrity check and transport recovery. Searching raw bytes for delimiters, C-style NUL termination, or ASCII/CVL-oriented markup parsing is unsafe. NODVS framing and network integrity algorithms remain separate specifications. A malformed record must not be repaired by scanning for an apparently printable byte.

## 5. Character-level examples (all numbers hexadecimal)

The nonlegacy entries below are **sandbox assignment fixtures only**, not claims that the 1997 fictional CSM actually approved those characters. They demonstrate how every representation works without importing Unicode numeric values.

| Text or fixture | CID | C24 bytes | W1 bytes |
| --- | --- | --- | --- |
| Latin A | 010041 | 01 00 41 | 41 |
| Greek Α | 010080 | 01 00 80 | 80 |
| Greek final ς | 010098 | 01 00 98 | 98 |
| Greek acute mark | 0100B8 | 01 00 B8 | B8 |
| 中 (trial) | 020000 | 02 00 00 | D0 00 |
| 文 (trial) | 020001 | 02 00 01 | D0 01 |
| ا (trial) | 020002 | 02 00 02 | D0 02 |
| क (trial) | 020003 | 02 00 03 | D0 03 |
| second-bank boundary fixture | 021FFF | 02 1F FF | EF FF |
| 人 (trial) | 030000 | 03 00 00 | F0 00 00 |
| third-bank boundary fixture | 03FFFF | 03 FF FF | F0 FF FF |
| historical-letter fixture (digamma ϝ) | 040001 | 04 00 01 | F1 04 00 01 |

The trial assignment of 人 to the three-byte bank merely exercises that branch, not a recommendation that a common Han character be costly. Actual compact-bank placement requires corpus and community review. Boundary fixtures are numeric examples only. The largest usable numerical position FFFFFE serializes as F1 FF FF FE; it is not an assigned character.

## 6. Migration and text semantics

A source file declared CVL-68/RC1-L must first pass the existing strict control and combining-mark grammar, including CR LF pairing and permitted Greek base/mark order. Source labels distinguish older Ledger A and RC1 P1 extensions. Then map each validated byte using section 2. The resulting CID sequence preserves the original byte identity and order, including distinct Greek punctuation and sigma forms. Serializing it as W1 produces **the same byte sequence**, while C24 expands each source byte to three octets. This is a limited, explicit subset compatibility theorem, not unrestricted CVL binary compatibility.

A W1 file might contain formerly reserved CVL bytes D0–EF/F0/F1 as valid leading octets; it must NOT be auto-detected as CVL or vice versa. Unknown old private extensions require their own source mapping. Do not retroactively apply P1 Greek grammar to all world scripts. W1/C24 define only sequence encoding; additional COS text/normalization profiles, including control and line-break policy, are separate. No normalization is performed by these codecs. Reversing an unnormalized migrated identity sequence is exact only when every CID has a valid inverse and the requested legacy profile accepts the resulting sequence. An archive should retain original bytes and source metadata independently.

CVL-54/63 must still be unpacked, parity-checked where applicable, and interpreted under their declared page state before mapping to these identities. SHIFT/PAD, physical framing and invalid old data are not characters. Pure text conversion cannot recover bit-identical tape structure.

## 7. Costs and alternatives

C24 costs three octets per CID, W1 costs one through four. W1 is compact for the existing Latin/Greek ecosystem and a limited international bank, not equally compact across all languages. Four-byte general IDs are more expensive than C24 for those characters. A general document's actual cost is the sum of the chosen lengths over its identity sequence, not a universal compression claim.

Real UTF-8 uses self-synchronizing byte classes and ASCII compatibility (RFC 3629, 2003). W1 deliberately gives up those properties to preserve this world's direct eight-bit bilingual text; record-oriented software has a plausible reason to accept the tradeoff. A separate self-synchronizing universal stream could compete later. The proposal does not copy actual UTF-8/Unicode numerical identities.

## 8. Ratification boundaries

Written: namespace, complete allocation classes, full legacy mapping rule, fixed-width C24 and canonical W1 framing at symbol boundaries, malformed input policy, example vectors.

Open: actual global character assignments beyond the legacy proposal, language-specific normalization and bidirectional layout, compact-bank criteria and representation, external record header/version encoding, domain-label algorithm, independent synchronization/recovery protocol, historical institutional approval and implementation. **No program, emulator, CI or CANON ratification is supplied.**

HIST comparisons: [Unicode encoding model](https://www.unicode.org/reports/tr17/), [Unicode publication history](https://www.unicode.org/history/publicationdates.html), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629).

Related: [full legacy mapping](COS-97-CVL-mapping.md), [worked vectors and history](../docs/cos-97-interchange-1997-2005.md), [CSM charter](CSM-charter-DRAFT.md).
