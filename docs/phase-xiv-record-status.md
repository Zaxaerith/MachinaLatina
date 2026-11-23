# Phase XIV — Status et Finis / The Birth of Queryable Record I/O

**2026-11-23 · Fictional 1970s technical history; modern Python reference implementation.**

## Where the previous phase stopped

Phase XIII introduced guest-native `CAPTA` input for both XXXVI and Nova, but a program reading past the end of its record received a machine fault. A real batch scientific software stack needs a distinguishable way to stop reading and move between records without relying on error traps.

P2 now defines `STAT` to query four device states (**DATA=0, EOR=1, EOF=2, OFFLINE=3**) and `PROX` to cross a record boundary. The source-machine differences remain: the old CPU reads packed six-bit character **words** and the Nova machine reads CVL-68 **bytes**.

## Historical plausibility and implications

The fictional early-1970s scientific centers now need to exchange not just one line but collections of structured records. Consistent EOF and EOR conventions provide a useful common vocabulary across incompatible devices. That does **not** imply the CPUs share ISA binaries, nor that the programmer can invoke a modern OS's read() syscall. The monitor is still hosted in a modern Python process.

The host card `SERIES SPOOL COUNT` allows a job to consume a strictly defined sequence of output records from a preceding batch. The earlier `ACCIPE` single-record behavior is preserved; the new path is separate so old programs are not silently upgraded.

## Reproducible cross-family demonstration

The [six-job deck](../examples/input_series.ord) provides two record-stream directions:

```text
XXXVI -> ACTA [SALVE ][ΛΟΓΟΣ] -> Nova CAPTA/STAT/PROX -> PROBA [SALVE ΛΟΓΟΣ]
Nova  -> ALTERA [SALVE ][ΛΟΓΟΣ] -> XXXVI CAPTA/STAT/PROX -> PROBA [SALVE ΛΟΓΟΣ]
```

This demonstration intentionally uses CVL-54 record lengths that avoid a padded intermediate print word, respecting an unresolved early terminal limitation rather than changing it behind the project's back.

## Verification

The [GitHub Actions run #45154527919](https://github.com/Zaxaerith/MachinaLatina/actions/runs/45154527919) passed **110/110 Python unit tests**, including native-CPU six-job replay, EOF/EOR state transitions, bad opcodes, atomic early-PROX faults, backward compatibility, missing spool records and failure rollback. The older four-job CLI replay passed as a separate workflow step.

At this milestone, the multi-record demo is covered by the *actual* integration tests on a clean GitHub checkout, not merely a mock monitor. The test suite's coverage remains bounded; a physical tape driver, status interrupts, full archive reconstruction and in-guest operating system are not implemented.

## Practical commands

```powershell
python -m ordo_operum run examples/input_series.ord --out-dir build/series
python -m ordo_operum inspect build/series/PROBA.omr
python -m unittest discover -s tests -v
```

## Next architectural tension

The host-side Ordo monitor is now beginning to resemble a supervisor, but there is still no guest-visible device selection, recoverable device-error register, memory protection, interrupt mechanism or real sequential file-open API. We should next investigate **device registers and structured I/O control blocks** (or a bounded guest-visible operating-system entry point) rather than declaring an entire Unix clone.

See the normative-candidate [P2 record interface](../specifications/ORDO-P2-STATUS.md), [P1 input interface](../specifications/ORDO-P1-DEVICE.md), and [Phase XIII](phase-xiii-device-io.md).
