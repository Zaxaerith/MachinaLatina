# CVL-63/TP1 — Seven-Unit Transmission with Six-Bit Characters
## 1963 年通信传输配置：六位数据＋一位偶校验

> **Status: DRAFT / RECOMMENDED RESEARCH PATH, NOT CANON.** Fictional 1963 communication-engineering proposal, authored in 2026. This is a **seven-bit transmission unit**, NOT an independent 128-character alphabet and NOT a replacement for the CVL-54 six-bit character code. It does not freeze CVL-54/P0, CVL-68/RC1 or a complete line/physical-tape protocol.

## Design verdict

**Recommend CVL-63 as a telecom transport profile ("TP1") for the six-bit dual-page CVL-54 family**, rather than an independent 7-bit character standard.

This is more defensible than inventing a third complete codebook solely because the real world had ASCII. For this timeline, the main pressure from 1954 to 1963 comes from accumulated scientific data and teletype line reliability; the genuine *character-identity break* waits for direct eight-bit CVL-68 in the late 1960s.

A distinct seven-bit two-page alphabet (the original Candidate A) is technically possible but would make legacy translation and serial-terminal compatibility more expensive without solving the fundamental shift-state problem. This is a **worldbuilding recommendation**, not a proof that a seven-bit alphabet is impossible.

## Three different meanings of "seven bits"

1. **Seven-bit character code:** 128 independent numeric values may be assigned to characters and controls. This is what actual ASCII historically became.
2. **Seven-bit transmission unit with parity:** **six existing source data bits** plus **one check bit**. It still carries just 64 underlying CVL-54 code values; the other 64 seven-bit combinations are **invalid parity words**, not new characters.
3. **Seven tracks on magnetic tape:** physically separate parallel tracks, which in real historical equipment could hold six information tracks plus one parity track. It is a useful analogy, but not the same physical interface as a seven-bit serial line.

CVL-63/TP1 adopts (2). It could plausibly be used with either seven-track media or serial links, **but their actual track ordering, serial framing and timing remain unspecified here**.

## Logical TP1 symbol (review profile)

Let c be an integer in 0..63, representing one unmodified CVL-54/P0 code unit. Compute even-parity bit p = popcount(c) modulo 2. Define the seven-bit transmitted slot:

    t = (p << 6) | c

A receiver must check popcount(t) modulo 2 == 0. If not, it marks the slot corrupt and rejects the containing **strict TP1 record**. Only after the parity check is the underlying six-bit c = t & 0x3F passed to the existing CVL-54/P0 page-state decoder.

The seventh bit therefore provides **error detection** for an odd number of bit flips in one slot (not only a single flip). It CANNOT detect an even number of bit flips, cannot repair missing/duplicated whole slots, and cannot recover a lost Latin/Greek shift command. These limitations are central to the later eight-bit direct-code movement.

| Original CVL-54/P0 c | Meaning at decoder state | Even-parity TP1 slot t (seven-bit binary) | Editorial hex |
| --- | --- | --- | --- |
| 01 octal | Latin A or Greek Α, depends on page | 1000001 | 41 |
| 22 octal | Latin S or Greek Σ, depends on page | 0010010 | 12 |
| 61 octal | SHIFT-GRC (state change) | 1110001 | 71 |
| 43 octal | SPACE (both pages) | 1100011 | 63 |

Hex values here are **editorial representations of seven-bit slots**; they are NOT byte codes in an eight-bit document and have NO ASCII/CVL-68 character meaning. For example, the slot 41 carries six-bit value 01 and is interpreted according to the current page, not necessarily Latin A.

## Record contract (TP1 logical layer)

A TP1 "record" is a finite, explicitly framed sequence of 7-bit units, declared as \`CVL-63/TP1 + CVL-54/P0\` with a known unit count and record boundary. A line controller may encode the record count/boundaries physically in different ways: **TP1 has not yet defined their wire representation**. Therefore this is not yet a complete interoperable serial-frame protocol.

1. At a **declared new logical record**, initialize the CVL-54 page state to LATINA.
2. Read exactly the declared number N of TP1 slots in order. N counts transmitted six-bit units, including SHIFT and optional EOT, not rendered letters.
3. Verify even parity for **each** slot before CVL-54 interpretation. A strict buffered gateway should not publish a partially decoded record after encountering any parity failure.
4. SHIFT-LAT (CVL-54/P0 code 60 octal) and SHIFT-GRC (61 octal) change page; neither is a printed character. State persists **inside** the record, including across any reconstructed 36-bit word boundary.
5. A logical EOT (64 octal) MAY be present as the last meaningful source unit. If present, it ends the text and resets to LATINA; later meaningful units in the same TP1 record are invalid.
6. The TP1 transmission stream deliberately **omits source 36-bit end-word PAD**. The source record's exact PAD count, EOT presence and original word framing need a sidecar if bit-perfect archive restoration is required.
7. The *out-of-band frame end* closes a record and resets page state regardless of whether an explicit CVL-54 EOT was present. It does not itself encode a printable newline.
8. If a frame is truncated, loses a full slot, fails any slot parity check, or has unknown initial page/record boundary, a strict decoder reports an invalid record and does **not** repair it by guessing shift positions or transliterating Greek to Latin.

**Engineering warning:** a real mechanical terminal that already printed characters cannot undo marks on paper after a later parity failure. The "reject before publishing" rule applies to buffered archive/network gateways, not to instant ink printing.

### Physical framing deliberately left open

Serial bit ordering, start/stop timing, electrical signal levels, tape track orientation, frame delimiters, retransmission/acknowledgment, checksums, maximum record length and signal rates still require independent link profiles. The logical profile's explicit record boundary is a **contract requirement**, not a claim that this document defines physical flag sequences.

A future TP1-F (framing) profile should solve these details. Do not fabricate 1963 hardware interoperability merely because seven-bit payload words are specified.

## Worked cross-era vector — SALVE ΛΟΓΟΣ

Two CVL-54/P0 36-bit words, **exactly as previously published**:

    220113240543  (octal)   = SALVE + SPACE (Latin page)
    611317031722  (octal)   = SHIFT-GRC + ΛΟΓΟΣ

Unpacked CVL-54 units (octal):

    22 01 13 24 05 43 | 61 13 17 03 17 22

TP1 seven-bit slots (editorial hex notation):

    12 41 4B 14 05 63 | 71 4B 0F 03 0F 12

There are **12 six-bit source units** and **12 transmitted seven-bit units**: 72 payload bits expand to 84 TP1 bit positions (**+16⅔%** before serial start/stop and record framing). The Greek SHIFT consumes a whole slot and prints nothing.

The **abstract decoded text** is SALVE ΛΟΓΟΣ. Under the separate 1968 CVL-68/RC1 *candidate* encoding it becomes the 11 direct byte values:

    52 41 4B 54 45 20 8A 8E 82 8E 91

Those are 88 data bits (11 × 8) before framing. **Do not claim a simple 6→7→8 byte reinterpretation**. A CVL-63/TP1 receiver first removes/checks parity, then decodes CVL-54/P0 page state, then maps abstract character identity to CVL-68.

## Damage examples and limits

- Clean SHIFT-GRC c=61 octal = 49 decimal → TP1 t=71 hex. Flip *one* parity bit: 71 → 31. The received slot has odd parity and MUST be rejected; the decoder must not proceed under a guessed language page.
- Flip *two* bits: 71 → 72. The resulting slot still has even parity, but c changes from 49 (SHIFT-GRC) to 50 (LF). Parity **will not detect this corruption**. A later checksum, link-level retransmission, physical error correction, or application check could help, but **none is present in TP1 alone**.
- Drop the entire SHIFT-GRC unit. Surviving units can have individually valid parity; the decoder will interpret later Greek letter codes under the wrong page. Record length/framing may detect missing unit counts, but if a different unit is duplicated or a coordinated error preserves count, the text can remain wrong.

This is a **parity-protected six-bit encoding**, not a stateless Greek/Latin direct text code.

## What TP1 does and does not preserve

| Property | Transport result |
| --- | --- |
| Six-bit code unit values | Exact, once parity passes |
| Latin/Greek character identity | Exact only with known CVL-54 page state and source profile |
| Input record boundaries | Preserved if external framing is intact |
| Original XXXVI machine-word grouping | Reconstructible only with separately specified packing and padding metadata |
| Original bit-identical magnetic tape | **Not guaranteed**: PAD, gaps, EOT choices, and physical layout can differ |
| Polytonic accents/lowercase not in CVL-54/P0 | **Cannot recover** |
| Future 1968 direct eight-bit text | Requires explicit decode + re-encode |
| All possible transmission errors | **Not detected** |

## Historical comparison, NOT a fictional standards citation

Real IBM seven-track tape used six data tracks and an additional parity track (see [IBM seven-track documentation](https://www.ibm.com/docs/en/zos/2.5.0?topic=characteristics-seven-track-tapes)); actual ITA2 teleprinters used shift states to share narrow character codes (see [ITA2](https://www.itu.int/rec/T-REC-S.1)). Real seven-bit ASCII was standardized in 1963 (see [NIST historical note](https://www.govinfo.gov/content/pkg/GOVPUB-C13-53e3b5dd0c4980c979cc8bc581eb642c/pdf/GOVPUB-C13-53e3b5dd0c4980c979cc8bc581eb642c.pdf)). These are **three distinct real technical ideas**. They do not jointly establish that a fictional historical seven-bit parity line existed.

See [legacy CVL-63 candidate comparisons](CVL-63.md), [CVL-54/P0 source page](CVL-54-P0.md), [conversion ledger](../docs/cvl63-transport-migration-ledger.md), [1963–1968 history](../docs/de-transmissione-codicum-1963-1968.md) and [CVL-68/RC1](CVL-68-RC1.md).
