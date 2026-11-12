# Phase X — Floating-Point Divergence in Two Scientific Computer Families

**Research date:** 2026-11-12. **Status:** fictional technical standards plus modern reference code; not genuine historical CPU specifications, and not IEEE 754.

## The question

Can an imagined 1954 **36-bit** computer and a 1968 **32-bit** computer both compile a common scientific programming language while obtaining different numeric answers? Yes. "Portable source" and "identical floating-point bit patterns" are separate properties.

We propose two **binary** formats with explicit normalized fractions: XXXVI-F36 (1 sign / 8 exponent / 27 fraction) and Nova-F32 (1 / 7 / 24). They use different biases, preserve only canonical zero, trap on unsupported exponent ranges, and apply round-to-nearest ties-to-even on each finite operation.

**This is a design choice, not a claim that real System/360 used binary exponent floats.** The real System/360 introduced a well-known hexadecimal-exponent short format, and IEEE 754 standardization came later.

## First numeric divergence

A source program declares:
- `X = 1.0`
- `EPS = 0.000000059604644775390625`, exactly `2^-24`
- `Y = X + EPS`

The XXXVI-F36 result for Y is **16777217/16777216**. The Nova-F32 result for Y is **1** due to the exact halfway case and ties-to-even rounding.

Both results meet the corresponding **declared semantics**. The integer variables A=7, B=5 and C=12 and the rendered message `SALVE ΛΟΓΟΣ` are identical across the two machines. Output is still restricted to the common legacy text subset and does not yet print formatted floating numbers.

## Implementation

Files: `machina_xxxvi/floating.py` (exact rational reference), extensions of `machina_xxxvi/machine.py` and `machina_nova/cpu.py` (four new float operations each), `tranfor/scientific.py` (typed dual compiler) and `examples/rounding.trf`.

CLI:

```powershell
python -m tranfor run-real examples/rounding.trf
python -m tranfor build-real examples/rounding.trf --out-dir build/floating
python -m unittest discover -s tests -p test_scientific.py -v
```

Expected source-level output:

```text
SALVE ΛΟΓΟΣ
A=7
B=5
C=12
X: XXXVI-F36=1 / Nova-F32=1
EPS: XXXVI-F36=1/16777216 / Nova-F32=1/16777216
Y: XXXVI-F36=16777217/16777216 / Nova-F32=1 [DIFFERENT ROUNDING]
TRANFOR/P1: BOTH TARGETS MATCH THEIR DEFINED FORMATS
```

## Verification provenance

A locally reconstructed Phase IX development tree (some legacy CPU files were smaller test doubles) was extended with the new math library, floating instructions, compiler and CLI. The local 11 dedicated floating tests plus 7 inherited TRANFOR tests passed, and the demo and build-real commands executed. The **full original GitHub repository was not cloned** because GitHub DNS resolution from the local container failed. The complete existing CPU files were patched through the GitHub connector instead of replacing them with local test doubles, but there is **not yet a verified full clean-checkout/CI result**. Test success should not be misreported as GitHub Actions success.

## Further research

Two formats need not remain politically neutral. Universities may favor the higher precision of a mature 36-bit scientific installation, while newer commercial 32-bit systems favor byte-oriented text and program portability. A shared language could respond with explicit precision types, software extended arithmetic and reproducibility profiles. These are future design questions, not decided consequences.

Historic comparisons:
- [IBM 704](https://www.ibm.com/history/704)
- [IBM System/360](https://www.ibm.com/history/system-360)
- [IEEE 754 standard](https://standards.ieee.org/ieee/754/6210/)
