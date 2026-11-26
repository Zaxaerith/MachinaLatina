# MENTIS / MATRICES R1 — Mixed-precision matrix calculation
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Proposed 2016–2021 numerical device contract. Not a GPU ISA, implemented accelerator, training system or benchmark.

## 1. Numerical lineage
The original FLOAT-P0 F32/F36 are finite normalized formats with explicit leading significand, nearest-even rounding and traps. Sextaria-F48/R1 is now a separate paper proposal; it is not an implemented GPU format. A new low-precision format M16 is proposed for matrix operands, not as a replacement for scientific archives.

M16 layout: sign bit 15; exponent E bits 14:10 (5 bits, bias 16); explicit fraction M bits 9:0 (10 bits). For nonzero, 1<=E<=30, 512<=M<=1023. Value=(-1)^s*(M/1024)*2^(E-16). All-zero is canonical zero; all other reserved exponents or unnormalized fractions invalid. Minimum positive 2^-16; maximum (1-2^-10)*2^14=16368. No NaN, infinity, negative zero or subnormal. Encode exact values using FLOAT-P0's normalize, pre-round exponent range trap, round-nearest ties-even, renormalize carry and post-round overflow trap. No implicit saturation, flush-to-zero or stochastic rounding. Underflow on input conversion is a possible serious limitation; scaled tensors and alternative formats are later research, not implicit conversion. M16 is not IEEE binary16 or bfloat16.

| Value | M16 hex |
| --- | --- |
| 0 | 0000 |
| 1 | 4600 |
| -1 | C600 |
| 1/2 | 4200 |
| 2^-10 | 1E00 |
| min positive | 0600 |
| max positive | 7BFF |

## 2. Bounded matrix interface
MATMUL(A,B,C) takes A[M,K] and B[K,N] of M16, output C[M,N] of existing Nova-F32. Dimensions each 1..256. Row-major tightly packed big-endian octets, exact lengths 2*M*K, 2*K*N, 4*M*N. Context supplies three separately granted nonoverlapping buffers; no raw pointers, hidden padding, transpose, broadcasting or implicit conversion. Validate sizes, permissions, all encodings and resource limits before effects. Inputs immutable during operation; output privately staged then published only on success. No partial result on numerical error. This abstract synchronous service does not define DMA, shared-memory ownership protocol, command queues or physical device fault recovery. Host must provide isolation and resource accounting separately.

For each output element start F32 canonical zero; for k increasing from 0 to K-1, decode exact M16 operands, form exact product, round to F32, then add to current F32 accumulator and round to F32. Products of valid M16 operands are exactly representable in existing F32 (at most 20 significant bits, exponent within F32 range); accumulator can still round. No reassociation, fused operation, arbitrary reduction tree or hidden wider accumulator. Different outputs can execute in parallel. A device unable to obey the per-element order may expose a separately named approximate profile; it cannot silently call its result R1. No claim this ordering is fastest.

## 3. Paper vectors
A= [1, 2^-10, -1], B= [1,1,1] column. A octets 46 00 1E 00 C6 00; B 46 00 46 00 46 00. Exact dot product 2^-10. F32 accumulation retains this; final F32 hex 37800000. Hypothetical M16-only accumulation rounds 1+2^-10 to 1 (tie-even, upward spacing 2^-9), then yields zero. This is a mathematical illustration, not a measured accelerator. RATIO-I/R1 has no matrix grammar; future RATIO matrix contracts can compare against exact rational dot products of declared inputs, distinguish quantization of original data from arithmetic error, and specify tolerance.

For two 256×256 M16 inputs and one F32 output, payload storage is 512 KiB (128+128+256 KiB); arithmetic is 16,777,216 multiply-accumulate steps (one multiplication and one addition each). Excludes scratch, transfer and model state. No throughput, latency, clock, training performance or wattage follows from these counts. In later profiles wider inputs, quantized integers, flexible reduction trees, gradients, nonlinear operators and mixed-precision optimization need independent definitions.

Related: [FLOAT-P0](FLOAT-P0.md), [F48](Sextaria-F48-R1.md), [FIGVRA](FIGVRA-95-R1.md), [RATIO](RATIO-I-R1.md).

## Phase XXXIX future scenario

[Nova Memoria R1](Nova-Memoria-R1.md) and [Sextaria scientific engine](Sextaria-scientific-engine-study.md) propose later platform/precision contracts. No earlier ISA, matrix arithmetic, F48 or RATIO-I accepted format is changed; F64/R0 and device ownership are unimplemented future candidates.

## Phase XLI future scenario

[LVMEN photonic R1](LVMEN-photonic-R1.md) and [system study](LVMEN-system-study.md) propose optional future links and approximate arithmetic. No silent substitution for exact arithmetic, no new device/ISA or RATIO grammar implied. Actual hardware and performance remain open.
