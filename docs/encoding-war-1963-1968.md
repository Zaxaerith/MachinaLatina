# Controversia Codicum (1963–1968) / 双文字编码之争

> **Status: DRAFT NARRATIVE · fictional historiography / 架空历史叙事草案**  
> The people, committees, debates, document titles and institutional positions below are invented. **No quotations are attributed to real historical figures.** The engineering constraints are informed by real-world history, with references at the end.

## The historical problem in this world / 争论的起点

The scientific community of Machina Latina writes ordinary administration in a continuing Classical Latin tradition, while Greek remains prestigious in mathematics and learned discourse. Scientists want to type `Α`, `α`, `π`, `λόγος` and Latin prose **within the same electronic document** without changing alphabets by hand or losing information.

By the early 1960s, three incompatible ecosystems have emerged:

| Fictional faction | Existing investment | Principal argument |
| --- | --- | --- |
| **Officinae Telegraphicae** — telecommunication operators | Narrow links, teleprinters, terminals using shifts | “Why replace functioning transmission gear merely for a larger character alphabet?” |
| **Collegium Machinarum** — legacy large-computer vendors | Six-bit packed records on 36-bit words; archived programs and tapes | “A new byte standard must not orphan scientific and government records.” |
| **Consortium Scientiarum** — universities and emerging manufacturers | Mixed-script textbooks, scientific libraries, printers | “Greek is not a decorative font. It must be addressable text.” |

These names are **fictional placeholders**, not attested institutions.

## The engineering argument / 算术不是政治立场

A direct representation of the *basic* upper- and lower-case alphabets needs:

- Latin 23 × 2 = **46** character codes;
- Greek 24 × 2 = **48** character codes;
- decimal digits = **10**;
- subtotal = **104 codes**, **before** spacing, punctuation, diacritics and controls.

A 7-bit code has 128 positions. **In abstract arithmetic, 104 fits into 128**. The difficulty arises once terminal, printing and communication controls are included: with 32 low controls and DEL, the budget is already 137 (104 + 33), *before even adding space and punctuation*. The conclusion is not that seven bits are mathematically incapable of representing both alphabets; it is that **seven-bit direct mixed-script, fully functional terminal text is an impractical mainline choice under these assumed control and typography requirements**.

An 8-bit byte has 256 possible values and room for direct Latin and Greek glyphs, controls, and a provisional set of combining marks.

### Cost of the eighth bit

| Transition | Raw data bits per character | Change for equal code-unit count |
| --- | ---: | --- |
| six → eight | 6 → 8 | **+33⅓%** |
| seven → eight | 7 → 8 | **+14²⁄₇%** (≈14.29%) |

These are **logical raw-bit comparisons**, not actual memory or network cost measurements. Physical line framing, padding, parity, compression, tape format and shift codes can make operational costs differ substantially.

## A possible chronology / 一段可能发生的虚构历史

### 1963: The interim compromise

A telecom-led standard, provisionally called CVL-63, retains stateful Latin/Greek presentation or a transmission translation profile. It meets immediate communication needs but remains troublesome for mixed-script random access.

**Decision still open:** Is CVL-63 a genuinely new seven-bit shift-coded character set, or merely a transmission convention for CVL-54 data? Do not write its specification as though this has already been decided.

### 1964–1966: The byte argument becomes economic

Byte-addressable processor families and terminals become more attractive in this world's industry, for the same general reasons real architectures sought compatible machine families and flexible data processing. Mixed-script scientific printing and text search create additional demand beyond alphabetic capacity alone.

No claim is made that the fictional vendors are IBM or that System/360 must exist identically in this world.

### 1967: The split over backward compatibility

The legacy faction proposes keeping six-bit tapes and encoding Greek shifts inside records. The university faction objects: searching for a Greek symbol in an arbitrary substring requires reconstructing the shift state from the beginning of a record or checkpoint. A lost shift can corrupt later letters without damaging their raw code values.

Some designers favor an escape-based hybrid to preserve narrow lines; others want a direct eight-bit machine alphabet and gateway transcoders for existing communications networks.

### 1968: CVL-68 adopted in the mainline

**CANON direction already adopted in this project:** CVL-68 becomes the preferred *native direct 8-bit* script encoding. The fictional standard may initially coexist with older six- and seven-bit links; those links need not vanish overnight.

CVL-68's **exact 256-entry mapping is still DRAFT**, and adoption does not make the old tapes disappear.

### The long shadow: 1970s–1990s

Old archives, embedded controllers, terminal gateways, scientific code and government registries remain hybrid for decades. A future international multilingual standard must supersede CVL-68's restricted repertoire without erasing existing byte sequences.

## A representative failure / 模拟故障

Imagine a legacy stream whose code `001011` means Latin `L` when LATINA is active but a Greek letter when GRAECA is active. These code assignments are **illustrative only**; CVL-54 has no frozen numeric table. If a shift-to-GRAECA code is dropped in transmission, subsequent six-bit data remain syntactically present yet decode under the wrong alphabet until state is restored.

A modern direct eight-bit encoding removes **alphabet shift-state errors in ordinary text**; it does not magically prevent bit corruption or solve font and normalisation problems.

## What is not yet canon / 尚未确定

- The membership, geography and institutional authority of the standards committee.
- The year and design details of any actual interim CVL-63 format.
- Which industrial group gets to name the standard, and how Greek scholars influence official orthography.
- A single winning strategy for 7-bit telecom gateways: escapes, transcoding or parallel networks.
- Whether the first CVL-68 printers support correct polytonic stacking in hardware or via software overstrikes.

## Historical anchors / 现实参考

- [IBM, *The IBM System/360*](https://www.ibm.com/history/system-360) — introduced in April 1964; standardized compatibility and helped establish the eight-bit byte.
- [ASCII, X3.4-1967 scanned standard](https://www.sensitiveresearch.com/Archive/CharCodeHist/Files/CODES%20standards%20documents%20ASCII%20Sean%20Leonard%20Oct%202015/ASCII%2068%2C%20X3.4-1967.pdf) — demonstrates the actual seven-bit standard's controls and printing repertoire. Historical ASCII's 1963 control assignments were not identical to 1967's.
- [ITA2/Baudot historical shift scheme](https://www.prc68.com/I/Baudot_ITA2_Simulator.html) — real five-bit letter/figure shift behavior as an analogy, **not a claim that the real telegraph code used Latin/Greek pages**.
- [Unicode Greek FAQ](https://www.unicode.org/faq/greek.html) — modern discussion of Greek combining marks and final sigma, used to formulate design questions, **not retroactively credited to the fictional engineers**.

*Controversia Codicum is a research scenario, not an assertion of what would inevitably occur under a Latin-speaking civilization.*
