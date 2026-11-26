# SERMO III — Server Tasks, Client Events and Explicit Authority
## 2005—2015 年的候选运行时与网络编程模型

> **DRAFT / conceptual runtime study · 2026-11-24.** This extends the historical language design, not the executable SERMO-I/R1 grammar. All example syntax in this study is illustrative. No bytecode, package manager, event record, interpreter, browser extension, authenticated RETE transport or client-side permission implementation is supplied.

## 1. Separation of execution profiles

| Profile | Suggested era | Role |
| --- | --- | --- |
| FORM | 2002–2004 | pure typed body construction from input parameters |
| MINISTER | 2005–2008 | server-side document queries, explicit host services, bounded request handling |
| CLIENS | 2009–2012 | optional local event handlers and transient views, no implicit filesystem or network |
| COMMVNE | 2013–2015 | shared pure modules with profile-specific service adapters |

These profile names are provisional Latin labels. A server module does not automatically run in a browser. NODVS-98/R1 remains passive and contains no executable script binding. A later application manifest would explicitly declare a module, runtime version, entry points, allowed services, provenance and permission policy. The manifest format is not defined. Merely loading a NODVS document or following its references does not launch code.

## 2. Proposed capability interfaces

A capability is an opaque host-issued handle, not a guessed string or numeric authority ID. The host validates every use against the granted operation, destination, user and limits. Scripts cannot manufacture authority by constructing REFERENTIA. Candidate interfaces:

| Capability | Permits | Explicitly not implied |
| --- | --- | --- |
| FONTES | Read declared local archive collection | Arbitrary filesystem reads or modifying original bytes |
| RETE-LECTIO | Fetch approved resource references | Credentials, mutation, arbitrary cross-origin access |
| VISVS | Update assigned transient presentation state | Editing archived NODVS revision or escaping application UI |
| NUMERI | Invoke defined numeric service | Silent precision changes or unrestricted native code |

Runtime permissions, code authenticity and secure transport are distinct. A grant does not make an unauthenticated RETE peer trustworthy; authenticated/confidential exchange depends on independent future protocols. Public documents should not be treated as trusted code. No mutation network opcode is added to RETE R1. Future form submission needs explicit method, validation, replay/idempotency and authorization semantics.

## 3. Errors and task lifecycle

Suggested built-in EXITVS(T) variants RECTE(value) and ERROR(code, diagnostic). Decode failure, unsupported registry, transport error, invalid reference, denied capability, missing resource and host limit are distinct error classes. Unrecognized errors are not successful empty documents. Error details must not expose credentials or unrelated private content.

An asynchronous task (NEGOTIVM(T), proposed type) has states queued, running, succeeded, failed or cancelled. A task resolves at most once. A cancellation request suppresses later view updates; it need not instantly interrupt physical I/O. All tasks are scoped to an invocation/application and bounded by host resource limits.

A candidate client runs one event loop per application context. One handler executes at a time until it yields at an asynchronous wait or returns. Ready continuations join the event queue. Scheduling of network completions is not deterministic across runs; no automatic thread creation or shared mutable state across contexts. A later runtime must define fairness and queue policy. Handlers should use generation counters or task identities to discard outdated results.

RETE-00/R1 allows one outstanding request per connection. Multiple concurrent application fetches must queue on a connection or use separately authorized connections. The runtime cannot introduce multiplexing by fiat.

## 4. Illustrative client notation (NOT SERMO-I syntax)

    EVENTVS SELECTIO(DESTINATIO: REFERENTIA);
        SIT T = PETE(LECTIO, DESTINATIO);
        CASVS EXSPECTA(T)
            RECTE(DOCUMENTVM):
                OSTENDE(VISVS, DOCUMENTVM);
            ERROR(E):
                NVNTIA(VISVS, E);
        FINIS;
    FINIS;

Here PETE initiates an approved read using an existing capability, EXSPECTA yields to the event loop, and CASVS examines a result. OSTENDE updates a transient view, not the original revision. LECTIO and VISVS are illustrative host-provided handles, not ordinary user variables that may be fabricated. This is a notation sketch; actual grammar, type inference, binding rules and event source IDs remain open.

For rapid successive selections A and B: increment the application's local selection generation; associate each fetch with its generation; display a result only if its generation is still current. If B returns first, display B. If A returns later, discard A's view update even if A itself succeeded. Closing the view cancels or detaches outstanding tasks. This protects against stale updates without requiring global deterministic I/O.

## 5. Dynamic views and immutable publication

Published NODVS identity is (authority, resource, revision). A client may make a derived view, filter a data table or highlight search results without changing that identity. It must not export the altered view under the original edition. Server-generated parameter-specific output needs a separately assigned resource/revision or a separately specified dynamic response type. If it changes logical content while returning the same resource/revision, it violates NODVS R1. Public cache keys need registry/codec and revision; private data additionally needs authorization partitioning and a future cache policy. No personal query data should be shared through a public immutable cache.

Unknown optional NODVS records cannot be discarded and then called losslessly edited. A layout or script sandbox may show a placeholder and preserve the original record; a new document publication requires the appropriate editor/serializer rules.

## 6. Portability, scientific interfaces and hardware

Early Nova clients could support a lightweight FORM/CLIENS interpreter, while server applications use MODVLA-backed host adapters for files and networking. This is a conceptual layering, not an actual VM ISA. A Sextaria-style numerical library can serve data to SERMO via explicit typed records and declared numeric representation. A data result is not made reproducible by passing it through a network language. RATIO-style error/units contracts and actual wire formats remain separately designed.

Open questions: source module/package identity, module signing and trust, permission mediation UX, browser origin binding, DOM-like view object API, garbage collection or ownership strategy, server authentication, rich object layout, event registration, service mutation semantics, stable bytecode and ABI. No need to decide all of these in 1999.

Related: [core form language](SERMO-I-R1.md), [NODVS](NODVS-98-R1.md), [RETE](RETE-00-R1.md), [historical narrative](../docs/de-sermone-1999-2015.md).

## Phase XXXVIII future scenario

[MENTIS agent task R1](MENTIS-agent-task-R1.md) and [system integration study](MENTIS-system-integration-study.md) propose later user-space contracts, not changes to this existing profile. No ambient authority, remote mutation protocol or native ABI is implied.
