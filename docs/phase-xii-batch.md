# Phase XII — Ordo Operum: A Bilingual Batch-Processing Civilization

**2026-11-13 · Alternate-history architectural proposal / 研究草案.** Earlier milestones built two executable computer architectures and a TRANFOR scientific compiler. This phase tests the *coordination layer*, deliberately before attempting a complete kernel.

## Historical anchors versus invention

In real computing history, early automatic job monitors reduced the need for operators to load each application by hand. Mainframe job-control conventions, compiler runs and sequential storage became important long before modern PC operating systems. In particular, IBM 709-era monitors and the later OS/360 family demonstrate the practical importance of batch workflows; our project's institutions, terms, job cards and record format are **fictional** and not IBM JCL in disguise.

This alternate world has a peculiar incentive: keeping a 36-bit scientific family operational while expanding a native eight-bit Latin/Greek ecosystem. The compromise is **source-level and data-level cooperation**, not a universal executable ABI.

## Architecture of the Phase XII prototype

```text
        common LABOR cards and TRANFOR/P2 source
                         |
               Ordo Operum/P0 host monitor
               /                         \
      XXXVI native compiler         Nova native compiler
         /                                   \
    36-bit word image                    32-bit instruction / 8-bit data image
         |                                   |
    XXXVI CPU emulator                     Nova CPU emulator
         | CVL-54                            | CVL-68
         +--------------- transcode / display text ------+
                                |
                  length-framed CVL-68 spool
                      ACTA.omr / PROBA.omr
                                |
                          report.json
```

**Important distinction:** the monitor controls modern emulator instances and translates output *after* execution. No guest program can open `ACTA.omr` via an in-CPU system call; no process manager resides inside the 1954 CPU.

## Four-job demonstration

The [sample deck](../examples/batch_science.ord) runs one scientific source on two CPUs and then runs preexisting native images on the corresponding machine. Its expected success outputs are four `SALVE ΛΟΓΟΣ` strings: two ordered records in `ACTA.omr`, two in `PROBA.omr`.

The same two TRANFOR jobs also produce architecture-specific typed-value metadata. In the scientific sample, the dot-product result can differ: XXXVI-F36 `1/16777216`, Nova-F32 `0`, without making the common text records inconsistent. The report is deliberately descriptive; comparing numeric records is not equivalent to comparing only the printable spool.

## What was actually checked

The standalone `ordo_operum` parser, archive serializer, result writer and mock-executor scheduling were exercised in 15 local tests, all passing. Cases cover invalid cards, duplicate job IDs, limits, path traversal, missing files, malformed archives, unsupported output bytes, byte-accurate framing, two records to one spool, and continuing after a failed job.

**Integration limitation:** the local GitHub network route is unavailable, so the full committed source tree was not cloned into the test environment. The tests used a small host-side shim reproducing the CVL-68 mapping and mock job execution, not a full four-job CPU run. The new GitHub monitor module calls the actual repository `tranfor.vectors`, `machina_xxxvi.machine` and `machina_nova.cpu` interfaces when installed, but that run remains an outstanding clean-checkout verification step.

## Research consequences for the alternate timeline

The standards dispute evolves in stages: common alphabets, then common source code, then **common job decks and sequential data records**. An institution can process experimental results from two incompatible computers without pretending that 36-bit and 32-bit binaries are the same.

This creates plausible institutional pressure for a common document archive, operators' handbooks, standardized numeric interchange, libraries and eventually virtualized device control. Whether these pressures culminate in a Unix-like time-sharing OS or an entirely different system should remain an open historical question, not be assumed from our own history.

## Commands

```powershell
python -m ordo_operum run examples/batch_science.ord --out-dir build/batch
python -m ordo_operum inspect build/batch/ACTA.omr
python -m unittest discover -s tests -p test_ordo.py -v
```

See [Ordo Operum/P0 technical specification](../specifications/ORDO-P0.md), [TRANFOR/P2](../specifications/TRANFOR-P2.md) and [Phase XI](phase-xi-vectors.md).
