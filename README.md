# Machina Latina
### Duae Linguae, Una Machina — Two Languages, One Computing Civilization

> **Speculative alternate history, not a reconstruction of actual Roman computers.**  
> **架空计算机技术史项目，并非真实历史或古罗马计算机复原工程。**

**Machina Latina** explores a counterfactual: What if Classical Latin had remained a living language of administration and engineering, while Greek retained an institutional role in mathematics and higher learning, through the electronic-computing revolution?

Instead of translating modern English keywords after the fact, this project asks how historical choices—character sets, machine words, instruction mnemonics, terminals, programming languages and compatibility obligations—could have accumulated into a different digital civilization.

**Current design direction: Timeline B, with native eight-bit Latin–Greek computing as the principal successor architecture.** The early six-bit dual-page system is retained as a historical predecessor, not as the long-term encoding.

## 中文简介

本项目从一个反事实问题出发：**如果古典拉丁语持续作为活语言，而希腊语在数学、哲学和高等科学领域一直具有制度性的文化地位，1950 年代以后诞生的电子计算机文明会是什么样？**

我们讨论的并非「把 Python 或 C 翻译成拉丁语」，而是重新推演字符编码、计算机字长、终端、指令集、编程语言、操作系统及网络标准之间的历史继承关系。

项目遵循 **Timeline B**：不是默认现实中的 ASCII、Unix、x86、C 等标准必然出现，而是保持物理学与计算理论大致同步，让标准化历史独立演化。

## Start here / 从这里开始

| Document | Purpose |
| --- | --- |
| [Premise / 核心世界观](docs/premise.md) | Assumptions, boundaries and confidence levels / 前提与推演边界 |
| [Chronology / 时间线](docs/chronology.md) | A speculative 1954–2026 chronology / 架空发展史 |
| [Decisions / 设计决策](docs/decisions.md) | Chosen directions and unresolved alternatives / 已选方向与待决问题 |
| [CVL-54](specifications/CVL-54.md) | Six-bit Latin–Greek shift encoding; predecessor draft |
| [CVL-63](specifications/CVL-63.md) | Transitional seven-bit communications proposal |
| [CVL-68](specifications/CVL-68.md) | Eight-bit bilingual character encoding; principal draft |
| [CVL-68 byte ledger](specifications/CVL-68-byte-ledger.md) | All 256 positions accounted for; non-normative test vectors and reserved positions |
| [Encoding War / 编码战争](docs/encoding-war-1963-1968.md) | Fictional 1963–1968 standards conflict |
| [Polytonic Greek P1](specifications/CVL-68-polytonic.md) | Candidate accent, breathing, sigma and normalization rules |
| [Legacy migration](specifications/CVL-54-to-68-migration.md) | Conversion and archival constraints for six-bit machine records |
| [Machina XXXVI ISA P0](specifications/Machina-XXXVI.md) | Fictional 1954 36-bit word-addressed machine and ten defined opcodes |
| [CVL-54/P0 character profile](specifications/CVL-54-P0.md) | First numerical six-bit bilingual-page mapping candidate |
| [Worked machine words](docs/machina-xxxvi-programs.md) | Octal/hex instruction and SALVE ΛΟΓΟΣ print vectors |
| [36-bit legacy](docs/machina-xxxvi-legacy.md) | Why an eight-bit bilingual successor creates compatibility pressures |
| [Phase V reference emulator](docs/phase-v-emulator.md) | Standard-library Python implementation and ISA P0 |
| [Phase VI assembler + CVL gateway](docs/phase-vi-assembler-gateway.md) | Two-pass assembler, direct-byte conversion experiment and locally executed tests |
| [Phase VII architecture fork](docs/phase-vii-architecture-fork.md) | 36-bit XXXVI-R0 versus 32-bit byte-addressed Nova-N0 |
| [XXXVI-R0 retrofit](specifications/Machina-XXXVI-R0.md) | Experimental four-byte packing in a 36-bit word |
| [Nova-N0 memory](specifications/Machina-Nova-N0.md) | Experimental 24-bit byte addressing and 32-bit big-endian memory |
| [Machina Nova-N1 ISA](specifications/Machina-Nova-N1.md) | Executable independent 1968 CPU with 12 candidate instructions |
| [Phase VIII: two executable machine languages](docs/phase-viii-nova-n1.md) | Cross-machine text comparison and local test evidence |
| [TRANFOR/P0 language](specifications/TRANFOR-P0.md) | First shared NAT15 scientific language and two native backends |
| [Phase IX: portable source](docs/phase-ix-tranfor.md) | Compiler results, usage and research limitations |
| [Floating profiles](specifications/FLOAT-P0.md) | Two non-IEEE exact-rounding F36/F32 formats |
| [TRANFOR/P1](specifications/TRANFOR-P1.md) | Typed scientific floating extension with two native backends |
| [Phase X: numerical divergence](docs/phase-x-floating.md) | How 36-bit and 32-bit computers compute different rounded answers |
| [TRANFOR/P2 vectors](specifications/TRANFOR-P2.md) | Ordered dot products and REALIS multiply/divide on both CPUs |
| [Phase XI: scientific vectors](docs/phase-xi-vectors.md) | Two-machine results, 69 local tests and limitations |
| [Ordo Operum/P0 batch cards](specifications/ORDO-P0.md) | Shared LABOR control cards, OMR1 sequential record format and error isolation |
| [Phase XII: batch monitor](docs/phase-xii-batch.md) | Fictional 1970s batch-processing research and validation scope |
| [Historical sources / 史实依据](docs/historical-sources.md) | Verifiable reality used to constrain the counterfactual |
| [Roadmap / 路线图](docs/roadmap.md) | Documentary milestones before any emulator or compiler |

## First executable experiment / 第五阶段程序

The Phase V Python reference emulator implements the **ten Machina XXXVI/P0 opcodes** and the **stateful six-bit CVL-54/P0 printer**. It uses Python 3.10+ with no third-party packages.

```sh
python -m machina_xxxvi demo
python -m machina_xxxvi run examples/salve_logos.m36
python -m unittest discover -s tests -v
```

Expected terminal output: `SALVE ΛΟΓΟΣ`. Phase VI **adds a two-pass assembler and conversion gateway**; 22 tests passed locally on a reconstructed source tree, with clean-checkout/CI verification still outstanding. Signed/floating arithmetic and CVL-68-native hardware are not implemented.

```sh
python -m machina_xxxvi assemble examples/salve_logos.mxa --output demo.m36
python -m machina_xxxvi run demo.m36
python -m machina_xxxvi bridge demo.m36 00100 00101 --output demo.cvl
```

## 1968 architecture fork / 第七阶段

The [Phase VII analysis](docs/phase-vii-architecture-fork.md) compares **XXXVI-R0** (four eight-bit bytes packed into each 36-bit word, with external length metadata) against **Nova-N0** (24-bit byte addresses and candidate 32-bit data words). It is a **memory-layout study**, not a new CPU or released emulator. The proposals coexist with the six-bit 1954 machine; they do not rewrite that history.

```sh
python -m machina_xxxvi.archlab
python -m unittest discover -s tests -p test_archlab.py -v
```

## Phase VIII: the independent Nova CPU / 第八阶段

The experimental [Machina Nova-N1 ISA](specifications/Machina-Nova-N1.md) now has its own 32-bit CPU interpreter, sample byte-addressed program and 12 focused tests. Running the two **different** machine-language greetings produces the same visible text, not binary-compatible code.

    python -m machina_nova demo
    python -m machina_nova run examples/nova_salve_logos.nvi
    python -m machina_nova compare

The Phase VIII tests **passed locally on reconstructed legacy sources**; clean GitHub checkout and CI execution are still unverified. See [Phase VIII report](docs/phase-viii-nova-n1.md).

## Phase IX: one source, two machines / 第九阶段

**TRANFOR/P0** is an experimental common high-level language for XXXVI and Nova. It supports restricted 15-bit natural integers, simple add/subtract calculations and the Latin–Greek characters shared by both systems. The two backends generate *different* native memory images.

```sh
python -m tranfor run examples/portable_greeting.trf
python -m tranfor build examples/portable_greeting.trf --out-dir build/tranfor
python -m unittest discover -s tests -p test_tranfor.py -v
```

Its seven focused tests passed in a **local reconstructed-source environment**, but the committed GitHub tree has not yet been verified by clean-clone CI. See [Phase IX report](docs/phase-ix-tranfor.md).

## Phase X: two floating-point architectures / 第十阶段

Both CPUs now support experimental floating-point extensions **without altering the old P0 integer instructions**. XXXVI-F36 and Nova-F32 use different precision/range profiles; TRANFOR/P1's exact rational oracle checks each target separately rather than incorrectly insisting every floating result match.

```sh
python -m tranfor run-real examples/rounding.trf
python -m tranfor build-real examples/rounding.trf --out-dir build/floating
python -m unittest discover -s tests -p test_scientific.py -v
```

The source example computes 1 + 2^-24: F36 retains the increment; F32 rounds the exact tie to 1. Local reconstructed-source tests ran successfully, but a full clean checkout and CI are unverified. See [Phase X study](docs/phase-x-floating.md).

## Phase XI: vector science / 第十一阶段

The experimental **TRANFOR/P2** language compiles bounded VECTOR declarations and **left-to-right rounded** PRODVC dot products to actual XXXVI and Nova floating instructions. The F36 and F32 CPU extensions now support FMVL and FDIV. In the sample, the shared dot product produces **1/16777216 on F36 and 0 on F32**, in accordance with their own accuracy models.

```sh
python -m tranfor run-vector examples/portable_dot.trf
python -m tranfor build-vector examples/portable_dot.trf --out-dir build/vectors
python -m unittest discover -s tests -p test_vectors.py -v
```

69/69 local unit methods passed in a reconstructed development tree (59 inherited, 10 new); a clean checkout/CI has not yet been validated. See [Phase XI](docs/phase-xi-vectors.md).

## Phase XII: Ordo Operum / 第十二阶段

**Ordo Operum/P0** is a modern *host-side job monitor* for the fictional XXXVI and Nova CPU emulators. It accepts identical **LABOR** cards for two machine families, compiles existing TRANFOR/P2 sources or loads native memory images, and appends decoded output as length-prefixed CVL-68/P0 records. Jobs run sequentially; a fault is recorded without halting later jobs.

```sh
python -m ordo_operum run examples/batch_science.ord --out-dir build/batch
python -m ordo_operum inspect build/batch/ACTA.omr
python -m unittest discover -s tests -p test_ordo.py -v
```

**Validation:** 15 isolated local unit tests passed with a CVL-68-compatible test shim and a mock job executor. Full native four-job CPU execution in a clean GitHub checkout has not been verified; the displayed output is expected by the design, not a measured end-to-end outcome. This is **not** yet a guest kernel or filesystem. See [Phase XII report](docs/phase-xii-batch.md).

## Three evidence levels / 三种证据等级

- **HIST** — documented events or standards from our real history, with cited sources.
- **CANON** — adopted assumptions *within this invented timeline*; coherent fiction, not history.
- **DRAFT** — open proposals or examples; not stable enough to implement as standards.

Dates and abbreviations such as CVL-54, CVL-63 and CVL-68 are **fictional names** unless explicitly described otherwise.

## Foundation / 基础约束

1. Electronics, binary logic and scientific advances broadly follow comparable real-world constraints.
2. Classical Latin orthography retains a **23-letter core** (no independent J/U/W); case, punctuation, terminology and typography may still develop.
3. Greek's prestige motivates **native Greek-script support**, not merely Latin-letter transliteration.
4. The world contains many other languages; no pair of alphabets suffices as a global writing standard.
5. A six-bit predecessor with shifting pages is plausible in the 1950s; a **directly addressable eight-bit bilingual encoding** is chosen for the later mainstream.
6. Every important design choice should explain its historical cause, engineering tradeoff and legacy cost.

## What this repository is not

- Not a claim that historical Romans built electronic computers.
- Not a complete ISO/Unicode-like standard or a working virtual machine (yet).
- Not proof that Latin or Greek necessarily imply a particular word size, opcode or instruction set.
- Not a collection of fabricated quotations attributed to real historical people.

## Status / 项目状态

**2026-11-13 — Phase XII host-side Ordo Operum/P0 batch monitor and spool drafts committed; 15 isolated local tests passed, clean-checkout native integration and CI still unverified.** All CVL mappings are **experimental drafts**. The hexadecimal entries are design proposals for the fictional world, not statements about actual ASCII, EBCDIC or Unicode. No binary compatibility is promised between CVL revisions.

### A small thought experiment

A 36-bit machine word holds six six-bit character *codes*:  
`6 characters × 6 bits = 36 bits`.

In the fictional six-bit encoding, the Latin inscription `VERBVM` can occupy one word. In this world, too, `verbum` could become a technical term for a machine word.

## Contributions and licensing

Historical corrections, philological suggestions and architecture critiques are welcome for discussion. **Licensing:** Original documentation, specifications and editorial tables are available under **CC BY 4.0** (see [LICENSE](LICENSE)); source code and code examples under **MIT** (see [LICENSE-CODE](LICENSE-CODE)). Third-party quotations and linked sources remain under their own terms. Credit the project and indicate changes when adapting documentation.

---

*Machina Latina is a thought experiment about technical path dependence: not merely different words on identical computers, but different computers shaped by different words.*
