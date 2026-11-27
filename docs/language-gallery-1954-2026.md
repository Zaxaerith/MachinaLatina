# Comparative language gallery (1954–2026)
> Phase XLV · DRAFT / NOT CANON. Editorial UTF-8 transcriptions; paper examples, not compiled or run. Existing subsets and future pseudocode are distinct.

A laboratory has seven samples, receives one more and needs to record eight. The four languages address different parts of the workflow.

## MXA/P0
The existing [greeting](../examples/salve_logos.mxa) uses ORG, EMIT and FIN with separate data words and a Greek page switch. It illustrates machine-specific output rather than sample arithmetic.

## TRANFOR/P0

    DATVM A = 7
    DATVM B = 1
    CALCVLA C = A + B
    SCRIBE "SALVE ΛΟΓΟΣ"
    FINIS

Expected C=8 in NAT15; SCRIBE prints a literal, not C. [P0](../specifications/TRANFOR-P0.md).

## MODVLA-I/R1

    MODVLVM MENSVRA;
    LINGVA LATINA;
    INTERFACIES;
        RECORDVM SPECIMEN;
            NVMERVS: NAT24;
        FINIS;
        EXTERNA SPECIMEN;
            NVMERVS AD 0;
            LONGITVDO 3;
            ORDO ALTVS;
        FINIS;
        OPVS SEQVENS(R: SPECIMEN): NAT24;
    FINIS;
    CORPVS;
        OPVS SEQVENS(R: SPECIMEN): NAT24;
            REDDE R.NVMERVS + 1;
        FINIS;
    FINIS;
    FINIS MODVLI;

Input record octets 00 00 07; logical return 8. A separate caller can construct a new record 00 00 08. No implied mutation or serialization call. NAT24 maximum fails checked addition. [R1](../specifications/MODVLA-I-R1.md).

## RATIO-I/R1

    RATIO SPECIMINA;
    FORMATVM F32;
    ROTVNDA PROXIMA PAR;
    ORDO SCRIPTVS;
    DATVM A: REALIS(VNVM) = 7;
    DATVM B: REALIS(VNVM) = 1;
    FORMVLA C: REALIS(VNVM) = A + B;
    TOLERANTIA C ABS 0 VNVM;
    SCRIBE C;
    FINIS;

Paper result: 8, exact reference 8, error 0. A fixed-width integer is more natural for a count; this illustrates the contract. A precision-sensitive [existing audit](../specifications/RATIO-numeric-audit-study.md) uses 524288 m and 524288.03125 m; F32 rounds both inputs to the same value and returns zero, failing 0.01 m tolerance. F36 preserves the difference. Neither proves the physical survey correct.

## SERMO-I/R1

    OPVS SEQVENS(N: NAT): NAT;
        REDDE N + 1;
    FINIS;

    FORMA RELATIO(N: NAT);
        SIT C: NAT = SEQVENS(N);
        TITVLVS 1 = "SPECIMINA";
        PARAGRAPHVS 2 = "SALVE ΛΟΓΟΣ";
    FINIS;

Paper result C=8 for N=7; the document contains title and greeting, not the number. NAT-to-TEXTVS conversion requires later library or host support. Registry and NODVS validation, then authorized host publication, are separate. [R1](../specifications/SERMO-I-R1.md).

## 2016–2026 design notebook

Conceptual pseudocode only, not grammar:

    MODVLA:
        owner := allocate buffer
        view := borrow read-only owner
        inspect(view)
        end view
        transfer owner to worker
        old owner is no longer usable

    SERMO:
        observations |> filter valid |> map title
        publish through granted host service

    RATIO:
        Δx := x₂ − x₁
        declare units, format, order and tolerance
        evaluate; preserve result and evidence separately

Greek and subscript identifiers need a new declared lexical profile; not R1 syntax. Formal lifetimes, effects, allocation and parsing are open. Same mathematical answer does not imply identical bytes, instructions, native ABI or permission to publish.
