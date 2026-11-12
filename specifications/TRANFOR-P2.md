# TRANFOR/P2 — Vector Arithmetic and Ordered Dot Products

**Status: DRAFT executable research profile, 2026-11-12.** This is a modern fictional language experiment; not a historical 1970s compiler or final scientific standard. P2 extends [TRANFOR/P1](TRANFOR-P1.md) and uses [F36/F32](FLOAT-P0.md) on the two existing CPU emulators.

## Syntax / language subset

```text
REALIS ONE = 1.0
REALIS THIRD = 3.0
FORMVLA DIV = ONE / THIRD
VECTOR P = [1.0, 1.0, 1.0]
VECTOR Q = [1.0, 0.000000059604644775390625, -1.0]
PRODVC S = P * Q
SCRIBE "SALVE ΛΟΓΟΣ"
FINIS
```

- `FORMVLA RESULT = LEFT * RIGHT` and `FORMVLA RESULT = LEFT / RIGHT` extend the old floating `+` and `-` operations. Operands must be previously defined REALIS variables. Division by zero, unrepresentable results and unsupported underflow/overflow are explicit errors.
- `VECTOR NAME = [x0, ..., xN]` declares a **fixed vector with 1–8 decimal REALIS literals**. No implicit type conversion. Elements become contiguous F36 words (one 36-bit word each) or contiguous F32 words (four bytes each).
- `PRODVC RESULT = LEFT * RIGHT` computes a **scalar dot product**, not elementwise vector multiplication, for two previously declared vectors of equal length. RESULT is a new REALIS scalar. Vectors and scalar names share the same six-character Classical Latin identifier namespace.
- `DATVM`, `CALCVLA`, `SCRIBE`, `FINIS`, single assignment and legacy character restrictions remain unchanged.
- The modern compiler uses internally generated labels such as `Z00000` and reserves all user-declared identifiers to avoid collisions; these are compiler-internal symbols, not a new machine instruction format.

## Exact execution order — critical numerical contract

For vectors `A=(a0,...,an)`, `B=(b0,...,bn)`, the dot product is:

```text
product_0 = round_fmt(a0 × b0)
sum_0     = product_0
for i = 1..n:
    product_i = round_fmt(ai × bi)
    sum_i     = round_fmt(sum_(i−1) + product_i)
result = sum_n
```

`round_fmt` means **round to each target's F36 or F32 format after each operation**, not a single final rounding of an infinite-precision sum. Order is strictly left-to-right. There is **no fused multiply-add**, parallel reduction, reassociation, vector unit or software extended accumulator. Source decimal entries are individually rounded to the target's format at declaration time.

The compiler lowers the vector expression to ordinary REALIS declarations and FORMVLA instructions; those lower to actual `FLEG/FMVL/FADD/FPON` CPU operations, not an answer calculated solely on the host at compilation. The compiler also computes **separate exact-rational format-specific expected results**, then reads actual target CPU memory to detect divergences.

## Characteristic numerical example

`P=[1, 1, 1]`, `Q=[1, 2^-24, -1]`.

- First product/sum: `1`.
- Second product: `2^-24`. XXXVI-F36 retains the exact `1+2^-24`; Nova-F32 rounds this halfway case to `1`.
- Third product: `-1`. Consequently the final dot product is **`1/16777216` in XXXVI-F36**, versus **`0` in Nova-F32**.

Both obey their format's independent rounding contract. This is not a compiler bug or bitwise portability requirement.

## Encoding and memory rules

- XXXVI: vectors contain consecutive 36-bit **word-addressed** F36 elements; `*.m36` emits the legacy octal image.
- Nova: vectors contain consecutive aligned **four-byte** F32 elements in byte-addressed memory; `*.nvi` emits the sparse hex-byte image.
- An auxiliary `*.map.json` stores source-visible/internal symbol addresses, vector element names and exact-rational expected scalar values.
- These formats are present-day test fixtures, not standard 1950s/1960s binaries.
- Existing CVL-54/CVL-68 textual limitations are unchanged. `SCRIBE` still accepts only characters representable by both systems.

## Commands

```powershell
python -m tranfor run-vector examples/portable_dot.trf
python -m tranfor build-vector examples/portable_dot.trf --out-dir build/vectors
python -m unittest discover -s tests -p test_vectors.py -v
```

This is a *bounded, unrolled* vector experiment. There is no vector-instruction opcode, dynamic indexing, general loops, matrix multiplication, bounds-checked runtime array access, float print formatting, or general scientific math library. A future TRANFOR/P3 could add these, but must declare reduction-order rules and cross-architecture accuracy expectations independently.
