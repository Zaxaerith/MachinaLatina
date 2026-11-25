# SERMO-I/R1 — A Record-Oriented Language for the Early Web
## SERMO 第一代语言候选：文字、记录与文档构造

> **REVIEW CANDIDATE / DRAFT / NOT CANON · 2026-11-24.** Fictional design window 1999–2004. This document specifies a small paper-level language subset, not a complete programming language, compiler, bytecode ISA, runtime or deployed product. Latin terms and historical version names remain provisional. NODVS, LIGAMEN, RETE and COS dependencies are themselves candidates.

## 1. Historical purpose

SERMO begins in library and publisher server-side programs that convert declared historical text, select records and produce NODVS documents. It is not initially a browser language. MODVLA is the proposed systems-interface tradition; RATIO is the proposed scientific numerical tradition. Their possible interoperation is through explicit typed data and service interfaces, not a shared unspecified memory ABI.

The distinguishing choice is a **document form**: an ordered typed construction of document records rather than concatenation of markup. The source notation is not the wire format. Text cannot inject a record header by containing punctuation or code-looking words.

## 2. Source identity and lexical subset

A source file has an external, explicit encoding declaration: CVL-68/RC1-L (validated and mapped to COS), COS-97/W1-R1 or COS-97/C24-R1, with the appropriate declared registry release. An undecodable or unknown identity fails before lexing. Modern UTF-8 examples in this repository are editorial transcriptions, not literal historical source bytes. Sandbox FFFF is allowed only in the paper examples.

Tokens are recognized on decoded CIDs. Whitespace outside strings is space, HT or paired CR LF; editors may show ordinary newlines in transcriptions. Reserved keywords are uppercase classical Latin letters; identifiers use the same 23 Latin letters, uppercase/lowercase, with optional digits and underscore after the initial letter. Case-sensitive identifiers; a keyword cannot be an identifier. Greek, Cyrillic or other scripts are not identifiers in this initial subset. International text literals remain supported. Latin A and Greek Alpha never compare equal as CIDs. Future scientific Greek identifiers require an independent policy; no automatic normalization or confusable folding.

Decimal integer literals are unsigned; no leading sign, suffix or hexadecimal notation in the core subset. An integer outside NAT range is invalid. Quoted text uses double quotes; no unescaped line break. Escape sequences are backslash followed by double quote, backslash followed by backslash, or backslash C followed by parentheses containing exactly six uppercase hexadecimal digits (a CID in the declared registry). No implicit Unicode escapes; a CID escape must name an assigned identity. Comments, imports, source-file packaging and advanced lexical features are postponed.

## 3. Types and semantics

| Type | Meaning |
| --- | --- |
| NAT | checked unsigned 64-bit integer, 0 through 2^64−1 |
| LOGICVM | VERVM or FALSVM |
| TEXTVS | immutable, ordered COS CID sequence under the program's registry release |
| OCTETI | immutable octet sequence; never implicitly a TEXTVS |
| REFERENTIA | LIGAMEN target tuple: authority u64, resource u64, revision u32, record u32 |
| LIGAMEN | typed logical link record; not a transport request or authority grant |
| NODVS | validated ordered logical document body, before host binds resource/revision and serializes |
| EXITVS(T) | built-in success value of type T or typed error, no implicit null; no user-defined generics in this subset |

An equality operation on TEXTVS compares the exact CID sequence; no automatic normalization, grapheme segmentation, casefolding or locale sorting. Texts from different registry releases require an explicit compatibility conversion. NAT addition is checked for overflow, TEXTVS addition concatenates two TEXTVS values. No implicit conversions between numbers, text, bytes, references or documents. LONGITVDO(TEXTVS) counts CIDs, not bytes or visible glyph clusters; MENSVRA(OCTETI) counts bytes. A later layout engine must provide user-visible text editing semantics separately.

## 4. Core authoring syntax

The following is a bounded grammar (EBNF notation is editorial and not part of SERMO source):

    program   = { declaration } ;
    declaration = form | operation ;
    form      = "FORMA" name "(" [ params ] ")" ";"
                { binding | record } "FINIS" ";" ;
    operation = "OPVS" name "(" [ params ] ")" ":" type ";"
                { binding } "REDDE" expr ";" "FINIS" ";" ;
    params    = param { "," param } ;
    param     = name ":" type ;
    type      = "NAT" | "LOGICVM" | "TEXTVS" | "OCTETI" | "REFERENTIA" ;
    binding   = "SIT" name ":" type "=" expr ";" ;
    record    = ("TITVLVS" | "PARAGRAPHVS") decimal "=" expr ";"
              | "CAPVT" decimal "(" decimal ")" "=" expr ";"
              | "LIGAMEN" decimal "EX" decimal
                "SPATIVM" "(" expr "," expr ")" "AD" expr ";" ;
    expr      = sum [ "=" sum ] ;
    sum       = atom { "+" atom } ;
    atom      = decimal | string | "VERVM" | "FALSVM" | name
              | name "(" [ expr { "," expr } ] ")" | "(" expr ")" ;

Assignment-like '=' in declarations and records is a syntactic separator; '=' inside an expression is equality. Addition associates left, equality has lower precedence and does not chain. Equality is supported only for same-type NAT, LOGICVM and TEXTVS. Parameters and SIT variables are immutable and cannot shadow each other; declarations have unique names. OPVS can call built-ins and earlier OPVS declarations, no recursive call cycle. FORMAs are host entry points, not expression-callable functions in this core. Expressions and records execute in source order. Arguments evaluate left to right. All expressions are pure. No implicit global variables, external I/O, mutation, loops, exceptions, classes or runtime evaluation of source strings in the core. Thus this is a bounded document generator subset rather than a claim of a complete general-purpose language.

OPVS explicitly returns its declared type; arithmetic/type failures halt the invocation with a typed host diagnostic. FORMA implicitly yields EXITVS(NODVS). A FORMA invocation never publishes a document or grants itself a resource identity. It accumulates typed records, then validates the entire body; failure yields an error and no partially published result. Source record IDs are literal positive u32 values. CAPVT level is 1–6. Link start/length must evaluate to NAT and fit u32; all R1 source-span rules apply. REF(a,r,v,o) produces REFERENTIA with the LIGAMEN-99/R1 range and latest/pinned restrictions. No invisible link targets from string parsing.

Built-ins: LONGITVDO(TEXTVS): NAT, MENSVRA(OCTETI): NAT, REF(NAT,NAT,NAT,NAT): REFERENTIA. Pure operation definitions may use only the listed core parameter/return types. The richer EXITVS handling and I/O interfaces below are future library/runtime candidates, not core grammar productions.

## 5. A first program

    OPVS SALVTATIO(NOMEN: TEXTVS): TEXTVS;
        REDDE "SALVE " + NOMEN;
    FINIS;

    FORMA INDEX(NOMEN: TEXTVS);
        TITVLVS 1 = "SALVE";
        PARAGRAPHVS 2 = SALVTATIO(NOMEN);
        LIGAMEN 3 EX 2 SPATIVM(6, LONGITVDO(NOMEN)) AD REF(1,2,1,0);
    FINIS;

Given sandbox NOMEN = 中文 (trial CIDs 020000 and 020001), the paragraph is SALVE 中文, with 8 CIDs and 10 W1 bytes. The link starts at CID 6 and spans 2 CIDs. It targets authority 1, resource 2, revision 1, whole document. An empty NOMEN produces an invalid zero-length link and a form error; arbitrary punctuation in NOMEN is data, not a new source token. Text must satisfy the NODVS title/paragraph controls and registry constraints. The host assigns valid nonzero resource and revision values under its authorized authority and selects W1 or C24. Same identity+revision must never be used for different logical content, including different parameters. A draft is not the published immutable revision.

## 6. Further development — not part of core grammar

- DECODIFICA(bytes, declared codec, declared registry): EXITVS(TEXTVS), with original bytes and diagnostics retained by the archive host.
- CODIFICA(text, codec): EXITVS(OCTETI). Reversibility depends on the actual repertoire; no hidden normalization.
- Typed NODVS record selection, projection and transformations; preserving opaque optional records requires a lossless editing API or explicit refusal, not reconstructing them from rendered text.
- Explicit result matching, local modules, server I/O, capability grants and asynchronous tasks in later profiles.
- Separate rich records/forms/attachment metadata, styles and event binding proposals; these must not be smuggled into unknown NODVS record types.

The core does not define floating-point precision, a native executable format or deployment ABI. Scientific computations should pass through a defined numerical service rather than implicitly inheriting one machine's float conventions. Future RATIO integration remains a proposal.

Related: [runtime evolution](SERMO-III-runtime-study.md), [history and paper examples](../docs/de-sermone-1999-2015.md), [NODVS](NODVS-98-R1.md), [COS](COS-97-R1.md), [LIGAMEN](LIGAMEN-99-R1.md).
