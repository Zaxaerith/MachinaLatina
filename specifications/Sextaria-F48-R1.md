# Sextaria-F48/R1 — Finite 48-bit Scientific Floating Point

> REVIEW CANDIDATE / NOT CANON · 2026-11-25. Independent paper proposal; existing FLOAT-P0 F36/F32 and RATIO I accepted formats are unchanged. No implementation.

## Encoding and range

48-bit word: sign s at bit 47; biased exponent E at 46:38 (9 bits); explicit fraction M at 37:0 (38 bits); bias 256. Nonzero requires 1<=E<=510 and 2^37<=M<=2^38-1.

    value = (-1)^s * (M/2^38) * 2^(E-256)

All-zero word is canonical zero. Other E=0 words, E=511, non-normalized fractions are invalid. No negative zero, subnormal, infinity, NaN or exception flag. Minimum positive 2^-256; maximum (1-2^-38)*2^254. Precision 38 binary significant bits (~11.44 decimal digits of precision, not a guaranteed number of correct result digits). Upward spacing at 1 is 2^-37.

## Arithmetic

Decode both finite operands; apply exact rational add/subtract/multiply/divide; round once to nearest-even. For nonzero result normalize to [1/2,1) in magnitude, compute biased exponent, trap before rounding for E<=0 or E>=511, matching existing FLOAT-P0 range convention. Round integer significand to nearest, ties even. Carry to 2^38 renormalizes to 2^37 and increments exponent; trap if reserved. Exact zero becomes canonical zero. Divide by zero faults. No FMA, hidden extended accumulator, or reassociation. Conversion from F32/F36 requires decode then encode, not bit reinterpretation; it can lose precision or trap.

## Paper vectors

| Value | F48 hex |
| --- | --- |
| 0 | 000000000000 |
| 1 | 406000000000 |
| -1 | C06000000000 |
| 1/2 | 402000000000 |
| 1/4 | 3FE000000000 |
| 3/2 | 407000000000 |
| 1+2^-24 | 406000002000 |
| 2^-24 | 3A6000000000 |
| minimum positive | 006000000000 |
| maximum positive | 7FBFFFFFFFFF |

1+2^-38 rounds to 1 (halfway); 1+2^-37 is the next value (406000000001). F48 and F36 retain (1+2^-24)-1; F32 yields zero. RATIO-I/R1 does not yet accept F48; a separate profile must approve it. Six-octet high-first serialization is possible under an explicit schema, not a complete archive format. See [S1](Sextaria-S1-R1.md), [FLOAT-P0](FLOAT-P0.md).
