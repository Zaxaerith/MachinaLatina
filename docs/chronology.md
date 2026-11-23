# Speculative Chronology / 架空技术发展史

This is a **fictional timeline**, not a chronology of actual inventions. Years are narrative anchors, chosen to reflect realistic constraints, not claims that alternate-world products definitely existed.

| Year | Status | Event | Engineering consequence |
| --- | --- | --- | --- |
| 1954 | DRAFT | **CVL-54** six-bit Latin/Greek shift pages and experimental **Machina XXXVI/P0** | Six six-bit codes fit one 36-bit word; 15-bit word addresses and printer page state; [architecture](../specifications/Machina-XXXVI.md) |
| 1957 | DRAFT | **TRANFOR** scientific formula language is adopted by research centers | Six-character identifiers and Greek mathematical labels emerge as design questions |
| 1963 | DRAFT | **CVL-63** seven-bit communication code developed for terminals | Retains shift-state costs; needs a documented transition from CVL-54 |
| 1964 | HIST anchor | Real-world System/360 helps demonstrate the relevance of 8-bit bytes | Our world need not have the same vendor; comparable byte-oriented pressures exist |
| 1968 | CANON direction | **CVL-68** native eight-bit Latin–Greek code becomes mainline standard | Direct access to both scripts, unambiguous character identity, no page shift for core letters |
| 1973–1975 | DRAFT | Scientific institutions dispute preservation of XXXVI software and tapes versus Nova's byte-oriented expansion | Text interchange, numeric interchange, and binary compatibility become separate procurement requirements |
| 1976 | DRAFT | **Sextaria-S0** 48-bit scientific-computer proposal enters laboratory consideration | Six eight-bit CVL characters per word is convenient, but cost and high-precision numerical requirements must justify wide hardware |
| 1979–1981 | DRAFT | TRANFOR source-sharing pressures motivate a proposed **MODVLA** structured-module language | Explicit record layouts, script profiles, target-specific binary objects |
| 1981–1982 | DRAFT | Cheaper Nova-derived systems enter offices and education; a script-confusable identifier incident becomes a possible plot | Not all Nova-compatible systems need identical CPU word width; Latin/Greek glyph identities require editor policy |
| 1983–1985 | DRAFT | **RATIO** numerical-contract language is proposed; three-machine coexistence considered as one ending | Auditability and explicit floating precision become more important than merely translating characters |
| 1970s | DRAFT | Broader system languages and multiuser operating systems develop | Specific ISA, file and process standards remain unresolved |

| 1981–1983 | DRAFT | Nova Minor affordable microcomputers and disputed CVL-68 font-ROM support | Shared character files need not imply a shared 32-bit Nova-N1 binary |
| 1984–1987 | DRAFT | TABVLA bilingual desktop concept and university printing procurement | Fonts, input, character clusters and printed page layout become distinct compatibility claims |
| 1987–1990 | DRAFT | Sextaria specialist scientific workstations coexist with low-cost Nova desktops | Graphics/numerical needs versus manufacturing scale; visual GUI compatibility differs from binary ABI |
| 1990–1992 | DRAFT | Universal character identity proposal addresses CVL-68 global repertoire limits | International text beyond first-class Latin/Greek; normalization and archives remain unresolved |
| 1993–1995 | DRAFT | Semantic document interchange competes with page-faithful printing | Multiple desktop formats, script identity and layout interchange |

| 1990s | DRAFT | Global text standard supersedes bilingual eight-bit ceilings | Polytonic Greek and world scripts require a coherent multibyte story |
| 2000s | DRAFT | Network standards and programming ecosystems mature | Protocol bytes and older storage formats carry CVL legacy |
| 2026 | DRAFT | Modern accelerators, operating systems and AI coexist with the inherited standards | Native classical-language terminology; legacy encoding vulnerabilities may persist |

The 1981–1995 entries are further developed in [the personal computer revolution](de-revolutione-machinarum-domesticarum-1981-1995.md). All dates, models, events, and TABVLA are **DRAFT**.

The 1973–1985 entries above are proposals developed in [De Bello Verborum et Machinarum](de-bello-verborum-et-machinarum-1973-1985.md), **not historical facts and not promoted to CANON**.

## Modern research implementation (not an alternate-history event)

On **2026-10-31 in our own world**, this repository added a Python reference emulator for the fictional 1954 Machina XXXVI/P0 instruction subset. See [Phase V report](phase-v-emulator.md). Source inclusion is not evidence that the fictional machine existed in 1954, or that the committed tests have passed.

## Related narrative

See [Controversia Codicum / Encoding War, 1963–1968](encoding-war-1963-1968.md). Its fictional factions and events are DRAFT, not real history.

## Transition pressures / 为什么标准必须更换？

**1954 → 1963:** Character-page switching works when uppercase terminals dominate but complicates recovery after transmission errors, indexing and embedded mathematical symbols.

**1963 → 1968:** 7-bit direct encoding cannot comfortably represent Latin and Greek uppercase/lowercase alphabets, digits, punctuation and controls together. A new 8-bit direct standard eliminates alphabet page shifts.

**1968 → 1990s:** 256 code points still cannot capture all world scripts and all polytonic Greek combinations as independent precomposed characters. A later universal standard needs canonical equivalence and legacy conversion rules.

## Work to do

- Identify what fictional industrial organization standardizes CVL and why.
- Decide whether CVL-63 is a genuine seven-bit shift encoding or merely a terminal profile.
- Describe how early packed six-bit tapes are transcoded to eight-bit files.
- Examine whether Greek mathematical identifiers are permitted in the first major scientific language or only in its successor.
- Separate *historical timing analogies* from the fictional brand and standard names.