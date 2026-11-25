# RATIO — Numerical Audit, Precision and Scientific Uncertainty
## 数值复算与误差契约研究

> DRAFT · 2026-11-25. Paper vectors derived from FLOAT-P0; no execution of existing emulators and no new program or CI. F48 is not defined.

## 1. Worked surveying example: loss of a small difference

Consider two projected eastings A=524288 m and B=524288.03125 m, on the same hypothetical metre-based projected axis. The exact coordinate difference is 1/32 m, or 3.125 cm. This is a one-dimensional displacement, not a geodesic distance, a complete surveyed baseline, or a statement of instrument accuracy.

Both existing formats store the leading normalized fraction bit explicitly, with p=27 (F36) or p=24 (F32). At A=2^19 the normalized exponent is 20; upward representable spacing is 2^(20-p), i.e. 1/128 m on F36 and 1/16 m on F32. B lies four F36 steps above A, and exactly halfway between A and the next F32 number. Nearest-even chooses A on F32 because the stored significand for A is even.

| Quantity | Exact value (m) | F36 bits (hex) | F32 bits (hex) |
| --- | --- | --- | --- |
| A | 524288 | 4A4000000 | 54800000 |
| B | 524288.03125 | 4A4000004 | 54800000 |
| D=B-A | 0.03125 | 3E4000000 | 00000000 |

These encodings follow FLOAT-P0 bias and explicitly stored significand. The encoded F32 value of the exact displacement itself would be 3C800000. That does not rescue a displacement already lost by rounding the two coordinates first.

| Format | Computed D (m) | Absolute numerical error (m) | Tolerance 0.01 m | Tolerance 0.04 m |
| --- | ---: | ---: | --- | --- |
| F36 | 0.03125 | 0 | PASS | PASS |
| F32 | 0 | 0.03125 | FAIL | PASS |

PASS refers only to this numerical tolerance, not a valid physical survey. Both formats obey their own rounding semantics. The tolerance is exact rational; it is not rounded into the selected execution format. A program that changes tolerance must record the revised contract, not claim the old one passed.

### Mitigation without changing the machine

If the source retains exact or sufficiently precise original coordinates, subtract an explicitly declared local origin before the first F32 encoding. For origin O=524288 m, A'=0, B'=0.03125. Both values and their difference are exactly representable in F32. Record O and the transformation order. If both absolute values were previously stored only as 54800000, their lost difference cannot be recovered from those words. Recentring is an input representation strategy, not a magical correction after information loss.

## 2. Ordered reductions and backend equivalence

TRANFOR/P2 already specifies rounded products and left-to-right accumulation. For P=[1,1,1], Q=[1,2^-24,-1], exact dot product is 2^-24. F36 returns 2^-24, F32 returns 0 under the documented order. RATIO can express a corresponding acceptance contract in a future vector grammar; R1 itself has no vector syntax. Different operation ordering or an exact accumulator can yield a different answer, and would be a different evaluation profile rather than an invisible optimization.

Three suggested audit levels:

| Level | Requirement | Non-guarantee |
| --- | --- | --- |
| FORMAT | Same named arithmetic, inputs and order reproduce specified result bits or fault | Not necessarily acceptable scientific accuracy |
| TOLERANTIA | Result meets declared numerical tolerance against a reference | Different formats may both pass without identical bits |
| EVIDENTIA | Input/provenance, physical model, uncertainty and execution evidence allow independent assessment | Does not guarantee the underlying science is correct |

A Nova and future Sextaria system can meet FORMAT for F36 only if both actually implement that same format (native or software); no automatic equivalence between native F32 and native F36. R1 has exact-rational reference, not a proof for every possible input or a general certified transcendental library.

## 3. Physical uncertainty example, separate from rounding

Suppose each source easting has a hard independent-of-probability bound of ±0.02 m around its stated decimal value; no statistical distribution or error correlation is assumed. The true difference lies within [0.03125-0.04, 0.03125+0.04] m = [-0.00875, 0.07125] m. The interval includes zero. This bound follows the worst-case triangle inequality, not a confidence interval, standard deviation or proof that both endpoints are physically attainable. If a shared instrument bias cancels, a tighter bound may be defensible only with extra evidence.

For F36 D=0.03125 m, worst-case error relative to that unknown physical difference is at most 0.04 m under these assumed input bounds. For F32 D=0, the bound is at most 0.07125 m (0.03125 numerical + 0.04 input). Model/CRS error is excluded. Neither calculation alone establishes centimetre survey accuracy. A future interval profile could propagate exact rational enclosures or use outward-rounded interval arithmetic; simply applying nearest-even to both bounds is not sufficient.

## 4. Candidate report fields (not a binary format)

    CONTRACT: MENSVRA / revision 1
    SOURCE INPUTS: A=524288 M, B=524288.03125 M
    CRS/AXIS: illustrative common projected easting; no real CRS asserted
    FORMAT: XXXVI-F36 / FLOAT-P0
    ROUNDING: nearest, ties-to-even
    ORDER: source; round input then each operation
    EXACT REFERENCE: 1/32 M
    COMPUTED VALUE: 1/32 M
    REPRESENTATION: 3E4000000
    ABS NUMERIC ERROR: 0 M
    ABS TOLERANCE: 1/100 M
    NUMERIC OUTCOME: PASS (paper calculation)
    INPUT UNCERTAINTY: not supplied for base vector
    EXECUTION EVIDENCE: none; documentary worked example

The actual machine-readable metadata schema, source revision format, archival transport and validation library are open. For a real study, use precise CRS and datum metadata, documented input accuracy, and toolchain versions. RATIO does not silently reclassify derived numerical confidence as empirical truth.

Related: [RATIO I](RATIO-I-R1.md), [FLOAT-P0](FLOAT-P0.md), [TRANFOR/P2](TRANFOR-P2.md), [history](../docs/de-ratione-1983-2026.md).
