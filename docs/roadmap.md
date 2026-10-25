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
- [ ] Decide control codes, Greek diacritic representation and case mapping
- [x] Publish initial manually checked Latin/Greek vectors
- [ ] Implement automated round-trip tests, including mixed-script text and combining marks
- [ ] Document incompatibility with our world's ASCII/Unicode
- [ ] Version and freeze first interoperable encoding profile

See [CVL-68 byte ledger](../specifications/CVL-68-byte-ledger.md) for the non-normative inventory. It is not a frozen standard.

## 0.3 — CVL-54 / CVL-68 converter

- [ ] Specify both six-bit shift pages in full
- [ ] Build compact reference encoder/decoder (Python or Rust; minimal dependencies)
- [ ] Test packing/unpacking six six-bit symbols in one 36-bit word
- [ ] Validate error recovery and lossy conversions

## 0.4 — Machina XXXVI design

- [ ] Data formats, registers, addressing, interrupts and I/O
- [ ] Completely specified ISA with executable test vectors
- [ ] Minimal emulator and assembler, not a real hardware claim

## Later phases

- [ ] TRANFOR scientific language sketch and compiler experiment
- [ ] Latin system calls, terminal emulation and primitive file system
- [ ] Historical 'compatibility incident' case studies
- [ ] Later universal multi-script encoding and fictional Internet standards

**Definition of done:** A milestone needs a readable spec, a rationale, a clear decision status, and reproducible example behavior. Architectural diagrams without semantics are not sufficient.