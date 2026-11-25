# Nova Family Evolution — From Minor to Mobilis

> DRAFT · 2026-11-25. Candidate product architecture and implementation economics, not actual released machines or benchmark data. Builds on [the earlier PC study](Nova-personal-computer-study.md).

## 1. Minor and Media

Minor (1981–1984): an independent eight-bit programmer model, proposed eight-bit ALU and 16-bit visible byte addresses. A low-cost candidate memory organization:

| Visible range (hex) | Size | Suggested role |
| --- | ---: | --- |
| 0000–7FFF | 32 KiB | fixed RAM |
| 8000–BFFF | 16 KiB | bank window |
| C000–FFFF | 16 KiB | ROM/firmware (device mapping remains open) |

A four-bit bank selector permits 16 distinct window banks; the selector resets to zero. With all banks populated, 256 KiB bank RAM plus 32 KiB fixed RAM = 288 KiB RAM, plus 16 KiB ROM = 304 KiB mapped storage across banks, not simultaneously addressable. An inexpensive initial example could install one 16 KiB bank, 32 KiB fixed RAM and 16 KiB ROM. Selecting an uninstalled bank is a fault in this candidate abstraction. Exact bank register location, interrupt save/restore, firmware, ISA and bus cycles are not defined. Pointers within a bank window alone do not identify data when the bank changes; applications need bank metadata and OS conventions. No N1 binary support is promised.

Media (1984–1989): proposed 16-bit programmer model, 24-bit linear byte addresses (16 MiB architecture limit), 8- or 16-bit external data bus, larger RAM and graphics options. This is a separate product/ISA design direction, not a defined instruction set or a Minor binary extension. Candidate installations differ from addressing limits. Common CVL-68 text and selected document/file formats aid migration, while software normally requires recompilation or translation.

Example graphics costs: 320×200 at 1 bit per pixel = 8,000 bytes; 640×480 at 4 bits per pixel = 153,600 bytes (150 KiB). The latter already exceeds a Minor's proposed initial 48 KiB RAM; separate video RAM or lower modes help. Neither figures include fonts or buffers. Greek composition and COS rendering are separate from CPU widths.

## 2. Maior and Magna

[Common register ISA R1](Nova-Maior-Magna-R1.md) is a concrete small base for Maior 32 and Magna 64. Sixteen registers and fixed 32-bit instructions replace N1's accumulator encoding. Magna retains the same encoding envelope with explicit M64 semantics and an optional M32 mode. Legacy address size, register overflow, OS calls and ABI must be checked; a 32-bit opcode does not imply a 32-bit CPU.

The 1998–2005 transition could be motivated by large databases, scientific models, higher-resolution graphical workstations and servers. A wider integer register alone does not create double-precision floating point. A candidate F64 profile needs an independent choice of stored/implicit leading bit, exponent, rounding, special values and archive conversion. F48 compatibility can remain a software library or optional accelerator, not a mandatory bit interpretation.

## 3. Mobilis and the alternative industry split

Recommended scenario: instead of two wholly unrelated dominant ISA camps, the 2007–2026 market divides mainly by execution profiles and implementation economics. Mobilis is a low-power **Nova-derived** family, with some 32-bit legacy cores and later 64-bit profiles. Where a vendor implements the common R1 semantics, portable native subsets can share a compiler backend. A distinct compact instruction encoding may compete but would need an explicit separate profile, decoder and translation policy. No such encoding is assigned here.

Desktop/server designs prioritize throughput, memory bandwidth and large address spaces; mobile designs prioritize energy, thermal limits, integration, sleep and device interfaces. ISA is not microarchitecture: identical instruction semantics can be implemented by different pipelines, caches, clock policies and SoCs. Vendors can disagree over extension licensing, firmware and signing even when sharing base opcodes. ORDO-N/PARTES/CVSTOS remain independent OS families; a shared base ISA does not imply one OS or ABI. A rival independent mobile ISA is retained as a historical branch, not excluded by Latin culture.

## 4. Multicore and heterogeneous computing

2005–2015 candidate descendants add multicore, with a future memory model, atomic operations and cache-coherence contract. None is implicitly supported by base R1. 2015–2026 candidate systems combine general Nova cores with independent graphics/matrix accelerators. A device command/data schema can use MODVLA external representations; RATIO can declare numerical formats, reduction order and error requirements; SERMO can present reports. A GPU or matrix device has its own addressing, execution and data formats; it need not use the CPU instruction set.

Shared buffers require explicit ownership/lifetime, synchronization and address translation. DMA access is not automatically safe, and shared virtual addresses are an optional future design. Accelerator throughput cannot be inferred from CPU word size. No invented transistor count, clock, price, sales share or benchmark.

## 5. Compatibility labels

| Claim | Needed evidence |
| --- | --- |
| CVL/COS data | Declared source/target profile and loss policy |
| Source | Compatible language subset, libraries and target backend |
| ISA | Same instruction profile, mode, required extensions |
| Native application | ISA plus ABI, loader, libraries, OS service compatibility |
| Scientific result | Declared formats, order, inputs and tolerance |

Related: [history](../docs/de-nova-1981-2026.md), [OS families](operating-system-families-2005-2015.md), [Sextaria](Sextaria-S1-R1.md).
