# Machina XXXVI — Worked Machine-Words / 机器字验算

**Status: P0 experimental test vectors · not a released emulator.**

This page makes the proposed 36-bit instruction encoding and CVL-54 printed output falsifiable. All addresses, instruction words and data words are written in **octal** (base 8), conventionally as 5-digit addresses and 12-digit words. For comparison, hexadecimal values have **9 digits**, since 36 / 4 = 9.

## Case 1: the first mixed Latin–Greek output

Goal: print **`SALVE ΛΟΓΟΣ`**. The input medium is a six-bit punched-card/packed-code stream, *not a modern Unicode keyboard*. Greek symbols below annotate what the six-bit printer renders.

### Assembler-style conceptual listing

```text
    ORG   00000
    EMIT  00100          ; send six codes from M[00100]
    EMIT  00101          ; send six codes from M[00101]
    FIN

    ORG   00100
    VER   22,01,13,24,05,43    ; S A L V E SPACE
    VER   61,13,17,03,17,22    ; GRC SHIFT, Λ Ο Γ Ο Σ
```

`ORG` and `VER` are **assembler directives**, not CPU opcodes. A not-yet-written assembler would use the `VER` list to pack six 6-bit code units into one 36-bit memory word. Greek comments are editorial annotations in the documentation, not claims about 1954 card input.

### Exact bit-encoding vectors

| Address₈ | Purpose | Machine word₈ (12 digits) | Machine word₁₆ (9 digits) |
| --- | --- | --- | --- |
| `00000` | `EMIT 00100` | `001000000100` | `008000040` |
| `00001` | `EMIT 00101` | `001000000101` | `008000041` |
| `00002` | `FIN` | `000000000000` | `000000000` |
| `00100` | CVL-54 `SALVE ` | `220113240543` | `4812D4163` |
| `00101` | CVL-54 `SHIFT-GRC ΛΟΓΟΣ` | `611317031722` | `C4B3C33D2` |

### Predicted trace

```text
PC=00000  EMIT 00100      printer LATINA
          22 01 13 24 05 43   => "SALVE "
PC=00001  EMIT 00101      printer LATINA => GRAECA
          61 13 17 03 17 22   => "ΛΟΓΟΣ"  (SHIFT emits nothing)
PC=00002  FIN
RESULT (no newline): SALVE ΛΟΓΟΣ
```

**Negative check:** if the printer page were erroneously reset between emitted words, the second word's first code `61` would still switch it to GRAECA, so this *particular* test cannot detect a between-word reset bug. A **separate two-word all-Greek continuation test is required** to exercise page persistence.

### Important boundary

The Greek word is printed in uppercase because CVL-54/P0 defines **uppercase only**. The polytonic word `λόγος` belongs to the later CVL-68 profile, not to this 1954 test.

## Case 2: elementary arithmetic

Memory begins at word 00000 with:

```text
    ORG   00000
    NVM   00007         ; A=7
    PONE  00102         ; M[00102]=7
    NVM   00005         ; A=5
    ADDE  00102         ; A=12
    PONE  00103         ; M[00103]=12
    FIN
```

| Address₈ | Expected instruction word₈ |
| --- | --- |
| 00000 | `001100000007` |
| 00001 | `000200000102` |
| 00002 | `001100000005` |
| 00003 | `000300000102` |
| 00004 | `000200000103` |
| 00005 | `000000000000` |

At halt, `A = 12` and `M[00103] = 12`. This deliberately checks positive integers only; the signed and floating formats remain unresolved.

## Case 3: index addressing

```text
    PONX  X1,00005      ; TAG=1, X1=5
    LEGE  X1+00100      ; word-effective address 00105
```

| Instruction | Octal 36-bit word |
| --- | --- |
| `PONX X1,00005` | `000700100005` |
| `LEGE X1+00100` | `000100100100` |

To validate, prepopulate `M[00105]` with a known value such as 17 decimal; after LEGE, `A=17`. This is **word indexing**, not character positioning.

## Test obligations before an emulator is claimed

- [ ] Verify the exact octal/hex word values using an independent program.
- [ ] Verify output state changes, including Greek page persistence across two consecutive Greek words.
- [ ] Verify TAG 1/2/4 and invalid TAG combinations.
- [ ] Reject I=1, nonzero AUX, unknown opcode and reserved CVL character codes.
- [ ] Verify modulo-2^36 ADD/SVBT behavior at wraparound.
- [ ] Define input formats and a small test runner without third-party runtime dependencies.
- [ ] Keep the ISA P0 label until signed arithmetic, faults and I/O are fully designed.

See [Machina XXXVI architecture](../specifications/Machina-XXXVI.md) for formal register and bit-field semantics.
