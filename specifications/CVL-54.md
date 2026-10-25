# CVL-54 — Six-Bit Dual-Page Character Encoding

**Status: DRAFT · fictional · not an implemented standard**

## Design goal

Support basic Latin and Greek uppercase text on equipment for which a compact 6-bit character code and 36-bit machine word are attractive. The name CVL is provisional, expanded here as *Codex Utriusque Linguae* (in a 23-letter orthography: **CODEX VTRIVSQVE LINGVAE**).

## Proposed model

- Each code unit has **6 bits** and 64 possible values.
- **LATINA** and **GRAECA** are separate active decoding pages.
- Reserved shift codes change the active page.
- Digits, spacing and essential control symbols have shared slots in both pages where possible.
- The initial page, message boundary reset behavior and error recovery MUST be specified before a codec can be implemented.

### 36-bit word

`6 × 6-bit code units = 36 bits`. This is a **storage packing rule**, not an architecture-wide definition of instruction format or floating-point arithmetic.

Example: `VERBVM` occupies six basic Latin code units and thus can be packed into one 36-bit word. No actual binary value is specified yet.

## Why shifts?

Two pages allow a limited fixed-width code to carry two alphabets without encoding all characters simultaneously. This is inspired by real five-bit teleprinter practice (letters/figures shifts), but CVL-54 and its dates are fictional.

## Costs

1. **Stateful decoding**: the meaning of a code depends on preceding shifts.
2. **Random access**: an address into text is insufficient without page state.
3. **Corrupted or missing shifts**: garble subsequent characters until state recovers.
4. **Mixed scripts**: mathematical prose may repeatedly switch pages.
5. **Typography**: uppercase-only pages do not capture accented polytonic Greek or a full lower-case printing tradition.

## Open issues

- [ ] Exact 64-entry page tables, including a NULL, SPACE, SHIFT-LAT and SHIFT-GRC.
- [ ] Whether code 0 is padding, NUL, or a printable space.
- [ ] How messages reset page state after errors or across word boundaries.
- [ ] Terminal printer handling for accent marks and overstrikes.
- [ ] Round-trip transcode to CVL-68; how to represent untranscodable content.

Do **not** treat any numerical examples elsewhere as normative until this table is fixed.