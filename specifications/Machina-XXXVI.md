# Machina XXXVI — Exemplar Primum (1954)

> **Phase IV architecture draft / DRAFT ISA P0, not a hardware reconstruction.**  
> Fictional machine. **Only the P0 subset in this document has concrete encoding semantics;** the complete scientific system, floating point, interrupts, tape controllers, and later binary compatibility are unimplemented and undecided.

## Design rationale / 设计理由

Machina XXXVI is a **word-addressed, six-character, Latin–Greek scientific machine**. Its era is anchored to the real 1950s scientific-mainframe landscape; its ISA is deliberately independent from IBM 704 and from later PDP-10. Classical Latin and Greek determine the *engineering requirements and software conventions*, **not** the transistor physics or the necessity of a specific word size.

- Native word: **36 bits**, not an 8-bit byte.
- Architectural addresses: **15-bit WORD addresses**, `00000–77777` octal (32,768 words).
- Full-memory raw bit capacity: 1,179,648 bits = 147,456 eight-bit-equivalent octets = **144 KiB**. This figure is only a comparison unit, not byte-addressability.
- Text: six **CVL-54/P0** six-bit symbols per 36-bit word. Mixed-script printed text remains **stateful** at the terminal.
- Display/program listings are conventionally **octal**, with 12 octal digits per 36-bit word.

## Registers / 寄存器

| Register | Width | P0 purpose |
| --- | ---: | --- |
| `A` | 36 | primary accumulator, modulo-2^36 unsigned arithmetic |
| `Q` | 36 | extension register **reserved for later multiply/divide**; P0 instructions do not read/write it |
| `X1, X2, X3` | 15 each | index offsets |
| `PC` | 15 | next instruction's word address |
| `Z` | 1 | true iff most recently updated `A` equals zero (derived; branching defined on `A`) |
| terminal page | 1 (external) | LATINA / GRAECA print state; **not a CPU register** |

Reset: `PC=0`, `A=0`, `Q=0`, `X1=X2=X3=0`, terminal page `LATINA`, and output empty. Memory initialization and tape-loading rules are *test-harness setup*, not promised physical hardware behavior.

## One-word instruction format / 36 位指令格式

```text
bit 35            24 23 22       18 17   15 14             0
   +----------------+--+-----------+-------+----------------+
   |  OP: 12 bits   | I| AUX:5 bits| TAG:3 | ADR:15 bits    |
   +----------------+--+-----------+-------+----------------+
        4 octal     1+5 =2 octal    1 octal   5 octal
```

**Exactly 36 bits = 12 + 1 + 5 + 3 + 15.** The octal listing is `OOOO FF T AAAAA`: `OOOO` opcode, `FF` a six-bit `I:AUX` group, `T` index selector and `AAAAA` word address.

Instruction encoding:

`W = (OP << 24) | (I << 23) | (AUX << 18) | (TAG << 15) | ADR`

For P0, **I=0 and AUX=0 are required**. The I bit is reserved for later indirect addressing; a P0 implementation **must reject I=1** rather than assuming IBM-709/PDP-10 semantics. Nonzero AUX is also invalid. Unknown opcodes trap or fail explicitly.

## Address calculation

- `TAG=0` means no index.
- `TAG=1,2,4` selects `X1,X2,X3`, respectively; other TAG values are reserved and invalid.
- For a memory or branch operation: `EA = (ADR + selected_X) mod 32768`. All are **word** addresses.
- `FIN`, `NVM` require `TAG=0`. `PONX` requires one of `1,2,4` and takes the literal ADR, without effective-address calculation.
- Instruction fetch uses `M[PC]` and increments `PC` modulo 32768 *before* executing; jumps replace that incremented value.
- No byte or character sub-address can be formed in P0, and no memory map, I/O-mapped address or paging scheme is asserted.

## First ten instruction mnemonics / 最小可定义指令集

These upper-case mnemonics deliberately fit the 23-letter Classical Latin base. Their Latin forms are **project coinages**, not attested 1950s terms. Opcodes below are *octal*, four digits each.

| Opcode₈ | Mnemonic | Meaning (A and M word-level) |
| --- | --- | --- |
| `0000` | `FIN` | stop machine; all fields zero |
| `0001` | `LEGE EA` | `A ← M[EA]` |
| `0002` | `PONE EA` | `M[EA] ← A` |
| `0003` | `ADDE EA` | `A ← (A + M[EA]) mod 2^36` |
| `0004` | `SVBT EA` | `A ← (A - M[EA]) mod 2^36` |
| `0005` | `SALTA EA` | `PC ← EA` |
| `0006` | `SI0 EA` | if `A=0`, then `PC ← EA`; otherwise continue |
| `0007` | `PONX TAG,ADR` | `X_TAG ← ADR`, TAG exactly 1/2/4 |
| `0010` | `EMIT EA` | send **six** 6-bit symbol codes from `M[EA]` to an output terminal in MSB-first order |
| `0011` | `NVM ADR` | `A ← unsigned zero-extended 15-bit ADR`, TAG=0 |

`Z` reflects whether `A` is zero after LEGE, ADDE, SVBT and NVM. PONE, EMIT and jumps leave A and Z unchanged. The original intent is numeric/scientific; **floating-point and signed number semantics are *not* defined** by P0, so claims of FORTRAN-compatible floating arithmetic must wait.

### Output interface / I/O character semantics

`EMIT EA` sends exactly six CVL-54/P0 codes to a **printer device**, with no CPU interpretation of letters. The printer retains LATINA/GRAECA state across emitted words; SHIFT-GRC or SHIFT-LAT changes only the printer page, and EOT ends/reset a logical record. PRINTING, not memory storage, converts codes into readable characters.

The CPU's `EMIT` operation is synchronous in this model; **real device latencies, interrupts and controllers are deferred**. No `INW`, tape DMA or buffered character I/O is specified yet.

## Scientific arithmetic / numerical formats deferred

A 1950s scientific computer would normally require signed integers and hardware floating point. Rather than quietly borrowing a later standard, P0 specifies only bitwise-stable unsigned modular integer arithmetic. Candidates for later review:

- sign–magnitude vs two's-complement negative integers;
- floating `1 sign + 8 exponent + 27 fraction` as a historically inspired **candidate**, not a defined numeric representation;
- precision, normalization, exceptions and rounding;
- 72-bit products using accumulator `A` and extension `Q`.

## Critical era boundary: CVL-68 is *later*

Machina XXXVI is dated **1954**, whereas the fictional direct eight-bit **CVL-68** belongs to the late 1960s. Thus:

- XXXVI hardware **does not natively read CVL-68 bytes**.
- A future tape or terminal **gateway** decodes six-bit stateful records then emits eight-bit CVL-68 values.
- Packing four eight-bit values into one 36-bit word with 4 spare bits is a *possible later adapter trick*, not the original architecture, not a standard conversion and not evidence of native byte-addressability.
- The historical reason newer machines favor bytes can be explored without retroactively installing 1968 hardware in 1954.

## Validation boundaries

See [worked programs](../docs/machina-xxxvi-programs.md) and [CVL-54/P0](CVL-54-P0.md). This document provides an **executable-style contract for ten opcodes**, but **not** a complete real machine: there are no defined interrupts, fault vectors, times, peripheral bus, magnetic-tape frames, signed/floating arithmetic or complete assembler language.

## Real-world comparative sources (not alternate history)

- [Columbia University, *The IBM 704*](https://www1.columbia.edu/cu/computinghistory/704.html) — real six-bit characters, 36-bit words and six-character identifier limit.
- [Computer History Museum, IBM 704 artifact](https://www.computerhistory.org/revolution/artifact/482) — real IBM 704 as a period example, not the blueprint of this machine.
- [PDP-10 instruction-format archival notes](https://pdp10.nocrew.org/docs/opcodes.html) — a *later* 36-bit architecture with different 9+4+1+4+18 layout; deliberately **not adopted** as the 1954 baseline.

Any association of these real products with the fictional `Machina XXXVI` would be erroneous.
