# COS, Language Models and the Classical-Language World (2015–2026)

> **DRAFT — linguistic/AI thought experiment.** No model was trained and no fictional benchmark results exist.

## Four representations, four different responsibilities

1. **Original source:** CVL-54/CVL-68 files, COS-tagged documents, NODVS records or scanned pages; keep bytes/images, provenance and licenses.
2. **Abstract characters:** strict decode according to the original codebook and mark order; do not mistake appearance for character identity.
3. **Model tokens:** vocabulary-dependent word pieces, characters or byte fragments; token count is neither character count nor a measure of intelligence.
4. **Meaning and evidence:** statistical model associations versus independently verifiable mathematics and actual document records.

The old CVL-68 sequence `52 41 4B 54 45` spells `SALVE`, not the ASCII-reading `RAKTE`; feeding undecoded bytes into model training silently corrupts the corpus. Latin A and Greek Α must remain distinct characters. Ancient Greek polytonic accents and final sigma need language-aware normalization, not global replacement rules.

## Why bilingual privilege becomes a problem

**DRAFT 2021:** a scholarly model trained predominantly on Latin engineering notes and Greek mathematical publications performs well in those academic domains, but handles underrepresented Asian, African and Middle Eastern texts poorly. This reflects **who generated, preserved, digitized and selected the data**, not a natural superiority of Latin or Greek.

A global COS character registry helps store text, but neither guarantees fair training coverage nor equal token efficiency. Compare source counts, quality, language/domain distributions, tokens per unit of text, retrieval quality, accuracy and harm rates. Language fairness remains a social and technical decision.

## The tokenization conflict

A tokenizer may compress common Latin suffixes efficiently while splitting less frequent Greek grammatical forms and other languages into many units. A byte-level tokenizer avoids unknown byte sequences but does not guarantee equal context cost or generation quality. Different model architectures and corpora can invert these rankings.

**Important:** the original CVL-68 draft uses a custom eight-bit layout; modern Unicode code-point values cannot be silently treated as historical COS identifiers. If model inputs use a modern research transcription, record the transcription procedure explicitly.

## One fictional scholarly incident

**DRAFT 2022:** an assistant cites a purported Greek scientific manuscript but fails to preserve its combining marks and points to a nonexistent NODVS node. The review board discovers two independent errors: incorrect source conversion and fabricated citation. A source link must be verified by a retrieval service, not merely generated as plausible-looking text.

## AI does not literally think in Latin

A machine can converse in Classical Latin, handle Greek variables and communicate in Chinese or Arabic, but its internal activation vectors are not a human-readable Latin-language chain of thoughts. Scientific terminology and model capability depend on training, tools, context and evaluation. This alternate world should not use long Greek–Latin cultural continuity to assert superior neural reasoning.

## Future standards questions

- Should training corpora retain original data alongside normalized COS text?
- How are reversible conversions, author rights and deletion requests recorded?
- How does an assistant indicate the original writing system and avoid Latin/Greek homoglyph attacks?
- Can public institutions fund reliable assessments for underrepresented languages and scripts?
- What is the difference between open inference code, model weights and training data?

Real-world comparisons: [Unicode UTS #39](https://www.unicode.org/reports/tr39/), [UNESCO AI ethics](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence).

Related: [Phase XIX](de-machinis-cogitantibus-2015-2026.md), [scientific provenance](ai-provenance-and-numerics-2015-2026.md), [COS study](../specifications/COS-universal-character-registry-study.md).

## 2026-11-26 MENTIS follow-up

[Matrices R1](../specifications/MENTIS-matrix-R1.md), [tokenizer R1](../specifications/MENTIS-tokenizer-R1.md) and [evidence R1](../specifications/MENTIS-evidence-R1.md) are later paper candidates. F48/R1 was separately proposed in Phase XXIX; no accelerator implementation or RATIO matrix grammar follows. Earlier unselected-format statements describe the original study. No trained model, benchmark or deployed assistant.
