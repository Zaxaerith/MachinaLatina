# Nova Maior / Magna — Common Register ISA R1

> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-25. Fictional 1988–2005 architecture proposal. Not an implemented CPU, full ISA, ABI or claim of historical product release. N1 remains unchanged.

## Motivation

The 1968 N1 has one accumulator, fixed four-octet instructions and 24-bit byte addresses. Retaining its entire instruction encoding would constrain a later register machine. The proposed Maior makes a clean ISA break while preserving big-endian data conventions and eight-bit byte addressing. Magna extends the new instruction format, not the old N1 format. Minor and Media are earlier separate implementation families; common branding alone does not establish binary compatibility.

## Machine profiles

| Property | Maior M32 | Magna M64 |
| --- | --- | --- |
| General registers | 16 writable 32-bit | 16 writable 64-bit |
| Address model | 32-bit byte addresses | low 48-bit byte addresses, high bits zero |
| Architectural byte address range | 4 GiB | 256 TiB |
| Instruction | 32 bits, four-byte aligned | same |
| Integer arithmetic | modulo 2^32 | modulo 2^64 |
| Byte order | big-endian | big-endian |
| Native floating point | separate future extension | separate future extension |

These address limits are mathematical architectural bounds, not installed RAM, implemented physical bus width or OS virtual memory guarantees. Base R1 is a single execution context with memory in an installed contiguous prefix. PC is a byte address. Reset clears PC/registers and halted/fault state; loader supplies memory. R0 is writable. No paging, protection, interrupt, atomics, device or privileged instruction is defined.

A Magna implementation may provide an M32 execution context: operations use 32-bit values, addresses, overflow and shift bounds; all general-register writes zero the upper 32 bits. LEG64/PON64 are invalid. The mode is selected externally by a hypothetical loader, not by a new instruction. A common M32 binary can be ISA-compatible if this mode implements the same contract, but requires matching OS/ABI/executable format and all extensions it uses to actually run. No automatic native compatibility with N1, Sextaria or Minor.

## Instruction layout

| Bits | Field |
| --- | --- |
| 31:24 | OP, 8 bits |
| 23:20 | D, register index |
| 19:16 | A, register index |
| 15:12 | B, register index |
| 11:0 | I, immediate |

All unused fields zero; registers read before any write. Signed I is a two's-complement 12-bit displacement (-2048..2047); NVM/ORI/SHL use unsigned I. For memory operations effective address = R[A] + signed(I), evaluated mathematically without address wrap. Word access aligned to its size; every accessed byte must be installed and within mode address range. Eight-bit access is unaligned. No hidden scaling of data addresses. Branches use signed word displacement relative to next instruction, i.e. -8192..8188 octets from PC+4. RET requires aligned valid target.

| OP hex | Mnemonic | Fields | Operation |
| --- | --- | --- | --- |
| 00 | FIN | — | Halt; PC unchanged |
| 10 | NVM | D,I | R[D] = unsigned I |
| 11 | ORI | D,A,I | R[D] = R[A] OR unsigned I |
| 12 | SHL | D,A,I | R[D] = R[A] shifted left I; require I < register width |
| 13 | ADD | D,A,B | R[D] = R[A] + R[B] modulo register width |
| 14 | SVB | D,A,B | R[D] = R[A] - R[B] modulo register width |
| 20 | LEG8 | D,A,I | Read one octet at effective address, zero extend |
| 21 | PON8 | D,A,I | Store low 8 bits of R[D] at effective address |
| 22 | LEG32 | D,A,I | Read aligned 32-bit big-endian value, zero extend |
| 23 | PON32 | D,A,I | Store low 32 bits at aligned effective address |
| 24 | LEG64 | D,A,I | M64 only: read aligned 64-bit big-endian word |
| 25 | PON64 | D,A,I | M64 only: store aligned 64-bit big-endian word |
| 30 | SI0 | A,I | If R[A] = 0 branch to PC+4+4*signed(I) |
| 31 | SALTA | I | Branch to PC+4+4*signed(I) |
| 32 | CALL | D,I | Save PC+4 in R[D], branch to PC+4+4*signed(I) |
| 33 | RET | A | Branch to R[A] |

16 distinct assigned opcodes, 240 reserved. ADD/SVB results wrap at the selected mode width; MODVLA checked arithmetic needs explicit compiler checks. NVM/ORI and shifts allow constructing wider constants, but this tiny base has no complete assembler, relocation, compare flags or calling convention. CALL is a link-register primitive, not an ABI.

## Execution contract

Fetch at aligned installed PC. Normal PC advances by four without wrap; if next PC exceeds mode address range, fault before commit. Sequential installed-memory check occurs at next fetch. For taken branches and RET, target must be aligned and installed; untaken SI0 ignores target. CALL additionally requires representable link PC+4. Compute relative target mathematically; no intermediate unsigned wrap. FIN halts without increment. Validate reserved fields, mode, shift and full memory span before updates. A fault leaves PC, registers and memory unchanged and stops the base context with a diagnostic; no resumable trap handler yet.

## Paper vector

Hexadecimal instructions at byte offsets 0,4,8,C,10:

    1010002A ; NVM R1, 42 decimal
    10200100 ; NVM R2, 100 hex
    23120000 ; PON32 R1, [R2+0]
    22320000 ; LEG32 R3, [R2+0]
    00000000 ; FIN

Expected: bytes at 100..103 = 00 00 00 2A, R3 = 42. This holds in both M32 and M64 modes with sufficient installed memory. In contrast, a full-width ADD of FFFFFFFF and 1 produces zero in M32 and 0000000100000000 in M64, so common instruction bytes are not automatically common execution semantics. No execution was performed.

## Extension boundaries

Native F32 compatibility, a new F64 numerical format, vector registers, condition/compare operations, privileged state, memory translation, atomics, device I/O, code density, executable format and ABI are open. Old F36/F48 scientific archives must be explicitly decoded; raw numerical bits are not a portable value. Related: [N1](Machina-Nova-N1.md), [MODVLA](MODVLA-I-R1.md), [family study](Nova-family-evolution-study.md).
