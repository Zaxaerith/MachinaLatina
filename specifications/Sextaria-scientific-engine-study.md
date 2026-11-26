# Sextaria scientific engine — Precision without a 48-bit host CPU
> FUTURE SCENARIO / DRAFT / NOT CANON · 2026-11-26. Candidate 2033–2035 numerical service. No implemented silicon, floating-point standard adoption or RATIO grammar extension.

## 1. Inheritance
Sextaria S1/F48 retained 38 explicit significant bits, 9 exponent bits and a six-octet external representation. Its scientific record tradition may survive on Nova Memoria without resurrecting 48-bit instruction decoding, mixed word/lane pointers or S2 region protection. A specialist engine could execute declared high-precision operations and archive conversions. It competes with ordinary CPU software and GPU numerical units; separate hardware is justified only if workload, performance, energy and cost support it. Historical F48 bytes stay unchanged.

## 2. F64/R0 paper proposal
To explore a successor independent of CPU register width, define a tentative finite F64/R0 format: bit 63 sign, bits 62:52 biased exponent E (11 bits, bias 1024), bits 51:0 explicit fraction M (52 significant bits). Nonzero requires E=1..2046 and 2^51<=M<=2^52-1. Value=(-1)^s*(M/2^52)*2^(E-1024). All-zero canonical zero; all other encodings outside these conditions invalid. Min positive 2^-1024, max (1-2^-52)*2^1022. No NaN, infinity, negative zero or subnormal. Same normalize, pre-round exponent range trap, nearest-even and carry/post-round range check as F48; exact zero canonical. Four elementary operations on exact decoded rational inputs, round once. Division by zero faults. No implicit FMA, reassociation or conversion. Big-endian eight-octet serialization under explicit profile. This is not IEEE binary64 (which has 53 significant bits for normal numbers). An alternative format supporting special values and subnormals remains open.

| Value | F64/R0 hex |
| --- | --- |
| 0 | 0000000000000000 |
| 1 | 4018000000000000 |
| -1 | C018000000000000 |
| 1+2^-40 | 4018000000000800 |
| 2^-40 | 3D98000000000000 |
| minimum positive | 0018000000000000 |
| maximum positive | 7FEFFFFFFFFFFFFF |

F48 spacing upward at 1 is 2^-37; F64/R0 spacing 2^-51. Thus sequential (1+2^-40)-1 yields zero in F48 but 2^-40 in F64/R0. Both remain finite for these operands. F48 and F36 retain earlier (1+2^-24)-1 example; F32 loses it. Wider precision does not cure invalid input, measurement error or unstable algorithms. Conversion is decode/encode, not native reinterpretation or merely appending bytes.

## 3. Candidate execution service
Logical read-only operand buffers and private output, with explicitly granted ownership per [Memoria R1](Nova-Memoria-R1.md). Proposed scalar batch ADD/SVB/MVL/DIV on paired arrays of equal element count 1..4096, one declared format F48 or F64/R0 for both inputs and output. Exact lengths count times 6 or 8 octets; big-endian; no overlap, broadcasting or implicit type conversion. Validate full encodings, ranges and rights before execution; independently compute each pair in index order, stage output, publish only if every element succeeds. Invalid operand, range trap or zero divisor fails the batch without published result; device uncertainty quarantines private allocation. Actual commands, status serialization, timing and execution are undefined. No RATIO-I change: current accepted F32/F36 scalar grammar cannot claim these new formats or MATRICES. Future RATIO profile could specify independent reference values, operation order, conversion policy and error tolerance.

An example 1,000,000-element array uses 6,000,000 octets as F48 or 8,000,000 octets as F64/R0 (not a single batch in this profile). F48 saves external archive space; F64 may be easier to align to host hardware and offers more precision. Neither implies scientific validity or performance. See [F48](Sextaria-F48-R1.md), [RATIO](RATIO-I-R1.md), [MATRICES](MENTIS-matrix-R1.md).

## Phase XLI future scenario

[LVMEN photonic R1](LVMEN-photonic-R1.md) and [system study](LVMEN-system-study.md) propose optional future links and approximate arithmetic. No silent substitution for exact arithmetic, no new device/ISA or RATIO grammar implied. Actual hardware and performance remain open.
