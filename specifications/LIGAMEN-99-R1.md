# LIGAMEN-99/R1 — Persistent Resource and Object References

> **DRAFT / NOT CANON · 2026-11-24.** Fictional reference layer for NODVS. No actual authority registry, resolver, domain algorithm or working browser exists.

## 1. Identity versus location

A resource key is (authority u64, resource u64), both nonzero. The authority number belongs to a future independent network directory, not a character code, domain spelling, IP address or cryptographic identity. Resource IDs are assigned by that authority and must not be reused for different logical resources. Moving a server does not change its resource key; moving responsibility to another authority requires a future authenticated alias/transfer mechanism. No such mechanism is defined here.

A revision u32 (nonzero) names an immutable logical document edition. Revision 0 in a request means latest available; it is not a stored edition. A target record ID u32 nonzero selects an object within a pinned edition; zero selects the whole document. R1 forbids nonzero target record with revision 0 to avoid silently pointing to a different object after edits.

## 2. Link record payload (36 octets)

Integers big-endian, no padding. NODVS record type 03.

| Offset | Size | Meaning |
| ---: | ---: | --- |
| 0 | 4 | Source text record ID |
| 4 | 4 | Source start CID index (zero-based) |
| 8 | 4 | Source span length in CIDs, nonzero |
| 12 | 8 | Target authority ID |
| 20 | 8 | Target resource ID |
| 28 | 4 | Target revision (0 = latest) |
| 32 | 4 | Target record ID (0 = whole document) |

Source must exist and be a title, paragraph or heading. For headings, the span excludes the heading metadata. Span must be within decoded CID length; reject integer overflow and overlapping source spans in one record. Record order is irrelevant to source lookup after parsing. R1 measures CIDs, not byte offsets or user-perceived grapheme clusters. Editors should avoid splitting a displayed cluster; complete language-specific segmentation is not yet standardized. A reader must not silently adjust offsets during normalization.

A missing destination is a broken link, not necessarily a corrupt source document. A malformed source reference is invalid. Clicking is an explicit request; merely opening a document does not retrieve every target. There is no automatic embedding or executable relationship. The client can present both the visible source span and numerical destination to avoid relying on ambiguous glyphs.

## 3. Why a revisioned object link?

A scientific citation can pin an exact document revision and table record, while a news portal can point to the latest whole document. This differs from requiring every citation to depend on a mutable path and HTML anchor. But stable IDs need a durable directory, publishers must preserve revisions, and archives may still lose resources. IDs do not guarantee persistence, authenticity, free access or truth.

International display labels and restricted resolver labels remain an independent naming specification. Latin A and Greek Α remain different COS identities, even if visually identical. No real Punycode or URI grammar is imported. A numeric diagnostic form such as authority 1 / resource 2 / revision 1 / record 0 is only human notation, not a standardized URL.

Related: [NODVS](NODVS-98-R1.md), [RETE](RETE-00-R1.md), [history and vectors](../docs/nodvs-rete-1998-2005.md).
