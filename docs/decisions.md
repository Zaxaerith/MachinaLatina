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

## D021 — Input records are real guest instructions, not host print simulation
**State:** DRAFT / executable implementation (2026-11-13)

The [Ordo Operum/P1 device interface](../specifications/ORDO-P1-DEVICE.md) assigns **CAPTA** to each existing fictional CPU: XXXVI reads one packed 36-bit CVL-54 word into word-addressed memory, and Nova reads one native CVL-68 byte into byte-addressed memory. A host `ACCIPE` job card consumes exactly one prior output spool record after successful guest execution, translating text strictly when necessary. Failed jobs do not consume the record. This establishes **input I/O**, not a guest kernel, physical tape transport or recoverable EOF status. [Phase XIII report](phase-xiii-device-io.md).

## D022 — Study a three-family 1973–1985 architecture ecology
**State:** DRAFT / research direction (2026-11-23), NOT CANON

Explore coexistence of the XXXVI 36-bit scientific legacy, Nova byte-addressed commercial family, and possible **Sextaria-S0 48-bit scientific family**. Six 8-bit characters fit a 48-bit word, but this gives **no intrinsic improvement in bits per character** over Nova. Justification must come from workload, numeric precision, data-movement granularity, institutional lock-in and realistic hardware cost, not linguistic determinism. Sextaria's pointer model, ISA, exact numeric format, vendors, and 1976 release remain unsettled. [Architecture-war narrative](de-bello-verborum-et-machinarum-1973-1985.md); [Sextaria study](../specifications/Sextaria-S0-study.md).

## D023 — Language history must follow technical pressures
**State:** DRAFT (2026-11-23)

**MODVLA** is a candidate structured-module language emerging from TRANFOR, record schemas, CVL-script distinctions and differing ABIs; **RATIO** is a candidate language for numerical contracts and auditable precision. These are not existing implementations, nor renamed C/Pascal/Rust. Their dates, names and grammar remain provisional. [Language genealogy](programming-languages-1974-1985.md).

## D024 — Documentation-first workflow; automated conformance retired
**State:** CANON as repository-workflow choice (2026-11-23)

The project emphasizes **counterfactual technical historiography and standards design**. Existing Python experiments are retained but no new CI, emulator milestone or automatic testing is required by default. The automatic `.github/workflows/ci.yml` workflow was removed to avoid noisy checks for a speculative documentation project. Future code experiments may be proposed explicitly and validated proportionately; this does not invalidate recorded historical test results.

## D025 — Distinguish Nova PC lineage from Nova-N1 binary compatibility
**State:** DRAFT / research hypothesis (2026-11-23)

The proposed **Nova Minor / Media / Maior** personal-computer tiers may share CVL-68 text storage, interchange formats and selected source APIs without all executing the experimental 1968 **Nova-N1** 32-bit fixed-width machine code. Inexpensive early machines may use eight- or sixteen-bit datapaths and narrow external buses, without claims of instruction-set compatibility. See [Nova PC study](../specifications/Nova-personal-computer-study.md).

## D026 — Native bilingual desktop does not imply correct typography
**State:** DRAFT / design question (2026-11-23)

The hypothetical **TABVLA** desktop family must distinguish four layers: encoded character identity, keyboard input state, editable character clusters, and print-quality glyph positioning. The proposed 1980s Greek manuscript tests include accents/breathings, case conversion, final sigma and Latin/Greek confusable glyphs. Neither TABVLA nor its dates are canonized or implemented. See [desktop study](../specifications/CVL-desktop-typography-study.md) and [Phase XVI history](de-revolutione-machinarum-domesticarum-1981-1995.md).

## D027 — Worldwide character identity must be separate from CVL-68 bytes
**State:** DRAFT / research proposal (2026-11-23)

A candidate global registry called **COS (Codex Omnium Scripturarum)** could assign stable abstract identities for worldwide scripts. It **must not assume** CVL-68 bytes remain unchanged or that the actual world's ASCII-compatible UTF-8 history necessarily repeats. File encoding declarations, original byte archives, conversion diagnostics, composed Greek character clusters and fair representation of non-Latin/Greek communities remain central. Neither a 24-bit registry nor any byte transform is frozen. [COS study](../specifications/COS-universal-character-registry-study.md).

## D028 — Typed hypertext is a plausible alternative network path
**State:** DRAFT / research proposal (2026-11-23)

The provisional **NODVS/LIGAMEN/RETE** vocabulary suggests typed content records, stable document identities and explicit links, drawing from TABVLA scholarly publication and Ordo sequential-record concepts. No actual wire format, server, parser, network name encoding, or standardization institution has been implemented or adopted. Multilingual domain security must distinguish Latin and Greek lookalikes. [Network format study](network-document-protocols-1995-2005.md); [Phase XVII](de-bello-scripturarum-et-retis-1995-2005.md).

## D029 — Software freedom may originate in archival and numerical reproducibility
**State:** DRAFT / alternative-history institution study (2026-11-23)

A hypothetical **LIBERTAS CODICVM** movement could emerge from institutional need to restore historical CVL-68 documents, scientific data and obsolete system software. Source rights, open interchange formats, device boot rights and legally enforceable copyleft are distinct. No fictional free-software license has been drafted; the repository's real MIT code / CC BY 4.0 document licenses stay unchanged. [Software freedom study](software-freedom-and-distribution-2005-2015.md).

## D030 — ORDO-N, PARTES and CVSTOS are separate OS design candidates
**State:** DRAFT / conceptual architectures (2026-11-23)

**ORDO-N** studies byte-stream general-purpose process systems; **PARTES** studies typed scientific records and separable user-space services; **CVSTOS** studies mobile device capability isolation, low power, fonts and distribution control. These OS lineages do **not** imply real runnable kernels, shared ISA compatibility, a shipping 48-bit CPU, or that the Python host-side Ordo Operum emulator is a historic guest OS. [Architecture study](../specifications/operating-system-families-2005-2015.md).

## D031 — Language lineage and package identity follow format and ABI constraints
**State:** DRAFT (2026-11-23)

Proposed **MODVLA** can express abstract text vs raw bytes vs numeric records and platform ABI differences; **SERMO** could manipulate COS/NODVS text/network objects; **RATIO** could express numerical precision and reproducibility. None is a completed executable language. Source repositories must distinguish COS character identities, original CVL bytes, machine binaries and build provenance; this does not automatically reproduce real-world Git object or package formats. [Language study](programming-ecosystem-2005-2015.md).

## D032 — Scientific numerical tradition may outlive Sextaria CPU hardware
**State:** DRAFT / 2015–2026 historical design (2026-11-23)

Study Nova-derived general-purpose CPUs, independent matrix acceleration and scientifically auditable higher-precision numerical tools. A Sextaria-inspired verification discipline is plausible even if the original 48-bit computers fade; this **does not** define an F48 numeric standard or assert any 48-bit tensor hardware was invented. [Heterogeneous computing study](../specifications/heterogeneous-computing-2015-2026-study.md).

## D033 — COS characters are neither ML tokens nor model understanding
**State:** DRAFT / multilingual AI design (2026-11-23)

Old CVL/COS text requires explicit versioned decoding, preservation of original source bytes and script identity. Model tokens have separate vocabulary/segmentation semantics; a global character registry does not guarantee linguistic comprehension or equal token cost. Training corpus imbalance may perpetuate Greek–Latin institutional privilege. [Language model study](ai-languages-and-cos-2015-2026.md).

## D034 — Model output must separate citation, calculation and adjudication
**State:** DRAFT / scientific provenance design (2026-11-23)

A plausible NODVS/RATIO-inspired AI research workflow separates model-generated prose from actually retrieved, authorized and versioned references, independently executed numeric calculations, and human-accepted scientific results. A well-formed but fabricated citation is never evidence. No research manifest protocol, model or proof engine has been implemented. [AI provenance study](ai-provenance-and-numerics-2015-2026.md).

## D035 — Phase XX history integrates but does not freeze proposal timelines
**State:** CANON as editorial / evidence classification policy (2026-11-23)

The [1954–2026 narrative history](historia-machinae-latinae-1954-2026.md) and [clean chronology](chronology.md) collect previous **DRAFT** periods in reading order. Their publication does **not** promote Sextaria-S0, COS/NODVS, TABVLA, ORDO-N/PARTES/CVSTOS, MODVLA/SERMO/RATIO, fictional institutional names or imagined 2026 AI products to CANON. Each requires an explicit subsequent technical and institutional decision; real Python experiments are preserved as separate research artifacts. See [institutions](institutions-and-lineages.md) and [continuity audit](continuity-audit.md).

## D036 — CVL-68/RC1 is ready for review, not ratified
**State:** REVIEW CANDIDATE / NOT CANON (2026-11-23)

The [CVL-68/RC1 proposed standard](../specifications/CVL-68-RC1.md) provides a complete [256-position ledger](../specifications/CVL-68-RC1-ledger.md), strict text controls/RESERVED rejection, a canonical-order *limited* polytonic grammar, distinct Latin/Greek character identities and explicit legacy migration boundaries. **33 control + 136 glyph + 11 combining + 76 RESERVED = 256.** Previous byte assignments, including `SALVE ΛΟΓΟΣ`, are unchanged. Compared with Ledger A, only three previously reserved positions (C0–C2) are newly proposed as scholarly breve/underdot/overline. Distinguish fictional 1968 core encoding from the proposed later P1 scholarly profile.

This decision **records publication for review**; it does not approve the byte map, validate every Greek philological form, guarantee Unicode-lossless punctuation conversion, change emulator code, or reinstate CI. Explicit approval is required before CANON promotion. Review [continuity audit](continuity-audit.md).

## D037 — Prefer CVL-63 as a seven-unit parity transport, not another alphabet
**State:** RECOMMENDED DRAFT / NOT CANON (2026-11-23)

A [CVL-63/TP1 proposal](../specifications/CVL-63-TP1.md) recommends preserving the CVL-54/P0 six-bit LATINA/GRAECA page-state codes in each seven-bit transmission **slot**, with the seventh bit for even parity. The valid transmitted units are **64 parity-consistent seven-bit patterns**, not 128 independent characters. This reduces needless re-encoding of stored XXXVI words between 1954 and the 1968 CVL-68 direct-byte transition, but does **not** eliminate lost-SHIFT errors, reject all multi-bit corruption, define a physical network frame, or guarantee archival tape restoration. The prior full seven-bit Candidate A is retained as an alternative.

The [worked ledger](cvl63-transport-migration-ledger.md) shows `SALVE ΛΟΓΟΣ` across two XXXVI words, twelve seven-bit TP1 slots and eleven direct CVL-68 bytes. The recommendation is **not a ratification**; CVL-54 source-table CANON status, record framing, parity policy and formal fictional institution remain open. No code or CI.

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