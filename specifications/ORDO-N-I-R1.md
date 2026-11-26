# ORDO-N I/R1 — Protected Processes and Byte Streams
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional early 1990s kernel contract requiring [M32 PROTECT-R1](Nova-M32-PROTECT-R1.md). Ordo Operum P0–P2 are modern host-monitor experiments, not an implemented guest kernel.

## Kernel and scheduler
A single privileged kernel owns scheduling, page tables, process-local handles and regular-file byte access. User libraries interpret CVL/COS, NODVS and scientific formats. OMR1 remains the modern research container, not a historical filesystem.

A process has nonzero PID, separate page root, saved user bank and PC, access policy and handle table. READY, RUNNING, EXITED; BLOCKED reserved for later blocking service. PID not reused within boot epoch. Trusted loader creates initial processes with empty handle tables (executable format and spawn syscall not defined). No threads, shared user pages, concurrent kernel or async I/O. Round-robin FIFO: on timer or CEDE append running process to ready tail; exit or fatal user fault removes it, releases frames/handles and retains exit status. Example 20 ms timer period is a design illustration, not hardware clock specification. Other syscalls complete before another process runs. No ready process: supervisor idle loop, platform mechanism unspecified.

## Namespace and file model
Logical mounted tree of directories and existing regular files. Early pathname profile: absolute slash-separated CVL-68/RC1-L byte names, each component 1–31 bytes drawn from 23 classical uppercase Latin letters, digits, underscore and period. Reject empty components, dot, dot-dot, trailing slash, controls; maximum 255 bytes. Root is directory, not regular file. No normalization or casefolding. This is deliberately limited; Greek content is supported independently, international COS filenames belong to a later profile. No links, create/delete, mounts or on-disk format.

Each process has trusted administratively supplied file read/write rights, checked on open; no runtime policy changes. Successful open creates independent offset zero and nonzero local handle; never recycle handle values within process lifetime. Handle number alone grants no access outside that process. Regular file maximum 16 MiB in this candidate. No devices or network files.

## M32 syscall ABI
SVCA = 80000000. R0 service number; R1–R4 arguments. Return R0 status, R1 result (zero on failure), R2–R15 preserved. Resume saved next PC, do not add four again. EXIT does not return; CEDE returns success when rescheduled. Unsigned octet counts and offsets; pointers user virtual addresses. This is not a general MODVLA procedure ABI.
| Hex | Service | Arguments | Result R1 |
| --- | --- | --- | --- |
| 01 | APERIRE | R1 path ptr, R2 byte length, R3 mode 1 read / 2 read-write | handle |
| 02 | LEGERE | R1 handle, R2 destination, R3 count | bytes read |
| 03 | SCRIPTVRA | R1 handle, R2 source, R3 count | bytes written |
| 04 | QVAERE | R1 handle, R2 absolute offset | resulting offset |
| 05 | CLAVDERE | R1 handle | 0 |
| 06 | CEDE | none | 0 |
| 07 | EXIT | R1 exit code | no return |

Status decimal 0 OK, 1 bad call/argument, 2 bad buffer, 3 invalid handle, 4 denied, 5 missing file, 6 limit, 7 I/O failure. Unused arguments ignored. Validate syntax, handle/rights, full buffer span and limits before side effects. Kernel checks user translation even though supervisor can access physical RAM. APERIRE reads exact declared bytes, no terminator. LEGERE requires writable destination; SCRIPTVRA readable source; max 4096 bytes each; validate whole requested buffer even at EOF. Zero count is no-op after handle/rights validation, pointer ignored. LEGERE returns min(count, length-offset), advances by actual count; zero on positive request means EOF. QVAERE accepts 0..length, no sparse holes. SCRIPTVRA overwrites or extends within limit, advances by count; abstract store provides full success or failure without file/offset/buffer mutation. No crash atomicity or disk durability promise. CLAVDERE invalidates handle. Failure does not change user destination, file content or offset. These contracts exclude future partial device writes/blocking streams.

## Paper vector
Existing file /ACTA contains 11 CVL-68 bytes:
    52 41 4B 54 45 20 8A 8E 82 8E 91
Path bytes: 2F 41 43 53 41. Path at 00401000 hex readable; buffer at 00402000 hex writable; granted read access.
| Call | R0 in | R1 in | R2 in | R3 in | R0 out | R1 out | Offset |
| --- | --- | --- | --- | --- | --- | --- | --- |
| open | 1 | 00401000 hex | 5 | 1 | 0 | 1 (fixture) | 0 |
| read | 2 | 1 | 00402000 hex | 6 | 0 | 6 | 6 |
| read | 2 | 1 | 00402006 hex | 8 | 0 | 5 | 11 |
| read | 2 | 1 | 0040200B hex | 1 | 0 | 0 | 11 |
| close | 5 | 1 | ignored | ignored | 0 | 0 | invalid |

User-space decoder renders SALVE ΛΟΓΟΣ. Kernel only copies bytes, no NUL appended. If output range is not writable, read returns 2 without advancing offset. This is a manual example, not executed code.

## Open work
MODVLA wrappers, process creation, executable and procedure ABI, persistent filesystem, drivers, terminals, pipes, international filenames, M64, multicore, TABVLA GUI and network services. See [history](../docs/de-ordine-novo-1970-2026.md).
