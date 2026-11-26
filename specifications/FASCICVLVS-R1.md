# FASCICVLVS R1 — Cross-Architecture Software Distribution
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional 2011–2015 package design; logical manifest and resolution contract only, not an installer, executable package format, signature format or implemented registry.

## Identity and target
Package identity is (authenticated publisher identity, stable nonzero u64 package number scoped to publisher), preserving the CVSTOS package model. Publisher key continuity or rotation must be authenticated externally; no implicit trust in display names. Each release has increasing u64 counter (nonzero); human-readable version label is informational. Multiple target artifacts may share a release but may not silently replace published artifact content. Package identity, source revision, binary content, installation identity and runtime permission are distinct.

A target tuple specifies ISA, execution mode, required instruction extensions, OS family, service ABI, native procedure ABI, loader format, and runtime profile. Character registry/codec and numeric profiles are declared separately where used. A target matches only if every requirement is supported; unknown labels are not wildcards. No common native ABI is assumed. Source packages may be rebuilt for a declared target using an available backend, but are not runnable artifacts.

## Manifest
Logical fields: publisher/package identity; release counter; COS display title and declared registry; license identifier or explicit terms reference; STEMMA source revision reference if available; build recipe and toolchain references when provided; ordered artifact table (target tuple, exact length, digest suite/ref); requested capabilities; dependency constraints on other publisher/package identities and minimum/maximum release counters. Canonical signing serialization, algorithm suite and key rotation are open. Source license grants no automatic execution rights; source provenance is not a signature, and signatures are not a guarantee of safety.

Resolver takes a finite verified catalogue snapshot, target profile, root package identity and release constraints. Select one release per identity and one matching artifact per release; intersect all transitive constraints, reject cycles in this base profile, reject missing/ambiguous target artifacts and report unsatisfiable constraints rather than silently substitute a different publisher or ABI. A deterministic selection policy chooses the lexicographically greatest vector of release counters in a fixed sorted identity order among complete valid solutions, using an explicit absent sentinel 0 for unused catalogue identities; bounded solver may return LIMIT. Do not claim that greedily picking the newest dependency always works.

Lock record binds catalogue snapshot identity, target tuple, selected identities/counters, artifact references, dependency edges and exact recipe/toolchain inputs if used. Installation verifies exact bytes and publisher authorization against lock and current device trust policy. No implicit fallback to a lower release; recovery and rollback require explicit approval/policy. Atomic installation, storage format and signature verification implementation remain open. Locking dependencies alone does not imply reproducible builds or reproducible scientific results.

## Example: one source, three artifacts
Illustrative package publisher P, number 42, release 3, source revision E3 (symbolic names, not actual digests). 
| Target | Artifact fixture | Compatibility |
| --- | --- | --- |
| Nova Maior M32 / ORDO-N I | A | M32 plus matching loader and ABI |
| Sextaria S2 / PARTES I | B | 48-bit word ISA and PARTES IPC ABI |
| Mobilis M32 / CVSTOS I | C | M32 plus CVSTOS service/loader ABI, sandbox |

A and C share some instruction semantics but cannot be substituted for each other. B may preserve an F48 data schema while A/C need explicit decode library; a binary package does not establish scientific equivalence. These ABI labels are symbolic placeholders because complete loaders/procedure ABIs are not yet specified. No actual artifacts exist.

Dependency example: P:42 requires library Q:7 releases 2..4; an additional dependency R:9 requires Q:7 releases 2..3. If 2,3,4 are available with matching targets, Q:7 release 3 is a possible highest compatible selection; 4 violates the second constraint. If Q:7 release 3 lacks the target and 2 matches, select 2. If none match, fail. No installation or network access occurred.

CVSTOS stores may restrict publisher trust roots; owner-controlled devices may accept independent signed packages, all sandboxed. ORDO-N and PARTES repositories may expose native and source packages independently. App signing is not boot signing or runtime consent. Related [CVSTOS policy](CVSTOS-distribution-and-energy-R1.md), [STEMMA](STEMMA-R1.md), [history](../docs/de-codicibus-2005-2026.md).
