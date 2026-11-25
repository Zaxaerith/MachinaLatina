# Sextaria-S1/R1 — A 48-bit Scientific Register Machine

> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-25. Fictional 1978–1980 successor to the [S0 study](Sextaria-S0-study.md). Paper specification, not a deployed CPU, emulator, compiler, privileged ISA or ABI.

## Architecture

| Item | Candidate |
| --- | --- |
| Word | 48 bits; six 8-bit lanes, lane zero most significant |
| Registers | R0–R15, all writable 48-bit raw registers |
| PC | 24-bit word address |
| Architectural memory | 2^24 words = 100,663,296 octets = 96 MiB |
| Illustrative initial installation | 65,536 words = 384 KiB |
| Instruction | One 48-bit word |
| Integer arithmetic | Unsigned modulo 2^48 |
| Floating arithmetic | [F48/R1](Sextaria-F48-R1.md) |

Reset clears registers, PC and halted/fault status; memory is supplied by loader. Installed memory is a contiguous prefix. No paging, device instructions, interrupts, privilege, DMA, concurrency or condition flags in base R1. This is not a complete OS-capable hardware standard.

## Hybrid H address model

A word address A is 24 bits; upper 24 bits of any register used as a word address must be zero. A byte pointer P=(A<<3)|L uses low 27 bits, upper 21 bits zero; L=0..5, lanes 6 and 7 invalid. Linear octet offset is 6*A+L, NOT P. BINC maps lane 5 to lane 0 of next word; e.g. 000000000005 to 000000000008. No wrap past final architectural byte. MKBP requires valid word address and lane. BINC and MKBP validate pointer range, not installed RAM until dereference. LEGB extracts and zero extends; PONB replaces only the selected lane. A pointer grants no object lifetime or OS access rights.

## Instruction layout

| Bits | Field |
| --- | --- |
| 47:40 | 8-bit OP |
| 39:36 | 4-bit D |
| 35:32 | 4-bit A |
| 31:28 | 4-bit B |
| 27:24 | 4-bit X, zero |
| 23:0 | unsigned 24-bit I |

Unused fields must be zero. R0 is not hardwired zero. Source values are sampled before any writes. Register operation results go to R[D] except stores and branches. All opcodes hexadecimal.

| OP | Mnemonic | Fields | Operation |
| --- | --- | --- | --- |
| 00 | FIN | — | Halt; PC unchanged |
| 10 | LEGW | D,I | R[D] = memory[I] |
| 11 | PONW | D,I | memory[I] = R[D] |
| 12 | LEGI | D,A | Load word at checked R[A] |
| 13 | PONI | D,A | Store R[D] at checked word address R[A] |
| 14 | NVM | D,I | Zero extend I into R[D] |
| 15 | MOV | D,A | Copy R[A] |
| 16 | MKBP | D,A,I | Make byte pointer from word address R[A] and lane I |
| 17 | BINC | D,A | Advance byte pointer by one octet |
| 18 | LEGB | D,A | Read selected octet, zero extend |
| 19 | PONB | D,A | Replace selected octet with low eight bits of R[D] |
| 20 | ADD | D,A,B | R[A]+R[B] modulo 2^48 |
| 21 | SVB | D,A,B | R[A]-R[B] modulo 2^48 |
| 22 | ET | D,A,B | Bitwise AND |
| 23 | AVT | D,A,B | Bitwise OR |
| 24 | EXCL | D,A,B | Bitwise XOR |
| 25 | SHL | D,A,I | Left shift by I=0..47, discard high bits |
| 26 | SHR | D,A,I | Logical right shift by I=0..47 |
| 30 | FADD | D,A,B | F48 rounded sum |
| 31 | FSVB | D,A,B | F48 rounded difference |
| 32 | FMVL | D,A,B | F48 rounded product |
| 33 | FDIV | D,A,B | F48 rounded quotient |
| 40 | SALTA | I | Jump to word address I |
| 41 | SI0 | A,I | Jump to I if R[A] is raw zero |
| 42 | CALL | D,I | Save PC+1 in R[D], jump to I |
| 43 | RET | A | Jump to checked word address R[A] |

Exactly 26 distinct assigned opcodes, 230 reserved. CALL saves a link only; software must preserve it for nested calls. No implicit stack or calling convention. Word loads/stores are raw bits, not float conversions.

## Execution and faults

Fetch requires installed PC. Normal instruction advances PC by one without wrap; if next PC exceeds architectural range, fault before commit. Sequential installed-memory check occurs at next fetch. Taken jump/call/return targets must be installed; untaken SI0 need not validate target installation. CALL also requires representable PC+1. FIN halts without increment. Memory accesses must be installed. Invalid opcode/unused field, pointer/lane, shift, address or numeric operand/result faults before any register, memory or PC update. Host reports fault PC/cause; no resumable handler. Floating operations validate both input words, including zero cases. MODVLA checked arithmetic requires explicit compiler checks; this ISA integer arithmetic wraps.

## Worked image (hex words)

    000000: 101000000100 ; LEGW R1,100
    000001: 102000000101 ; LEGW R2,101
    000002: 313210000000 ; FSVB R3,R2,R1
    000003: 113000000102 ; PONW R3,102
    000004: 000000000000 ; FIN
    000100: 406000000000 ; 1
    000101: 406000002000 ; 1+2^-24
    000102: 000000000000 ; initial output

Expected paper result at word 102 is 3A6000000000 (=2^-24). Code occupies 5 words or 30 octets; no executed result is claimed. This listing is not a standardized object file. Existing XXXVI/Nova ISAs remain incompatible. Hardware may implement operations over many cycles; no cycle, cost or performance claim. See [historical study](../docs/de-sextaria-1976-2005.md).
