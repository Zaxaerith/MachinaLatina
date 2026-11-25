# RATIO-I/R1 — Numerical Contracts and Physical Quantities
## 第一代科学计算契约语言候选（1983—1985）

> REVIEW CANDIDATE / DRAFT / NOT CANON · editorial 2026-11-25. Fictional language proposal; no parser, compiler, prover, runtime or new floating-point implementation. F36/F32 refer to the existing experimental FLOAT-P0 profiles, not real historical computers. F48 remains undefined.

## 1. Why a separate scientific language?

TRANFOR expresses numerical computation; its modern P2 experiment fixes the order of rounded products and sums on each target. RATIO proposes an additional layer: a scientific result must identify its physical dimension, reference mathematical expression, evaluation format, admissible error and audit evidence. It need not replace TRANFOR as the fast numerical implementation language. It may eventually be a language of contracts around existing scientific routines.

Three independent questions must be answered: is the expression dimensionally meaningful; does the execution obey its selected numerical format; does its numerical error satisfy the requested tolerance? A correct implementation can still fail the last question. Passing a numerical contract does not prove the observations or physical model true.

## 2. Bounded source subset

Source is declared CVL-68 with an appropriate validated text profile; Latin identifiers use the classical 23 letters, digits and underscore after an initial letter. Case-sensitive names, uppercase reserved words. No J/U/W required. Unicode in the editorial Markdown is not a historical file encoding. Greek identifiers and COS support belong to later proposals. Whitespace separates tokens; decimal literals are exact rational numbers before conversion, no scientific notation in this subset. A minus sign is allowed on numeric literals. There are no loops, mutable variables, recursion or transcendental functions in R1.

    RATIO MENSVRA;
    FORMATVM F32;
    ROTVNDA PROXIMA PAR;
    ORDO SCRIPTVS;

    DATVM A: REALIS(M) = 524288;
    DATVM B: REALIS(M) = 524288.03125;
    FORMVLA D: REALIS(M) = B - A;
    TOLERANTIA D ABS 0.01 M;
    SCRIBE D;
    FINIS;

This is a paper-level candidate syntax with the following bounded grammar (EBNF is editorial):

    program = "RATIO" name ";"
              "FORMATVM" ("F32" | "F36") ";"
              "ROTVNDA" "PROXIMA" "PAR" ";"
              "ORDO" "SCRIPTVS" ";"
              { datum | formula } { tolerance } "SCRIBE" name ";" "FINIS" ";" ;
    datum = "DATVM" name ":" "REALIS" "(" unit ")" "=" decimal ";" ;
    formula = "FORMVLA" name ":" "REALIS" "(" unit ")" "="
              name ("+" | "-" | "*" | "/") name ";" ;
    tolerance = "TOLERANTIA" name "ABS" decimal unit ";" ;
    unit = "M" | "S" | "KG" | "VNVM" | "M2" | "M3" | "M_PER_S" ;

Identifiers are unique, defined once; operands must refer to previous declarations. At least one declaration and one tolerance are required. The output must have an explicit tolerance; repeated tolerances on the same name are invalid. All declared tolerances are evaluated, and a failure in any prevents acceptance of the invocation. A source declaration is not a claim of actual physical measurement.

## 3. Dimensions and exact units

Use integer dimension vector (L,T,MASS). Unit registry for this subset:

| Token | Dimension | Scale relative to metre, second, kilogram |
| --- | --- | --- |
| VNVM | (0,0,0) | 1 |
| M | (1,0,0) | 1 |
| S | (0,1,0) | 1 |
| KG | (0,0,1) | 1 |
| M2 | (2,0,0) | 1 |
| M3 | (3,0,0) | 1 |
| M_PER_S | (1,-1,0) | 1 |

Addition/subtraction require matching dimensions and return that dimension; multiplication adds exponents, division subtracts them. A result must match its declared unit. Unsupported result dimensions are rejected in R1, not silently stripped. All listed units have scale 1; conversion of centimetres, feet, angles and offset temperatures is future work. Unit identity alone does not establish coordinate reference system, datum, axis or measurement uncertainty. This deliberately small modern comparative unit vocabulary does not imply every fictional 1983 laboratory used an identical legal metrology system.

## 4. Two evaluations, one contract

For every datum x, retain its exact source rational r(x) and compute v(x) by encoding that rational in the explicitly selected FLOAT-P0 format. For each formula, evaluate the same declared binary operation twice:

- Reference r: use exact rational operands r(a), r(b) and exact rational arithmetic, no floating rounding. Division by exact zero fails.
- Execution v: use represented rational operands v(a), v(b); perform the exact operation then apply the specified target rounding once. Division by represented zero fails. Input conversion, arithmetic overflow, underflow, invalid encodings and divide-by-zero are errors according to FLOAT-P0, not infinities or NaN results.

R1 uses round-to-nearest ties-to-even, one rounding at each declaration/operation, in source order. No FMA, reassociation, extended intermediate retention, parallel reduction or hidden precision switching. A software backend on a wider processor may reproduce the chosen format, but must not claim native execution. F48 cannot be selected; a 48-bit CPU could emulate F32/F36 after its software environment is specified.

For TOLERANTIA name ABS epsilon unit, epsilon is a nonnegative exact rational in the same unit. Define error e=abs(v(name)-r(name)). The numerical contract passes if e <= epsilon. This tolerance applies to the particular declared input and expression, not all possible inputs. Both exact values may require growing rational integers; a bounded implementation must report a resource-limit error rather than manufacture a result. Exact rational reference is a mathematical specification; a real 1980s laboratory might evaluate small cases manually or on a separate verifier, not necessarily run an exact interpreter for every production array.

A result is accepted only if source/type checks, format execution, reference evaluation and all declared tolerances succeed. Distinguish STATIC_ERROR, NUMERIC_FAULT, REFERENCE_LIMIT, TOLERANCE_FAIL and ACCEPTED (editorial diagnostic labels, not source keywords). A tolerance failure retains the computed value and diagnostic but does not certify it. No output is silently replaced with the exact answer or automatically rerun at a higher precision.

## 5. Scientific evidence boundaries

Numerical error against exact declared inputs is not measurement error. A separate instrument uncertainty model, spatial CRS/datum, sampling and model error may dominate. Exact rational reference to a decimal literal does not make the physical quantity exact. Correlated input errors cannot generally be added as if independent random variables. See [audit and uncertainty study](RATIO-numeric-audit-study.md).

A run record should name the source revision, input values and provenance, units, selected arithmetic profile and revision, backend/toolchain, native versus emulated execution, operation/reduction order, result representation, exact reference if available, error and tolerance outcome. Old archival storage is not made reproducible by recording a CPU name alone. No historical binary report format, cryptographic scheme or automatic proof engine is specified.

Related: [FLOAT-P0](FLOAT-P0.md), [TRANFOR/P2](TRANFOR-P2.md), [MODVLA](MODVLA-I-R1.md), [RATIO audit](RATIO-numeric-audit-study.md), [history](../docs/de-ratione-1983-2026.md).

## 2026-11-25 Sextaria follow-up

[S1/R1](Sextaria-S1-R1.md) and [F48/R1](Sextaria-F48-R1.md) are subsequent paper candidates, not CANON or implementation. Earlier statements about undefined F48 describe the original study. Existing F32/F36 and RATIO-I accepted execution formats remain unchanged.
