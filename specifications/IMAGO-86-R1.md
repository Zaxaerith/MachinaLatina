# IMAGO-86/R1 — Device-independent 2D surfaces and drawing records
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional 1984–1990 candidate, not an implemented graphics API, GPU, native driver ABI or real historical product. TABVLA remains a desktop and publishing tradition, not an ISA.

## 1. Origins and boundaries
Nova Minor's inexpensive RAM configuration is 48 KiB. A 320×200 monochrome bitmap costs 8000 octets; an independent 8 KiB video store is a plausible optional configuration, not a universal Minor feature. A 640×480 four-bit indexed screen costs 153600 octets before fonts and other buffers; Media-class systems can justify more memory or dedicated display hardware. Character ROM, font composition and pixel generation are separate: CVL code units are not glyph indices, and correct Greek breathings need layout. IMAGO accepts pixels and geometry after text layout; it never parses CVL or COS. Its contract is independent of the native CPU word and OS procedure ABI.

## 2. Surface descriptor
The host allocates an opaque context-local surface ID (nonzero u32). A descriptor declares width,height u16 (1..4096), stride u32 in octets, format u8 and exact storage length stride×height <= 64 MiB. Origin top left, x increases right, y down. Rows in order, stride at least ceiling(width×bits/8); no pixel spans rows. Padding has no pixel meaning, initialized zero and not altered by drawing. All allocated storage is initialized by the host before use. Format IDs:
| ID | Name | Layout |
| --- | --- | --- |
| 01 | MONO1 | high bit is leftmost pixel, values 0 black and 1 white |
| 02 | INDEX4 | high nibble first, 16-entry palette of big-endian R5G6B5 values |
| 03 | RGB16 | big-endian R5G6B5, red bits 15:11, green 10:5, blue 4:0 |
Palette belongs to the surface, fixed for one execution batch. Indexed values are not RGB intensities; copies between indexed surfaces require identical palettes. Unused tail bits/nibbles are preserved. Presentation timings, colorimetry, gamma, alpha, font metrics and printer formats are separate future profiles.

## 3. Bounded drawing stream
Proposed external command records, not native GPU machine code. Each starts with OP u8, flags u8 zero, total record length u16 (including header), reserved u32 zero. All multioctet numbers high-first. Batch context supplies a granted destination surface and read access to any source surfaces; IDs never encode arbitrary addresses. At most 4096 commands, total 65536 octets. Validate complete batch (including exact record boundaries, permitted surfaces and ranges) before effects. Abstract synchronous execution, ordered commands, no concurrent access during batch. Hardware implementation, fault recovery, shared buffers and device authorization left to host adapters. No raw DMA or arbitrary GPU code.

| OP | Name | Payload | Total |
| --- | --- | --- | --- |
| 01 | COMPLE | x,y,w,h u16; color u16; reserved u16 zero | 20 |
| 02 | TRANSFER | source ID u32; sx,sy,dx,dy,w,h u16 | 24 |

Rectangles half-open, w,h positive, entirely within their respective surfaces; reject overflow/out-of-range (no implicit clipping). Color must fit format (0..1, 0..15, or 0..65535). COMPLE replaces pixels. TRANSFER copies same-format pixels, preserving destination padding and using a snapshot of the source rectangle at the start of that command, including overlap in one surface. No scaling or blending. Unknown opcode/flags/length reject whole batch. Later window systems must perform clipping before submission and enforce per-surface grants; a compositor is not supplied.

## 4. Paper vector
An 8×2 MONO1 surface with stride 1 initially 00 00. COMPLE x=2,y=0,w=4,h=2,color=1:
    01 00 00 14 00 00 00 00
    00 02 00 00 00 04 00 02 00 01 00 00
Result 3C 3C, each row 00111100. This is a manual vector, not executed. RGB16 640×480 requires 614400 octets (600 KiB); double buffering needs 1200 KiB excluding metadata. Display memory and CPU RAM may differ, no asserted bus speed.

A future TABVLA layout engine could rasterize a glyph mask to an intermediate surface, then use a later transparent-mask operation; base R1 TRANSFER is opaque and cannot by itself implement arbitrary text compositing. See [FIGVRA](FIGVRA-95-R1.md), [LVDVS](LVDVS-console-study.md), [history](../docs/de-imaginibus-1975-2026.md).
