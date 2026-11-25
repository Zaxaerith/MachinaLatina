# MODVLA — Native Layouts, External Records and System Boundaries
## 数据表示与 ABI 候选研究

> DRAFT · 2026-11-25. The three native storage profiles here are hypothetical compiler choices, not actual machine ABI specifications. No change to XXXVI/P0, Nova-N1 or Sextaria-S0 ISA is made.

## 1. One record, three local representations

Use the logical SPECIMEN record from [MODVLA-I/R1](MODVLA-I-R1.md).

| Field | Logical type | Value (decimal) | External octets |
| --- | --- | ---: | --- |
| IDENTITAS | NAT16 | 4660 | 12 34 |
| NOTA | NAT8 | 165 | A5 |
| NVMERVS | NAT24 | 66051 | 01 02 03 |

The explicit external schema is six octets: 12 34 A5 01 02 03. This remains unchanged regardless of host architecture. The following are *proposed* native compiler layout strategies for addressable scalar fields (not the only possible choices).

| Target profile | Native field locations | Native total |
| --- | --- | --- |
| XXXVI-W | word offsets 0, 1, 2; zero-extended low bits of each 36-bit word | 3 words = 108 bits |
| Nova-B | byte offsets 0, 2, 4; NAT16 occupies 2 bytes, NAT8 1 byte, byte 3 padding, NAT24 in low 24 bits of 32-bit slot at 4 | 8 octets = 64 bits |
| Sextaria-H-W | word offsets 0, 1, 2; zero-extended low bits of each 48-bit word | 3 words = 144 bits |

Local initialized example (hex, each word fixed width):

    XXXVI-W:
    000001234 0000000A5 000010203
    Nova-B (zero padding in this illustrative initialized layout):
    12 34 A5 00 00 01 02 03
    Sextaria-H-W:
    000000001234 0000000000A5 000000010203

Nova native layout uses big-endian numeric storage, with the NAT24 slot's upper byte zero. The example fixes byte 3 to zero for reproducibility of the illustration, not a promise that arbitrary native padding is safe to transmit. XXXVI word displays use hex here for comparison (nine hex digits per 36-bit word); historical listings normally use octal. A compiler can choose tighter layouts or registers if its target ABI agrees. No estimate here measures actual RAM bandwidth or program speed.

**Packed external storage is different:** Nova stores the six external octets consecutively; the candidate Sextaria-H can pack them into one 48-bit word, high lane first (1234A5010203). For XXXVI a simple candidate archival buffer convention stores four octets per word in its low 32 bits (high four bits zero), most-significant octet first, zero-fill unused final lanes and keep the exact external octet count independently. The six-octet record becomes 01234A501 002030000 (two 36-bit words). These are *new proposed software packing rules*, not the CVL-54 six-character word format. They are not physical tape framing and cannot be inferred from an arbitrary XXXVI file. Other packing strategies are possible.

| Case | XXXVI | Nova | Sextaria-H |
| --- | --- | --- | --- |
| Unpacked native example | 108 bits | 64 bits | 144 bits |
| External payload held in proposed buffer | 72 stored bits | 48 bits | 48 bits |
| Abstract external record | 48 bits | 48 bits | 48 bits |

Counts exclude metadata, descriptors, allocation, checksums, physical record framing. The smaller packed form requires decoding and may be less convenient for updates. Native padding is never a wire field.

## 2. Address types

A portable reference cannot just be a NAT24 number. A proposed LOCVS(T) is a local typed reference, whose storage/representation is target-specific. An ordinary typed reference must designate a valid aligned T object while its lifetime remains valid; it may not be converted implicitly into an integer or external byte sequence. FENESTRA(T) is a conceptual base+element-count view with checked indexing; actual descriptor widths, lifetime enforcement and allocation policy remain undecided.

- XXXVI: architectural word address 15 bits; no octet load address in P0. A software octet cursor in the proposed buffer is (word address, lane 0..3); it is not a native pointer. The old six-bit CVL-54 word has its own distinct 0..5 symbol index.
- Nova: architectural address 24-bit byte address; 32-bit native word accesses require four-byte alignment. NAT8 accesses may use LEGB/PONB; this does not establish a call ABI.
- Sextaria-H: proposed word+lane(0..5) pair; address width and binary pointer encoding are still unknown. Lane 6 or 7 is invalid in a hypothetical 3-bit selector; this does not define a hardware register.

Pointer arithmetic counts declared elements, not the target's arbitrary byte or word unit. Before accessing a view, check the logical index and address calculation without wraparound. A reference into an expired object is invalid even if its old address is numerically within RAM. These requirements are design intent, not a claim of implemented borrow checking, GC, hardware memory protection or full memory safety.

## 3. Linking and crossing boundaries

A target build should record: module/interface revision, source encoding profile, ISA and revision, OS service API revision, native ABI revision, address/layout profile and relevant number representation. Binary linker accepts matching imports/exports only under compatible native ABI and target; interface version alone cannot establish binary compatibility. Physical stack layout, register convention, object relocations, exception machinery and executable loader remain independent open work.

Three different operations:

1. Local call: native ABI defined by target; logical signature is checked.
2. Cross-process service: encode declared external records into a validated message; no raw native pointers. Handles require authorization and scope.
3. Archive/file: use declared schema and source format, not native memory dumps. Version and length supplied by containing record/file profile; R1 SPECIMEN has no magic or frame header.

An opaque TESSERA service handle is not an address or a permission string. A host may mediate read/write/close operations under different OS interfaces. It does not establish actual kernel capabilities, authentication or authority across machines. Later profiles must specify handle lifetime, denial/error semantics, resource ownership and message framing.

## 4. Operating-system implications

ORDO-N can expose byte streams through a MODVLA adapter; PARTES can expose typed record services; CVSTOS can mediate access through constrained handles. A common interface can be implemented by all three without demanding the same filesystem, kernel, CPU or binary. A future module can export a data service for SERMO or RATIO without serializing native stack objects. This is a plausible lineage from the 1980s record controversy into later OS architecture, not a deployed ABI.

Related: [MODVLA I](MODVLA-I-R1.md), [OS families](operating-system-families-2005-2015.md), [SERMO](SERMO-I-R1.md).
