# MENTIS — System Integration and Personal Computing
> FUTURE SCENARIO / DRAFT · 2026-11-26. Candidate 2027–2030 architecture; no new kernel or deployed AI platform.

## 1. A layer above operating systems
Keep existing ORDO-N, PARTES and CVSTOS families. A host task broker, model worker, tool adapters and trusted task view are user-space/system-service components; no inference in privileged kernel. Host owns authority and effect enforcement; a model is replaceable, can fail, and has no ambient grants. The trusted view lets people use ordinary applications, inspect raw files/records and undo reversible operations independently of the assistant. A local model may operate offline under local scopes; remote models are optional separately authorized services, not a universal fallback.

| Family | Candidate integration | Native boundary |
| --- | --- | --- |
| ORDO-N | task service and ordinary app adapters | byte streams, files, processes; full modern storage/ABI absent |
| PARTES | typed record and calculation services | message/schema interfaces; Nova IPC port and shared buffers absent |
| CVSTOS | trusted document picker, TESSERA, foreground/background policy | per-installation identity and quotas; native mobile ABI/device isolation absent |

An application can expose versioned typed operations through a manifest with parameter and result schema, effect class, required resource scopes, resource limits, offline/remote status and user-facing name. A manifest is documentation, not a grant. Adapter registration/trust and canonical signing depend on later FASCICVLVS work. A text menu label is not a service identity. GUI automation is a fallback subject to the same authorization; never treat arbitrary screen content as trusted instructions. Prefer typed operations to brittle UI sequences.

## 2. TABVLA task workspace
Candidate 2029 desktop displays user goal, proposed plan, actual task state, resource grants, staged results and confirmed effects. Conventional windows remain available. Tasks can be minimized, cancelled or resumed only if state is retained and grant/deadline rechecked. A task log is not a global immutable surveillance archive: retention and deletion follow owner policy, and secrets are not included by default. Private artifacts and published revisions must be visibly distinct. Output text is not proof of completion.

## 3. A local/remote decision
Illustrative policy: local-only for selected private data unless the user grants a specific external destination and payload class; if no local capability exists, offer manual operation or request consent, never silently upload. A task can use a remote model for public planning and a local adapter for private data without sending private input to that model. The broker must also account for information derived from private data; no general noninterference guarantee. Model weights, personal memory, task state and permissions have separate identities. User may export and delete personal memory under a defined storage policy; deletion cannot erase previously transmitted copies. Long-lived grants and persistent scheduling require future consent, recovery and revocation contracts.

Illustrative capacity calculation: 8 billion parameters stored as tightly packed 4-bit values require 4,000,000,000 octets (about 3.73 GiB) for weights alone. Scale tables, activations, KV cache, allocator and runtime overhead add capacity; no inferred throughput, model quality or device fit. Such a weight encoding is an assumption, not a defined MENTIS format or M16 replacement. The existing 256×256 M16/F32 matrix contract is only a small arithmetic profile, not a complete model accelerator. Modern memory bandwidth, cache, energy, GPU isolation, F64 and M64 protection remain unresolved.

## 4. Developer workflow
STEMMA can identify an actual base revision and staged candidate once digest suite exists. Agent proposes source edits, human reviews exact diff, maintainer authorizes branch update. Do not invent test evidence, CI passes, signatures or source access. Source-level reasoning does not certify binary behavior. FASCICVLVS locks toolchain inputs where available; a dependency lock is not a guarantee of reproducibility. MODVLA provides candidate typed adapters, RATIO numeric conditions, SERMO task/event presentation. Ordinary languages remain useful because exact algorithms, review and repeatability matter even when natural language is the primary interface.

## 5. Preconditions and alternatives
A full 2030 deployment would require C19 M64/ABI, C20 secure remote protocols, C21 source/package trust, C22 numerical extension, C23 device support, C24 registry and text processing, among others (see audit). Assume only a bounded local broker for the R1 fixture; no assertion that these open dependencies have been solved. Alternative futures: fragmented vendor-specific assistants, local-first interoperable services (preferred scenario), or slower adoption with conventional applications dominant. No market shares or performance predictions.

See [task contract](MENTIS-agent-task-R1.md), [CVSTOS policy](CVSTOS-distribution-and-energy-R1.md), [STEMMA](STEMMA-R1.md), [FASCICVLVS](FASCICVLVS-R1.md), [audit](../docs/continuity-audit.md).
