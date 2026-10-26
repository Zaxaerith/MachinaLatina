# CVL-54/P0 — Provisional Six-Bit Character Profiles

**Status: DRAFT / instructional profile; not a frozen fictional standard.**

This is the minimum concrete character assignment needed to define Machina XXXVI's first machine-word and terminal tests. It resolves enough symbols to make examples reproducible while deliberately leaving **CVL-54 as a provisional historical standard**. All character codes in this file are invented.

## Concept

Each logical code unit is six bits (0–63 decimal; 00–77 octal). Two pages use the same numeric codes:

- **LATINA:** 23 Classical Latin uppercase letters.
- **GRAECA:** 24 uppercase Greek letters.

The active page is a **terminal/stream state**, not an inherent property of the 36-bit data word. **The character codes for LATINA A and GRAECA Α are both 01 octal**; the page state disambiguates them. By contrast, later CVL-68 assigns distinct direct codes.

### Assigned positions in P0

| Decimal | Octal | LATINA | GRAECA | Semantics |
| ---: | :---: | --- | --- | --- |
| 0 | 00 | PAD | PAD | padding only at record end; not a printable NUL |
| 1 | 01 | A | Α | character |
| 2 | 02 | B | Β | character |
| 3 | 03 | C | Γ | character |
| 4 | 04 | D | Δ | character |
| 5 | 05 | E | Ε | character |
| 6 | 06 | F | Ζ | character |
| 7 | 07 | G | Η | character |
| 8 | 10 | H | Θ | character |
| 9 | 11 | I | Ι | character |
| 10 | 12 | K | Κ | character |
| 11 | 13 | L | Λ | character |
| 12 | 14 | M | Μ | character |
| 13 | 15 | N | Ν | character |
| 14 | 16 | O | Ξ | character |
| 15 | 17 | P | Ο | character |
| 16 | 20 | Q | Π | character |
| 17 | 21 | R | Ρ | character |
| 18 | 22 | S | Σ | character |
| 19 | 23 | T | Τ | character |
| 20 | 24 | V | Υ | character |
| 21 | 25 | X | Φ | character |
| 22 | 26 | Y | Χ | character |
| 23 | 27 | Z | Ψ | character |
| 24 | 30 | RESERVED | Ω | Greek letter Omega; not a LATINA character |
| 25 | 31 | 0 | 0 | shared digit |
| 26 | 32 | 1 | 1 | shared digit |
| 27 | 33 | 2 | 2 | shared digit |
| 28 | 34 | 3 | 3 | shared digit |
| 29 | 35 | 4 | 4 | shared digit |
| 30 | 36 | 5 | 5 | shared digit |
| 31 | 37 | 6 | 6 | shared digit |
| 32 | 40 | 7 | 7 | shared digit |
| 33 | 41 | 8 | 8 | shared digit |
| 34 | 42 | 9 | 9 | shared digit |
| 35 | 43 | SPACE | SPACE | shared space |
| 36 | 44 | . | . | shared full stop |
| 37 | 45 | , | , | shared comma |
| 38 | 46 | : | : | shared colon |
| 39 | 47 | ; | ; | shared semicolon |
| 40 | 50 | + | + | shared plus |
| 41 | 51 | - | - | shared minus |
| 42 | 52 | * | * | shared multiplication sign in plain text |
| 43 | 53 | / | / | shared slash |
| 44 | 54 | = | = | shared equals |
| 45 | 55 | ( | ( | left parenthesis |
| 46 | 56 | ) | ) | right parenthesis |
| 47 | 57 | ? | ? | question mark |
| 48 | 60 | SHIFT-LAT | SHIFT-LAT | set page to LATINA, no printed glyph |
| 49 | 61 | SHIFT-GRC | SHIFT-GRC | set page to GRAECA, no printed glyph |
| 50 | 62 | LF | LF | line feed |
| 51 | 63 | CR | CR | carriage return |
| 52 | 64 | EOT | EOT | end logical text record; reset page to LATINA |
| 53–63 | 65–77 | RESERVED | RESERVED | unassigned P0 slots |

## Terminal state contract P0

1. Device reset, boot, and an explicit **new logical record** select LATINA.
2. SHIFT-GRC and SHIFT-LAT persist across physical 36-bit word boundaries within that record.
3. SHIFT symbols emit no printed glyph. EOT ends a record and resets the page. LF/CR act as controls, not ordinary letters.
4. PAD = 00 may appear **only after the last meaningful symbol within a record's final machine word**, where it does not print. An interior PAD followed by meaningful data in the same record is invalid.
5. A tape/stream reader **must be supplied with record boundaries and initial state**. A raw 36-bit word containing only letter codes cannot identify its intended alphabet.
6. Accents, breathings, lowercase, final sigma, and Greek scholarly typography are **not represented** by this P0 profile; their later reconstruction must never be invented silently.

## Packing into a 36-bit word

Six codes in transmission order are packed left to right: `W = (c0 << 30) | (c1 << 24) | (c2 << 18) | (c3 << 12) | (c4 << 6) | c5`. Each `ci` is 0–63.

- `SALVE `: octal codes `22 01 13 24 05 43` → word `220113240543` (octal).
- `SHIFT-GRC ΛΟΓΟΣ`: `61 13 17 03 17 22` → `611317031722` (octal).

The printer sees `SALVE ΛΟΓΟΣ` after outputting those two words **without resetting the page between them**.

See [Machina XXXVI sample programs](../docs/machina-xxxvi-programs.md) for reproducible hexadecimal instruction/data words.

## Migration warning

This P0 table is not CVL-68's table and cannot be reinterpreted without decoding. `A` and `Α` are distinguished by state here but by distinct values in the candidate [CVL-68 byte ledger](CVL-68-byte-ledger.md). This profile is intentionally uppercase-only and cannot generate the missing original spelling of polytonic Greek text.

## Decisions pending

Printer overstrike conventions; correctness of historical spelling in full ancient Greek manuscripts; punched-card layout; escapes for scientific symbols; whether PAD/EOT assignments and record boundaries should be frozen as a later design decision.
