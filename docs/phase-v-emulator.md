# Phase V — Machina XXXVI/P0 reference emulator

**Status: implementation committed; automated test execution still requires a Python environment with this checkout.**

The first implementation of the fictional 1954 Machina XXXVI is written in **Python 3.10+ using only the Python standard library**. This is a modern reference interpreter for a counterfactual architecture, not software recovered from an historical computer.

## What runs

- 36-bit word storage: 32,768 word addresses; PC wraps after 0o77777.
- Primary 36-bit accumulator A, reserved extension Q, three 15-bit X registers.
- Four-field 36-bit instruction encoding `OP12 I1 AUX5 TAG3 ADR15`.
- Exactly ten initial opcodes: FIN, LEGE, PONE, ADDE, SVBT, SALTA, SI0, PONX, EMIT, NVM.
- 6-bit CVL-54/P0 printer with persistent LATINA/GRAECA page selection.
- Octal text memory-image loader with fixed five-digit addresses and twelve-digit words.
- Bounded execution; explicit instruction and character decoding faults.
- Built-in demo plus a checked-in sample image.

## Run locally

From the repository root:

```sh
python -m machina_xxxvi demo
python -m machina_xxxvi run examples/salve_logos.m36
python -m machina_xxxvi demo --trace
python -m unittest discover -s tests -v
```

Expected demo output:

```text
SALVE ΛΟΓΟΣ
```

Use `--max-steps 1000` to limit programs or loops; the CLI defaults to 100,000 instruction steps. When tracing, instruction lines go to stderr and output text goes to stdout. The trace is a diagnostic, not a cycle-accurate history.

## Image format

One memory word per line:

```text
00000 001000000100 ; EMIT 00100
00001 001000000101 ; EMIT 00101
00002 000000000000 ; FIN
00100 220113240543 ; SALVE SPACE
00101 611317031722 ; SHIFT-GRC ΛΟΓΟΣ
```

The left column is a five-digit octal **word address**, not a character or byte offset. The right column is a 12-digit octal 36-bit word. `; comments` and blank lines are permitted. Duplicate addresses and malformed values are errors.

## Implemented contracts and intentional limits

| Topic | Current P0 behavior | Not implemented |
| --- | --- | --- |
| Integers | unsigned mod-2^36 accumulation | signed integers and floating point |
| Instructions | ten defined opcodes; reserved fields rejected | indirect addressing, privileged modes |
| Memory | 32,768 36-bit words | subword loads, byte addressing, virtual memory |
| Printer | six symbols per EMIT, page shifts | real-world device timing, paper tape controller |
| Code | Python reference execution | era-authentic punched-card compiler/assembler |
| Validation | unittest conformance cases committed | cross-platform CI and external independent oracle |

`Q` remains a reserved 36-bit extension register. `FIN` is the single all-zero instruction; all other field combinations obey the existing P0 ISA rules.

### Error handling

An instruction with I=1, nonzero AUX, invalid index TAG, undefined opcode or malformed FIN/PONX/NVM fields produces a machine fault instead of pretending that a later extension exists. A character stream with reserved codes or an illegal PAD suffix raises a character fault. The terminal stages output per 36-bit word so malformed words do not partially print.

A program without FIN eventually hits a bounded step limit. HALT occurs **only** through FIN or a trapped error, never by reading an empty/uninitialized word by intention (uninitialized memory currently contains zero, which happens to encode FIN; this is a test-harness initialization choice).

## Validation status / 验证状态

The test suite in `tests/test_machina_xxxvi.py` was created alongside the implementation; **a successful end-to-end test run has not yet been recorded** in this development environment, because the local execution container could not reach GitHub to materialize the remotely committed source. Do not claim green tests until `python -m unittest discover -s tests -v` is actually run against a synchronized checkout.

Future work: independent word-vector verification; end-to-end command-line tests; CI; assembler syntax; reliable 36-bit archival and text gateway semantics.
