# Nova M32 PROTECT-R1 — Protected Execution
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Proposed 1988–1995 extension to Maior M32, not implemented hardware or a change to N1. Single core only.

## Modes and memory
USER and SUPERVISOR have separate banks of sixteen 32-bit registers and a shared byte PC. Reset selects supervisor, physical PC zero, cleared registers and unset page root. RAM comes from a loader. Supervisor accesses physical RAM directly. USER uses two-level translation: VA bits 31:22 directory index, 21:12 table index, 11:0 page offset. Each table contains 1024 big-endian u32 entries and occupies an aligned 4 KiB physical frame.

Directory entry: physical table base in bits 31:12, present bit 0, other low bits zero. Leaf entry: physical frame base in bits 31:12; flags P=1, U=2, R=4, W=8, X=16; other low bits zero. User fetch requires P,U,X; data read P,U,R; store P,U,W. Missing entries, illegal bits, noninstalled frames, and permission failures fault before effects. Kernel must not expose private frames/page tables as user-writable and must zero newly allocated user frames. No TLB, swap, accessed/dirty bits, device mappings or demand paging.

Example VA 00402034: directory 1, table 2, offset 034. Root 00001000, directory entry at 00001004 = 00002001, leaf at 00002008 = 00009007. Read translates to 00009034; write and fetch denied. One directory plus one table requires 8 KiB, excluding mapped pages.

## Traps and timer
User fault saves faulting PC and cause; syscall saves representable PC+4; timer saves next not-yet-executed PC. Trap switches register bank and enters supervisor at physical 00000100. No implicit stack write. External periodic timer sets one pending bit; events coalesce, delivered and cleared at a user instruction boundary, deferred in supervisor. Synchronous instruction fault/trap takes precedence over a pending timer at the completion of the instruction. Supervisor faults stop execution with diagnostic; no nested traps. Platform timer hardware and boot devices remain undefined.

Cause 1 syscall, 2 timer, 3 invalid instruction, 4 address/translation/access, 5 privilege. User FIN is a privilege fault, not machine halt. Faulting instruction leaves user registers and memory unchanged. Trap entry changes privileged state only.

## Seven added instructions
Common Maior/Magna R1 32-bit layout; unused fields zero. All opcodes below hexadecimal; disjoint from base 16.
| OP | Mnemonic | Fields | Semantics |
| --- | --- | --- | --- |
| 80 | SVCA | none | user syscall trap |
| 81 | LEGCA | D | supervisor reads saved cause into R[D] |
| 82 | LEGPC | D | supervisor reads saved user PC into R[D] |
| 83 | RADIX | A | supervisor sets aligned installed page-root frame R[A] |
| 84 | RETV | A | supervisor enters user at virtual PC R[A] |
| 85 | LEGREG | D,A | supervisor R[D] = user R[A] |
| 86 | PONREG | D,A | user R[A] = supervisor R[D] |

Saved cause/PC invalid until user trap; reading invalid state faults in supervisor. RETV requires set root and aligned executable mapped target, validates before changing mode, clears saved-trap validity. No implicit restore of registers; kernel saves bank and PC in process table then prepares the next bank. All seven except SVCA are supervisor-only; SVCA in supervisor faults. Base integer instructions retain common M32 semantics. SVCA word = 80000000; service number is in user R0.

No full native calling ABI, M64 paging, multicore, cache-coherence, DMA isolation, interrupt controller or real implementation. See [ORDO-N I](ORDO-N-I-R1.md).
