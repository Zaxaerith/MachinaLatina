# CVL-68 — Candidate Byte Ledger A

**Status: DRAFT, NON-NORMATIVE — version 0.2 study (2026-10-25).**

This ledger proposes **one possible full accounting of the 256 byte positions** of the fictional CVL-68 standard. `RESERVED` means **unassigned**, not a printable character or a guaranteed decoding result. No software should present this as the final interoperable mapping.

## Chosen tradeoffs

- Keep `0x00–0x1F` as 32 conventional terminal **control roles**. The ASCII-derived labels in this document are modern explanatory glosses, not necessarily the fictional Latin names.
- Reuse ASCII byte values for digits, ASCII-space and much punctuation (`0x20–0x40`), **but not for Latin letters after I**.
- Encode the **23-letter Classical Latin alphabet in continuous order**, uppercase at `0x41–0x57` and lowercase at `0x61–0x77` (case offset `0x20`). This intentionally breaks ASCII compatibility for many English words.
- Encode Greek uppercase `0x80–0x97`, lowercase `0xA0–0xB7` (case offset `0x20`), preserving **Greek alphabet order**.
- Give lowercase final sigma `ς` a distinct position `0x98`. Its relationship to `σ` for case-folding needs language-aware rules.
- Propose **eight combining diacritics** at `0xB8–0xBF`: acute, grave, circumflex/perispomeni, smooth and rough breathings, iota subscript, diaeresis and macron. The displayed Unicode equivalents are a research bridge, **not historical dependencies**.
- Leave **remaining positions reserved**; do not invent a stable glyph repertoire merely to fill every box.

## Key test examples

- `SALVE` → `52 41 4B 54 45`.
- `VERBVM` → `54 45 50 42 54 4C`.
- `ΛΟΓΟΣ` → `8A 8E 82 8E 91`.
- `Α` (Greek Alpha) → `80`; `A` (Latin A) → `41`. They are deliberately distinct.
- `λόγος` → `AA AE B8 A2 AE B1` with the acute mark encoded after the preceding vowel. **This is a provisional decomposed sequence**; Unicode `ό` may normalize differently.
- A decode/encode round trip is byte-exact only for assigned glyph sequences *without normalization*. Unicode canonical normalization or case folding **may change byte sequences** and is outside this first profile.

## Important protocol caveats

1. A diacritic byte **does not consume a new base-character position on a rendered terminal**; its placement and stacking order must be specified separately.
2. The historical Greek circumflex/perispomeni glyph is not identical in rendering to every modern font's representation; typography must be independently addressed.
3. Not every valid ancient Greek text is expressible with this table alone. Word-final sigma and breathings are represented, but other polytonic and editorial signs remain to be assigned.
4. Unicode equivalents in this document are used solely as a **comparison transcription layer**. UTF-8 is not CVL-68.
5. Latin `A` vs Greek `Α` should trigger editor warnings when mixed in one identifier but **must not collapse into one character**.
6. The use of ASCII-like control bytes is an engineering simplification in this *proposal*; an alternate code layout should be compared before freezing.

## Full 256-position inventory

| CVL byte | Meaning | Reference Unicode | Kind |
| --- | --- | --- | --- |
| `00` | NUL | — | Control |
| `01` | SOH | — | Control |
| `02` | STX | — | Control |
| `03` | ETX | — | Control |
| `04` | EOT | — | Control |
| `05` | ENQ | — | Control |
| `06` | ACK | — | Control |
| `07` | BEL | — | Control |
| `08` | BS | — | Control |
| `09` | HT | — | Control |
| `0A` | LF | — | Control |
| `0B` | VT | — | Control |
| `0C` | FF | — | Control |
| `0D` | CR | — | Control |
| `0E` | SO | — | Control |
| `0F` | SI | — | Control |
| `10` | DLE | — | Control |
| `11` | DC1 | — | Control |
| `12` | DC2 | — | Control |
| `13` | DC3 | — | Control |
| `14` | DC4 | — | Control |
| `15` | NAK | — | Control |
| `16` | SYN | — | Control |
| `17` | ETB | — | Control |
| `18` | CAN | — | Control |
| `19` | EM | — | Control |
| `1A` | SUB | — | Control |
| `1B` | ESC | — | Control |
| `1C` | FS | — | Control |
| `1D` | GS | — | Control |
| `1E` | RS | — | Control |
| `1F` | US | — | Control |
| `20` | SPACE | U+0020 | Glyph |
| `21` | ! | U+0021 | Glyph |
| `22` | " | U+0022 | Glyph |
| `23` | # | U+0023 | Glyph |
| `24` | $ | U+0024 | Glyph |
| `25` | % | U+0025 | Glyph |
| `26` | & | U+0026 | Glyph |
| `27` | ' | U+0027 | Glyph |
| `28` | ( | U+0028 | Glyph |
| `29` | ) | U+0029 | Glyph |
| `2A` | * | U+002A | Glyph |
| `2B` | + | U+002B | Glyph |
| `2C` | , | U+002C | Glyph |
| `2D` | - | U+002D | Glyph |
| `2E` | . | U+002E | Glyph |
| `2F` | / | U+002F | Glyph |
| `30` | 0 | U+0030 | Glyph |
| `31` | 1 | U+0031 | Glyph |
| `32` | 2 | U+0032 | Glyph |
| `33` | 3 | U+0033 | Glyph |
| `34` | 4 | U+0034 | Glyph |
| `35` | 5 | U+0035 | Glyph |
| `36` | 6 | U+0036 | Glyph |
| `37` | 7 | U+0037 | Glyph |
| `38` | 8 | U+0038 | Glyph |
| `39` | 9 | U+0039 | Glyph |
| `3A` | : | U+003A | Glyph |
| `3B` | ; | U+003B | Glyph |
| `3C` | < | U+003C | Glyph |
| `3D` | = | U+003D | Glyph |
| `3E` | > | U+003E | Glyph |
| `3F` | ? | U+003F | Glyph |
| `40` | @ | U+0040 | Glyph |
| `41` | A | U+0041 | Glyph |
| `42` | B | U+0042 | Glyph |
| `43` | C | U+0043 | Glyph |
| `44` | D | U+0044 | Glyph |
| `45` | E | U+0045 | Glyph |
| `46` | F | U+0046 | Glyph |
| `47` | G | U+0047 | Glyph |
| `48` | H | U+0048 | Glyph |
| `49` | I | U+0049 | Glyph |
| `4A` | K | U+004B | Glyph |
| `4B` | L | U+004C | Glyph |
| `4C` | M | U+004D | Glyph |
| `4D` | N | U+004E | Glyph |
| `4E` | O | U+004F | Glyph |
| `4F` | P | U+0050 | Glyph |
| `50` | Q | U+0051 | Glyph |
| `51` | R | U+0052 | Glyph |
| `52` | S | U+0053 | Glyph |
| `53` | T | U+0054 | Glyph |
| `54` | V | U+0056 | Glyph |
| `55` | X | U+0058 | Glyph |
| `56` | Y | U+0059 | Glyph |
| `57` | Z | U+005A | Glyph |
| `58` | RESERVED | — | Reserved |
| `59` | RESERVED | — | Reserved |
| `5A` | RESERVED | — | Reserved |
| `5B` | [ | U+005B | Glyph |
| `5C` | \ | U+005C | Glyph |
| `5D` | ] | U+005D | Glyph |
| `5E` | ^ | U+005E | Glyph |
| `5F` | _ | U+005F | Glyph |
| `60` | BACKTICK | U+0060 | Glyph |
| `61` | a | U+0061 | Glyph |
| `62` | b | U+0062 | Glyph |
| `63` | c | U+0063 | Glyph |
| `64` | d | U+0064 | Glyph |
| `65` | e | U+0065 | Glyph |
| `66` | f | U+0066 | Glyph |
| `67` | g | U+0067 | Glyph |
| `68` | h | U+0068 | Glyph |
| `69` | i | U+0069 | Glyph |
| `6A` | k | U+006B | Glyph |
| `6B` | l | U+006C | Glyph |
| `6C` | m | U+006D | Glyph |
| `6D` | n | U+006E | Glyph |
| `6E` | o | U+006F | Glyph |
| `6F` | p | U+0070 | Glyph |
| `70` | q | U+0071 | Glyph |
| `71` | r | U+0072 | Glyph |
| `72` | s | U+0073 | Glyph |
| `73` | t | U+0074 | Glyph |
| `74` | v | U+0076 | Glyph |
| `75` | x | U+0078 | Glyph |
| `76` | y | U+0079 | Glyph |
| `77` | z | U+007A | Glyph |
| `78` | RESERVED | — | Reserved |
| `79` | RESERVED | — | Reserved |
| `7A` | RESERVED | — | Reserved |
| `7B` | RESERVED | — | Reserved |
| `7C` | RESERVED | — | Reserved |
| `7D` | RESERVED | — | Reserved |
| `7E` | RESERVED | — | Reserved |
| `7F` | DEL | — | Control |
| `80` | Α | U+0391 | Glyph |
| `81` | Β | U+0392 | Glyph |
| `82` | Γ | U+0393 | Glyph |
| `83` | Δ | U+0394 | Glyph |
| `84` | Ε | U+0395 | Glyph |
| `85` | Ζ | U+0396 | Glyph |
| `86` | Η | U+0397 | Glyph |
| `87` | Θ | U+0398 | Glyph |
| `88` | Ι | U+0399 | Glyph |
| `89` | Κ | U+039A | Glyph |
| `8A` | Λ | U+039B | Glyph |
| `8B` | Μ | U+039C | Glyph |
| `8C` | Ν | U+039D | Glyph |
| `8D` | Ξ | U+039E | Glyph |
| `8E` | Ο | U+039F | Glyph |
| `8F` | Π | U+03A0 | Glyph |
| `90` | Ρ | U+03A1 | Glyph |
| `91` | Σ | U+03A3 | Glyph |
| `92` | Τ | U+03A4 | Glyph |
| `93` | Υ | U+03A5 | Glyph |
| `94` | Φ | U+03A6 | Glyph |
| `95` | Χ | U+03A7 | Glyph |
| `96` | Ψ | U+03A8 | Glyph |
| `97` | Ω | U+03A9 | Glyph |
| `98` | ς | U+03C2 | Glyph |
| `99` | · | U+0387 | Glyph |
| `9A` | ; | U+037E | Glyph |
| `9B` | RESERVED | — | Reserved |
| `9C` | RESERVED | — | Reserved |
| `9D` | RESERVED | — | Reserved |
| `9E` | RESERVED | — | Reserved |
| `9F` | RESERVED | — | Reserved |
| `A0` | α | U+03B1 | Glyph |
| `A1` | β | U+03B2 | Glyph |
| `A2` | γ | U+03B3 | Glyph |
| `A3` | δ | U+03B4 | Glyph |
| `A4` | ε | U+03B5 | Glyph |
| `A5` | ζ | U+03B6 | Glyph |
| `A6` | η | U+03B7 | Glyph |
| `A7` | θ | U+03B8 | Glyph |
| `A8` | ι | U+03B9 | Glyph |
| `A9` | κ | U+03BA | Glyph |
| `AA` | λ | U+03BB | Glyph |
| `AB` | μ | U+03BC | Glyph |
| `AC` | ν | U+03BD | Glyph |
| `AD` | ξ | U+03BE | Glyph |
| `AE` | ο | U+03BF | Glyph |
| `AF` | π | U+03C0 | Glyph |
| `B0` | ρ | U+03C1 | Glyph |
| `B1` | σ | U+03C3 | Glyph |
| `B2` | τ | U+03C4 | Glyph |
| `B3` | υ | U+03C5 | Glyph |
| `B4` | φ | U+03C6 | Glyph |
| `B5` | χ | U+03C7 | Glyph |
| `B6` | ψ | U+03C8 | Glyph |
| `B7` | ω | U+03C9 | Glyph |
| `B8` | COMBINING ACUTE | U+0301 | Combining |
| `B9` | COMBINING GRAVE | U+0300 | Combining |
| `BA` | COMBINING PERISPOMENI | U+0342 | Combining |
| `BB` | COMBINING PSILI | U+0313 | Combining |
| `BC` | COMBINING DASIA | U+0314 | Combining |
| `BD` | COMBINING YPOGEGRAMMENI | U+0345 | Combining |
| `BE` | COMBINING DIAERESIS | U+0308 | Combining |
| `BF` | COMBINING MACRON | U+0304 | Combining |
| `C0` | RESERVED | — | Reserved |
| `C1` | RESERVED | — | Reserved |
| `C2` | RESERVED | — | Reserved |
| `C3` | RESERVED | — | Reserved |
| `C4` | RESERVED | — | Reserved |
| `C5` | RESERVED | — | Reserved |
| `C6` | RESERVED | — | Reserved |
| `C7` | RESERVED | — | Reserved |
| `C8` | RESERVED | — | Reserved |
| `C9` | RESERVED | — | Reserved |
| `CA` | RESERVED | — | Reserved |
| `CB` | RESERVED | — | Reserved |
| `CC` | RESERVED | — | Reserved |
| `CD` | RESERVED | — | Reserved |
| `CE` | RESERVED | — | Reserved |
| `CF` | RESERVED | — | Reserved |
| `D0` | RESERVED | — | Reserved |
| `D1` | RESERVED | — | Reserved |
| `D2` | RESERVED | — | Reserved |
| `D3` | RESERVED | — | Reserved |
| `D4` | RESERVED | — | Reserved |
| `D5` | RESERVED | — | Reserved |
| `D6` | RESERVED | — | Reserved |
| `D7` | RESERVED | — | Reserved |
| `D8` | RESERVED | — | Reserved |
| `D9` | RESERVED | — | Reserved |
| `DA` | RESERVED | — | Reserved |
| `DB` | RESERVED | — | Reserved |
| `DC` | RESERVED | — | Reserved |
| `DD` | RESERVED | — | Reserved |
| `DE` | RESERVED | — | Reserved |
| `DF` | RESERVED | — | Reserved |
| `E0` | RESERVED | — | Reserved |
| `E1` | RESERVED | — | Reserved |
| `E2` | RESERVED | — | Reserved |
| `E3` | RESERVED | — | Reserved |
| `E4` | RESERVED | — | Reserved |
| `E5` | RESERVED | — | Reserved |
| `E6` | RESERVED | — | Reserved |
| `E7` | RESERVED | — | Reserved |
| `E8` | RESERVED | — | Reserved |
| `E9` | RESERVED | — | Reserved |
| `EA` | RESERVED | — | Reserved |
| `EB` | RESERVED | — | Reserved |
| `EC` | RESERVED | — | Reserved |
| `ED` | RESERVED | — | Reserved |
| `EE` | RESERVED | — | Reserved |
| `EF` | RESERVED | — | Reserved |
| `F0` | RESERVED | — | Reserved |
| `F1` | RESERVED | — | Reserved |
| `F2` | RESERVED | — | Reserved |
| `F3` | RESERVED | — | Reserved |
| `F4` | RESERVED | — | Reserved |
| `F5` | RESERVED | — | Reserved |
| `F6` | RESERVED | — | Reserved |
| `F7` | RESERVED | — | Reserved |
| `F8` | RESERVED | — | Reserved |
| `F9` | RESERVED | — | Reserved |
| `FA` | RESERVED | — | Reserved |
| `FB` | RESERVED | — | Reserved |
| `FC` | RESERVED | — | Reserved |
| `FD` | RESERVED | — | Reserved |
| `FE` | RESERVED | — | Reserved |
| `FF` | RESERVED | — | Reserved |

## Inventory check

- Control: **33**
- Glyph: **136**
- Reserved: **79**
- Combining: **8**

**Total: 256/256 positions accounted for**, including reserved slots.

## Decisions before a normative release

- Fix the origin and definitions of the control character semantics, including carriage return and newline.
- Decide Greek combining-mark ordering, overstriking and normalization rules.
- Compare alternate placements for Greek punctuation and math operators.
- Test a minimally useful classical Greek corpus (accented vowels and breathings) rather than assuming eight diacritics cover every editorial convention.
- Document mappings from CVL-54 (stateful) and CVL-63 (if retained as an independent standard).
- Choose whether `0x58–0x5A` and `0x78–0x7E` are reserved permanently or become mathematical signs.
