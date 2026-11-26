# STEMMA R1 — Distributed Source Genealogy
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional 2008–2012 design. A paper object model, not a running version-control system, complete hash suite, or historical release. The name is provisional.

## Motivation
Archives must retain actual CVL/COS source bytes; Latin A and Greek Α are different identities. Scientific code must be traceable independently of the CPU and ABI used to build it. Drawing on MODVLA external records and NODVS revisions, STEMMA stores immutable typed objects and a directed acyclic revision graph. NODVS documents are not the repository transport or executable source.

## Candidate object model
An object reference is (suite u16, digest 32 octets), 34 octets. R1 reserves suite 0001 for a future specified 256-bit digest function; no digest algorithm or cryptographic strength claim is assigned yet. References from other suites cannot silently compare equal. The canonical preimage is magic D7 53 54 01, type u8, three zero octets, body length u64 big-endian, then exact body. Limit body to 16 MiB in this small profile. A conforming future suite must define the digest over the entire preimage, including type and length; never hash just displayed text. Verify type, length and digest before accepting an object; conflicting bytes for an identical reference are an integrity incident, not a deduplication success. This contract defines preimages, not actual hashes.

| Type | Name | Body |
| --- | --- | --- |
| 01 | MATERIA | exact original file octets, including binary or empty content |
| 02 | ACTA | directory snapshot as below |
| 03 | EDITIO | revision with ordered parents and snapshot |

All integers big-endian. ACTA begins with entry count u16. Each entry has kind u8 (1 file, 2 directory), name length u16 in CIDs (1..63), name in C24 (3 octets per CID), codec u8, registry u16, object reference (34 octets). Names use the repository's declared COS release, exact CID identity, and are ordered lexicographically by unsigned CID sequence. Reject duplicate names, slash, NUL/control identities, dot/dot-dot, unassigned CIDs and cycles. Name registry fixed by external repository profile; no implicit Unicode normalization. A directory entry must have codec/registry zero; file codec 0 means opaque bytes and registry zero, 1 CVL-68/RC1-L with registry zero, 2 W1, 3 C24 with declared nonzero COS release. A file with text declaration must validate before semantic display; invalid historical bytes may be preserved as opaque with separately documented provenance. CVL data may contain Greek without changing file bytes. No symlinks, executable bits or native pathname assumption. A checkout to an OS that cannot represent distinct names losslessly must reject or use an explicit reversible export mapping, never overwrite one name with a visually similar one.

EDITIO body: root ACTA ref (34), parent count u8 (0..2), that many ordered EDITIO refs (34 each, no duplicates), author ID u64 nonzero (self-declared, not proof), logical time u64 (author claim, not authoritative clock), message registry u16, message length u16 in CIDs, C24 message. Require assigned message identities, no trailing bytes; zero-length message allowed. First parent is previous line of development, second is merged line. Root revision has zero parents. Validate reachable types, sizes and graph acyclicity, subject to explicit resource limits. A revision ID changes when any bound bytes change; identical source file bytes may share MATERIA while revisions differ. Author claims require separate signatures to authenticate.

## Paper vector
MATERIA containing the five CVL bytes SALVE has a 16-octet header plus 5-octet body:
    D7 53 54 01 01 00 00 00 00 00 00 00 00 00 00 05
    52 41 4B 54 45
Total 21 octets. Re-encoding these five letters as C24 produces 15 body octets and a different preimage. Merely rendering the same word does not establish source identity. No digest fixture claimed before suite definition.

## Collaboration
A local repository stores reachable objects and mutable named heads. A head name is a local alias, not immutable identity. Copying a repository brings objects and selected heads; divergent edits can create revisions offline. Fast-forward only when expected current head equals the supplied old reference and is an ancestor of proposed new head. Divergence requires explicit merge (two parents, reviewed new root), or publication on another head. No automatic conflict resolution, rename detection or history rewriting semantics mandated. A public forge may protect heads or refuse a proposed update; authority to change a head is separate from ability to compute a revision reference.

## Boundaries
Storage compression, delta format, transport, signatures, directory mapping, diff/merge algorithms, access control and hash suite are open. A content graph is not proof of authorship, availability, legal rights or secure execution. An independent repository mirror can preserve objects without a particular forge. See [FASCICVLVS](FASCICVLVS-R1.md), [history](../docs/de-codicibus-2005-2026.md).
