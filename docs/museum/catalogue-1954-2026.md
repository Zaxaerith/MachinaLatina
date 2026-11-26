# Catalogue — Eleven machines, 1954–2026
> DRAFT · Phase XLIV · 2026-11-26. “Profile” refers to an existing candidate specification; “exhibit configuration” is newly chosen illustrative hardware. No measured clock rates, sales, real products or complete peripheral interfaces. KiB/MiB/GiB use powers of 1024. Word-oriented capacities are expressed as equivalent octets, not byte-addressability. Disk capacities are nominal examples; controller and media format remain open.

| ID | Profile / CPU | Exhibit RAM | Architectural address ceiling | Example display or output | Example storage |
| --- | --- | --- | --- | --- | --- |
| M01 | XXXVI/P0, 36-bit accumulator | 4096 words (18 KiB equivalent) | 32768 words (144 KiB equivalent) | uppercase dual-page line printer | punched paper tape, magnetic tape option |
| M02 | N1, 32-bit accumulator | 64 KiB (not emulator default 256 KiB) | 16 MiB | character terminal, 80×24 candidate | 5 MiB disk cabinet, tape |
| M03 | Sextaria S1, 48-bit, 16 registers | 65536 words (384 KiB) | 2^24 words (96 MiB equivalent) | terminal and vector plotter | 10 MiB disk, tape |
| M04 | Nova Minor, 8-bit | 48 KiB, 16 KiB ROM separate | 64 KiB visible, banked | optional 320×200 MONO1, separate 8 KiB video store | cassette, optional removable disk |
| M05 | LVDVS I, 8-bit direction | hypothetical 2 KiB CPU RAM + separate display storage | not defined | 256×224, 16 palette entries, 32 sprites | hypothetical 32 KiB cartridge |
| M06 | Nova Media, 16-bit | 512 KiB + separate 192 KiB video RAM | 16 MiB | 640×480 INDEX4 option | 720 KiB removable disk, optional 10 MiB disk |
| M07 | Sextaria S2, 48-bit | 393216 words (2.25 MiB) | 96 MiB equivalent | 640×480 MONO1, separate 64 KiB video RAM | 20 MiB disk |
| M08 | Maior M32, 16 registers | 8 MiB + separate 2 MiB video RAM | 4 GiB | 640×480 RGB16 | 200 MiB disk |
| M09 | Magna M64, optional M32 | 512 MiB + separate 64 MiB graphics RAM | low 48-bit addresses, 256 TiB | 1024×768 color display | 40 GiB disk |
| M10 | Mobilis M32 | 512 MiB shared system RAM | M32 4 GiB architectural byte range | 480×800 touch display | 8 GiB flash |
| M11 | Nova M64 successor / PRISMA | 32 GiB host + 12 GiB device RAM | M64 candidate 256 TiB, subject to actual mapping | 2560×1440 color display | 1 TiB solid-state store |

## M01 — Machina XXXVI, 1954
Room-size bank of cabinets with paper terminal, separate operator panel, octal lamps and 36-bit word listings. Scientific batch calculation is the user scenario; 1954 software is handwritten machine code, not later TRANFOR. Six six-bit symbols fit one word, but shifts consume slots and terminal state persists. Installed memory 4096 words is this exhibit's choice. P0 defines synchronous EMIT and a tiny integer instruction set, not physical input/tape control, floating-point device or complete operating system. Later F36 research is not a retroactive shipping feature. [Profile](../../specifications/Machina-XXXVI.md).

## M02 — Nova N1, 1968
Cabinet-based business installation with separate text terminal, tape reels and disk unit. Direct basic Latin/Greek CVL-68 candidate bytes remove page shifting in text, without implying polytonic composition or all later RC1 assignments already shipped. User reads inventory lists, types transactions and prints reports; a hypothetical monitor and data-processing software are product concepts, not an implemented kernel. N1 fixed 4-byte instructions and byte addressing do not execute XXXVI words. [Profile](../../specifications/Machina-Nova-N1.md), [CVL](../../specifications/CVL-68-RC1.md).

## M03 — ACRIBIA Sextaria S1, 1978
Modular scientific cabinet, instrument terminal and pen plotter. F48 with 38 explicit significant bits is the scientific selling point, not display quality or text density. 65536 six-octet words = 393216 octets. TRANFOR-style scientific programs need a new compiler backend; candidate field survey or astronomy routines are not shipped applications. S1 has no protection, paging or physical peripherals specified. [S1](../../specifications/Sextaria-S1-R1.md), [F48](../../specifications/Sextaria-F48-R1.md).

## M04 — DOMESTICA D1, 1981
Cream-colored low desktop keyboard chassis and separate monochrome display, optional cassette recorder. Visible memory 32 KiB fixed RAM, 16 KiB bank window, 16 KiB ROM; installed one bank initially. 320×200 one-bit frame takes 8000 octets, fits separate 8 KiB store if display controller exists. School users type short programs and simple documents; ROM monitor/editor and language interpreter are candidate applications, not an already specified interpreter. CVL storage and glyph rendering are different capabilities. No N1 binary compatibility. [Minor](../../specifications/Nova-family-evolution-study.md).

## M05 — ARCADIA LVDVS I, 1985
Low horizontal console with cartridge slot, two detachable controller ports and television output. Candidate CPU RAM and cartridge capacity above are distinct from graphics storage. The R1 snapshot consists of 8192 pattern octets, 1792 map octets, 32 palette octets, 128 sprite octets = 10144 total. Allow an illustrative dedicated 12 KiB graphics store; no actual memory map or timing asserted. Games such as the earlier Iter Romanvm concept may explore tile reuse, not a released title. Controller, audio, cartridge bus and full game CPU ISA remain undefined. [LVDVS](../../specifications/LVDVS-console-study.md).

## M06 — DOMESTICA D2, 1986
Beige desktop case, separate keyboard, pointer device and removable disk drives. 640×480 four-bit indexed framebuffer = 153600 octets (150 KiB), fits proposed 192 KiB separate video store. TABVLA-style workspace, text editor and publishing tools are plausible; PAGINA FORMA I is dated 1987, not preinstalled in a 1986 launch exhibit. Media is a separate 16-bit family, not a binary-compatible Minor extension. [Nova family](../../specifications/Nova-family-evolution-study.md), [IMAGO](../../specifications/IMAGO-86-R1.md).

## M07 — ACRIBIA Sextaria S2, 1989
Tall professional desk-side cabinet, high-resolution mono monitor, plotting peripherals and scientific keyboard. S2 retains S1 word and lane model, adds USER/SUPERVISOR and contiguous relocatable regions (not paging). The 2.25 MiB installation is the previous dossier's 393216 complete words. A 640×480 monochrome frame occupies 38400 octets. PARTES-style typed record services, engineering drawing, spatial analysis and numerical library are candidate software. GEOGRAPHIA is a later ecosystem concept, not an asserted 1989 shipping version. Full drivers, shared memory and actual IPC implementation are open. [S2](../../specifications/Sextaria-S2-PROTECT-R1.md), [PARTES](../../specifications/PARTES-I-R1.md).

## M08 — OFFICINA NOVA Maior, 1993
Modular tower or desktop chassis, expansion slots, separate RGB monitor and bilingual keyboard. M32 has 16 writable registers, four-byte instructions and candidate 4 KiB page protection; 8 MiB installed is not the 4 GiB address ceiling. ORDO-N I desktop and file services, MODVLA and scientific software are product directions. 640×480 RGB16 single color surface needs 600 KiB; 2 MiB video store is a proposed installation, not proof of 3D support. FIGVRA-95 belongs to a later candidate generation. [Maior](../../specifications/Nova-Maior-Magna-R1.md), [PROTECT](../../specifications/Nova-M32-PROTECT-R1.md), [ORDO-N](../../specifications/ORDO-N-I-R1.md).

## M09 — OFFICINA NOVA Magna, 2003
Tower system, optical drive, flat-panel option and network port. M64 has 64-bit registers but 48-bit effective address profile; optional M32 mode preserves selected ISA semantics, not the complete OS/ABI. 512 MiB installed and 64 MiB graphics store are new exhibit choices. COS C24/W1 and NODVS/LIGAMEN/RETE exchange are era-appropriate candidates. Fetch-only RETE R1 does not establish commercial login or write protocols. M64 protection, native loader, full floating-point and actual network/graphics drivers remain open. [Magna](../../specifications/Nova-Maior-Magna-R1.md), [COS](../../specifications/COS-97-R1.md).

## M10 — DOMESTICA Mobilis, 2011
Touchscreen handheld, compact solid-state enclosure, soft Latin/Greek input pages and separate charging/data interface. M32-derived candidate SoC and CVSTOS installation-scoped permissions; 512 MiB system RAM, 8 GiB flash and 480×800 display are exhibit choices. CVSTOS II distribution direction does not mean signing formats or actual phone hardware are specified. Documents, navigation and games are possible application categories, not a catalogue of released apps. Native desktop programs are not automatically compatible. [Mobilis](../../specifications/Nova-family-evolution-study.md), [CVSTOS](../../specifications/CVSTOS-I-R1.md).

## M11 — Nova / PRISMA workstation, 2026
Repairable tower, replaceable graphics board and cooling, high-resolution monitor; 32 GiB host RAM and 12 GiB separate device RAM, not a unified 44 GiB GPU allocation. ORDO-N or PARTES application environment with MENTIS local/remote assistance, FIGVRA graphics and MATRICES M16/F32 reference contract as candidate directions. No 2030s Memoria R1, F64/R0, LVMEN or CONCORDIA retroactively installed. An 8-billion-parameter dense model at hypothetical 4-bit storage requires 4e9 octets of weights alone; actual memory, throughput and device compatibility depend on missing quantization, runtime, cache and driver contracts. [Heterogeneous study](../../specifications/heterogeneous-computing-2015-2026-study.md), [MATRICES](../../specifications/MENTIS-matrix-R1.md), [MENTIS](../de-mente-1965-2026.md).

See [visitor guide](visitor-guide.md) for relative purchase-cost scenarios, input conventions and compatibility. All configurations, peripherals and physical appearances are textual exhibit proposals; no rendered product images or new programs.
