# NODVS-98/R1 — Typed Hypertext Documents
## 1998—2005 年类型化网页的候选技术规范

> **DRAFT / REVIEW CANDIDATE / NOT CANON · 2026-11-24.** All names, historical dates and byte contracts below are editorial proposals, not deployed historical products. This is a bounded base document format, not a complete browser, layout engine, scripting runtime or world-character registry. COS-97/R1 is itself a candidate.

## 1. Why records?

TABVLA scientific publishing and older record-oriented computing offer a plausible alternative to a markup-first web. Each document contains ordered typed records. Text bytes are not executable markup. A reader can show titles, paragraphs and links without interpreting a scientific attachment. A document editor is not required to expose the wire representation as its authoring language.

A late-1990s implementation would pay for parsing, indexing and editing tools; plain text markup remains a competitive alternative. No claim that typed records necessarily win worldwide.

## 2. Binary conventions

All integers are unsigned, big-endian octets, independent of Nova/Sextaria memory ABI. Hexadecimal constants below are numeric wire values, not ASCII, CVL or COS spellings. No implicit alignment, padding, terminators, compression or byte-order mark. The document's length includes the header. Maximum total length 16,777,216 octets (16 MiB); at most 65,535 records. Read exact lengths, check bounds before addition/allocation, reject truncation or trailing bytes. Implementations may impose lower disclosed resource limits.

## 3. Header (28 octets)

| Offset | Size | Meaning |
| ---: | ---: | --- |
| 0 | 4 | Magic D7 4E 44 01 (numeric signature for this format/version) |
| 4 | 1 | Text codec: 01 COS/W1-R1, 02 COS/C24-R1 |
| 5 | 1 | Flags, zero in R1 |
| 6 | 2 | Registry release ID: 0000 invalid, FFFF sandbox only, other values require a published release mapping |
| 8 | 8 | Resource ID within serving authority, nonzero |
| 16 | 4 | Document revision, nonzero |
| 20 | 4 | Entire document length in octets |
| 24 | 2 | Number of records |
| 26 | 2 | Reserved, zero |

The serving authority is provided by the containing RETE response or explicit archive metadata. A local file path is not an authority. A naked NODVS file does not authenticate the origin of its ID. Resource ID and revision must agree with the request/response context. FFFF registry is permitted only in the paper sandbox, never ordinary production interchange. No release IDs have yet been approved.

## 4. Record header (12 octets)

| Offset | Size | Meaning |
| ---: | ---: | --- |
| 0 | 1 | Type |
| 1 | 1 | Flags: bit 0 = critical; bits 1–7 zero |
| 2 | 2 | Reserved, zero |
| 4 | 4 | Nonzero record ID, unique within this document revision |
| 8 | 4 | Payload length in octets (not character count) |

Records occur consecutively, no padding. Type 00 is invalid. All IDs are unique including unknown optional records. Exactly the declared count must consume exactly the declared document length. Known types require their designated flags. Unknown critical types prevent rendering a validated document; unknown optional types may be skipped by length, with an explicit unsupported-content notice. Editors must preserve unknown optional records and their position/ID byte-for-byte when round-tripping or refuse a lossless edit. Skipping does not authorize deletion.

| Type | Flags | Name | Payload |
| --- | --- | --- | --- |
| 01 | 01 | TITVLVS | nonempty encoded title text |
| 02 | 01 | PARAGRAPHVS | nonempty encoded paragraph text |
| 03 | 01 | LIGAMEN | fixed 36-octet link record, see LIGAMEN-99 |
| 04 | 00 | ANNEXVM | media kind u16, reserved u16=0, remaining opaque attachment bytes |
| 05 | 01 | CAPVT | heading level u8 (1–6), three zero bytes, nonempty encoded heading text |
| 06–FF | 00 or 01 | unassigned | governed by unknown-record rules |

Exactly one TITVLVS is required and is the first record. Remaining records are in presentation order; LIGAMEN records modify source spans, not visible paragraphs. A basic reader shows title, paragraphs and headings, link affordances and an attachment placeholder. Attachments remain downloadable only through explicit user action; no execution. Media kinds 0001 image, 0002 table, 0003 map data are illustrative type families, not complete internal image/table/GIS encodings. Unknown media stay opaque. Media payload standards, alternative text metadata and accessible rich layout need follow-up profiles.

## 5. Text processing

Decode each text payload from its first byte through its exact length with the header's COS codec/release. No raw delimiter scan, C-string termination or reset across a multibyte symbol. Reject malformed or unregistered identities under the declared registry. W1 payload bytes may equal punctuation, NUL or prefix bytes. This is why record lengths, not byte searches, locate the next record.

In this base profile the mapped HT/LF/CR identities are prohibited in title and headings; paragraphs permit HT and paired CR LF only. Other device/format control identities require an explicit future extension. Registry properties must distinguish controls from ordinary text. Codec validation is distinct from normalization or typography. Preserve exact CID order, with no automatic normalization; Greek P1 rules apply when converting legacy source, not to arbitrary COS scripts. Complete multilingual shaping, bidi, grapheme segmentation and font fallback remain external work.

## 6. Revision and rendering

Resource identity = (authority ID, resource ID); immutable logical revision = identity plus revision number. A server may serialize the same logical revision as W1 or C24. Identity sequence, ordered record IDs, types, flags and nontext payloads must remain equivalent; offsets in link records count CIDs rather than wire bytes. Different encodings produce different file lengths and cache representations. A content edit creates a new revision. Record IDs are revision-local; do not assume they survive edits.

No inline scripting, external font fetching, implicit network activity, styling language or interactive forms are defined by R1. No remote attachment is executed. A client should display only after complete structural/semantic validation, including links. Transport authentication and origin policy are separate issues.

Related: [LIGAMEN-99](LIGAMEN-99-R1.md), [RETE-00](RETE-00-R1.md), [COS-97/R1](COS-97-R1.md), [worked document](../docs/nodvs-rete-1998-2005.md).
