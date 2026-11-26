# Scientific AI, Provenance and Numerical Contracts (2015–2026)

> **DRAFT — proposed research culture, not a deployed AI assistant, verification system or RATIO implementation.**

## An archive contains more than readable text

A 2026 scientist in this imagined civilization may consult XXXVI packed data, CVL-68 bilingual reports, COS multilingual documents, typed NODVS research objects and simulated data from an accelerator. They do not share the same byte encoding, numeric formats or authority.

One proposed workflow preserves **original files, source/usage rights, strict conversion logs, mathematical inputs, tool versions and independent output checks**. It distinguishes a readable source from a reproducible scientific result.

## Four output statuses

| Status | What an AI system supplies | What must be independently verified |
| --- | --- | --- |
| Generated explanation | hypothesis, translation or summary | do not label as an official original |
| Documentary citation | NODVS node/version, page or data record | confirm the source exists and the user has access |
| Executed computation | calculation, program and output | execute using declared precision and inputs |
| Human acceptance | published scientific conclusion | name responsible review authority and revision record |

A synthetic but well-formed NODVS ID is not evidence. A verified citation also does not prove the accompanying explanation is true.

## Proposed research manifest (illustrative terms only)

```text
INVESTIGATIO
    ORIGO        original source bytes and permission
    CODICATIO    CVL-54 / CVL-68 / COS decoder and version
    NODVS        document ID, location and revision
    ALGOR        model or algorithm identity
    NUMERATIO    operands, rounding and reduction order
    PROBATIO     checked result, tolerance and reviewer
FINIS
```

These are editorial Latin-flavored labels, not a working RATIO parser or data format.

## Repeatable build ≠ repeatable scientific result

A deterministic build reproduces identical binary artifacts given defined inputs; a numerical result may still depend on floating-point precision, reduction order and accelerators. The earlier F36/F32 example `1 + 2^-24` demonstrates why architecture-specific differences can be legitimate. Future RATIO-like annotations could require strict bit equality, tolerance-based equivalence or statistical replication as separately declared goals.

## Training provenance is not inference evidence

**Training provenance:** origin, permission, CVL/COS conversion, dataset curation, tokenizer version, model checkpoint and evaluation coverage.

**Inference evidence:** particular retrieved document nodes, access permissions, tool results and verification of the current answer. Merely claiming a model was trained on scholarly texts is not evidence for any particular response.

## Constraints and unresolved decisions

- Protect confidential data while making provenance auditable.
- Preserve non-Latin/Greek perspectives in a globally adopted standard.
- Never silently normalize away historical marks, mathematical signs or source metadata.
- Keep generated claims distinguishable from independent scientific checks.
- Record computational energy and available resources where relevant.
- Keep source-code, model-parameter and dataset licenses distinct.

HIST comparisons: [UNESCO 2021 AI ethics](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence), [Attention Is All You Need](https://research.google/pubs/attention-is-all-you-need/).

Related: [Phase XIX](de-machinis-cogitantibus-2015-2026.md), [COS and language models](ai-languages-and-cos-2015-2026.md), [RATIO research](programming-ecosystem-2005-2015.md).

## 2026-11-26 MENTIS follow-up

[Matrices R1](../specifications/MENTIS-matrix-R1.md), [tokenizer R1](../specifications/MENTIS-tokenizer-R1.md) and [evidence R1](../specifications/MENTIS-evidence-R1.md) are later paper candidates. F48/R1 was separately proposed in Phase XXIX; no accelerator implementation or RATIO matrix grammar follows. Earlier unselected-format statements describe the original study. No trained model, benchmark or deployed assistant.
