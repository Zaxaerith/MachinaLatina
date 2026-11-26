# LVMEN — Optical links, conversion costs and hybrid systems
> FUTURE SCENARIO / DRAFT · 2026-11-26. Architecture alternatives only. No measured link, manufacturing forecast, deployed system or new programming language.

## 1. Three separate device roles
LVMEN links: electronic serialization, optical modulation, propagation, detection, electronic decoding and integrity checks. A link transfers bytes, not a shared-memory authority. Candidate package/die links, board links and datacentre networks have different distances and budgets. No specified encoding, wavelength plan, FEC, framing, latency, cache coherence or RETE security. Optical transport can carry existing external byte records only through a defined adapter.
LVMEN compute: calibrated approximate linear transform, electronic conversion/control and optional digital verification. Use a separate numerical profile from exact ordered MATRICES and high-precision Sextaria. Nonlinear operators, storage and general branch/control remain electronic in the preferred branch.
LVMEN hybrid system: Nova Memoria broker grants resources, transfers ownership, checks completion. CPU and electronic GPU/NPU remain available. No new privileged ISA or optical general-purpose OS.

## 2. Illustrative link budget
Assume 8 parallel optical channels each carrying 50 Gbit/s gross, aggregate 400 Gbit/s = 50 GB/s decimal. Assume net payload efficiency 80%, yielding 40 GB/s; 1 GiB payload requires at least 26.84 ms of payload serialization under sustained assumed capacity, excluding setup, propagation, queueing, retries and copies. No actual device is claimed. For end-to-end energy, include laser power (including idle share), modulators, receivers, conversion, clocking, electronic interfaces, cooling and errors/retries; link energy does not equal total job energy.

## 3. Compare whole jobs rather than optical core speed
Illustrative serialized time model T = T_setup + T_move + T_encode + T_core + T_decode + T_verify. Overlap can change critical path but is not assumed. Example digital job 10 ms; optical candidate setup 1 ms, transfer 2 ms, input conversion 1 ms, core 0.2 ms, output conversion 1 ms, reference verification 8 ms = 13.2 ms, slower despite a fast core. A later independently qualified workload with 1 ms verification would total 6.2 ms under otherwise identical assumptions; it is NOT the full audit R1 and needs its own acceptance contract. All times synthetic, not measured or predicted. Compare energy, accuracy, utilization, throughput, calibration, area, lifecycle costs and workload size as well as latency.

## 4. Programming and deployment
MODVLA candidate service manifests declare shape, numerical profile, tolerance, calibration requirement, buffer grants, latency/resource limits, exact/approximate nature and fallback policy. The R1 photonic service is a separate adapter, not new compiler syntax or native ABI. A portable application may ask for a capability rather than a specific physical device, provided requested arithmetic is preserved. Exact MATRICES tasks must not be silently mapped to approximate LVMEN. RATIO contract extensions and heterogeneous scheduling remain future work. ORBIS may use qualified linear surrogate inference, but scientific validation and physical control stay independent. End-device use depends on power and packaging; datacentre adoption may precede mobile integration.

Preferred branch: optical interconnect first, selective approximate acceleration second. Alternatives: links alone succeed while compute remains electronic; specialized optical appliances remain niche; integration stalls due to cost or precision. No assumption of general optical RAM or an all-optical CPU.
See [photonic R1](LVMEN-photonic-R1.md), [Memoria](Nova-Memoria-R1.md), [ORBIS](ORBIS-world-model-study.md), [future history](../docs/de-lvmine-2040-2045.md).

## Phase XLII future scenario

[CONCORDIA task federation R1](CONCORDIA-task-federation-R1.md) and [personal computing study](CONCORDIA-personal-computing-study.md) propose a separate future coordination layer. No existing protocol, native ABI, device permission or local task contract is changed; remote trust and durable reconciliation remain open.
