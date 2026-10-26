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
- [ ] Implement a minimal emulator and assembler; **not yet delivered**

## Later phases

- [ ] TRANFOR scientific language sketch and compiler experiment
- [ ] Latin system calls, terminal emulation and primitive file system
- [ ] Historical 'compatibility incident' case studies
- [ ] Later universal multi-script encoding and fictional Internet standards

**Definition of done:** A milestone needs a readable spec, a rationale, a clear decision status, and reproducible example behavior. Architectural diagrams without semantics are not sufficient.