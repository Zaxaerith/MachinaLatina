# MENTIS Agent Task R1 — Intent, Authority and Bounded Execution
> FUTURE SCENARIO / DRAFT / NOT CANON · 2026-11-26. Candidate 2027–2030 user-space contract. No agent runtime, model, native ABI, cryptographic signature or deployed service.

## 1. Design
MENTIS is an unprivileged planner, not a kernel or authority. A trusted host binds the actual user/session, checks available tools and scopes, mediates each call, records receipts, and owns the task state. The model cannot turn a NODVS document, generated instruction or a numeric handle into authority. Existing TESSERA handles remain process-local and nontransferable. A host may perform an operation on behalf of a task only with a live grant checked for that actual caller; no transfer protocol is implied. Existing SERMO profiles are illustrative, not implemented adapters. This is a logical service contract, not a binary message format.

A task has a host-issued nonzero session-local u64 ID, user goal (declared COS profile), plan revision, ordered steps, explicit budgets, allowed outputs and state. A plan revision is immutable once approved; changes to a tool, target, input revision, effect, scope or budget require a new plan revision and appropriate authorization. Model output is only a proposal. Host-generated trusted confirmation displays exact effects separately from model prose. User can inspect, cancel and decline; a normal application route remains available.

## 2. Typed steps
Each step has nonzero unique u32 ID, list of predecessor IDs smaller than its own, service identity and interface revision, typed input bindings to pinned records or earlier results, resource scope, effect class and output schema. At most 32 steps; no loops, recursion or dynamic subplans in R1. Execute eligible steps in increasing ID order, one at a time. Missing predecessor, unsupported schema, failed binding or ungranted operation prevents execution. Model may propose a new plan after failure but never silently add tools. No arbitrary shell execution in this base profile.

| Class | Contract |
| --- | --- |
| INSPECT | Read specifically granted resource/revision; no write; local or explicitly authorized remote destination |
| COMPUTE | Pure declared computation on granted inputs, no external effect; retain arithmetic profile and actual outcome |
| STAGE | Produce private candidate artifact; no publication or modification of originals |
| COMMIT | Explicitly authorized bounded mutation through a trusted adapter |

A step's class is declared and enforced by the trusted adapter, not a self-asserted model label. Sending private input to a remote COMPUTE service needs separate disclosure authorization; pure computation does not mean harmless transmission. No broad network, credentials, camera or filesystem access by default. Outputs from tools are untrusted data; they do not expand authority.

## 3. State and budget
Task: PROPOSED -> READY (host validates plan and obtains required consent) -> RUNNING -> SUCCEEDED/FAILED/CANCELLED/UNCERTAIN. READY may be cancelled before launch. During execution an effect requiring confirmation yields WAIT_APPROVAL; approval is scoped to exact plan revision, step, target, expected old revision and staged content identity. A refusal cancels the remaining plan. A changed target or staged result invalidates the approval. UNCERTAIN means an effect may have happened but no reliable receipt is available; stop and reconcile before any retry. Cancellation stops future admissions and suppresses late private presentation; cannot retract a committed external effect or data already disclosed.

Example independent limits: at most 32 admitted calls, 64 MiB of local input bytes and 8 MiB of remote disclosed payload per task, and a 600-second monotonic deadline. These are illustrative configurable policy bounds, not hardware or model limits. Reserve before admission; charge attempted calls even on failure, meter input/delivery bytes, reject work without a sufficient reservation; elapsed time is not CPU time. Do not refill on retry or process restart under the same task ID. Persistent accounting across crashes is a platform prerequisite for durable agents. Device CPU/network/wakeup limits from CVSTOS still apply independently. No background recurrence is authorized by a one-time task grant.

## 4. Commit semantics
The R1 local publication example uses an abstract trusted object store providing a single atomic compare-and-set operation. Stage bytes privately with explicit schema and immutable staging identity. COMMIT takes (resource identity, expected current revision, staging identity, approval binding); recheck grant generation and confirmation at the commit boundary, compare revision and publish one new immutable revision on success. A mismatch returns CONFLICT, no write. No multi-object transaction, no automatic destructive rollback. Abort discards private staged artifacts where policy permits; retain diagnostic receipts, not necessarily content. A native implementation needs real storage durability and identity contracts, not supplied by this proposal.

For remote writes RETE-00/R1 is insufficient: require separately defined authenticated transport, authorization, idempotency and outcome reconciliation before enabling the adapter. Do not assume exactly-once delivery. No remote write is part of the paper fixture.

## 5. Receipts
Trusted host records task/plan/step ID, actual service and version, granted resource identity and revision, input/output references, admission/completion time, measured cost, status and actual effect receipt (if any). Redact secrets; local log access follows permissions. A model-generated summary cannot create CALCVLATVM or RECEPTVM records. The MENTIS evidence types remain independent; a completed task does not establish scientific validity. Receipt integrity, durable recovery and portable signing remain open.

## 6. Paper fixture
A user asks to generate a derived map report without replacing the input. Read pinned elevation object 42 revision 3 (INSPECT); compute a declared analysis (COMPUTE); create a private report proposal S1 (STAGE); ask permission to publish to local report object 90 expected revision 7 (COMMIT). If the current revision is still 7 and permission remains valid, publication returns new revision 8. If another editor already published revision 8, return CONFLICT without changing it. If grant revoked after confirmation but before commit, deny. An actual calculation, result bytes and receipt are not supplied; all IDs are symbolic paper fixtures. No real GIS program ran.

Related: [MENTIS evidence](MENTIS-evidence-R1.md), [CVSTOS](CVSTOS-I-R1.md), [SERMO](SERMO-III-runtime-study.md), [RETE](RETE-00-R1.md).

## Phase XLII future scenario

[CONCORDIA task federation R1](CONCORDIA-task-federation-R1.md) and [personal computing study](CONCORDIA-personal-computing-study.md) propose a separate future coordination layer. No existing protocol, native ABI, device permission or local task contract is changed; remote trust and durable reconciliation remain open.
