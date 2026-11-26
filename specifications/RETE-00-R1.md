# RETE-00/R1 — Record-Oriented Resource Exchange

> **DRAFT / NOT CANON · 2026-11-24.** A small application-layer protocol candidate, not a transport, name resolver, TLS replacement, deployed HTTP competitor or functioning server.

## 1. Preconditions

RETE uses an externally established reliable ordered octet stream with a known initial frame boundary and an independently resolved authority. Its transport addressing, security handshake and directory are outside R1. On an unauthenticated channel, a numeric authority ID does not prove the peer owns it. Production confidential or authenticated retrieval requires an independently specified secure transport; R1 alone provides no confidentiality, integrity protection or authentication against a malicious peer.

All integers big-endian. One outstanding request per connection, no pipelining. Read exact frame sizes, validate bounds and close on malformed or unexpected frames. No scan for magic after desynchronization; payload bytes may contain the same signature. No retry after malformed data on the same connection. No compression, streaming partial response, server push, mutation, credentials or cookies.

## 2. Frame header (16 octets)

| Offset | Size | Meaning |
| ---: | ---: | --- |
| 0 | 4 | Numeric magic D7 52 45 01 |
| 4 | 1 | Version 01 |
| 5 | 1 | Operation 01 FETCH / 81 RESULT |
| 6 | 2 | Flags zero |
| 8 | 4 | Nonzero request ID, echoed by RESULT; no reuse on one connection |
| 12 | 4 | Payload length (excludes frame header), max 16,777,220 octets |

Unknown version, opcode or flags close connection. An externally known new connection starts with a new request-ID space. Magic values are not Latin or ASCII tokens.

## 3. FETCH payload (24 octets)

| Offset | Size | Meaning |
| ---: | ---: | --- |
| 0 | 8 | Nonzero target authority |
| 8 | 8 | Nonzero target resource |
| 16 | 4 | Desired revision, zero = latest |
| 20 | 1 | Accepted codecs bit 0 W1, bit 1 C24; at least one, all other bits zero |
| 21 | 3 | Reserved zero |

FETCH asks for a complete NODVS document, even if LIGAMEN ultimately selects a record. The receiver selects an accepted codec, preferring W1 when both are possible (candidate policy). Registry version is declared in the returned document; R1 does not negotiate installed registry releases. Unsupported release produces a client diagnostic, never guesses. A request to the wrong authority receives error status; redirects and authority transfers remain out of scope.

## 4. RESULT payload

First 4 octets: status u16, reserved u16 zero. Status 0000 = success, followed by exactly one complete NODVS document; status 0001 unknown resource, 0002 unavailable revision, 0003 unsupported codec, 0004 access denied, 0005 wrong authority, 0006 server limit; errors have exactly four octets total. Unknown status invalid in R1.

A successful response must echo the request ID, return the requested resource and requested nonzero revision (or an actual nonzero revision when latest was requested), use an accepted codec and belong to the requested serving authority as established externally. The document size equals RESULT payload length minus four. All other inconsistencies reject the response. No response can be accepted just because its text decodes.

## 5. Caching and revisions

Cache by authority, resource, resolved nonzero revision, codec and registry release; maintain access-context partitioning if authenticated channels are added. Only cache immutable revisions whose source authority and semantics can be trusted. A request for latest must contact the server in R1, because no freshness/validation metadata exists. A cached revision does not prove current access authorization; private caching policy remains to be specified. No global content-addressed equivalence is claimed.

## 6. Next work

Directory allocation and secure authority resolution; international labels; secure transport and content integrity; version/repertoire negotiation; partial retrieval and large attachment support; dynamic requests and SERMO; caching freshness. R1 intentionally remains small enough to reason about using paper vectors.

Related: [NODVS](NODVS-98-R1.md), [LIGAMEN](LIGAMEN-99-R1.md), [worked example and fictional history](../docs/nodvs-rete-1998-2005.md).

## Phase XLII future scenario

[CONCORDIA task federation R1](CONCORDIA-task-federation-R1.md) and [personal computing study](CONCORDIA-personal-computing-study.md) propose a separate future coordination layer. No existing protocol, native ABI, device permission or local task contract is changed; remote trust and durable reconciliation remain open.
