# PARTES I/R1 — Microkernel and Typed Message Services
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional late-1980s/early-1990s architecture. Bounded single-core IPC contract, not a running kernel, complete device stack or filesystem. Uses candidate [Sextaria S2 protection](Sextaria-S2-PROTECT-R1.md).

## 1. Kernel versus services
Kernel owns isolated address regions, context switching, scheduler, endpoint/handle tables and message copying. Storage, record parsing, CVL text conversion, F48 interpretation, document layout and network policy run in independent user-mode service processes. Trusted bootstrap creates processes/endpoints and grants process-local handles. Kernel mediates any device access; this baseline assumes preloaded record data in a service's memory and no real disk drivers. A service cannot access client memory directly. No dynamic spawn, endpoint discovery, handle transfer, shared memory, DMA or automatic restart in R1.

States READY, RUNNING, WAIT_REQUEST, WAIT_REPLY, EXITED. FIFO round-robin ready queue, timer preemption and voluntary yield; blocked processes are not scheduled. Single kernel execution context. Each process has at most one outstanding CALL; server receives at most one active request, must finish/reply before receiving another, and cannot CALL while serving it. Server-only processes cannot CALL at all in this bounded profile, preventing IPC call cycles (not guaranteeing every service will progress). Trusted configuration caps each endpoint's FIFO queue at 16 pending requests, excluding its one active request; a full queue causes immediate error. No timeouts in R1; administrator termination is the recovery option for a hung peer.

## 2. Message representation
Exact external octets, independent of native layout. Integers big-endian. Maximum envelope 1536 octets (256 Sextaria words), including 24-octet header (4 words); payload maximum 1512. No implicit padding in logical envelope. Native IPC buffers begin at lane 0 and occupy ceil(length/6) words; final unused lanes zeroed on delivery, excluded from logical length. Validate entire source/destination word span without wrap, including last partial word. Kernel-private pending storage and reply capacity bounded by boot configuration; resource exhaustion returns LIMIT without enqueueing.

| Offset | Width | Field |
| --- | --- | --- |
| 0 | 4 | Schema ID, nonzero |
| 4 | 2 | Schema revision, nonzero |
| 6 | 2 | Operation, nonzero |
| 8 | 4 | Client-selected correlation tag, nonzero |
| 12 | 4 | Body length (octets) |
| 16 | 4 | Service status (0 in requests) |
| 20 | 4 | Reserved zero |

Exactly 24+body length octets, no scanning for delimiters. Kernel validates structural header and exact length, not application schema or numeric validity. Response must echo schema/revision/operation/tag. For this baseline nonzero service status requires empty body; service status is separate from kernel transport status. A tag is not authentication. Kernel supplies actual sender PID and a kernel-issued per-server delivery ticket outside the message, through return registers; no field in user payload grants identity or permissions. Tickets never reused within server lifetime; only the active ticket can be answered. An endpoint handle authorizes CALL on that endpoint; possession of arbitrary integer is insufficient outside its process table.

## 3. S2 syscall ABI
SVCA word 800000000000; user R0 service number. Registers 48 bits; values of sizes below must be zero-extended, invalid upper bits reject. Buffer pointers are checked S1 word/lane pointers, lane zero required. Counts and handles are unsigned 32-bit; EXIT code u32. Return R0 transport status, R1 actual delivered message length or zero; R2 sender PID and R3 ticket on successful RECV only, zero otherwise. R4–R15 preserved. Saved next PC resumes on completion, not incremented again.
| Hex | Call | Input registers | Behavior |
| --- | --- | --- | --- |
| 01 | MITTE | R1 endpoint handle, R2 request pointer, R3 length, R4 reply pointer, R5 reply capacity | CALL; copies request into kernel and blocks until response/error |
| 02 | ACCIPE | R1 receive pointer, R2 capacity | RECV on server's sole bootstrap endpoint; blocks if queue empty |
| 03 | RESPONDE | R1 ticket, R2 reply pointer, R3 length | REPLY to active request |
| 04 | CEDE | none | yield |
| 05 | EXIT | R1 code | terminate, no return |

Transport status decimal 0 OK, 1 INVALID, 2 BAD_BUFFER, 3 DENIED_OR_BAD_HANDLE, 4 LIMIT, 5 PEER_EXIT, 6 SHORT_BUFFER, 7 BAD_STATE. For successful MITTE return response length; RESPONDE and CEDE return zero length. Reply/receive capacities must be 24..1536; entire writable capacity checked at submission. Source and destination may overlap in CALL because request is copied first and caller remains blocked. Error leaves destination unchanged. RECV with insufficient capacity for head request returns SHORT_BUFFER without dequeue; retry with larger capacity. A reply larger than client's reserved capacity fails with SHORT_BUFFER for both parties, releases ticket and wakes caller without delivery. Invalid reply header/tag or pointer fails for server, leaves active request available to correct. Exiting server wakes queued and active callers with PEER_EXIT; exiting caller removes its queued request or invalidates its active ticket, and server receives PEER_EXIT on attempted reply to that cancelled ticket, releasing it. No automatic retries or replay of writes. No partial delivery. These are abstract atomic kernel operations, not crash-durable transactions.

## 4. Costs
For request q and reply r, the buffered baseline copies q from client to kernel and q to server, r from server to kernel and r to client: 2(q+r) logical octets copied, excluding final-lane zeroing, metadata and implementation overhead. At least two user-process handoffs in an isolated single-client/server exchange; actual switches depend on scheduling. No measured performance. Later large scientific arrays may use read-only shared buffers or explicit ownership transfer, requiring hardware protection/lifetime and synchronization contracts; no zero-copy promise now. See [record service](PARTES-record-service-R1.md) and [history](../docs/de-partibus-1987-2026.md).
