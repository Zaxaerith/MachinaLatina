# CVL-54 → CVL-68 Migration / 六位到八位字符迁移

> **Status: DRAFT MIGRATION CONTRACT · fictional**  
> No normative 64-entry CVL-54 page table exists yet. This document specifies constraints and a candidate algorithm, **not a completed byte-perfect transcoder**.

## Scope

CVL-54: **six-bit code units** packed into **36-bit machine words**, interpreted under an active LATINA or GRAECA page.

CVL-68: **eight-bit direct code units**, proposed Latin and Greek identities without changing alphabet pages, with optional combining marks.

Converting the *data format* requires a real transcode. The fact that a fictional old and new standard use familiar letters does not justify reinterpreting the bits.

## Logical decode → encode pipeline

```text
CVL-54 word/tape records (6-bit packed; stateful)
    |
    v
Unpack six 6-bit codes per 36-bit word
    |
    v
Decode with correct initial page and shift-state rules
    |
    v
Abstract character stream (Latin, Greek, digits, symbols)
    |       + conversion diagnostics + source record metadata
    v
Map characters to CVL-68 bytes and validate mark profile
    |
    v
CVL-68 8-bit text records + migration report
```

### Provisional physical packing

For a 36-bit unsigned word `W`, the candidate *most-significant-first* layout extracts:

`c[i] = (W >> (30 - 6*i)) & 0x3F`, for `i = 0…5`.

This is **not yet CVL-54 CANON**. Word endianness, tape framing, record padding, bit significance, and shift-state reset points must be defined independently. A shift symbol consumes a six-bit slot but produces **no visible text character**.

### State-machine decode pseudocode (illustrative)

```text
page = LATINA    // assumed at explicit record boundary; not yet standard
for each 6-bit symbol in physical order:
    if symbol == SHIFT_LAT: page = LATINA
    else if symbol == SHIFT_GRC: page = GRAECA
    else if symbol == PAD: apply padding policy
    else:
        character = lookup(CVL54_table[page], symbol)
        if character is undefined: report error with record and offset
        else: emit character
for each decoded character:
    if CVL68 has a mapping: emit mapped byte(s)
    else: report nonrepresentable character; stop or use declared escape mode
```

**Never guess** the current page when a record begins midway through a stream. When page state is unknown, the converter must either reject or require an explicit state/checkpoint. Do not reinterpret misdecoding as Greek-to-Latin transliteration.

## Three different meanings of “round-trip”

| Promise | Can the migration guarantee it? | Reason |
| --- | --- | --- |
| **Same decoded characters, 54 → 68** | In principle for the defined shared repertoire | Must know the full old tables, page state and new mapping |
| **Same decoded characters, 54 → 68 → 54** | Only for characters representable in both, under an agreed canonical re-encoding | Case, diacritics and late additions may be unrepresentable in CVL-54 |
| **Byte/bit-identical original CVL-54 after 54 → 68 → 54** | **No general guarantee** | Redundant shifts, padding, record layout and tape framing are lost in text transcoding |

To preserve exact original records, **retain the original raw 36-bit data and conversion metadata**. A textual reconstruction cannot recover shifts or unused padding in general.

## Loss taxonomy / 信息损失分类

- **Unrepresentable source glyph:** a CVL-54 value has no CVL-68 target mapping; treat as conversion error unless a documented extension exists.
- **Unrecoverable diacritic:** printed or overstruck accents not encoded in the six-bit stream are not inferable from plain base letters.
- **Missing shift / damaged record:** subsequent page assignments may be uncertain.
- **Mixed-script visual ambiguity:** Latin `A` and Greek `Α` must not be conflated during transliteration.
- **Record boundaries / padding:** a 36-bit physical word boundary is not an 8-bit character boundary.
- **Character case:** uppercase-only legacy text must not be automatically assigned hypothetical lowercase original spelling.

## Conceptual sample

The six letters `VERBVM` can occupy one CVL-54 36-bit word **if** each letter has a valid code and a LATINA page is active. Because the legacy 6-bit values are **not frozen**, we provide **no invented packed word** here. Under the current non-normative CVL-68 ledger, the *decoded text* `VERBVM` would encode as:

`54 45 51 42 54 4C`

This example is about abstract **characters**, not bit-for-bit data conversion.

## Compatibility test plan (before implementation)

1. Freeze both six-bit page maps, shifts and record reset semantics.
2. Define binary packing with at least one known 36-bit hexadecimal word.
3. Test Latin-only, Greek-only and repeated switching.
4. Test reset boundaries, corrupt shifts, unknown starting page and truncated records.
5. Test at least one character legal in CVL-68 but not CVL-54 (expected rejection/loss report).
6. Establish textual round-trip and raw archival preservation as separate acceptance conditions.

## Historical engineering analogies

- ITA2 teleprinters used stateful letter/figure shifts (see [reference](https://www.prc68.com/I/Baudot_ITA2_Simulator.html)).
- IBM System/360's 1964 byte-oriented architecture illustrates why vendors might shift toward a new compatible family (see [IBM](https://www.ibm.com/history/system-360)).
- This fictional plan **does not** imply that real ITA2, IBM equipment or ASCII used CVL codes.
