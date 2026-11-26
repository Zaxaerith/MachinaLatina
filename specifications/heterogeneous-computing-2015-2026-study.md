# Heterogeneous Computing after Sextaria (2015–2026)

> **DRAFT — alternate-history technical study, not an implemented CPU/GPU.** At the time of this original study Sextaria-S0 had no specified ISA or F48 arithmetic. Later S1/F48-R1 paper candidates and the MENTIS matrix contract are linked below; none is implemented or ratified. Do not assert a 48-bit tensor accelerator exists.

## Architecture split

| Candidate | Historical inheritance | Function | Engineering constraint |
| --- | --- | --- | --- |
| Nova-derived 64-bit CPU | byte-oriented commercial computing | OS, network, host scheduling | independent successor ISA, not automatically Nova-N1 compatible |
| Sextaria-inspired numerical subsystem | scientific records and precision discipline | high-precision reference and deterministic verification | can be software or coprocessor, need not use 48-bit physical words |
| Matrix accelerator | parallel algebra | low-precision / mixed-precision training and inference | bandwidth, memory capacity, interconnect, power, cooling |

## Why word width is no longer destiny

The 1976 Sextaria proposal used 6×8-bit CVL-68 characters per 48-bit data word and considered scientific precision. Neither fact yields a fast tensor core. A matrix engine may multiply low-precision inputs, accumulate in a wider format, then write a different output format. Its throughput depends on array dimensions, parallel lanes, clock, bandwidth and occupancy. It cannot be deduced from CPU word width.

The old TRANFOR prototype already demonstrated a conceptual issue: F36 preserves the increment in `1+2^-24` while F32 with nearest-even rounds to 1. Large-scale parallel reductions further change order. Possible RATIO-derived numerical declarations therefore include operand formats, accumulator precision, rounding, contraction/FMA, reduction tree, error tolerance and reference implementation. **RATIO is not an implemented compiler**.

## A credible transition

**DRAFT 2015:** independent Sextaria science workstations become expensive to maintain compared with standardized server hardware. **DRAFT 2017–2022:** scientific institutions continue using numerical verification libraries and specialist accelerator instructions without retaining old 48-bit system binaries. **DRAFT 2026:** a Nova successor coordinates general compute and specialized matrix engines; PARTES-like record services describe scientific data and reproducibility contracts.

This is a plausible software-tradition inheritance, not a claim that production 48-bit GPU chips exist or that proprietary science code automatically migrates.

## Concrete but unresolved design questions

- Will accelerator inputs use 8/16-bit formats, block floating point or other task-specific formats? **Not selected.**
- Can reductions be deterministic across parallel implementations, and at what cost?
- How are COS text, NODVS records and numerical arrays passed without excessive copies?
- What is the memory model for device kernels and DMA?
- What energy and cooling budget permits the imagined 2026 machine?

## HIST comparisons

Real Tensor Cores debuted in NVIDIA's 2017 Volta platform; the 2024 Blackwell architecture again shows the importance of mixed precision, fast interconnect and system design. These are analogies, not the fictional product roadmap.

Sources: [NVIDIA Volta](https://nvidianews.nvidia.com/news/nvidia-launches-revolutionary-volta-gpu-platform-fueling-next-era-of-ai-and-high-performance-computing), [NVIDIA Blackwell](https://investor.nvidia.com/news/press-release-details/2024/NVIDIA-Blackwell-Platform-Arrives-to-Power-a-New-Era-of-Computing/).

Related: [Phase XIX](../docs/de-machinis-cogitantibus-2015-2026.md), [Sextaria-S0](Sextaria-S0-study.md), [FLOAT-P0](FLOAT-P0.md).

## 2026-11-26 MENTIS follow-up

[Matrices R1](MENTIS-matrix-R1.md), [tokenizer R1](MENTIS-tokenizer-R1.md) and [evidence R1](MENTIS-evidence-R1.md) are later paper candidates. F48/R1 was separately proposed in Phase XXIX; no accelerator implementation or RATIO matrix grammar follows. Earlier unselected-format statements describe the original study. No trained model, benchmark or deployed assistant.
