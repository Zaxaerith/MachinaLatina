# MODVLA-I/R1 — Interfaces, Values and External Records
## 第一代系统编程语言候选（1979—1985）

> REVIEW CANDIDATE / DRAFT / NOT CANON · editorial 2026-11-25. All language syntax, layouts and historical adoption below are proposed alternate history. No compiler, object code, native ABI, operating system or hardware extension is delivered.

## 1. Motivation

XXXVI/P0 has 36-bit words and 15-bit word addresses; Nova-N1 has aligned big-endian 32-bit words and 24-bit byte addresses. Sextaria-S0 is a 48-bit research proposal with undecided addressing, preferably H (word address plus lane). These incompatible machines make an unqualified "integer", "character pointer" or "memory image" unsuitable as a portable record contract. MODVLA distinguishes a logical value, a local storage layout, and an external representation. The compiler may lower the same source differently. Neither P0 nor N1 has a defined general calling ABI; actual compilation requires successor ISA/toolchain support. S0 has no settled ISA at all.

HIST analogues, not fictional ancestry: Wirth's Modula-2 was designed in 1978–79 for modular systems; Xerox Mesa introduced intermodule interface checking in 1977. See [Wirth's retrospective](https://people.inf.ethz.ch/wirth/Articles/Modula-Oberon-June.pdf), [Mesa programming environment](https://xeroxparcarchive.computerhistory.org/ivy/sweet/mesapaper/.mesasummary.tioga%212.html). The later real [XDR RFC 1014 (1987)](https://www.rfc-editor.org/rfc/rfc1014) illustrates external data representation. MODVLA is not a renamed version of any of these.

## 2. Types

| Type | Abstract meaning | Portability boundary |
| --- | --- | --- |
| NAT8, NAT16, NAT24, NAT32 | unsigned values of exactly 8, 16, 24, 32 bits | width of value is not sizeof native storage |
| LOGICVM | VERVM / FALSVM | no implied in-memory bit pattern |
| RECORDVM | named ordered fields with individually declared types | no implicit external representation |
| OCTETVM (later profile) | 8-bit uninterpreted data unit | even on a machine without byte addresses |
| SIGNVM6 (later profile) | CVL-54 six-bit code unit | page-dependent, not an abstract character |
| SIGNVM8 (later profile) | CVL-68 eight-bit code unit | not identical to OCTETVM semantically |
| VERBVM (target profile) | native unsigned machine word | 36, 32 or proposed 48 bits; nonportable |
| LOCVS(T), FENESTRA(T), TESSERA (later study) | local typed reference, bounded view, opaque service handle | never portable external addresses |

Only the first four fixed-width numeric types and named flat records are executable-semantics candidates in the small grammar below. Checked addition does not wrap; an overflow halts the invocation with a typed diagnostic. A later explicit wrapping operator may serve device drivers. Host arithmetic may wrap, but compiler lowering must enforce the source semantics or refuse compilation. No silent float or native-word promotion.

Text/code units are deliberately separate from later COS character identities. A 1979 compiler cannot require a 1997 registry. Early modules declare source encoding CVL-68 and LINGVA LATINA; a future GRAECA profile may allow Greek identifiers with explicit import aliases. Core identifiers are case-sensitive classical 23-letter Latin plus digits/underscore after the first letter; keywords uppercase. No J/U/W. Source is decoded under a declared codebook before lexing; spaces, HT and CR LF separate tokens. Unicode in this Markdown file is editorial transcription. The core has no string literal syntax. Greek source profile and CVL-54 source adaptation remain research questions.

## 3. A bounded module syntax

The first proposal intentionally omits loops, mutable variables, pointers, device access, interrupts and concurrency. It specifies separately compiled interface and implementation concepts, not yet a production systems compiler.

    MODVLVM MENSVRA;
    LINGVA LATINA;

    INTERFACIES;
        RECORDVM SPECIMEN;
            IDENTITAS: NAT16;
            NOTA: NAT8;
            NVMERVS: NAT24;
        FINIS;

        EXTERNA SPECIMEN;
            IDENTITAS AD 0;
            NOTA AD 2;
            NVMERVS AD 3;
            LONGITVDO 6;
            ORDO ALTVS;
        FINIS;

        OPVS SEQVENS(R: SPECIMEN): NAT24;
    FINIS;

    CORPVS;
        OPVS SEQVENS(R: SPECIMEN): NAT24;
            REDDE R.NVMERVS + 1;
        FINIS;
    FINIS;
    FINIS MODVLI;

INTERFACIES declares public logical types, optional external schemas, and function signatures. CORPVS provides exactly one definition of every declared operation with the same parameter/return types. Modules are identified by exact names and declared interface revision metadata outside this source subset. IMPORTA module-name may appear after LINGVA and before INTERFACIES; it imports the exported interface, not its private layout. Qualified imported names and cyclic dependency rules beyond the simple acyclic graph are future grammar work; this subset uses only local record and function names.

Restricted grammar: one MODVLVM name; LINGVA LATINA; zero or more IMPORTA name; INTERFACIES; one or more RECORDVM blocks followed by zero or more EXTERNA blocks and one or more OPVS signatures; FINIS; CORPVS; matching OPVS definitions; FINIS; FINIS MODVLI;. RECORDVM name; consists of one or more unique name : NAT-width ; fields and FINIS;. EXTERNA record-name; lists every field once as name AD decimal-offset; then LONGITVDO decimal; ORDO ALTVS; FINIS;. OPVS name (name: record-name): NAT-width; takes one record by logical value; its definition contains REDDE parameter.field + decimal; FINIS;. Decimal integers are unsigned; field and parameter names must resolve uniquely. The literal on the right of + must fit the field's declared width, which must equal return width. No implicit widening. This tiny subset suffices for the example and can be extended later without pretending to specify a full language.

In EXTERNA, offsets and LONGITVDO are in **8-bit octets**, including on XXXVI. ORDO ALTVS means high-order octet first within each fixed-width integer. Every field occupies width/8 consecutive octets; field spans must be nonoverlapping and cover the whole declared external record exactly (no holes or implicit padding in R1). For NAT16 4660, NAT8 165 and NAT24 66051, the external representation is 12 34 A5 01 02 03. SEQVENS returns 66052; at NAT24 max (16777215) the operation fails instead of silently wrapping.

## 4. Contracts, not shared object files

The module interface guarantees logical argument/result types and declared error semantics. A native calling convention must independently define argument locations, alignment, register saving, returns, relocations and fault handling. A record schema guarantees the specified external octets, not native memory bytes. Call-by-value here is a logical property, not a mandated stack copy. No native binary may be linked across ISA/ABI mismatches; equivalent signatures alone are insufficient.

The external schema implies a conceptual serializer/deserializer, not a built-in callable routine in the above grammar. See [layout and ABI study](MODVLA-layout-and-abi-study.md) for exact proposed storage examples. Unknown lengths and incomplete external records fail before constructing a logical value.

## 5. Open systems features

Later MODVLA editions may add checked views, explicitly unsafe hardware operations, opaque service handles, I/O, modules with private state, interrupt routines, generic interfaces, dynamic linking and ABI-specific intrinsics. These are not retroactively implemented in R1. In particular a safe pointer policy does not itself provide MMU protection, privilege separation, concurrency safety or an OS. The contemporary XXXVI and Nova research prototypes cannot run this example without extensions or a new backend; Sextaria hardware is not specified.

Related: [layout and ABI](MODVLA-layout-and-abi-study.md), [historical narrative](../docs/de-modvlis-1979-2015.md), [XXXVI](Machina-XXXVI.md), [Nova](Machina-Nova-N1.md), [Sextaria](Sextaria-S0-study.md).
