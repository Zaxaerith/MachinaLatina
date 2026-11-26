# FIGVRA-95/R1 — Screen-space scientific and entertainment rasterization
> REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-26. Fictional 1993–1998 candidate. Bounded fixed-function triangle profile, not a complete 3D API, shader language or implemented accelerator.

## 1. Geometry versus display
Sextaria F48 calculations may retain precise model coordinates while Nova game systems favor lower-cost fixed-point transformations. Neither CPU format is a pixel format. Host transforms and clips geometry into bounded screen coordinates, quantizes to signed Q12.4 (s16, value raw/16), and supplies a depth value u16. In this baseline all vertices must be inside the closed viewport rectangle [0,W]×[0,H], with W,H 1..1024. No implicit 3D transformation, perspective divide, near-plane clip, texture sampling or lighting. A GIS program must preserve source CRS, units and precision separately; a displayed mesh is not a substitute for original data.

## 2. Target and triangle records
Context supplies an authorized RGB16 surface per IMAGO and a separate equal-size tightly packed big-endian u16 depth surface. Depth clear value FFFF; smaller depth nearer, valid vertex depths 0..65534. Initial color chosen by host. One TRIANGVLVM record: OP=10 hex, flags zero, length u16=28, reserved u32 zero (same 8-octet envelope convention as IMAGO). Payload: three vertices, each x s16, y s16, z u16 (18 octets total), flat color u16 RGB16. All multioctet fields big-endian. No padding. This is a separate FIGVRA batch profile; IMAGO-only readers reject opcode 10. Maximum 4096 triangles and 114688 octets; validate whole batch including access and vertex ranges before rasterizing. Degenerate zero-area triangles are legal no-ops. No asynchronous execution, concurrent target access or failure rollback for hardware malfunction in the paper model.

## 3. Exact raster contract
Compute oriented edge E(a,b,p)=(bx-ax)(py-ay)-(by-ay)(px-ax), using raw Q12.4 integer coordinates. Swap vertices 1 and 2 (including depth) if signed area E(v0,v1,v2) is negative. For positive area and y increasing down, a directed edge is inclusive when dy<0 or (dy=0 and dx>0). Pixel center (i,j) is raw (16i+8,16j+8). A sample is covered when all three edge values are positive or zero on an inclusive edge. Iterate only legal target pixels. This top-left rule assigns shared edges once for adjacent consistently quantized nondegenerate triangles; no antialiasing. Compute depth as nearest-even integer of exact barycentric interpolation: (E(v1,v2,p)z0+E(v2,v0,p)z1+E(v0,v1,p)z2)/area. Use sufficient integer width (signed 64-bit intermediates suffice for this bounded viewport); no wrap. Write color and depth iff new depth strictly less than stored depth; ties retain earlier fragment. No blending. Results are specified by arithmetic, not by hardware execution order outside this synchronous profile.

## 4. Worked vector
4×4 target initially black RGB16 0000 and depth FFFF. Triangle vertices (0,0),(4,0),(0,4), all z=1000 decimal (03E8), color F800 (red). Exact record:
    10 00 00 1C 00 00 00 00
    00 00 00 00 03 E8
    00 40 00 00 03 E8
    00 00 00 40 03 E8
    F8 00
Expected mask (X=red):
    XXX.
    XX..
    X...
    ....
Six pixel centers satisfy x+y<4; centers on descending diagonal are excluded. Draw same triangle at depth 2000: no change. At depth 500 with color 07E0: the six pixels become green. This is a manual example, not a GPU execution result. At 640×480, RGB16 plus u16 depth requires 1200 KiB; adding a second color buffer requires another 600 KiB.

## 5. Later evolution, not defined by R1
1995–2005: texture coordinates, perspective-correct interpolation, depth/stencil, hardware transformation, tile rendering. 2005–2015: programmable vertex/fragment stages, separate shader modules and typed pipeline interfaces, with explicit resource bindings. 2015–2026: independent compute queues, synchronization, ownership and matrix accelerators. Shader ISA, floating arithmetic profiles, GPU memory model, command submission, fences, fault isolation, device DMA and driver ABI remain open. RATIO may audit declared computation separately from visual raster rules; rendering success does not prove scientific accuracy. See [IMAGO](IMAGO-86-R1.md) and [history](../docs/de-imaginibus-1975-2026.md).
