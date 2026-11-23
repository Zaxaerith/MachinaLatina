# Concilium Codicum et Litterarum (CCL)
## 《编码与文字标准委员会章程》草案 · DRAFT 1961 / editorial 2026

> **Status: FICTIONAL CHARTER PROPOSAL, NOT CANON.** The Latin title is provisional and open to classical-language review. No legal entity or standards body was formed by this GitHub document. The bylaws describe how one *hypothetical* multi-stakeholder organization might reach recommendations while preserving the power of dissent and separate purchasing decisions.

## Article I — Purpose and limits

CCL is a proposed non-governmental technical coordination council among telecommunications operators, machine manufacturers/archivists, and scientific/publishing institutions. Its tasks are to publish:
- character identity/codebook recommendations;
- terminal and transmission compatibility profiles;
- archive preservation and migration guidelines;
- registration of revisions, extensions, deprecations and public dissent.

**It may not:** legislate national language policy, grant monopoly rights to a vendor, forbid competing systems, require everyone to purchase particular processors, compel nations to join, or claim to represent all global scripts by virtue of Latin/Greek expertise.

The organization should be funded by declared member subscriptions and publication services, with waivers for academic/public archival participation; possible budget amounts and national jurisdictions remain **DRAFT**.

## Article II — Membership and chambers

| Chamber | Five voting seats | Historical base (fictional) | Primary interest |
| --- | ---: | --- | --- |
| **T — Transmission** | 5 | Officinae Telegraphicae and participating line operators | transmission integrity, terminal cost, deployment |
| **M — Machines & Archives** | 5 | Collegium Machinarum, computing vendors, archive operators | binary/media survival, source interoperability, machine and tape compatibility |
| **S — Science & Letters** | 5 | Consortium Scientiarum, universities, scholarly printers | Greek/Latin text, precision, research and manuscript requirements |

Members are **organizations**, not self-appointed inheritors of the Roman Empire; an organization may hold at most **one voting seat** across the whole Council at one time. A nomination committee must disclose financial ties. Researchers may serve as advisors without multiple proxy votes. Each chamber selects its own five delegates by publicly recorded elections or rotations (specific fictional electoral procedures are still open).

Observers from other languages, national standards institutions, public purchasers and independent users may participate and submit objections; they **do not yet have guaranteed voting seats**. This weakness must be recorded as the source of later COS global-governance tensions. The council's limited linguistic legitimacy must not be overstated.

## Article III — How a proposal moves

1. **Problema (Issue):** a sponsor files a machine-readable or written problem statement with affected devices, scripts, numeric formats and economic cost.
2. **Examinatio (Working draft):** at least one technical delegate from two separate chambers prepares a written draft; attach tested vectors **when available**, not mandatory automatic CI for fictional scholarship.
3. **Commentarii (Public comment):** circulate the draft with explicit deadline, glossary, source provenance and dissent statements; publication channel and duration remain proposals.
4. **Suffragium (Vote):** a council plenary approves, returns for revision or rejects a **recommendation**.
5. **Editio (Publication):** label it with a named version and scope; distinguish character table, transport profile, typography, or archive conversion.
6. **Adoptio (Adoption):** vendors, public purchasers or communications regulators separately choose whether and how to adopt it. Council publication is **not** evidence of deployed products.
7. **Recensio (Review):** registration and maintenance track known errors, incompatible upgrades, old records and unassigned code points.

The words above are invented procedural labels, **not executable MODVLA or other language syntax**.

## Article IV — Quorum and approval arithmetic

**Proposed 1963-era voting rules:**

- Five voting seats in each of three chambers, **15 total**.
- Quorum: at least **12 of 15 voting delegates present**, and **at least four** present from **each** chamber.
- Pass threshold: **at least two-thirds of non-abstaining votes cast** (yes ≥ ceil(2 × (yes+no) / 3)).
- Cross-interest condition: **at least two chambers** must each record yes votes exceeding half of that chamber's **non-abstaining** yes/no votes. Empty/all-abstaining chamber never satisfies this condition.
- A tie in any chamber is not a majority. Abstentions count for quorum only, not for yes or no.
- The recorded dissent of a defeated chamber is attached to the recommendation; technical objections must be answered or acknowledged rather than erased.

The threshold and chamber arrangement are **fictional editorial design choices**, not reconstructions of actual ISO, Ecma or ITU voting rules.

A recommendation MAY pass against opposition in the third chamber. Its application then depends on purchase contracts and separate national/industry approval, so a council majority alone cannot change every machine in the world.

## Article V — Profiles and stability

Every publication should identify one of:
- **COD** — character identities and their direct bit values;
- **TEL** — communication-unit/parity/link profile;
- **TYP** — scholarly input, glyph composition and printing;
- **ARC** — old record preservation and decoding.

Each recommendation should include:
- document version, profile identifier, host/hardware requirements where relevant;
- declared assigned/reserved bit values;
- source-to-target migration loss conditions;
- tests/examples **when appropriate** (not a claim of mandatory CPU simulation);
- deprecation policy and public errata.

A rule assigned in one publication does **not** automatically apply to the other profile categories. In particular, **TEL 63/TP1** adds parity but no new character identities; **COD 68** proposes eight-bit direct character identities, but cannot promise full polytonic rendering without TYP extensions. The 2026 [CVL-68/RC1](CVL-68-RC1.md) is **not** thereby retroactively treated as an approved fictional 1968 CCL edition.

## Article VI — Rights, disclosures and adoption

A hypothetical vendor seeking a public interoperability certification should disclose:
- which specified features its equipment can actually exchange;
- known incompatibilities and source archive conversion losses;
- essential patent/technical dependencies if a rule cannot be implemented freely;
- whether an "open profile" requires a manufacturer-specific font or gateway.

The charter proposes public readability of final technical recommendations and an archival copy of superseded editions. It leaves **actual copyright licensing and patent terms undecided**; using modern MIT/CC BY/GPL legal text as if issued in 1961 would be anachronistic. The real GitHub repository licenses (code MIT, docs CC BY 4.0) are entirely separate from CCL's fictional publications.

## Article VII — Limitations and future constitutional dispute

CCL's three chambers would be badly placed to set a global multilingual character repertoire in 1995. The charter therefore proposes an obligation to invite other writing-system experts when affected, **without pretending this solves representation**.

Possible later reform options remain open: add a fourth public/linguistic chamber, affiliate with national standard bodies, establish a separate worldwide COS constituent assembly, or relinquish repertoire decisions while continuing old CVL archive maintenance.

An effective fictional standards organization must be capable of **losing authority** as its original remit becomes obsolete.

## Article VIII — CANON and document reality

- **Historical premise CANON:** living Classical Latin, prestigious academic Greek, a late-1960s shift toward direct native eight-bit bilingual encoding.
- **Fictional institutional proposal DRAFT:** CCL's existence, fifteen seats, quorum, vote design, document categories and 1961 founding.
- **Technical documents still DRAFT:** CVL-54/P0, CVL-63/TP1, CVL-68/RC1 numeric assignments, all full physical link and typography details.
- **No actual legal force or deployed standard is claimed** in this repository. A fictional vote described in an [invented meeting record](../docs/acta-concilii-codicum-1961-1972.md) does not ratify a modern design decision.

Related: [institutional history](../docs/de-conciliis-codicum-1954-1972.md), [provisional meeting records](../docs/acta-concilii-codicum-1961-1972.md), [decisions](../docs/decisions.md).
