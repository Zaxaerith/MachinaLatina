# Sextaria S2 / PROTECT-R1 — Relocatable Protected Workstation
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Proposed 1987–1992 successor extension to [S1](Sextaria-S1-R1.md), not a complete machine or implementation.

## Word-oriented protection
Preserve 48-bit words, sixteen writable registers, 24-bit word PC, fixed 48-bit instruction and six-lane byte pointers of S1. Add USER and SUPERVISOR modes with distinct sixteen-register banks. Reset selects supervisor at physical word 0, clears both banks, leaves user region unset. Loader supplies RAM. Supervisor accesses installed physical words directly. USER has a contiguous relocatable region defined by physical BASE (24-bit word address) and LIMIT (word count, 1..2^24). Require BASE+LIMIT <= installed word count without wrap. Every user fetch, word access or decoded byte-pointer dereference checks virtual word A < LIMIT and translates to BASE+A; lane remains unchanged. Pointer construction/increment retains S1 architectural range checks, not allocation checks until dereference. PC is virtual in user mode. Taken branches must target an allowed word; sequential fetch checked at next fetch. No page tables, swapping, per-page rights or shared user segments in this initial profile. Kernel allocates disjoint regions and clears them before reuse. User code and data are not separated by hardware; no claim of W^X. Region placement may cause external fragmentation, and growth may require relocation while stopped. This is an alternative to Nova's 4 KiB paged protection, not a claim that segmentation always wins.

Example BASE=000800 hex, LIMIT=000400 hex (1024 words = 6144 octets). User word 000120 maps to 000920; virtual byte pointer for word 120 lane 5 is 000000000905, physical word 920 lane 5. User word 400 is outside the region; lanes 6 and 7 still invalid.

## Trap extension
Use S1 OP/D/A/B/X/I layout, unused fields zero. Seven new opcodes, disjoint from S1's 26. Names are provisional.
| OP hex | Mnemonic | Fields | Meaning |
| --- | --- | --- | --- |
| 80 | SVCA | none | user syscall; save next virtual word PC |
| 81 | LEGCA | D | supervisor reads saved cause |
| 82 | LEGPC | D | supervisor reads saved user word PC |
| 83 | REGIO | A,B | supervisor installs BASE=R[A], LIMIT=R[B], checked as above |
| 84 | RETV | A | supervisor enters user at checked virtual word PC R[A] |
| 85 | LEGREG | D,A | supervisor R[D] = user R[A] |
| 86 | PONREG | D,A | user R[A] = supervisor R[D] |

SVCA saves PC+1, requiring architectural representability, not PC+4. Instruction word 800000000000. User faults save faulting PC; periodic timer saves next unexecuted PC. Enter supervisor at physical word 000100, without touching user bank or implicit stack. Causes 1 syscall, 2 timer, 3 bad instruction/field, 4 address/lane, 5 privilege, 6 numeric fault. User FIN and privileged opcodes trap; supervisor SVCA or faults stop machine with diagnostic. Saved cause/PC invalid until trap; read when invalid faults. RETV validates region and target before mode change and clears saved validity. Single pending timer bit coalesces external events, delivered at user instruction boundary, deferred while supervisor runs; synchronous traps take priority. No nested traps. All faults retain S1 atomicity of user instruction effects. Kernel explicitly saves/restores contexts.

Timer source, loader, bus and physical devices remain independent platform requirements; user device-service code cannot access arbitrary MMIO under this profile. Device work needs bounded kernel mediation or a later isolated device profile. No DMA, interrupts for real peripherals, multicore or implemented protection. Related [PARTES IPC](PARTES-I-R1.md).
