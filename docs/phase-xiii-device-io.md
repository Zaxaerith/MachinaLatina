# Phase XIII — Guests Can Read Records / 从宿主作业到真实机器输入

**2026-11-13. Counterfactual computer history, draft engineering profile.**

The earlier Ordo Operum/P0 host monitor could launch programs and capture their output, but programs could not receive input records. That meant it was still a one-way batch wrapper, not an interesting machine-level I/O facility.

Phase XIII introduces **CAPTA**, implemented as a distinct native input instruction in both CPU interpreters, and **ACCIPE**, the job-card instruction for consuming a prior successful output record. The guest now actually executes its own input and output instructions instead of being handed a precomputed transcript.

## Why the design must differ by machine

Machina XXXVI remains a word-addressed 36-bit machine with six packed six-bit codes and a stateful Latin/Greek printing page. Its CAPTA reads **one packed 36-bit word**. Nova-N1 is an 8-bit byte-addressed machine with direct CVL-68 text and reads **one byte**. This intentionally preserves historical path dependence instead of retrofitting byte addresses into the earlier CPU.

Both directions can share records **only after transcoding**. A text byte stream is not an executable program; incompatible native ISAs remain incompatible.

## A round trip across incompatible CPU families

```text
TRANFOR/P2 source
   ├── XXXVI compile + run ──> ACTA record 1 (CVL-68)
   └── Nova compile + run ────> ACTA record 2 (CVL-68)
                                    │
           ┌────────────────────────┴──────────────────────┐
           │                                               │
     Nova CAPTA/EMIT                                 XXXVI CAPTA/EMIT
     reads ACTA #1                                  reads ACTA #2 after
     as 8-bit bytes                                CVL-54 word transcoding
           │                                               │
     PROBA record 1                                   PROBA record 2
```

If all four jobs succeed, `PROBA.omr` contains two `SALVE ΛΟΓΟΣ` records with proper logical record boundaries. The two echo programs are native machine-code memory images, not host-level text-copy functions.

## Delivered source files

- XXXVI `CAPTA`: new opcode octal 0020, traps on missing/exhausted input.
- Nova `CAPTA`: new opcode hexadecimal 66, reads raw bytes into guest RAM.
- `ordo_operum/device.py`: strict CVL-68 → CVL-54 word translation, and direct CVL-68 byte mounting for Nova.
- `ordo_operum/monitor.py`: ACCIPE job-card parser and deterministic, successful-job-only consumption from a prior output spool.
- `examples/echo_xxxvi.m36`, `examples/echo_nova.nvi`, `examples/input_roundtrip.ord`: two genuine native echo programs and one four-job demonstration.
- `tests/test_device_input.py`: 13 focused integration-oriented test methods.
- `.github/workflows/ci.yml`: one minimal Python 3.11 GitHub Actions workflow to run the **entire repository test suite** and four-job demonstration on a clean checkout.

## Validation status

The Phase XIII source, executable-image examples and tests are in the GitHub repository. The conformance workflow is now configured to run when main changes. At documentation time, **no observed clean-checkout test/CI PASS is claimed**. In particular, earlier local Phase XII tests exercised a mock executor; the new four-job tests must be executed for real before reporting end-to-end success.

## How this changes the fictional timeline

The fictional 1970s computer operator can now schedule a computation, place its output into a named logical record, then send that record **back into an incompatible machine** as input. This is more than synchronized text display, but much less than an operating system.

The next historical problem is not automatically Unix: device record sizes, EOF reporting, restartable jobs, numeric data interchange and ownership of external storage may drive their own institutional standards. We should explore a guest-visible status channel and an actual file-input convention before describing a kernel.

See [Ordo P1 input specification](../specifications/ORDO-P1-DEVICE.md) and [Phase XII](phase-xii-batch.md).
