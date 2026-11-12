# Floating-Point Profiles: XXXVI-F36 and Nova-F32

**Status: experimental fictional standard — Phase X, 2026-11-12.** Neither encoding is IBM-compatible, IEEE 754, nor an attested historic specification. Only finite normalized values and one canonical zero are defined.

## Motivation

1954 Machina XXXVI has 36-bit words. 1968 Machina Nova has 32-bit data words. The designs should make numeric compatibility **explicit**, not assume that a 1968 computer automatically uses the much later IEEE 754 standard.

Both experiment formats use sign–magnitude representation, **base-2 exponent**, an explicitly stored fractional significand `m` with `1/2 ≤ m < 1`, and a biased exponent `E`:

`value = (-1)^sign × (fraction_integer / 2^F) × 2^(E - bias)`

| Format | Total bits | Sign | Exponent | Fraction F | Bias |
| --- | ---: | ---: | ---: | ---: | ---: |
| XXXVI-F36 | 36 | 1 | 8 | 27 | 128 |
| Nova-F32 | 32 | 1 | 7 | 24 | 64 |

The leading one in the normalized fraction is **stored**, not implicit. The exponent field `0` and all-ones field are reserved; no special infinities or NaNs are assigned.

## Zero, representability and errors

- All-zero word is exactly zero. Negative zero is **invalid**, as are other zero exponent field variants.
- Subnormals/gradual underflow, infinities, NaN payloads and special overflow values are **not supported**.
- Attempting to encode a nonzero number with biased exponent ≤0 **traps as underflow**. Biased exponent ≥all-ones **traps as overflow**.
- Decoding a non-normalized fraction or a reserved exponent raises a fault instead of silently reinterpreting bits.
- The reference arithmetic uses Python `fractions.Fraction` for exact mathematical sums and differences, then rounds **once per arithmetic instruction** to the destination's own format.
- Round-to-nearest, **ties-to-even**: when an exact mantissa lies halfway between representable values, choose the even last bit of the stored significand.
- A carry from significand rounding renormalizes and increments the exponent; an overflow after this increment traps too.
- A software implementation may choose a different microarchitecture but must reproduce these finite result semantics for any eventual interoperable profile.

These rules are original counterfactual design decisions. Real scientific machines used different exponent bases, normalization conventions and rounding rules.

## Exact bit-pattern vectors

| Value | F36 (9 hex digits) | F32 (8 hex digits) |
| --- | --- | --- |
| 0 | `000000000` | `00000000` |
| 1 | `40C000000` | `41800000` |
| −1 | `C0C000000` | `C1800000` |
| 3/2 | `40E000000` | `41C00000` |
| 1/4 | `3FC000000` | `3F800000` |

All values above are computed by the modern prototype and are **not** real IBM/IEEE encoding vectors.

## Key divergence: 1 + 2^-24

`2^-24 = 1/16777216`.

- F36 stores `1 + 2^-24` exactly because its stored significand has 27 bits.
- F32 has 24 stored significand bits. At 1, the next representable larger number is `1 + 2^-23`; hence `1 + 2^-24` lies exactly halfway.
- Nearest-even rounds this F32 value **to exactly 1**, whereas F36 retains the increment.

In other words, a **shared source** can have **two correct architecture-specific outputs**. Bit-for-bit numeric identity is *not* the meaning of portability.

## Four new float instructions (P1 extension, preserving P0)

| XXXVI octal opcode | Nova hex opcode | Mnemonic | Semantics |
| --- | --- | --- | --- |
| `0012` | `60` | `FLEG` | load and validate floating data word into A |
| `0013` | `61` | `FADD` | A = rounded(A + memory float) |
| `0014` | `62` | `FSVB` | A = rounded(A − memory float) |
| `0015` | `63` | `FPON` | validate A and store its bits to data memory |

Old XXXVI opcodes are **octal**; Nova opcodes are **hexadecimal**. Both float instruction families operate directly on the previously defined accumulator A, interpreting its current bits as floating only during float instructions. Integer instructions remain unchanged. Programs must not assume integer and floating meanings can be freely interchanged.

XXXVI operands address **36-bit words**; Nova operands address **four-byte-aligned 32-bit words**. All float faults are trapped; a faulting instruction must not partially update A, PC or output. No floating multiply/divide, exceptions with hardware status flags, transcendental math or real I/O formats are defined.

## Validation and historical perspective

The modern exact-rational library is `machina_xxxvi/floating.py`; both CPU interpreters now use it. See the [TRANFOR/P1](TRANFOR-P1.md) source contract and [Phase X report](../docs/phase-x-floating.md).

Relevant *actual-world* comparisons (not sources of our invented encoding):
- [IBM 704 and early scientific arithmetic](https://www.ibm.com/history/704)
- [IBM System/360](https://www.ibm.com/history/system-360) — short hexadecimal floating-point format is a materially different real-world solution.
- [IEEE 754 historical overview](https://standards.ieee.org/ieee/754/6210/) — 1985 standardization, later developments.
