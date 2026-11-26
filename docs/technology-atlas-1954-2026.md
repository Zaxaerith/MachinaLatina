# Technology Atlas / 技术世系图谱 (1954–2026)
> Phase XXXVII · 2026-11-26 · DRAFT integration, not a ratification or exhaustive conformance audit. Source baseline: 9ec3dca91822b6fd9e957e89b3981d8eb87fd0e5 (Phase XXXVI). Dates refer to candidate fictional eras; modern research commits are distinct.

## 1. Read by technical domain

| Domain | Early roots | Successor candidates | What remains unproven |
| --- | --- | --- | --- |
| Text | [CVL-54/P0](../specifications/CVL-54-P0.md), [TP1](../specifications/CVL-63-TP1.md) | [CVL-68/RC1](../specifications/CVL-68-RC1.md), [COS C24/W1](../specifications/COS-97-R1.md) | Final repertoires, approval, full normalization and fonts |
| CPU | [XXXVI](../specifications/Machina-XXXVI.md), [Nova N1](../specifications/Machina-Nova-N1.md) | [S1](../specifications/Sextaria-S1-R1.md), [Nova Maior/Magna](../specifications/Nova-Maior-Magna-R1.md), [Mobilis](../specifications/Nova-family-evolution-study.md) | Full ISAs, complete hardware, loader/procedure ABI |
| Numerical | [FLOAT-P0](../specifications/FLOAT-P0.md), [TRANFOR P2](../specifications/TRANFOR-P2.md) | [F48](../specifications/Sextaria-F48-R1.md), [RATIO](../specifications/RATIO-I-R1.md), [M16/F32 matrices](../specifications/MENTIS-matrix-R1.md) | F64, broader RATIO profiles, device execution |
| Languages | TRANFOR scientific tradition | [MODVLA](../specifications/MODVLA-I-R1.md), [SERMO](../specifications/SERMO-I-R1.md), RATIO | Complete grammars, compilers, runtime/ABI; no mandatory direct syntax ancestry |
| OS | [Ordo host study](../specifications/ORDO-P0.md) (modern research analogy only) | [ORDO-N](../specifications/ORDO-N-I-R1.md), [PARTES](../specifications/PARTES-I-R1.md), [CVSTOS](../specifications/CVSTOS-I-R1.md) | Native kernels, storage, drivers, M64 protection, actual devices |
| Network | TABVLA, COS | [NODVS](../specifications/NODVS-98-R1.md), [LIGAMEN](../specifications/LIGAMEN-99-R1.md), [RETE](../specifications/RETE-00-R1.md), [SERMO runtime](../specifications/SERMO-III-runtime-study.md) | Secure resolution/transport, mutation, browser, deployment |
| Software | LIBERTAS CODICVM | [STEMMA](../specifications/STEMMA-R1.md), [FASCICVLVS](../specifications/FASCICVLVS-R1.md), FORVM CODICVM | Digest/signature suites, installers, federation |
| Graphics | TABVLA / Minor / Sextaria | [IMAGO](../specifications/IMAGO-86-R1.md), [FIGVRA](../specifications/FIGVRA-95-R1.md), [LVDVS](../specifications/LVDVS-console-study.md) | Full pipeline, font engine, device and console ISA |
| AI | Symbolic/statistical studies | [MENTIS tokenizer](../specifications/MENTIS-tokenizer-R1.md), [matrices](../specifications/MENTIS-matrix-R1.md), [evidence](../specifications/MENTIS-evidence-R1.md) | Actual model, training, accelerators, benchmarks |

## 2. Dependency map (arrows mean design input, not binary compatibility)

- CVL-54 -> TP1 (same six-bit data, parity wrapper); CVL-54 -> CVL-68 (explicit conversion, not bit reinterpretation); CVL-68 -> COS (legacy identity mapping); COS -> NODVS -> LIGAMEN/RETE; COS -> STEMMA names and MENTIS tokenizer.
- XXXVI -> old scientific archive and TRANFOR/F36; Nova N1 -> byte-oriented commercial tradition; Maior -> Magna (optional M32 execution); Minor/Media are product-family branches rather than compatible N1 binaries; Mobilis may share a Nova base subset.
- Sextaria S0 -> S1/F48 -> S2 protected region proposal -> PARTES I; Nova M32 + PROTECT -> ORDO-N I and possible CVSTOS I hardware; PARTES migration to Nova requires a new native IPC ABI.
- MODVLA logical/external contracts -> typed service and package interfaces; RATIO -> numerical acceptance; SERMO -> document construction and proposed application runtime.
- TABVLA -> IMAGO and document layout; FIGVRA adds screen raster contract; LVDVS develops reusable tile/sprite and later console profiles. FIGVRA parallel heritage informs future matrix devices without defining a device ISA.
- STEMMA source identity -> FASCICVLVS release metadata; packages depend on actual target ABI and publisher trust; neither implies device permission.
- MENTIS uses COS token identity, NODVS/LIGAMEN retrieved evidence and separately executed numerical tools. Model output is not a trusted record merely because formatted correctly.

## 3. Compatibility is a vector, not a version number

| Pair / operation | Candidate contract | Does NOT follow |
| --- | --- | --- |
| CVL-54 -> TP1 | recover same six data bits after parity validation | all corruption detected, independent 128-character code |
| CVL-54 -> CVL-68 | explicit page-aware decoding/transcoding | lossless for every historical record |
| RC1 -> COS/W1 | mapped legacy code units remain one octet in W1 at known boundaries | arbitrary binary/CVL control streams valid, random resynchronization |
| COS C24 <-> W1 | equivalent registered CID sequence if same declared registry and valid input | same file bytes or font layout |
| XXXVI -> Nova N1 | document/record conversion and source-level numerical comparison | same executable, same float result |
| N1 -> Maior | byte-oriented lineage, big-endian convention | same instruction bytes |
| Maior M32 -> Magna M64 | optional M32 execution preserves selected ISA semantics | M64 native overflow semantics or automatic OS compatibility |
| Sextaria -> Nova | exact external MODVLA records and separately decoded F48 | native pointer/structure/IPC compatibility |
| ORDO-N -> PARTES -> CVSTOS | user-space document/schema portability | common file APIs, authority handles or native binaries |
| IMAGO -> FIGVRA | shared RGB16 surface contract in bounded raster profile | actual GPU interoperability, full shader support |
| STEMMA -> FASCICVLVS | link source revision and exact artifact identity | deterministic builds, legal permission or authenticated publication by itself |
| COS -> MENTIS | exact CID/token vocabulary binding | one token per character, model fairness or factual truth |

A usable cross-system application requires independently sufficient source support, ISA, loader, procedure ABI, service API, permissions and data semantics. Numerical equivalence and scientific validity are additional checks, not a property of binary compatibility.

## 4. Four evidence classes

CANON world assumptions only as in [premise](premise.md); HIST real comparison only as in [historical sources](historical-sources.md); DRAFT all specific proposed architectures, formats, institutions and market outcomes unless explicitly ratified; modern executable research includes historical Python XXXVI/Nova/TRANFOR/Ordo artifacts, with prior test evidence only. No new tests were run. See [audit](continuity-audit.md) and [era portraits](era-portraits-1954-2026.md).
