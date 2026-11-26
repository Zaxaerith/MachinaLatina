# MENTIS — Scientific assistant evidence boundary R1
> DRAFT · 2026-11-26. Candidate 2022–2026 workflow contract; no model, working retrieval service, trust protocol or verification engine.

## Roles
Model proposes text, queries and calculations; a trusted host mediates tools under user/session grants. A generated citation does not grant retrieval rights or prove source existence. Documents are untrusted data, not executable instructions or new grants. CVSTOS TESSERA-like handles are local to their owning process/service and cannot be embedded as reusable authority in NODVS. Remote requests require future authenticated transport; RETE-00/R1 fetch is not a security handshake or write API.

## Logical evidence record
Each claim has a local claim ID, generated text, and zero or more separately typed evidence entries. A document entry binds LIGAMEN authority u64, resource u64, nonzero revision u32, record u32 (0 whole document), optional zero-based CID span within a selected text record, retrieval outcome, actual returned revision, source access context and retrieval time. Validate requested and returned identity and span; a latest request must pin the actual retrieved edition before citation. An unavailable or unauthorized source stays unverified; never replace it silently with another edition. No claim that a correct reference proves entailment or authenticity. A computation entry identifies inputs, units, tool/version, arithmetic contract, actual execution outcome and error/reference evidence if available. A review entry identifies responsible reviewer and accepted revision/scope; model cannot fabricate acceptance. No binary serialization or cryptographic attestation assigned.

| Status | Meaning |
| --- | --- |
| PROPOSITVM | Generated explanation/hypothesis, not independent evidence |
| REPERTVM | Source actually retrieved and identity/span checked, not proof of claim |
| CALCVLATVM | Tool actually executed with declared inputs/profile, not necessarily accepted |
| RECEPTVM | Explicit human review recorded for a particular result/revision |

These are distinct record types, not an automatic ladder: a claim can have a verified document and an unverified calculation, or be reviewed with stated limitations. Numeric tolerance acceptance and human review are different. Source retrieval, evaluation of support, numerical validation and publication all retain separate outcomes.

## Example workflow
A hypothetical survey researcher asks for the coordinate difference in the RATIO audit example. MENTIS may retrieve an authorized pinned NODVS record containing the source inputs (no real resource ID asserted), propose B-A, ask a calculation tool for a declared F32/F36 profile, then attach execution evidence and numerical tolerance result. Paper reasoning predicts F32 zero, F36 0.03125 m, with 0.01 m tolerance failing F32. Do not mark these paper predictions CALCVLATVM: no fictional tool was run. Measurement uncertainty and CRS remain distinct. Human acceptance cannot be inferred from a passing tolerance. A model reading user documents must not send them to a remote tool without separate permission; revocation cannot erase already disclosed copies.

See [RATIO audit](RATIO-numeric-audit-study.md), [LIGAMEN](LIGAMEN-99-R1.md), [CVSTOS](CVSTOS-I-R1.md), [prior AI evidence study](../docs/ai-provenance-and-numerics-2015-2026.md).

## Phase XXXVIII future scenario

[MENTIS agent task R1](MENTIS-agent-task-R1.md) and [system integration study](MENTIS-system-integration-study.md) propose later user-space contracts, not changes to this existing profile. No ambient authority, remote mutation protocol or native ABI is implied.
