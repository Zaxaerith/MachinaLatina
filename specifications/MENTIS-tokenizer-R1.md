# MENTIS — COS-native tokenization R1
> DRAFT / NOT CANON · 2026-11-26. Illustrative 2018–2026 deterministic tokenization contract, not a trained tokenizer, actual model vocabulary or language benchmark.

## 1. Representation pipeline
Retain source bytes or images, source rights, declared CVL codebook/COS registry and conversion logs. Decode strictly into COS CID sequences. CVL-54 page state and CVL-68 custom byte order must be respected. Reject undecodable input from this tokenization profile without destroying the archived original. No automatic transliteration, case folding, normalization, removal of accents or conflation of Latin/Greek homoglyphs. For training, select data under a separate documented policy; preservation does not itself authorize training. A derived normalized dataset needs its own mapping and version.

## 2. Vocabulary and algorithm
An identified vocabulary revision binds one published COS registry release and a finite set of nonempty CID sequences (1..32 CIDs), each with a distinct positive u32 token ID. No duplicate sequences. Require a singleton for every assigned CID admitted by the profile; an unsupported CID fails explicitly. Reserve token 0 for external control, not text. Special model controls are separate typed events, never inferred from displayed strings. Longest matching vocabulary sequence at the current CID offset wins; emit its ID and advance by its length. With unique sequences this is deterministic and needs no tie break. Decode by concatenating the recorded vocabulary sequences; re-encoding arbitrary token sequences need not yield identical token boundaries. This is a simple greedy dictionary, not BPE training, a morphology analyzer or a claim of optimal compression. Maximum input 1,048,576 CIDs per invocation in this reference profile; reject excess rather than truncate. Real streaming and context windows are separate.

## 3. Illustrative vocabulary
COS-97/R1 maps eligible CVL-68 b to CID 010000+b. SALVE = 010052 010041 01004B 010054 010045. ΛΟΓΟΣ = 01008A 01008E 010082 01008E 010091. The following are selected entries of a fixture vocabulary; other singleton entries required for the full admitted set are not enumerated here.

| Token ID (decimal) | CID sequence | Display |
| --- | --- | --- |
| 101 | 010052 010041 01004B 010054 010045 | SALVE |
| 102 | 010020 | space |
| 103 | 01008A 01008E | ΛΟ |
| 104 | 010082 01008E 010091 | ΓΟΣ |
| 201 | 010052 | S |
| 202 | 010041 | Latin A |
| 203 | 01004B | L |
| 204 | 010054 | V |
| 205 | 010045 | E |
| 206 | 01008A | Λ |
| 207 | 01008E | Ο |
| 208 | 010082 | Γ |
| 209 | 010091 | Σ |

SALVE ΛΟΓΟΣ (11 CIDs) -> [101,102,103,104], four tokens. With only singleton entries it would be 11 tokens. CVL-68 source length 11 octets; C24 representation 33 octets; a token ID may be stored as u32 in one proposed diagnostic representation, but the neural model need not store tokens that way. The fixture is intentionally tiny, not evidence of Latin or Greek comparative token efficiency. Latin A and Greek Α have different registry entries; same rendered shape does not imply same token. Combining marks remain distinct CIDs unless a vocabulary entry explicitly contains the sequence.

## 4. Global language evaluation
Record corpus source rights, language/domain coverage, conversion failures, vocabulary revision and model checkpoint. Evaluate token counts per comparable text/task, accuracy, retrieval and generation quality across languages; singleton fallback alone does not ensure fair representation. Distinct tokenizers may tokenize the same text differently; token ID is not COS identity, and token count is not intelligence. Training vocabulary construction, model architecture, attention, checkpoint format and multilingual benchmarks remain open. See [COS](COS-97-R1.md) and [prior AI study](../docs/ai-languages-and-cos-2015-2026.md).
