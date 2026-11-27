# OFFICINA workbench gallery
> Phase XLVI · DRAFT. Text-only conceptual UI mockups; not screenshots or implemented commands. Latin labels are provisional technical neologisms. No terminal escape sequence or source encoding change.

## M01 (1954): paper listing
    MACHINA XXXVI
    ADRESSA (VERBA OCTALIA)    VERBVM (36 BIT)
    00000                      000000000000
    00001                      000000000001
The two words are display examples, not an executable instruction sequence. A 36-bit word and a 15-bit address fit twelve and five octal digits respectively. Physical tape framing is separate.

## M02 (1968): terminal
    NOVA N1                 80 X 24
    LINGVA: LATINA           [GRAECA]
    LINEA 001  SALVE ΛΟΓΟΣ
    CODEX: CVL-68            STATUS: EDITIO
This shows an illustrative text editor, not an actual N1 operating system. The greeting is eleven octets under the candidate basic mapping; Latin/Greek mode affects only new input. CVL-68 byte mapping is not ASCII.

## M06 (1986): TABVLA / SCRIPTVRA
    + SCRIPTVRA -------------+
    | FONTES  MENSVRA        |
    | INTERFACIES;           |
    | ...                    |
    | CORPVS;                |
    | ...                    |
    + NVNTII ----------------+
    | Schema / target checks |
    +------------------------+
This is an incomplete source excerpt, not a full module. Native record alignment and external record format need separate inspectors. Candidate 640×480 indexed display and limited RAM discourage modern multi-process IDE assumptions.

## M11 (2026): integrated workbench
    OFFICINA   |  MENSVRA  |  EDITIO: [revision]
    FONTES     |  INTERFACIES     |  MENTIS
    source     |  logical types   |  proposal
    ------------ NVNTII / MEMORIA ------------
    HOST: Nova M64        TARGET: selected profile
    ABI: declared        CODEX: declared COS registry
    BUILD: not run        PUBLISH: not authorized

Suggested panes: source, interface navigator, diagnostics, memory/variables, revision review, optional AI assistant. MENTIS proposals are not executable proof or authority. A remote target needs its own debugging adapter.

## Byte/character inspection
The candidate greeting SALVE ΛΟΓΟΣ is 11 direct CVL-68 octets:
    52 41 4B 54 45 20 8A 8E 82 8E 91
Under the existing COS mapping it may be 11 W1 octets or 33 C24 octets. In CVL-54 the shift-bearing example uses 12 six-bit units, two 36-bit words, before reset/end handling. The UI must show the declared profile, not silently transcode. Latin A and Greek Α differ in identity even if drawn identically.
A source diagnostic should include revision, encoding/profile, source span with unit, target and error category. An editor may highlight a whole combining cluster while preserving original identities; cursor movement and lexical normalization are separate unresolved policies.

## Worked numeric debugger panel
From RATIO-I/R1's coordinate example:
    FORMVLA D = B - A
    FORMATVM F32
    REFERENCE: 0.03125 M
    EXECUTION: 0 M
    ERROR ABS: 0.03125 M
    TOLERANTIA: 0.01 M
    RESULT: TOLERANCE_FAIL
With F36 the difference can be retained. This is a paper calculation, not a tool execution. No assertion about measurement validity. The UI excerpt is not valid complete RATIO syntax.

## Candidate future terminology
OFFICINA workbench; SCRIPTVRA editor (existing desktop study); FONTES sources; NVNTII diagnostics; MEMORIA memory; PVNCTA breakpoint list; INSPECTIO inspection; EDITIO revision (existing STEMMA); EMENDATIO proposed change (existing collaboration study). No normative language or filename extension is defined.
