# Ordo Operum/P2 — Input State, End-of-Record and End-of-File

**Status: DRAFT fictional computer standard. Implementation: 2026-11-23.** This P2 extension builds on [Ordo Operum/P1](ORDO-P1-DEVICE.md), without modifying the original CVL-54 or CVL-68 character assignments.

The 1954-derived XXXVI and 1968 Nova remain fictional architectures. The present-day Python reference interpreters now provide a **pollable record-device state** and explicit record advancement, but neither is a full guest operating system.

## Common guest status codes

| Code in accumulator A | Meaning | Next guest action |
| ---: | --- | --- |
| `0` | **DATA**: unread units in current record | CAPTA may read one native unit |
| `1` | **EOR**: record exists, no unread units | PROX may advance to next record or EOF |
| `2` | **EOF**: no further mounted record | Finish reading; PROX at EOF is idempotent |
| `3` | **OFFLINE**: no input device mounted | Report problem; CAPTA/PROX still trap |

An **empty but mounted input sequence** is EOF (2), not OFFLINE (3). An **empty first record** is EOR (1), and requires an explicit PROX to advance to subsequent records. A status query has no I/O cursor side effects.

## Two additional native CPU instructions

| Operation | XXXVI opcode (octal) | Nova opcode (hex) | Semantics |
| --- | --- | --- | --- |
| `STAT` | `0021` (decimal 17) | `67` | Read current input status code into A |
| `PROX` | `0022` (decimal 18) | `68` | Advance exactly once when at EOR; remain at EOF if already EOF |

Both opcodes require all other operand bits to equal zero; XXXVI also requires index TAG=0. These fictional assignments extend the existing ISA and do not reinterpret old opcodes.

- CAPTA remains **word-oriented on XXXVI** and **byte-oriented on Nova**.
- The input record and its cursor belong to the CPU interpreter's mounted virtual device, not its general-purpose accumulator.
- STAT overwrites the accumulator; code wanting to preserve a previously calculated number must store it first.
- PROX before EOR or while OFFLINE still **faults atomically** (PC, accumulator, record cursor and destination data remain unchanged).
- CAPTA at EOR/EOF or while OFFLINE still faults. P2 encourages the application to use STAT before CAPTA to avoid the expected end-of-input fault.
- There is no recoverable hardware error latch, interrupt, real tape drive, or device number at P2. OFFLINE provides a distinguishable status, not a promise that the missing device will reappear.

## Host-side SERIES card

The existing `ACCIPE SPOOL` card **still selects one logical record**, with its earlier successful-job-only consumption semantics unchanged. Multi-record input uses a **separate** optional card:

```text
LABOR TERTIA NOVA IMAGE
IMAGO echo_series_nova.nvi
SERIES ACTA 2
EDE PROBA
FINIS
```

`SERIES NAME COUNT` binds **exactly COUNT unread records** of a previously produced spool to a single job. COUNT is a positive decimal integer from 1 to 32. SERIES and ACCIPE are mutually exclusive. When fewer than COUNT unread records exist, the job fails without consuming records. The monitor requires a SERIES guest to advance through the final EOR and reach EOF before a completed job's output is committed; otherwise the job fails and the selected input records remain unconsumed. If the guest completes successfully, COUNT records are removed from the *logical unread queue* (the spool archive remains append-only and intact).

This is deterministic **sequential batch scheduling** with a host-side completion check, not a transactional filesystem, an application-managed stream handle or concurrent tape sessions. It does not support arbitrary guest-initiated attachment of a new spool or random access between records.

## Six native-machine jobs: two exchange directions

[examples/input_series.ord](../examples/input_series.ord) submits:

1. XXXVI compiles and writes the text `SALVE ` into the ACTA spool.
2. XXXVI compiles and writes `ΛΟΓΟΣ` into ACTA.
3. Nova runs its native CAPTA/EMIT/STAT/PROX image to consume **both** ACTA records, emitting one combined text record `SALVE ΛΟΓΟΣ` into PROBA.
4. Nova compiles and writes `SALVE ` into ALTERA.
5. Nova compiles and writes `ΛΟΓΟΣ` into ALTERA.
6. XXXVI runs its own native word-oriented CAPTA/EMIT/STAT/PROX program to consume **both** ALTERA records, emitting `SALVE ΛΟΓΟΣ` into PROBA.

**XXXVI's CVL-54 printer has an earlier P0 PAD limitation:** it cannot emit another word after a padded word within one print run. The two chosen records are deliberately aligned to full six-code units (`SALVE ` = six codes; `SHIFT-GRC ΛΟΓΟΣ` = six codes). P2 does *not* silently change that printer contract; fully general multi-record formatted output and per-record printer resets require another proposal.

## Run

```powershell
python -m ordo_operum run examples/input_series.ord --out-dir build/series
python -m ordo_operum inspect build/series/PROBA.omr
python -m unittest discover -s tests -p test_record_status.py -v
```

## Verification

[GitHub Actions run #45154527919](https://github.com/Zaxaerith/MachinaLatina/actions/runs/45154527919) passed **110/110 full-repository Python tests**, including 13 new native status/series tests. The workflow separately ran the older four-job input deck. The new six-job demonstration was also invoked by its test methods against the actual CPU interpreters; adding a separate workflow step to show the six-job CLI output in CI remains worthwhile.

The tested research implementation does not provide a real Unix-like kernel, physical EOF signals, hardware device-driver timing, byte-level tape encoding, or multiplexed user processes.

## 2026-11-26 ORDO-N follow-up

[PROTECT-R1](Nova-M32-PROTECT-R1.md) and [ORDO-N I/R1](ORDO-N-I-R1.md) are subsequent paper candidates, not a change to implemented CPU/monitor code or an approved guest OS. M64 and later profiles remain open.
