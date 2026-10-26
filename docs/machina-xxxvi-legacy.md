# When a Six-Character Machine Meets an Eight-Bit Future

**Phase IV discussion / DRAFT · fictional counterfactual**

## Why the first computer is 36-bit rather than 48-bit

`23 Latin + 24 Greek letters` does not automatically force a character width. Machina XXXVI starts with a **six-bit, stateful dual alphabet** and packs six codes into a 36-bit word because a relatively small alphabet, limited I/O equipment and scientific computation make this economical in the **early 1950s**.

By the late 1960s, the very same design becomes a liability: direct lowercase in two scripts, Greek diacritics, search/indexing and independent character identities favor the direct 8-bit CVL-68 successor. It would be anachronistic to install CVL-68 on the original 1954 processor.

## The important architectural split

| Aspect | XXXVI scientific family | 1968 direct bilingual family |
| --- | --- | --- |
| Storage address | 15-bit **word** address | byte addressability is **proposed**, not yet a finalized successor architecture |
| Native word | 36-bit | 32-bit or 40-bit or larger, **undecided** |
| Text unit | 6-bit stateful CVL-54 | 8-bit direct CVL-68 |
| Mixed Latin/Greek | printer page latch + shift codes | Latin and Greek code values distinct |
| Greek lower case / polytonic | limited or unavailable | basic lowercase direct; marks via developing conventions |
| Text seek | needs correct shift state | direct core letters; combining marks still complicate character indexing |
| Tape archives | six-code packing + record boundaries | gateway transcode plus archives of originals |

No single Latin or Greek lexical choice determines any architecture shown above. The design is a historical *path-dependence* exercise.

## What language actually changes

The strongest linguistic influence sits at the **I/O boundary and surrounding software**, not ALU gates:

1. Production demand for two national/scientific writing systems makes code-page shifts an engineering bottleneck.
2. Punched-card layouts and terminal inventories evolve to expose Greek glyphs.
3. Compiler source encodings must preserve Greek identifiers—or else scientific mathematicians must type transliterations.
4. Binary archives survive, so even after the encoding war the six-bit legacy remains expensive to convert.
5. The same visible `A` could be a different logical Greek `Α`, which requires script-aware validation in later assemblers/editors.

## The unresolved bridge

A **retrofit interface** can decode CVL-54 records and produce CVL-68 bytes, but must know page resets and logical record boundaries. The hypothetical mainline successor should not be forced to adopt 36-bit words. We should next compare:

- **Bridge A:** keep 36-bit word CPU, add CVL-68 terminal encoder/decoder and record translation channels;
- **Bridge B:** design new byte-addressed CPU family, preserve old program compatibility through an instruction-set emulator or batch translator;
- **Bridge C:** abandon machine-code continuity and standardize document/data gateways only.

The project has not canonized a particular bridge. The future computer architecture should be **derived**, not asserted.

## Sources for the realistic constraints

- [Columbia University — IBM 704](https://www1.columbia.edu/cu/computinghistory/704.html)
- [IBM historical overview of IBM 700-series scientific computers](https://www.ibm.com/history/700)
- [Computer History Museum — IBM 704 artifact](https://www.computerhistory.org/revolution/artifact/482)
- [PDP-10 instruction format](https://pdp10.nocrew.org/docs/opcodes.html) (later counterexample; do not transplant its actual encoding into 1954)
