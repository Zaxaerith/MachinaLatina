# COS-97/R1 — CVL-68 Migration Ledger

> **DRAFT / NOT CANON · 2026-11-24.** Generated as an editorial table from the existing [CVL-68/RC1 ledger](CVL-68-RC1-ledger.md), not an implemented converter. Exactly 256 source slots, 150 proposed CID mappings and 106 unmapped slots. This preserves the source codebook rather than copying modern Unicode numbers. Unicode names/values in the source are comparative, not COS IDs.

## Rule

For a Glyph or Combining row, or HT/LF/CR (09/0A/0D), set CID = 010000 + source byte. W1 retains that byte; C24 stores 01 00 followed by the byte. Source records must first satisfy their declared CVL text profile; in particular a lone LF in RC1-L cannot be rescued by the fact it has a COS identity. All remaining rows have no text mapping in this proposed legacy window; a device-specific control belongs to its own protocol, not automatically to a new character. RESERVED bytes never silently map. The 106 holes in 010000–0100FF are permanently invalid in R1.

| CVL byte | Source meaning | Source kind | Proposed CID | W1 | C24 |
| --- | --- | --- | --- | --- | --- |
| 00 | NUL | Control | — | — | — |
| 01 | SOH | Control | — | — | — |
| 02 | STX | Control | — | — | — |
| 03 | ETX | Control | — | — | — |
| 04 | EOT | Control | — | — | — |
| 05 | ENQ | Control | — | — | — |
| 06 | ACK | Control | — | — | — |
| 07 | BEL | Control | — | — | — |
| 08 | BS | Control | — | — | — |
| 09 | HT | Control | 010009 | 09 | 01 00 09 |
| 0A | LF | Control | 01000A | 0A | 01 00 0A |
| 0B | VT | Control | — | — | — |
| 0C | FF | Control | — | — | — |
| 0D | CR | Control | 01000D | 0D | 01 00 0D |
| 0E | SO | Control | — | — | — |
| 0F | SI | Control | — | — | — |
| 10 | DLE | Control | — | — | — |
| 11 | DC1 | Control | — | — | — |
| 12 | DC2 | Control | — | — | — |
| 13 | DC3 | Control | — | — | — |
| 14 | DC4 | Control | — | — | — |
| 15 | NAK | Control | — | — | — |
| 16 | SYN | Control | — | — | — |
| 17 | ETB | Control | — | — | — |
| 18 | CAN | Control | — | — | — |
| 19 | EM | Control | — | — | — |
| 1A | SUB | Control | — | — | — |
| 1B | ESC | Control | — | — | — |
| 1C | FS | Control | — | — | — |
| 1D | GS | Control | — | — | — |
| 1E | RS | Control | — | — | — |
| 1F | US | Control | — | — | — |
| 20 | SPACE | Glyph | 010020 | 20 | 01 00 20 |
| 21 | ! | Glyph | 010021 | 21 | 01 00 21 |
| 22 | " | Glyph | 010022 | 22 | 01 00 22 |
| 23 | # | Glyph | 010023 | 23 | 01 00 23 |
| 24 | $ | Glyph | 010024 | 24 | 01 00 24 |
| 25 | % | Glyph | 010025 | 25 | 01 00 25 |
| 26 | & | Glyph | 010026 | 26 | 01 00 26 |
| 27 | ' | Glyph | 010027 | 27 | 01 00 27 |
| 28 | ( | Glyph | 010028 | 28 | 01 00 28 |
| 29 | ) | Glyph | 010029 | 29 | 01 00 29 |
| 2A | * | Glyph | 01002A | 2A | 01 00 2A |
| 2B | + | Glyph | 01002B | 2B | 01 00 2B |
| 2C | , | Glyph | 01002C | 2C | 01 00 2C |
| 2D | - | Glyph | 01002D | 2D | 01 00 2D |
| 2E | . | Glyph | 01002E | 2E | 01 00 2E |
| 2F | / | Glyph | 01002F | 2F | 01 00 2F |
| 30 | 0 | Glyph | 010030 | 30 | 01 00 30 |
| 31 | 1 | Glyph | 010031 | 31 | 01 00 31 |
| 32 | 2 | Glyph | 010032 | 32 | 01 00 32 |
| 33 | 3 | Glyph | 010033 | 33 | 01 00 33 |
| 34 | 4 | Glyph | 010034 | 34 | 01 00 34 |
| 35 | 5 | Glyph | 010035 | 35 | 01 00 35 |
| 36 | 6 | Glyph | 010036 | 36 | 01 00 36 |
| 37 | 7 | Glyph | 010037 | 37 | 01 00 37 |
| 38 | 8 | Glyph | 010038 | 38 | 01 00 38 |
| 39 | 9 | Glyph | 010039 | 39 | 01 00 39 |
| 3A | : | Glyph | 01003A | 3A | 01 00 3A |
| 3B | ; | Glyph | 01003B | 3B | 01 00 3B |
| 3C | < | Glyph | 01003C | 3C | 01 00 3C |
| 3D | = | Glyph | 01003D | 3D | 01 00 3D |
| 3E | > | Glyph | 01003E | 3E | 01 00 3E |
| 3F | ? | Glyph | 01003F | 3F | 01 00 3F |
| 40 | @ | Glyph | 010040 | 40 | 01 00 40 |
| 41 | A | Glyph | 010041 | 41 | 01 00 41 |
| 42 | B | Glyph | 010042 | 42 | 01 00 42 |
| 43 | C | Glyph | 010043 | 43 | 01 00 43 |
| 44 | D | Glyph | 010044 | 44 | 01 00 44 |
| 45 | E | Glyph | 010045 | 45 | 01 00 45 |
| 46 | F | Glyph | 010046 | 46 | 01 00 46 |
| 47 | G | Glyph | 010047 | 47 | 01 00 47 |
| 48 | H | Glyph | 010048 | 48 | 01 00 48 |
| 49 | I | Glyph | 010049 | 49 | 01 00 49 |
| 4A | K | Glyph | 01004A | 4A | 01 00 4A |
| 4B | L | Glyph | 01004B | 4B | 01 00 4B |
| 4C | M | Glyph | 01004C | 4C | 01 00 4C |
| 4D | N | Glyph | 01004D | 4D | 01 00 4D |
| 4E | O | Glyph | 01004E | 4E | 01 00 4E |
| 4F | P | Glyph | 01004F | 4F | 01 00 4F |
| 50 | Q | Glyph | 010050 | 50 | 01 00 50 |
| 51 | R | Glyph | 010051 | 51 | 01 00 51 |
| 52 | S | Glyph | 010052 | 52 | 01 00 52 |
| 53 | T | Glyph | 010053 | 53 | 01 00 53 |
| 54 | V | Glyph | 010054 | 54 | 01 00 54 |
| 55 | X | Glyph | 010055 | 55 | 01 00 55 |
| 56 | Y | Glyph | 010056 | 56 | 01 00 56 |
| 57 | Z | Glyph | 010057 | 57 | 01 00 57 |
| 58 | RESERVED | Reserved | — | — | — |
| 59 | RESERVED | Reserved | — | — | — |
| 5A | RESERVED | Reserved | — | — | — |
| 5B | [ | Glyph | 01005B | 5B | 01 00 5B |
| 5C | \ | Glyph | 01005C | 5C | 01 00 5C |
| 5D | ] | Glyph | 01005D | 5D | 01 00 5D |
| 5E | ^ | Glyph | 01005E | 5E | 01 00 5E |
| 5F | _ | Glyph | 01005F | 5F | 01 00 5F |
| 60 | BACKTICK | Glyph | 010060 | 60 | 01 00 60 |
| 61 | a | Glyph | 010061 | 61 | 01 00 61 |
| 62 | b | Glyph | 010062 | 62 | 01 00 62 |
| 63 | c | Glyph | 010063 | 63 | 01 00 63 |
| 64 | d | Glyph | 010064 | 64 | 01 00 64 |
| 65 | e | Glyph | 010065 | 65 | 01 00 65 |
| 66 | f | Glyph | 010066 | 66 | 01 00 66 |
| 67 | g | Glyph | 010067 | 67 | 01 00 67 |
| 68 | h | Glyph | 010068 | 68 | 01 00 68 |
| 69 | i | Glyph | 010069 | 69 | 01 00 69 |
| 6A | k | Glyph | 01006A | 6A | 01 00 6A |
| 6B | l | Glyph | 01006B | 6B | 01 00 6B |
| 6C | m | Glyph | 01006C | 6C | 01 00 6C |
| 6D | n | Glyph | 01006D | 6D | 01 00 6D |
| 6E | o | Glyph | 01006E | 6E | 01 00 6E |
| 6F | p | Glyph | 01006F | 6F | 01 00 6F |
| 70 | q | Glyph | 010070 | 70 | 01 00 70 |
| 71 | r | Glyph | 010071 | 71 | 01 00 71 |
| 72 | s | Glyph | 010072 | 72 | 01 00 72 |
| 73 | t | Glyph | 010073 | 73 | 01 00 73 |
| 74 | v | Glyph | 010074 | 74 | 01 00 74 |
| 75 | x | Glyph | 010075 | 75 | 01 00 75 |
| 76 | y | Glyph | 010076 | 76 | 01 00 76 |
| 77 | z | Glyph | 010077 | 77 | 01 00 77 |
| 78 | RESERVED | Reserved | — | — | — |
| 79 | RESERVED | Reserved | — | — | — |
| 7A | RESERVED | Reserved | — | — | — |
| 7B | RESERVED | Reserved | — | — | — |
| 7C | RESERVED | Reserved | — | — | — |
| 7D | RESERVED | Reserved | — | — | — |
| 7E | RESERVED | Reserved | — | — | — |
| 7F | DEL | Control | — | — | — |
| 80 | Α | Glyph | 010080 | 80 | 01 00 80 |
| 81 | Β | Glyph | 010081 | 81 | 01 00 81 |
| 82 | Γ | Glyph | 010082 | 82 | 01 00 82 |
| 83 | Δ | Glyph | 010083 | 83 | 01 00 83 |
| 84 | Ε | Glyph | 010084 | 84 | 01 00 84 |
| 85 | Ζ | Glyph | 010085 | 85 | 01 00 85 |
| 86 | Η | Glyph | 010086 | 86 | 01 00 86 |
| 87 | Θ | Glyph | 010087 | 87 | 01 00 87 |
| 88 | Ι | Glyph | 010088 | 88 | 01 00 88 |
| 89 | Κ | Glyph | 010089 | 89 | 01 00 89 |
| 8A | Λ | Glyph | 01008A | 8A | 01 00 8A |
| 8B | Μ | Glyph | 01008B | 8B | 01 00 8B |
| 8C | Ν | Glyph | 01008C | 8C | 01 00 8C |
| 8D | Ξ | Glyph | 01008D | 8D | 01 00 8D |
| 8E | Ο | Glyph | 01008E | 8E | 01 00 8E |
| 8F | Π | Glyph | 01008F | 8F | 01 00 8F |
| 90 | Ρ | Glyph | 010090 | 90 | 01 00 90 |
| 91 | Σ | Glyph | 010091 | 91 | 01 00 91 |
| 92 | Τ | Glyph | 010092 | 92 | 01 00 92 |
| 93 | Υ | Glyph | 010093 | 93 | 01 00 93 |
| 94 | Φ | Glyph | 010094 | 94 | 01 00 94 |
| 95 | Χ | Glyph | 010095 | 95 | 01 00 95 |
| 96 | Ψ | Glyph | 010096 | 96 | 01 00 96 |
| 97 | Ω | Glyph | 010097 | 97 | 01 00 97 |
| 98 | ς | Glyph | 010098 | 98 | 01 00 98 |
| 99 | · | Glyph | 010099 | 99 | 01 00 99 |
| 9A | ; | Glyph | 01009A | 9A | 01 00 9A |
| 9B | RESERVED | Reserved | — | — | — |
| 9C | RESERVED | Reserved | — | — | — |
| 9D | RESERVED | Reserved | — | — | — |
| 9E | RESERVED | Reserved | — | — | — |
| 9F | RESERVED | Reserved | — | — | — |
| A0 | α | Glyph | 0100A0 | A0 | 01 00 A0 |
| A1 | β | Glyph | 0100A1 | A1 | 01 00 A1 |
| A2 | γ | Glyph | 0100A2 | A2 | 01 00 A2 |
| A3 | δ | Glyph | 0100A3 | A3 | 01 00 A3 |
| A4 | ε | Glyph | 0100A4 | A4 | 01 00 A4 |
| A5 | ζ | Glyph | 0100A5 | A5 | 01 00 A5 |
| A6 | η | Glyph | 0100A6 | A6 | 01 00 A6 |
| A7 | θ | Glyph | 0100A7 | A7 | 01 00 A7 |
| A8 | ι | Glyph | 0100A8 | A8 | 01 00 A8 |
| A9 | κ | Glyph | 0100A9 | A9 | 01 00 A9 |
| AA | λ | Glyph | 0100AA | AA | 01 00 AA |
| AB | μ | Glyph | 0100AB | AB | 01 00 AB |
| AC | ν | Glyph | 0100AC | AC | 01 00 AC |
| AD | ξ | Glyph | 0100AD | AD | 01 00 AD |
| AE | ο | Glyph | 0100AE | AE | 01 00 AE |
| AF | π | Glyph | 0100AF | AF | 01 00 AF |
| B0 | ρ | Glyph | 0100B0 | B0 | 01 00 B0 |
| B1 | σ | Glyph | 0100B1 | B1 | 01 00 B1 |
| B2 | τ | Glyph | 0100B2 | B2 | 01 00 B2 |
| B3 | υ | Glyph | 0100B3 | B3 | 01 00 B3 |
| B4 | φ | Glyph | 0100B4 | B4 | 01 00 B4 |
| B5 | χ | Glyph | 0100B5 | B5 | 01 00 B5 |
| B6 | ψ | Glyph | 0100B6 | B6 | 01 00 B6 |
| B7 | ω | Glyph | 0100B7 | B7 | 01 00 B7 |
| B8 | COMBINING ACUTE | Combining | 0100B8 | B8 | 01 00 B8 |
| B9 | COMBINING GRAVE | Combining | 0100B9 | B9 | 01 00 B9 |
| BA | COMBINING PERISPOMENI | Combining | 0100BA | BA | 01 00 BA |
| BB | COMBINING PSILI | Combining | 0100BB | BB | 01 00 BB |
| BC | COMBINING DASIA | Combining | 0100BC | BC | 01 00 BC |
| BD | COMBINING YPOGEGRAMMENI | Combining | 0100BD | BD | 01 00 BD |
| BE | COMBINING DIAERESIS | Combining | 0100BE | BE | 01 00 BE |
| BF | COMBINING MACRON | Combining | 0100BF | BF | 01 00 BF |
| C0 | COMBINING BREVE | Combining | 0100C0 | C0 | 01 00 C0 |
| C1 | COMBINING DOT BELOW | Combining | 0100C1 | C1 | 01 00 C1 |
| C2 | COMBINING OVERLINE | Combining | 0100C2 | C2 | 01 00 C2 |
| C3 | RESERVED | Reserved | — | — | — |
| C4 | RESERVED | Reserved | — | — | — |
| C5 | RESERVED | Reserved | — | — | — |
| C6 | RESERVED | Reserved | — | — | — |
| C7 | RESERVED | Reserved | — | — | — |
| C8 | RESERVED | Reserved | — | — | — |
| C9 | RESERVED | Reserved | — | — | — |
| CA | RESERVED | Reserved | — | — | — |
| CB | RESERVED | Reserved | — | — | — |
| CC | RESERVED | Reserved | — | — | — |
| CD | RESERVED | Reserved | — | — | — |
| CE | RESERVED | Reserved | — | — | — |
| CF | RESERVED | Reserved | — | — | — |
| D0 | RESERVED | Reserved | — | — | — |
| D1 | RESERVED | Reserved | — | — | — |
| D2 | RESERVED | Reserved | — | — | — |
| D3 | RESERVED | Reserved | — | — | — |
| D4 | RESERVED | Reserved | — | — | — |
| D5 | RESERVED | Reserved | — | — | — |
| D6 | RESERVED | Reserved | — | — | — |
| D7 | RESERVED | Reserved | — | — | — |
| D8 | RESERVED | Reserved | — | — | — |
| D9 | RESERVED | Reserved | — | — | — |
| DA | RESERVED | Reserved | — | — | — |
| DB | RESERVED | Reserved | — | — | — |
| DC | RESERVED | Reserved | — | — | — |
| DD | RESERVED | Reserved | — | — | — |
| DE | RESERVED | Reserved | — | — | — |
| DF | RESERVED | Reserved | — | — | — |
| E0 | RESERVED | Reserved | — | — | — |
| E1 | RESERVED | Reserved | — | — | — |
| E2 | RESERVED | Reserved | — | — | — |
| E3 | RESERVED | Reserved | — | — | — |
| E4 | RESERVED | Reserved | — | — | — |
| E5 | RESERVED | Reserved | — | — | — |
| E6 | RESERVED | Reserved | — | — | — |
| E7 | RESERVED | Reserved | — | — | — |
| E8 | RESERVED | Reserved | — | — | — |
| E9 | RESERVED | Reserved | — | — | — |
| EA | RESERVED | Reserved | — | — | — |
| EB | RESERVED | Reserved | — | — | — |
| EC | RESERVED | Reserved | — | — | — |
| ED | RESERVED | Reserved | — | — | — |
| EE | RESERVED | Reserved | — | — | — |
| EF | RESERVED | Reserved | — | — | — |
| F0 | RESERVED | Reserved | — | — | — |
| F1 | RESERVED | Reserved | — | — | — |
| F2 | RESERVED | Reserved | — | — | — |
| F3 | RESERVED | Reserved | — | — | — |
| F4 | RESERVED | Reserved | — | — | — |
| F5 | RESERVED | Reserved | — | — | — |
| F6 | RESERVED | Reserved | — | — | — |
| F7 | RESERVED | Reserved | — | — | — |
| F8 | RESERVED | Reserved | — | — | — |
| F9 | RESERVED | Reserved | — | — | — |
| FA | RESERVED | Reserved | — | — | — |
| FB | RESERVED | Reserved | — | — | — |
| FC | RESERVED | Reserved | — | — | — |
| FD | RESERVED | Reserved | — | — | — |
| FE | RESERVED | Reserved | — | — | — |
| FF | RESERVED | Reserved | — | — | — |

## Accounting and limits

- Source ledger: 136 graphic slots, 11 combining, 33 controls, 76 reserved.
- Mapped: 136 + 11 + 3 = 150. Unmapped: 30 other controls + 76 reserved = 106.
- No duplicate source positions or derived IDs; no mapped source byte overlaps W1 prefix D0–F1.
- Source Greek ano teleia and question mark retain distinct identities; Unicode normalization may collapse comparative transcriptions, so preserve the original bytes for lossless archival round trips.
- No claim of complete global character coverage, final CVL-68 ratification, cross-encoding normalization, or historical implementation.

See [COS-97/R1](COS-97-R1.md).
