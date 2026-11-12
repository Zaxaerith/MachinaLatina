# TRANFOR/P1 — Typed Scientific Arithmetic

**Status: DRAFT executable profile; extension of [TRANFOR/P0](TRANFOR-P0.md).**

P1 adds **REALIS** declarations and **FORMVLA** floating addition/subtraction, without changing P0's portable `NAT15` integers or the shared Latin–Greek text repertoire.

## Example

```text
DATVM A = 7
DATVM B = 5
CALCVLA C = A + B
REALIS X = 1.0
REALIS EPS = 0.000000059604644775390625
FORMVLA Y = X + EPS
SCRIBE "SALVE ΛΟΓΟΣ"
FINIS
```

- `DATVM NAME = unsigned_integer` and `CALCVLA RESULT = LEFT +/- RIGHT`: exactly as in P0; both operands and result must be NAT15 (0–32767).
- `REALIS NAME = decimal_literal`: parse the decimal **exactly** as a rational number, then separately round into XXXVI-F36 and Nova-F32. Decimal notation supports an optional sign, fractional digits and scientific `e` notation within a bounded literal length.
- `FORMVLA RESULT = LEFT +/- RIGHT`: both operands must be previously declared **REALIS**; evaluate from each target's previously *rounded* values and round again once after this operation.
- `SCRIBE` and `FINIS`: retain P0 restrictions (numeric operations must precede all text output). No implicit mixing or conversion between `NAT15` and `REALIS`.
- Source identifiers still use the Classical Latin 23-letter uppercase alphabet and at most six positions. Mixed-case, `J`, `U`, `W` and Greek variable identifiers remain unavailable in this legacy-portable subset.

Values in `REALIS` declarations must be encodable on **both** targets, but the encodings and their rounded meanings need not be identical. Each target's operation must remain representable in that target's own format or compilation fails. This is **architecture-specific reproducibility**, not bitwise identity.

## Compilation

Each target has its own variable memory, float literal pool and text section. F36 literals are 36-bit **word values** and F32 literals are 32-bit **big-endian byte words**. The compiler emits `FLEG/FADD/FSVB/FPON` for REALIS and retains `NVM/LEGE/ADDE/SVBT/PONE` for NAT15.

Generated artifacts:
- `*.m36`: XXXVI 12-digit octal word-image format.
- `*.nvi`: Nova sparse byte-image format.
- `*.map.json`: source variable names, distinct target addresses, types and **exact-rational expected results**.

The verification runner executes **both independent native CPU interpreters** and checks their values against their own exact-rational predictions. It compares rendered text for equality, but float values are checked **per target**, not required to equal each other.

## Commands

```powershell
python -m tranfor run-real examples/rounding.trf
python -m tranfor build-real examples/rounding.trf --out-dir build/floating
python -m unittest discover -s tests -p test_scientific.py -v
```

## Phase XI extension

`FORMVLA` also accepts scalar `*` and `/` in the experimental Phase XI implementation. This extends but does not reinterpret the earlier P1 `+` and `-` forms. `CALCVLA` remains NAT15 addition/subtraction only. [TRANFOR/P2](TRANFOR-P2.md) adds bounded vectors and ordered dot products via unrolled actual machine operations.

## Non-goals

No general functions, loops, arrays, user input, variable reassignment, real-number formatted printing, automatic numeric promotion, full polytonic Greek text, a historical 1950s compiler or interoperability with modern IEEE 754 software.

See [floating profile](FLOAT-P0.md) and [Phase X report](../docs/phase-x-floating.md).
