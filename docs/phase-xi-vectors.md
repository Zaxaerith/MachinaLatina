# Phase XI — Scientific Vectors and the Cost of Rounding

**Research date: 2026-11-12. Status: DRAFT alternate-world development.** The 1954 XXXVI and 1968 Nova systems are fictional machines; the Python reference programs are present-day experimental tools.

## Historical/technical motivation

After the Greek–Latin bilingual character-encoding conflict and the split between 36-bit scientific and 32-bit byte-addressed computers, scientists encounter a less visible incompatibility: **the same mathematical expression can compute different numeric values** because each computer rounds independently and algorithmic evaluation order matters.

Phase XI therefore adds two *finite* floating instructions on each target and gives TRANFOR a small bounded vector abstraction, rather than prematurely creating a comprehensive BLAS or FORTRAN-equivalent library.

## Implementation and new operations

The exact-rational reference in `machina_xxxvi/floating.py` now includes `multiply` and `divide` in both formats, with round-to-nearest ties-to-even after each operation. Divide-by-zero and unrepresentable finite results raise `FloatFault`.

| Target | Multiply opcode | Divide opcode | Meaning |
| --- | --- | --- | --- |
| XXXVI | octal `0016` (`FMVL`) | octal `0017` (`FDIV`) | F36 accumulator with word-addressed memory operand |
| Nova | hex `64` (`FMVL`) | hex `65` (`FDIV`) | F32 accumulator with four-byte-aligned operand |

The previous instructions and integer semantics remain unchanged. The new instructions are **fictional experimental opcode assignments**, not claims about historic IBM or System/360 instructions.

TRANFOR/P2 accepts `VECTOR` literals (1–8 values) and `PRODVC` dot products, compiled by unrolling into real P1 floating machine operations. No CPU gets an unannounced vector/SIMD instruction.

## First numeric experiment

The new [portable_dot.trf](../examples/portable_dot.trf) defines:

```text
VECTOR P = [1.0, 1.0, 1.0]
VECTOR Q = [1.0, 0.000000059604644775390625, -1.0]
PRODVC S = P * Q
```

It also computes `DIV = 1 / 3` using the target's own floating format. Both computers output `SALVE ΛΟΓΟΣ`, but differ in their correctly rounded finite results.

| Variable | XXXVI-F36 | Nova-F32 |
| --- | --- | --- |
| S = P·Q | `1/16777216` | `0` |
| DIV = 1/3 | `89478485/268435456` | `11184811/33554432` |

The dot product is evaluated left-to-right, with a rounded multiplication followed by a rounded addition for each element. Reordering the sum or adding a fused multiply-add could change results, but neither is allowed by the present P2 profile.

## Verification and provenance

A reconstructed local working tree combined the previous phases' module implementations with this new float instruction and TRANFOR/P2 extension. **69 of 69 local unittest methods passed**: 59 inherited tests and 10 new vector/multiply/divide cases. The CLI generated both memory images and executed the same source on the two native CPU interpreters. The old source files in the local tree were consolidated from previous reconstructed development directories; consequently, **the exact complete GitHub tree has not yet passed clean-clone or GitHub Actions conformance**. Do not report this as remote CI evidence.

The new GitHub changes were applied as *incremental patches against the actual fetched existing source files*, rather than replacing those files with old reduced test doubles. The code and docs are published to `main` with no tag or Release.

Run:
```powershell
python -m tranfor run-vector examples/portable_dot.trf
python -m tranfor build-vector examples/portable_dot.trf --out-dir build/vectors
python -m unittest discover -s tests -p test_vectors.py -v
```

## What this adds to the fictional timeline

Scientific teams may share the same source program and the same mathematical definitions while disagreeing about which numerical results are sufficiently accurate. This produces plausible pressures for precision declarations, documented test tolerances, software high-precision libraries and stable reduction ordering. Unlike the earlier character-set controversy, the new conflict cannot be solved merely by transcoding bytes.

**Next candidates:** choose a numerical reproducibility convention; design a small user-space vector library; or study scientific program/data portability across batch-processing systems. Do not yet claim a full matrix library, operating system or standard-compliant historical floating point.

See [TRANFOR/P2](../specifications/TRANFOR-P2.md), [floating profiles](../specifications/FLOAT-P0.md), [Phase X](phase-x-floating.md).
