# TRANFOR/P0 — Shared Scientific Language for XXXVI and Nova

**Status: DRAFT executable subset; modern experiment, NOT a historical implementation.**

TRANFOR is a speculative high-level programming language in Machina Latina's fictional computing history. This P0 subset demonstrates that an independently specified *source-level* numeric and text contract can target two architectures whose binary formats, memory address units and text encodings differ.

## Syntax and types

TRANFOR/P0 is a tiny **straight-line, single-assignment** language (no arrays, branches, functions, floating point or runtime input). Source files are UTF-8 for the modern implementation; neither CPU executes UTF-8.

```text
DATVM A = 7
DATVM B = 5
CALCVLA C = A + B
CALCVLA D = C - A
SCRIBE "SALVE ΛΟΓΟΣ"
FINIS
```

- `DATVM NAME = n`: declare a new **NAT15** variable, initialized to a base-10 integer `0..32767`.
- `CALCVLA NAME = LEFT + RIGHT` or `LEFT - RIGHT`: declare a *new* NAT15 variable using two previously defined variables. The result **must** remain in `0..32767`; overflow and negative subtraction are compilation errors.
- `SCRIBE "text"`: append a quoted literal to the output. Any number of SCRIBE directives may follow the numeric section; numeric statements **after** the first SCRIBE are rejected.
- `FINIS`: mandatory final statement, no executable statements afterward.
- A semicolon starts a comment **outside a quoted string**.
- Variable names are **one to six Classical Latin uppercase letters/digits**, first character a letter. The alphabet is `ABCDEFGHIKLMNOPQRSTVXYZ`, excluding J/U/W. Identifiers may not be redeclared.

The common text repertoire is the **intersection of the CVL-54/P0 and CVL-68 candidate encodings**: upper-case Latin and Greek, shared digits and punctuation, and line controls supported in both. Native CVL-68 lowercase, final sigma and polytonic marks are intentionally *not* portable to XXXVI/P0. A text literal is rejected rather than silently uppercased, transliterated or stripped of accents.

## Semantics: two distinct notions of portability

1. **Value portability**: every variable's mathematical NAT15 value is identical after execution on both computers, even though XXXVI stores it in a 36-bit word and Nova in a 32-bit word.
2. **Text portability**: observable output strings are identical after decoding each machine's own code stream. The underlying output bytes, shifts, records and instruction encodings are **not equal**.

P0 supports only compile-time-checkable, defined statements; it makes no claim about portable general 36/32-bit signed arithmetic. Numeric values and final variables are independently obtained from each emulator's simulated memory after execution.

## Backend 1: 1954 XXXVI/P0

- `DATVM` → `NVM immediate`, `PONE variable_word`.
- `CALCVLA` → `LEGE left_word`, `ADDE/SVBT right_word`, `PONE target_word`.
- `SCRIBE` → CVL-54/P0 code units with LATINA/GRAECA shift insertion, packed six units per 36-bit word; `EMIT` per packed data word.
- `FINIS` → `FIN`. Machine addresses count **36-bit words**, with data starting after the instruction section or at octal `00100`, whichever is larger.

## Backend 2: 1968 Nova-N1

- `DATVM` → `NVM immediate`, `PONW aligned_byte_address`.
- `CALCVLA` → `LEGW left_address`, `ADDE/SVBT right_address`, `PONW target_address`.
- `SCRIBE` → direct candidate CVL-68 bytes; one `EMIT byte_address` instruction per output byte.
- `FINIS` → `FIN`. Variable storage is four-byte aligned; data start at byte address `0x100` or just after the instruction section, whichever is larger.

The naive EMIT loop intentionally highlights the cost of different instruction sets. Nova-N1 has no buffer-output instruction yet; optimizing away many EMIT operations would require a newly documented ISA extension.

## Language/implementation boundaries

- No user input, loops, labels, subroutines, pointers, arrays, IO buffering, files or floating point.
- No binary portability and no attempt to execute one target's machine code on the other.
- The compiler uses its own parsed expression results as an **expected-value oracle**, then runs both target machines and checks both simulated memories; this detects mismatches but is not a formal proof of compiler correctness.
- Numeric declaration values and expression results are constrained to NAT15, avoiding undefined differences between 36-bit and 32-bit wrapping.
- The two .m36/.nvi files are **modern memory-image test fixtures**, not published ancient-world executable standards.

## Run locally

```sh
python -m tranfor run examples/portable_greeting.trf
python -m tranfor build examples/portable_greeting.trf --out-dir build/tranfor
python -m unittest discover -s tests -p test_tranfor.py -v
```

The build command emits both images and a JSON variable-address map. The map distinguishes **octal XXXVI word addresses** from **hexadecimal Nova byte addresses**.

See [Phase IX discussion](../docs/phase-ix-tranfor.md), [XXXVI/P0](Machina-XXXVI.md) and [Nova-N1](Machina-Nova-N1.md).
