# CVSTOS I/R1 — Mobile Application Identity and Scoped Authority
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional 2007–2010 base service contract with later extensions studied separately. No implemented OS, cryptographic stack, driver or native ABI.

## 1. Hardware and trust boundary
A candidate Nova Mobilis M32 platform implements Maior/M32 and [PROTECT-R1](Nova-M32-PROTECT-R1.md), plus platform-specific device mediation not yet specified. It does not obtain DMA protection, radio drivers or M64 support from that instruction subset. CVSTOS chooses a capability-oriented hybrid kernel: kernel isolates address spaces and mediates execution/resources; trusted user services handle documents, location and other policies. The idea draws on [PARTES](PARTES-I-R1.md), not its S2 register ABI or bounded synchronous protocol. Calls below are abstract service contracts, not syscall numbers. Trusted brokers, compositor, package manager and kernel are in the trusted computing base; compromised trusted components can defeat policy.

## 2. Identity
An installation has a kernel-assigned nonzero u64 installation ID, scoped to device and user profile, never reused in that profile. Publisher and package identity are separately authenticated by the installer; a package display name is not an identity. A process is associated with one installation by the trusted launcher; applications cannot claim another identity in a message. Private storage belongs to the installation and is not globally enumerable. Reinstall after removal obtains a new installation ID. Updates preserving verified publisher/package identity retain installation ID but may not expand prior grants silently. Process death destroys live handles; persistent consent records (later policy) are separate from handle values.

## 3. Capability table
TESSERA is a nonzero process-local u32 handle backed by a trusted table entry:
- owner installation and process instance; resource type and stable identity; operation set; optional immutable revision; grant ID and generation; scope (foreground or explicit background); expiration using monotonic time when applicable.
- Handles are not transferable in R1, not reusable during a process lifetime, and cannot be manufactured by copying another process's number.
- Every operation checks owner, live grant generation, resource, operation, scope, deadline and buffer bounds. Requests queued before revocation must be checked again at their service commit/delivery boundary. Kernel/broker serializes revocation and delivery in this abstract contract. Revocation prevents future delivery, not erasure of data already delivered or external effects already committed.
- Removal of an installation invalidates its grants and handles; deletion of private data and backups needs a separate storage policy. An app may keep copies of information it was previously allowed to read; this model does not promise perfect information-flow control.

| Proposed operation | Contract |
| --- | --- |
| ELIGE | launch trusted user document chooser, returning selected object read handle or cancellation |
| PETE | request a declared device/service scope; trusted UI evaluates consent and policy |
| LEGERE | read bounded octets from a granted immutable document revision |
| DIMINVE | voluntarily drop a handle; does not revoke another process's grant |
| REVOCATIO | trusted settings or policy revokes a grant and increments generation |
| PONE_NOVVM | later broker-mediated publication of a new document revision, not defined as writable access in I/R1 |

The caller cannot grant itself a resource by declaring a permission in a manifest. No direct peripheral MMIO for normal apps; actual device enforcement and network access controls are platform work. Error classes: DENIED, EXPIRED, REVOKED, BAD_HANDLE, BAD_RANGE, UNSUPPORTED, CANCELLED, LIMIT, IO_ERROR. Service errors must not expose other apps' private data.

## 4. Document broker (SCRINIVM)
A user-controlled shared document collection has opaque object u64 IDs within a broker namespace and nonzero u32 immutable revisions. Names and COS display strings are not authority. The trusted picker displays the document and requested access; selection grants read of exactly one revision. It can return a typed descriptor: content class, declared codec/version or scientific schema, byte length, object ID, revision. No automatic code execution or transcode. NODVS stays passive; LIGAMEN references are not grants. A user-visible file manager may import, export, organize or remove shared documents, without exposing every app's private directory. Opening one item does not grant collection enumeration, sibling objects, write or network rights.

LEGERE(handle, offset, count, destination) requires 0<=offset<=length and count<=4096. It validates full destination capacity, returns min(count,length-offset) octets, does not append NUL, and leaves buffer unchanged on failure. Zero count is allowed for a valid handle with in-range offset. The immutable original bytes are kept; application decodes under the declared profile. No write API in this subset. A later editor creates a new revision or new object via explicit user-mediated publication. Cloud sync and access to remote targets require independent authorization, authentication and transport.

## 5. Paper example
Map reader installation 17, process 3, receives handle 9 for broker object 42 revision 3, CVL-68/RC1-L, length 11. Source octets: 52 41 4B 54 45 20 8A 8E 82 8E 91 (SALVE ΛΟΓΟΣ). LEGERE(9,6,5) returns 8A 8E 82 8E 91 (ΛΟΓΟΣ). Access to revision 4 or object 43 is not implied. A different process's handle 9 has no relationship. User revokes grant generation 1; any subsequent read returns REVOKED (assuming retained tombstone), including a pending read not delivered before revocation. Previously returned five bytes cannot be recalled. This fixture is documentary, not an execution result.

## 6. Evolution
Later versions may support foreground camera/microphone/location sessions, one-time permissions, explicit durable consent, bounded background grants and separate app-distribution trust. See [policy study](CVSTOS-distribution-and-energy-R1.md). No automatic sharing of ORDO-N paths, PARTES endpoints, SERMO runtime or native binaries. M64 protection, loader/ABI, device IOMMU, secure transport, storage encryption and real GUI remain open.
