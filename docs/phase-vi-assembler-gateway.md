# Phase VI — First Assembler and the 1954/1968 Text Bridge

**Status:** Python implementation and tests checked in. A locally reconstructed copy of the original Phase V files and the new Phase VI implementation passed **22 unittest methods** on Python 3.13.5 on 2026-11-12. The GitHub-hosted tree was independently re-read, but it has **not** yet been executed from a clean GitHub checkout or tested by GitHub Actions.

## Why this is an architectural milestone

The fictional 1954 Machina XXXVI can now be programmed with symbolic **Latin P0 assembly** rather than handwritten octal words. A separate external gateway interprets its stateful six-bit text and emits candidate CVL-68 direct-byte text. The original CPU remains strictly a 36-bit **word-addressed** machine. The gateway is a **later software bridge**, not a retroactive native 1968 peripheral.

The new commands and implementations are present-day developer tools. They do not purport to be an actual 1954 assembler or archaeological discovery.

## Run (Python 3.10+, standard library only)

```sh
python -m machina_xxxvi assemble examples/salve_logos.mxa --output demo.m36
python -m machina_xxxvi run demo.m36
python -m machina_xxxvi bridge demo.m36 00100 00101 --output demo.cvl
python -m unittest discover -s tests -v
```

The first command generates a **modern text-based octal memory image**, the second executes it, and the third **selects and transcodes two data words**. Note that `bridge` does **not** automatically detect text regions or decode machine instructions.

Expected text: `SALVE ΛΟΓΟΣ`.

Expected candidate CVL-68 byte sequence (hexadecimal):

```text
52 41 4B 54 45 20 8A 8E 82 8E 91
```

For reproducibility, the assembly output from `examples/salve_logos.mxa` is the same mapping of addresses to words as `examples/salve_logos.m36`, ignoring comments.

## P0 source language / 汇编器范围

The assembler is **two-pass** and supports forward references and deliberately short, six-character, Classical-Latin labels. Examples:

```text
ORG 00000
EMIT SALVE
EMIT LOGOS
FIN

ORG 00100
SALVE: VER 22,01,13,24,05,43
LOGOS: VER 61,13,17,03,17,22
```

Supported instructions: `FIN`, `LEGE`, `PONE`, `ADDE`, `SVBT`, `SALTA`, `SI0`, `PONX`, `EMIT`, `NVM`. Directives: `ORG` for octal word address, `VER` for six explicit octal codes, and `TEX "string"` for **automatic CVL-54/P0 page-shift encoding**. `TEX` may occupy multiple adjacent words and pads its final word with the PAD code.

All bare numeric operands are **octal**, not decimal. Labels start with a Classical Latin uppercase letter, contain only Classical Latin uppercase letters and digits, and are **at most six characters long**. `X1+LABEL` indexes a word address; `PONX X2,00005` sets index register X2 to five (octal).

`TEX` is an **independent string literal** encoded from initial page LATINA. It does not force a terminal page reset or insert EOT; the caller must ensure the terminal starts in LATINA, and may not emit additional words after the final PAD within the same P0 printer run. For sequences of messages and record boundaries, prefer manually controlled `VER` and shifts. The `TEX` source file is modern UTF-8 but the resulting six-bit machine words are not UTF-8.

This P0 assembler is not a linker, object format, macro assembler or full source-language frontend. It rejects undefined symbols, invalid addresses, duplicate labels, overlapping output words and unsupported characters.

## The bridge / 字符网关的边界

`transcode_words(words)` performs:

1. six-bit code unpacking;
2. stateful LATINA/GRAECA interpretation;
3. exact Unicode *display characters* in the host application as an intermediate representation;
4. a **subset** of the proposed CVL-68 byte mapping.

The gateway discards physical 36-bit packing, shift codes, PAD and EOT; it is **not** an archival round-trip. It does not synthesize lost original accents, lowercase letters or old record metadata. Full CVL-68 remains a **DRAFT**: reserved code points and unknown symbols raise errors.

The `encode_cvl68()` helper accepts a few standalone combining mark code points in decomposed form, but **does not normalize** precomposed Unicode polytonic Greek and does not validate all combinations. It is a deliberately strict mapping subset, not a complete Greek text processor.

### What actually passed locally

- 13 Phase V tests reproduced from the existing GitHub test source;
- 9 Phase VI tests of assembler, indexing, full memory image round trip, mixed-script print, direct character conversion, reserved code rejection, and CLI execution;
- `python -m compileall` for the Python package;
- built-in `demo` output and memory-image `run` output both matched `SALVE ΛΟΓΟΣ`.

The validation was performed in a **reconstructed working directory because direct container GitHub networking was unavailable**. Tests were not run on a clean clone, so the reported results are explicitly *local validation*, not a CI gate.

## Next plausible fork in the fictional timeline

The project now has a technical reason for the late-1960s standard war: a six-bit word machine can be kept operational with a gateway, but cannot natively index Greek lowercase letters or individual CVL-68 bytes. Next compare **36-bit gateway retrofits** with an independently designed **byte-addressed 1968 successor CPU**, without declaring one inevitable.

Related: [Machina XXXVI architecture](../specifications/Machina-XXXVI.md), [CVL-54/P0](../specifications/CVL-54-P0.md), [CVL-68 draft ledger](../specifications/CVL-68-byte-ledger.md), [legacy migration specification](../specifications/CVL-54-to-68-migration.md).
