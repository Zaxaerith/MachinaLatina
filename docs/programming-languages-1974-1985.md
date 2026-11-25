# Programming Languages 1974–1985 / 拉丁—希腊计算文明的语言分化

> **DRAFT historical-language proposal.** TRANFOR/P0/P1/P2 have existing experimental Python backends. **MODVLA** and **RATIO** below are fictional candidate families; there is NO parser, compiler, standard, or executable implementation for them. Their names are technical neologisms, not claims about idiomatic Classical Latin.

## Why a new language must emerge

An alternative history that merely renames FORTRAN, C, Pascal and Modula is cosmetic. Language evolution must respond to **actual source-level pain** in this world's computing environment:

- Scientific codes already depend on legacy XXXVI word-addressed data and F36 numeric conventions.
- Nova treats bytes as directly addressable and is expanding into business, communications and interactive machines.
- Sextaria research proposes 48-bit words and six CVL-68 byte slots per data word, but its pointer model has not been settled.
- CVL-68 can address Latin and Greek core letters distinctly. Neither the existing six-character TRANFOR/P0 source subset nor the old six-bit terminal can express all desired identifiers.
- Ordo Operum batch records have a logical-length protocol, yet little to say about reusable modules, data formats or resident system services.

## Family tree, proposed rather than preordained

    TRANFOR (1957 narrative anchor, scientific)
        |
        +-- TRANFOR scientific extensions (1970s, arrays/numerics)
        |       |-- XXXVI backend
        |       |-- Nova backend
        |       '-- Sextaria backend? [DRAFT, not delivered]
        |
        +-- MODVLA (ca. 1979–1981 proposal)
        |       |-- structured modules; explicit record schemas
        |       |-- source-linguistic profiles LATINA / GRAECA
        |       '-- separate OS/ABI-specific compilation
        |
        '-- RATIO (ca. 1983–1985 proposal)
                |-- constraints and auditable scientific models
                '-- possible proof/contract influence [DRAFT]

Dates, names and genealogy are hypotheses.

## 2026-11-25 MODVLA follow-up

[MODVLA-I/R1](../specifications/MODVLA-I-R1.md) proposes a bounded concrete source subset; the [layout and ABI study](../specifications/MODVLA-layout-and-abi-study.md) gives illustrative native layouts and an invariant external record. The original open grammar sketch below remains historical context. No compiler or native ABI has been implemented.

## MODVLA should solve a specific problem

**Candidate role:** writing large system software whose data declarations are explicit enough to cross byte-oriented Nova and word-oriented scientific machines.

Distinctive *proposed* features:

1. A module declares imported types and its own exported record schema, rather than pretending that raw in-memory structs share identical sizes across CPUs.
2. Stored records specify units (byte, word, character), character encoding and numeric format separately.
3. Source declares a **script profile**. A LATINA module may allow strict Latin identifiers; a GRAECA scientific submodule may explicitly permit Greek mathematical symbols. This is a policy proposal, not an implementation.
4. The compiler rejects ambiguous or confusable mixed-script identifier spellings by default, while permitting deliberate aliases through explicit declarations.
5. I/O is described through typed sequential records; a user program does not automatically possess arbitrary host file-system privileges.
6. Compilation produces ISA-specific objects. Common source contracts do not imply identical executable binary formats.

A fictional textbook might write (illustrative, **not runnable syntax**):

    MODVLVM MENSVRA
    LINGVA LATINA
    IMPORTA RECORDVM GEO
    ...
    FINIS MODVLI

This sketch deliberately avoids an entire C/Pascal clone. The actual grammar is an open decision.

## A hypothetical 1982 confusable-identifier incident

Consider two different source identifiers:

    Latin A    : character U+0041 in a modern display transcription
    Greek Α    : character U+0391 in a modern display transcription

In the CVL-68 candidate byte ledger they occupy distinct values (Latin A = 0x41; Greek Α = 0x80). The Unicode references are a **modern comparative notation**; the fictional 1982 engineers would not use Unicode as their standard.

A code-review system that merely renders glyphs without exposing their script origin could mislead a reviewer into approving a reference to the wrong variable. The plausible institutional response is an **explicit script annotation / confusable-warning profile**, not an ahistorical copy of today's Unicode security rules. Case folding, final sigma and polytonic accents must be designed, not assumed solved.

## 2026-11-25 RATIO follow-up

[RATIO-I/R1](../specifications/RATIO-I-R1.md) now proposes a small dimensional scalar contract language. [Paper numerical audit](../specifications/RATIO-numeric-audit-study.md) distinguishes exact rational reference, format rounding and measurement uncertainty. No implementation or F48 specification.

## RATIO should not become a retroactive Rust clone

**Candidate role:** verification-friendly numerical and engineering specifications around 1983–1985.

It might be driven by the real project problem of non-identical float arithmetic: how do researchers write contracts such as “error is below a declared tolerance”, or “reduction order is fixed”? Its identity would be **numeric contracts and auditability**, not modern ownership/borrowing syntax invented decades early.

Possible modules:
- exact physical-unit annotations and interval bounds;
- declared target precision and rounding profiles;
- human-checkable pre/postconditions for numerical routines;
- transparent output metadata specifying CPU and compiler revision.

A useful historical plot: laboratories accept a program whose math is correct, then reject its results because the data interchange format omitted precision declarations. RATIO grows from that audit failure, not from premonition about modern language fashion.

## Why Greek in source is hard even with CVL-68

Greek string literals and Greek identifiers are different engineering questions. Greek lowercase and mathematical letters may be available in text storage while old compiler symbol tables assume uppercase six-character Latin identifiers. Upgrading requires:
- lexer/tokenization changes;
- clear identifier script and normalization policy;
- error messages and terminal/keyboarding support;
- object-file symbol naming and cross-target ABI rules;
- a way to preserve byte identity during source distribution.

Do not mislabel existing TRANFOR/P2 experiments as if they already offer these facilities.

## Open questions for the next chapters

- Which year and institution defines MODVLA's first portable source profile?
- Should **Sextaria** favor a stack machine, descriptor-heavy design, accumulator, or general registers?
- Will system APIs expose a single *byte stream* abstraction, or will typed **record streams** remain dominant?
- How will non-Latin/non-Greek languages participate in future programming standards?
- Do RATIO-like numerical contracts become part of TRANFOR, or remain a separate field?

See [1973–1985 narrative](de-bello-verborum-et-machinarum-1973-1985.md), [TRANFOR/P2](../specifications/TRANFOR-P2.md), and [CVL-68 byte ledger](../specifications/CVL-68-byte-ledger.md).
