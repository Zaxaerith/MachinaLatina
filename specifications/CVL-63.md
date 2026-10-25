# CVL-63 — Seven-Bit Transitional Communications Code

**Status: DRAFT · fictional · provisional existence**

## Purpose

A plausible transition from six-bit packed scientific-machine text to seven-bit communications networks while preserving Latin and Greek requirements.

A 7-bit character carries 128 code values. With 23 Latin and 24 Greek base letters, both cases already occupy **94** values; add 10 decimal digits and the result is **104**, leaving just 24 for every space, punctuation mark and control—too few for an ASCII-like terminal if its 33 control/reserved slots are retained.

## Candidate A: 7-bit page switching

- 128 codes per page, two pages selected by shift control sequences.
- Latin and Greek texts can coexist, but text decoding remains stateful.
- An explicit reset at record boundaries mitigates, but does not eliminate, recovery challenges.

## Candidate B: only a transmission profile

- Keep six-bit packed storage on legacy mainframes.
- Define seven-bit transmission framing and transliteration for unsupported text.
- Skip a true independent CVL-63 encoded character set.

**Decision open:** Whether a full CVL-63 standard is worthwhile, or the history should jump from CVL-54 directly to CVL-68.

## Compatibility warning

'7-bit' by itself does not imply ASCII, byte orientation, or a literal subset of CVL-68. No binary compatibility is established without exact mappings and transition rules.