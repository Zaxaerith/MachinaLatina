# Phase IX — TRANFOR: One Source, Two Native Programs

**Status: modern research implementation and fictional language proposal (2026-11-12).** No historical compiler or antique document is being claimed.

Machina XXXVI/P0 (1954) and Machina Nova-N1 (1968) can both run their own machine code. Phase IX gives them a tiny **common source language**, provisionally called TRANFOR/P0, that compiles to both architectures without imposing binary compatibility.

## The first cross-generation source

```text
DATVM A = 7
DATVM B = 5
CALCVLA C = A + B
CALCVLA D = C - A
SCRIBE "SALVE ΛΟΓΟΣ"
FINIS
```

Each backend produces different instructions, addressing conventions, text data and machine-word sizes. Both execute with **A=7, B=5, C=12, D=5** as *named source variables* (not the CPU accumulator), and both display **SALVE ΛΟΓΟΣ** after appropriate decoding.

### Engineering significance

The original 36-bit scientific computer carries six-bit stateful character codes and needs page shifts for Greek. The newer byte-oriented computer stores distinct Latin and Greek byte values. TRANFOR does not hide this difference by calling every memory location a byte; its compiler emits two different memory-image formats and preserves the appropriate address units in its variable map.

The language introduces **NAT15** as a semantic restriction: unsigned integers from **0 through 32767 inclusive**. This narrow portable range fits both 36-bit and 32-bit integer registers, allowing simple safe addition and subtraction without inventing either architecture's later floating point conventions. Exceeding the common range is an error, not a wrapped answer.

This is deliberately *not* real FORTRAN, not a complete compiler, and not evidence that a 1950s language would inevitably look like this. The 1957 TRANFOR entry in the project's fictional timeline remains a proposed milestone, and P0 is a modern teaching model.

## Commands

```powershell
python -m tranfor run examples/portable_greeting.trf
python -m tranfor build examples/portable_greeting.trf --out-dir build/tranfor
python -m unittest discover -s tests -p test_tranfor.py -v
```

Expected output of `run`:

```text
SALVE ΛΟΓΟΣ
A=7
B=5
C=12
D=5
TRANFOR/P0: BOTH TARGETS AGREE
```

The `build` command creates `portable_greeting.m36` (36-bit octal word-image), `portable_greeting.nvi` (32-bit instruction/byte-data image) and `portable_greeting.map.json` (addresses and expected values). No Release or system installation is necessary.

## Validation and caveats

Seven dedicated TRANFOR/P0 unit tests and the command-line smoke check passed in a local reconstructed environment on 2026-11-12. The validation used **reconstructed adapters for existing XXXVI/Nova code** because direct GitHub cloning was unavailable; its result should not be described as clean-checkout CI or independent verification of the full GitHub branch. Additional integration verification against the exact existing GitHub source files remains to be done.

Major limitations: only straight-line declarations and two-variable plus/minus expressions; no input; numeric operations must precede SCRIBE; all strings must fit both legacy six-bit and newer eight-bit repertoires; no Greek lowercase/polytonic text. The compiler does not generate a relocatable object format, linker, assembler or OS process.

## The historical consequence in the imaginary world

Once universities begin sharing scientific programs, architecture divergence becomes an incentive for portable *source* distributions and multiple compiler backends, even while binary executables remain vendor-specific. Greek prestige creates pressure for richer source notation, but the legacy six-bit input devices restrict how soon such notation can become genuinely portable. This makes a plausible conflict for the 1970s: should a source-language standard prioritize the lowest-common-denominator scientific mainframe or the broader CVL-68 native alphabet?

**Next design issue:** move from NAT15 to scientifically useful floating-point numbers with explicitly documented and testable semantics, or improve the compiler with buffers and functions. These should be studied independently rather than smuggled in as unspecified default behavior.

See [TRANFOR/P0 grammar](../specifications/TRANFOR-P0.md), [Phase VIII](phase-viii-nova-n1.md), [Phase VII](phase-vii-architecture-fork.md).
