# LVDVS — Home consoles, handhelds and game portability
> DRAFT · 2026-11-26. Candidate product families and logical display profile, not an actual console ISA, ROM standard, emulator or commercial product.

## 1. 1980s tile hardware
LVDVS-I (candidate 1983–1986) may use a low-cost Nova Minor-derived CPU or independent game CPU; the Minor ISA is not specified, so no claimed binary compatibility. A dedicated display controller avoids writing every pixel every frame. Proposed logical snapshot:
| Item | Size |
| --- | ---: |
| 256 patterns, 8×8 pixels at 4 bpp | 8192 octets |
| 32×28 map of 2-octet tile entries | 1792 octets |
| 16 RGB16 palette entries | 32 octets |
| 32 sprite entries, four octets each | 128 octets |
| Total | 10144 octets |

Viewport 256×224, no scrolling in this tiny first profile. Pattern rows are four octets, high nibble leftmost. Tile entry byte 0 pattern ID, byte 1 flags: bit 0 horizontal flip, bit 1 vertical flip, other bits zero. Map row-major. Palette index 0 opaque on background. Sprite entry x u8,y u8,pattern u8,flags u8; bit 0 enable, bit 1 horizontal flip, bit 2 vertical flip, others zero. Draw enabled sprites by ascending slot, later slots overwrite earlier nontransparent pixels; sprite index 0 transparent; clip at viewport edges, no wrap. Snapshot evaluated at frame boundary, not timing-accurate bus behavior. This defines a simple compositing result, not sprite-per-scanline limit, video sync, audio, controller, DMA, physical memory bus or cartridge mapping. A full indexed bitmap would require 28672 octets (28 KiB); tile snapshot uses less for reusable patterns, but cannot represent arbitrary unique tiles simultaneously. Display output storage, game code, CPU RAM and audio excluded. Palette precision is a candidate storage choice, not a claim all low-cost displays reproduce 65536 colors simultaneously.

## 2. Candidate console generations
| Era | Family | Direction |
| --- | --- | --- |
| 1983–1986 | LVDVS I | cartridge-style games, tile/sprite display |
| 1989–1993 | LVDVS II | Media-class 16-bit direction, scrolling, audio and handheld variants |
| 1995–2001 | LVDVS III | 32-bit Maior-class or independent CPU, optical media, fixed-function 3D |
| 2006–2015 | LVDVS IV | programmable graphics and network distribution |
| 2016–2026 | LVDVS V | Magna/Mobilis-derived SoCs, independent GPU and portable engine |

No processor clock, RAM quantity beyond the tile snapshot, frame rate, sales, game library or media format is asserted. Handhelds can use distinct screen/controller/power profiles. Platform vendors may retain exclusive hardware or choose common API contracts; shared Nova lineage does not establish ROM compatibility.

## 3. Engine and preservation
A later MODVLA game engine may share simulation, assets and tools across ORDO-N, PARTES, CVSTOS and LVDVS, with target-specific native builds and graphics/audio/input/storage adapters. FIGVRA defines a small screen-space triangle contract, not a full engine. Network play needs independently specified synchronization and secure services; deterministic replay requires versioned input, tick, RNG and math contracts. Preserve original ROM bytes and metadata using STEMMA-like object identity or archive stores where licensed; emulation and recompilation are distinct approaches, neither supplied. Rebuild via FASCICVLVS target manifests only when toolchains and rights permit. No claim that assets are freely redistributable.

## 4. Games as software culture
Possible Latin interface names LVDVS (game), INCEPTVM (start), CONTINVA (continue), SERVA (save), OPTIONES (settings). Technical coinages provisional. Greek mythology, Roman history and local cultures may inspire games; language is not a constraint on genre, game rules or art style. International communities require COS display and local input; save files should not depend on display spelling alone. Real-world game titles are not copied into fictional release history.
See [IMAGO](IMAGO-86-R1.md), [FIGVRA](FIGVRA-95-R1.md), [history](../docs/de-imaginibus-1975-2026.md).
