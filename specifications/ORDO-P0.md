# Ordo Operum/P0 — Experimental Batch Job and Sequential Record Profile

**Status: DRAFT, 2026-11-13 · fictional 1970s-style computer operations.** The Python implementation is a *modern host-side monitor* that drives already existing XXXVI and Nova emulators. It is **not an in-guest operating system**, protected-mode kernel, magnetic-tape driver, syscall ABI or reconstructed historical software.

## Why these cards exist

In the imagined 1970s, a research institution owns both a 36-bit word-addressed Machina XXXVI family and 32-bit-byte-addressed Machina Nova systems. They cannot share executable files, but can share portable scientific *source*, job-submission conventions and carefully framed **CVL-68** output records.

**Ordo Operum** is a provisional Latin project term meaning the order/arrangement of works. Its exact philological suitability and historical standardizing institution remain open.

## Job-control cards

Each block is one **LABOR** with a unique Classical-Latin identifier. Job/spool names use the 23-letter base `ABCDEFGHIKLMNOPQRSTVXYZ`, are uppercase, start with a letter and contain at most **eight** letters/digits.

```text
LABOR PRIMA XXXVI TRANFOR
FONTE portable_dot.trf
EDE ACTA
LIMES 1000
FINIS

LABOR SECVN NOVA TRANFOR
FONTE portable_dot.trf
EDE ACTA
LIMES 1000
FINIS
```

| Card | Definition |
| --- | --- |
| `LABOR NAME TARGET MODE` | Open a job. TARGET `XXXVI` or `NOVA`; MODE `TRANFOR` or `IMAGE` |
| `FONTE PATH` | TRANFOR source path, restricted to `.trf`, relative to deck directory |
| `IMAGO PATH` | Native memory image: `.m36` on XXXVI, `.nvi` on Nova |
| `EDE NAME` | Append successfully decoded **text** as one record to named spool |
| `LIMES N` | Maximum *executed instructions*, 1–100000 (default 10000) |
| `FINIS` | End job block; does **not** mean a CPU FIN opcode |

Cards are UTF-8 textual **modern research input**. The bytes on a real 1970s card reader, card columns, parity and operator console are *not* specified. Semicolon comments and blank lines are allowed.

No arbitrary shell commands, scripts, network requests or include files are part of P0. Path containment is checked after resolving symlinks. A deck contains at most 32 jobs; each source file at most 2 MiB; one output text record at most 1 MiB. This is a laboratory **input validation policy**, not a general adversarial sandbox: native interpreter code executes in the host Python process; the monitor does not claim OS-level resource isolation.

## Modes and real execution boundaries

**TRANFOR:** compile a `*.trf` program with the actual TRANFOR/P2 compiler. It emits an XXXVI word image or Nova byte image and then **runs the appropriate CPU emulator**. Its exposed source-variable values are compared against the target-specific exact-numeric oracle; this is not merely simulating a successful exit code. The job spool receives only the program's **text output**.

**IMAGE:** load the existing `*.m36` or `*.nvi` image in the corresponding machine interpreter. There is no attempt to translate instruction bits. On XXXVI the printer decodes stateful CVL-54; Nova returns native candidate CVL-68 bytes. The monitor converts the resulting *displayed string* to the common candidate CVL-68 spool alphabet.

Every job creates a new emulator instance. A failed job is recorded as `ERROR`, produces **no successful spool record**, and does not prevent the next LABOR from running. Successful jobs are recorded as `FINIS`, with their instruction counts, display text and optional typed source variables. There is no multitasking, persistent guest process memory or shared-memory concurrency.

## OMR1 sequential spool format

The modern experimental binary record format is:

```text
offset  size       field
0       4 bytes    ASCII magic "OMR1" (file framing; NOT CVL-68 text)
4       4 bytes    length N of first logical record, unsigned big-endian
8       N bytes    CVL-68/P0 candidate character bytes
...     repeat     subsequent length + record pairs until EOF
```

The 4-byte length prefix is a **modern container framing convention**, not a fictional mainframe word instruction. An empty text record is legal, as are embedded CVL-68 control characters supported by the current strict gateway. Physical tape blocking, reel labels, checksums, disk allocation and metadata for external input datasets are **not yet specified**.

Record boundaries cannot be recovered from newlines or trailing zero bytes. `OMR1` preserves exact ordered record lengths for successful jobs, but **not** original CVL-54 six-bit physical packing, original shift codes or source control-card layout. The report JSON separately identifies each LABOR, its target and success/error.

```text
ACTA.omr
  record #1: SALVE ΛΟΓΟΣ    (output from XXXVI)
  record #2: SALVE ΛΟΓΟΣ    (output from Nova)
```

Note that the magic bytes are a file-format convention and are *not themselves part of the encoded linguistic record*.

## Running Phase XII

```powershell
python -m ordo_operum run examples/batch_science.ord --out-dir build/batch
python -m ordo_operum inspect build/batch/ACTA.omr
python -m unittest discover -s tests -p "test_ordo.py" -v
```

The example deck includes four jobs: two `TRANFOR` jobs compiling one shared source separately and two native `IMAGE` jobs using the old demonstration machines. It produces the `ACTA` and `PROBA` spools plus `report.json`.

**Verification boundary:** the deck/spool/unit-test logic passed **15 isolated local tests** using a test-only CVL-68 gateway implementation reproducing the existing code assignments. The four native jobs have **not** been fully executed against a clean checkout of the actual GitHub source tree, and there is no GitHub Actions green run. Do not treat the expected sample output as a confirmed end-to-end CPU result.

## What P0 does not provide

No guest filesystem, guest input APIs, persistent machine supervisor, jobs submitted concurrently, I/O scheduling, magnetic tape bit format, disk blocks, users/permissions, process switching, memory protection, kernel/user boundary, dynamic linker or executable interoperability across XXXVI/Nova.

**Next research:** direct file *input* to guest programs requires a separately defined `LEGE/READ` I/O contract or software calling convention; a host-only spool is not a substitute.
