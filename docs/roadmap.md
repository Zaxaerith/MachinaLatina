# Roadmap / 项目路线图

**Approach:** literature and design first; small prototypes later. No large speculative compiler or OS project until there is an internally consistent character and machine model.

## 0.1 — Founding documentation (current)

- [x] Bilingual Greco-Roman counterfactual and explicit evidence labels
- [x] Draft chronology, architectural decision log
- [x] CVL-54, CVL-63, CVL-68 exploratory specification documents
- [x] Initial historical sources list
- [ ] Technical and philological peer review
- [x] Project-wide licensing decision: CC BY 4.0 documents; MIT code

## 0.2 — CVL-68 normative table

- [x] Publish an exploratory 256-slot inventory (including explicitly RESERVED positions)
- [ ] Finalize every assigned character and establish interoperable CVL-68 decoding semantics
- [x] Publish polytonic P1 candidate and initial sigma/combining comparison policy
- [ ] Finalize control codes, diacritics, case mapping and normative validation
- [x] Publish initial manually checked Latin/Greek vectors
- [ ] Implement automated round-trip tests, including mixed-script text and combining marks
- [x] Document first incompatibility analysis and legacy migration constraints
- [ ] Complete implementable ASCII/Unicode mapping and compatibility tests
- [ ] Version and freeze first interoperable encoding profile

See [CVL-68 byte ledger](../specifications/CVL-68-byte-ledger.md) for the non-normative inventory. It is not a frozen standard.

The [encoding war narrative](encoding-war-1963-1968.md), [polytonic proposal](../specifications/CVL-68-polytonic.md) and [migration proposal](../specifications/CVL-54-to-68-migration.md) are now published as **drafts**, not locked standards.

## 0.3 — CVL-54 / CVL-68 converter

- [ ] Specify both six-bit shift pages in full
- [ ] Build compact reference encoder/decoder (Python or Rust; minimal dependencies)
- [ ] Test packing/unpacking six six-bit symbols in one 36-bit word
- [ ] Validate error recovery and lossy conversions

## 0.4 — Machina XXXVI design (Phase IV in progress)

- [x] Publish experimental 36-bit word layout, 15-bit word addresses, registers, and synchronous output subset
- [x] Specify P0 ten-opcode ISA and worked octal/hex machine words **on paper**
- [x] Propose six-bit CVL-54/P0 two-page character assignments and shift semantics
- [ ] Independently verify every machine word and output trace with code
- [ ] Specify signed/floating arithmetic, interrupts, failures, tapes and physical I/O
- [x] Commit a minimal Python P0 emulator, octal image loader and sample program
- [x] Add unit tests covering instruction words, arithmetic, invalid fields and Greek printer state
- [x] Run 22 local unit tests against a reconstructed working tree (2026-11-12)
- [ ] Execute full suite on a clean GitHub checkout / CI
- [x] Implement P0 two-pass assembler and handwritten / TEX word generation

## 0.5 — Python reference interpreter (Phase V)

- [x] Ten ISA P0 operations implemented in standard-library Python
- [x] CVL-54/P0 stateful printer, octal image loader and demo program
- [x] Test suite checked in (success not yet independently demonstrated)
- [x] Run and record 22 local tests (reconstructed tree, not clean clone)
- [ ] Run CI / clean-clone conformance tests
- [ ] Cross-platform smoke/CI and external test vectors

See [Phase V report](phase-v-emulator.md).

## 0.6 — Phase VI: assembler and text gateway

- [x] Two-pass Latin mnemonic assembler with forward labels, ORG/VER/TEX, and octal memory-image export
- [x] Candidate CVL-54/P0 to CVL-68 direct-byte subset gateway (lossy with respect to original archive metadata)
- [x] 22/22 local test methods passed on 2026-11-12 (13 legacy + 9 new)
- [ ] Verify the committed GitHub tree in CI or a clean clone
- [ ] Develop a coherent record framing / printer reset contract and fuller polytonic treatment

See [Phase VI report](phase-vi-assembler-gateway.md).

## 0.7 — Phase VII: bifurcation of machine architectures

- [x] Document 1968's fictional 36-bit compatibility line (**Machina XXXVI-R0**)
- [x] Document experimental byte-addressed 32-bit data family (**Machina Nova-N0**), explicitly memory-only
- [x] Implement a reversible R0 record pack/unpack with external logical length
- [x] Implement 24-bit-address-space / 32-bit big-endian N0 memory laboratory
- [x] Run 7 focused local memory-layout tests (2026-11-12)
- [ ] Validate full repository tests on a synchronized checkout or GitHub Actions
- [x] Propose and implement an experimental Nova-N1 ISA and reference CPU; **not yet canonized**
- [ ] Specify controller record framing and software-level compatibility

See [Phase VII architecture fork](phase-vii-architecture-fork.md).

## 0.8 — Phase VIII: first independent Nova CPU

- [x] Specify Nova-N1 fixed 32-bit instruction format (8-bit opcode + 24-bit operand)
- [x] Implement twelve byte-addressed CPU instructions, native byte output and hex-byte memory images
- [x] Run two independent machine-language greetings; both decode to SALVE ΛΟΓΟΣ
- [x] Execute twelve local Phase VIII tests and document limitations
- [ ] Validate the full GitHub repository checkout under CI
- [ ] Research a compact Nova instruction scheme and buffered I/O
- [ ] Explore a portable high-level programming language with two backends

See [Phase VIII](phase-viii-nova-n1.md).

## 0.9 — Phase IX: TRANFOR/P0 portable source experiment

- [x] Publish a constrained NAT15 and shared Latin–Greek text-language contract
- [x] Implement dual XXXVI/P0 and Nova-N1 compiler backends
- [x] Emit two distinct native memory-image formats plus variable-address metadata
- [x] Run local compiler and interpreter smoke test; 7 focused tests passed using reconstructed existing target interfaces
- [ ] Validate exact committed source across both real repository CPU implementations and clean-checkout CI
- [ ] Study portable floating-point semantics, a source-to-source front end, and cross-machine I/O protocols

See [Phase IX](phase-ix-tranfor.md) and [TRANFOR/P0 specification](../specifications/TRANFOR-P0.md).

## 1.0 — Phase X: portable scientific arithmetic, not identical floating results

- [x] Publish experimental 36-bit XXXVI-F36 and 32-bit Nova-F32 binary float profiles
- [x] Implement exact-rational finite encoding, round-to-nearest ties-to-even and trapped invalid codes
- [x] Add four FLEG/FADD/FSVB/FPON instructions to **each** CPU, preserving original P0 integer opcodes
- [x] Add typed REALIS/FORMVLA to TRANFOR/P1, with two per-format backend oracles
- [x] Demonstrate deterministic divergence for 1 + 2^-24 on F36 vs F32
- [x] Run 11 new local floating tests and 7 prior TRANFOR tests against a reconstructed development environment
- [ ] Validate a clean checkout of the full GitHub repository (including Phase V–IX tests) in CI
- [x] Define float multiplication/division with per-format deterministic rounding
- [ ] Define comparison, formatted numeric I/O and cross-format conversion

See [Phase X report](phase-x-floating.md), [floating profile](../specifications/FLOAT-P0.md) and [TRANFOR/P1](../specifications/TRANFOR-P1.md).

## 1.1 — Phase XI: bounded scientific vectors

- [x] Extend both fictional finite floating formats with exact-rational multiplication/division, one rounding per operation
- [x] Extend XXXVI and Nova with separate experimental FMVL/FDIV opcodes
- [x] Extend TRANFOR to P2 bounded VECTOR literals (1–8 REALIS values) and ordered PRODVC dot products
- [x] Generate actual machine instructions rather than compiler-only dot-product constants
- [x] Demonstrate F36 1/16777216 versus F32 0 after identical ordered dot-product source
- [x] Run 10 new tests; 69/69 in reconstructed local tree on 2026-11-12
- [ ] Confirm clean checkout/full-suite reproducibility via CI
- [ ] Investigate library and precision contracts, no speculative premature OS

See [Phase XI](phase-xi-vectors.md) and [TRANFOR/P2](../specifications/TRANFOR-P2.md).

## 1.2 — Phase XII: Ordo Operum/P0 batch jobs

- [x] Define Latin LABOR/FONTE/IMAGO/EDE/LIMES/FINIS job-control deck
- [x] Add host-side monitor routing TRANFOR/P2 sources to XXXVI/Nova native interpreters
- [x] Load architecture-specific .m36/.nvi images without claiming binary compatibility
- [x] Define OMR1 length-prefixed sequential CVL-68 spool and JSON job report
- [x] Implement per-job instruction ceilings, source path confinement and continuation after failures
- [x] Run 15 isolated local parser/archive/mock-executor tests (2026-11-13)
- [ ] Run full four-job sample against exact committed CPU code in a clean checkout
- [ ] Test archive and scheduler semantics in GitHub Actions
- [ ] Research guest-level input device, record I/O, and resource protection separately

See [Ordo Operum/P0](../specifications/ORDO-P0.md) and [Phase XII](phase-xii-batch.md).

## Later phases

- [x] First experimental TRANFOR/P0 scientific language sketch and dual-target compiler (not a production compiler)
- [ ] Latin system calls, terminal emulation and primitive file system
- [ ] Historical 'compatibility incident' case studies
- [ ] Later universal multi-script encoding and fictional Internet standards

**Definition of done:** A milestone needs a readable spec, a rationale, a clear decision status, and reproducible example behavior. Architectural diagrams without semantics are not sufficient.