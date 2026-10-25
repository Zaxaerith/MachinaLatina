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
| [Historical sources / 史实依据](docs/historical-sources.md) | Verifiable reality used to constrain the counterfactual |
| [Roadmap / 路线图](docs/roadmap.md) | Documentary milestones before any emulator or compiler |

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

**2026-10-25 — founding documentation, pre-implementation.** All CVL mappings are **experimental drafts**. The hexadecimal entries are design proposals for the fictional world, not statements about actual ASCII, EBCDIC or Unicode. No binary compatibility is promised between CVL revisions.

### A small thought experiment

A 36-bit machine word holds six six-bit character *codes*:  
`6 characters × 6 bits = 36 bits`.

In the fictional six-bit encoding, the Latin inscription `VERBVM` can occupy one word. In this world, too, `verbum` could become a technical term for a machine word.

## Contributions and licensing

Historical corrections, philological suggestions and architecture critiques are welcome for discussion. A project-wide license has **not yet been selected**; public visibility alone does not grant a blanket reuse license. Please discuss substantial external contributions before submitting.

---

*Machina Latina is a thought experiment about technical path dependence: not merely different words on identical computers, but different computers shaped by different words.*
