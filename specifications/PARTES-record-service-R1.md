# PARTES Record Service R1 — Scientific Records Without Native Memory Images
> DRAFT / NOT CANON · 2026-11-26. One read-only paper service over [PARTES I IPC](PARTES-I-R1.md). No storage engine, implementation or deployed registry.

## Service contract
Bootstrap grants a read endpoint to authorized clients. Service uses its own configured per-PID object access table, not a PID claimed in payload. Request schema 00000001, revision 0001, operation 0001 (GET); body exactly 12 octets: nonzero u64 object ID then nonzero u32 immutable revision. Object identity is scoped to this service instance's stable archive namespace, not a RETE authority or process handle. GET returns the exact requested edition, not latest. Service has preloaded immutable records; no writes, namespace traversal or persistent on-disk layout. Service status 1 invalid schema/operation/body, 2 not accessible (covers absent or denied), 3 unavailable edition, 4 corrupt record; errors have empty body. Access check precedes edition disclosure.

Success body = same object ID and revision (12 octets), followed by the six-octet SPECIMEN external representation from [MODVLA](MODVLA-I-R1.md): NAT16 IDENTITAS, NAT8 NOTA, NAT24 NVMERVS, high-first. Schema ID/revision/op define representation; no raw native address or padding. Units and floating-point format are not implicit; this schema has only integers. A later F48 measurement schema must explicitly define numeric profile, units, coordinate reference and provenance, with RATIO acceptance separately documented. COS/NODVS document services similarly declare codec/registry in their own schemas, not a universal kernel text decoder.

## Paper vector
Client requests object 2 revision 1 with tag 7 (all hex).
Request header (24):
    00 00 00 01 00 01 00 01 00 00 00 07
    00 00 00 0C 00 00 00 00 00 00 00 00
Request body (12):
    00 00 00 00 00 00 00 02 00 00 00 01
Total 36 octets = six S2 words.
Response header (24):
    00 00 00 01 00 01 00 01 00 00 00 07
    00 00 00 12 00 00 00 00 00 00 00 00
Response body (18):
    00 00 00 00 00 00 00 02 00 00 00 01
    12 34 A5 01 02 03
Total 42 octets = seven S2 words. Client decodes 4660,165,66051, independent of native structure layout. Baseline logical copy volume 2*(36+42)=156 octets. Header + object identity overhead is substantial for a six-octet record; bulk arrays require later batching/shared-buffer research. No execution or benchmark.

## Migration
Sextaria and Nova can exchange the exact schema octets, although they require different native ABI, pointer types and kernel implementations. A possible early Nova port uses M32 PROTECT hardware with a separate IPC syscall ABI; M64 hardware protection is not yet defined. Preserve original six-octet F48 archives even where later CPUs use different floating-point hardware. Neither a record schema nor a process message is itself the RETE network protocol. Remote access requires authentication, transport, authorization and network framing outside this profile.
