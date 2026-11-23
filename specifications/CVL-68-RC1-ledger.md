# CVL-68/RC1 — Complete 256-Position Byte Ledger

> **Status: REVIEW CANDIDATE, NOT CANON, NON-NORMATIVE · 2026-11-23.** Full mechanical accounting of every byte. Fictional 1968 core code plus proposed later scholarly P1 additions. Compared to the original [Ledger A](CVL-68-byte-ledger.md), **only previously reserved C0–C2 receive new combining-sign meanings**. All other mappings and test vectors remain unchanged. An assigned control code is not thereby valid inside strict RC1-L text; consult the [RC1 interpretation rules](CVL-68-RC1.md).

## Structural and compatibility notes

- Basic Latin upper/lower: 41–57 and 61–77; classical Latin alphabet order excludes separate J/U/W.
- Basic Greek upper/lower: 80–97 and A0–B7; final sigma 98 is separately encoded. The letter case offset is 20 hexadecimal only for the basic blocks.
- Latin A = 41; Greek Α = 80. Similar appearance must not erase script identity.
- The spelling SALVE = 52 41 4B 54 45 (NOT ASCII spelling bytes); ΛΟΓΟΣ = 8A 8E 82 8E 91; λόγος = AA AE B8 A2 AE 98.
- B8–BF are eight legacy Ledger A scholarly combining marks; new P1 C0, C1, C2 mean breve, dot below and overline respectively. Their permitted order and base-letter restrictions are specified by RC1.
- All positions labelled RESERVED are invalid in the RC1-L strict text profile, not undiscovered glyphs.
- The Unicode column is only an **editorial comparison layer**, not evidence the alternate 1968 standards body adopted actual Unicode.
- The inventory below contains exactly 256 positions, from 00 through FF, without omissions or duplicated positions.

## Full inventory

| Byte | Meaning | Modern Unicode comparison | Kind |
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
| `C0` | COMBINING BREVE | U+0306 | Combining |
| `C1` | COMBINING DOT BELOW | U+0323 | Combining |
| `C2` | COMBINING OVERLINE | U+0305 | Combining |
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

## Allocation audit

| Kind | Number of byte values |
| --- | ---: |
| Control | **33** |
| Glyph (includes space and punctuation) | **136** |
| Combining | **11** |
| RESERVED | **76** |
| **Total** | **256** |

The three scholarly additions change the old Ledger A count **Reserved 79 / Combining 8** to **Reserved 76 / Combining 11**. There is no overlapping assignment. **Assigned ≠ valid everywhere**: a binary archive may carry bytes prohibited by the strict text profile; a device protocol may carry controls prohibited inside a text record. The P1 profile label is required to interpret the added C0–C2 marks.

See [CVL-68/RC1](CVL-68-RC1.md) for strict decoding, mark order, line breaks and migration; [original Ledger A](CVL-68-byte-ledger.md) for the preserved earlier draft.
