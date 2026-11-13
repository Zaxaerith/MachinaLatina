"""Host-side experimental job monitor, not a guest OS or physical tape controller."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable

from machina_xxxvi.gateway import encode_cvl68, decode_cvl68

NAME = re.compile(r"[ABCDEFGHIKLMNOPQRSTVXYZ][ABCDEFGHIKLMNOPQRSTVXYZ0-9]{0,7}\Z")
MAGIC = b"OMR1"
MAX_JOBS = 32
MAX_STEPS = 100_000
MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_RECORD_BYTES = 1024 * 1024


class OrdoError(ValueError):
    """Bad job card, source location, resource or spool record."""


@dataclass(frozen=True)
class Job:
    name: str
    target: str
    mode: str
    source: str
    spool: str
    limit: int = 10_000
    input_spool: str | None = None


@dataclass(frozen=True)
class Execution:
    text: str
    steps: int
    values: dict[str, str]


@dataclass(frozen=True)
class JobResult:
    name: str
    target: str
    mode: str
    status: str
    spool: str
    steps: int
    text: str
    values: dict[str, str]
    error: str = ""


class Archives:
    """Named, sequential CVL-68 *logical* records; not physical tapes."""

    def __init__(self) -> None:
        self.records: dict[str, list[bytes]] = {}

    def append(self, name: str, data: bytes) -> None:
        if not NAME.fullmatch(name):
            raise OrdoError("invalid spool name")
        if type(data) is not bytes or len(data) > MAX_RECORD_BYTES:
            raise OrdoError("invalid or oversized output record")
        decode_cvl68(data)
        self.records.setdefault(name, []).append(data)

    def serialize(self, name: str) -> bytes:
        out = bytearray(MAGIC)
        for record in self.records.get(name, ()):
            out.extend(len(record).to_bytes(4, "big"))
            out.extend(record)
        return bytes(out)

    @staticmethod
    def deserialize(payload: bytes) -> tuple[bytes, ...]:
        if type(payload) is not bytes or not payload.startswith(MAGIC):
            raise OrdoError("invalid OMR1 header")
        pos, records = len(MAGIC), []
        while pos < len(payload):
            if len(payload) - pos < 4:
                raise OrdoError("truncated record length")
            size = int.from_bytes(payload[pos:pos+4], "big")
            pos += 4
            if size > MAX_RECORD_BYTES or size > len(payload) - pos:
                raise OrdoError("truncated or oversized record payload")
            record = payload[pos:pos+size]
            decode_cvl68(record)
            records.append(record)
            pos += size
        return tuple(records)


def parse_deck(deck: str) -> tuple[Job, ...]:
    """LABOR/FONTE/IMAGO/EDE/LIMES/FINIS only; no shell or includes."""
    jobs: list[Job] = []
    seen: set[str] = set()
    current: dict[str, str | int] | None = None
    for lineno, raw in enumerate(deck.splitlines(), 1):
        line = raw.split(";", 1)[0].strip()
        if not line:
            continue
        fields = line.split()
        command, args = fields[0], fields[1:]
        if command == "LABOR":
            if current is not None:
                raise OrdoError(f"line {lineno}: previous LABOR lacks FINIS")
            if len(args) != 3:
                raise OrdoError(f"line {lineno}: LABOR NAME TARGET MODE")
            name, target, mode = args
            if not NAME.fullmatch(name) or name in seen:
                raise OrdoError(f"line {lineno}: invalid or duplicate job name")
            if target not in ("XXXVI", "NOVA") or mode not in ("TRANFOR", "IMAGE"):
                raise OrdoError(f"line {lineno}: unknown target or execution mode")
            if len(jobs) >= MAX_JOBS:
                raise OrdoError("job deck exceeds 32 jobs")
            seen.add(name)
            current = {"name": name, "target": target, "mode": mode}
        elif command == "FINIS":
            if current is None or args:
                raise OrdoError(f"line {lineno}: misplaced FINIS")
            if "source" not in current or "spool" not in current:
                raise OrdoError(f"line {lineno}: incomplete LABOR")
            jobs.append(Job(**current))
            current = None
        else:
            if current is None:
                raise OrdoError(f"line {lineno}: card outside LABOR")
            if len(args) != 1:
                raise OrdoError(f"line {lineno}: card requires one value")
            if command in ("FONTE", "IMAGO"):
                expect = "FONTE" if current["mode"] == "TRANFOR" else "IMAGO"
                if command != expect or "source" in current:
                    raise OrdoError(f"line {lineno}: invalid or duplicate source card")
                current["source"] = args[0]
            elif command == "EDE":
                if "spool" in current or not NAME.fullmatch(args[0]):
                    raise OrdoError(f"line {lineno}: invalid or duplicate EDE spool")
                current["spool"] = args[0]
            elif command == "ACCIPE":
                if "input_spool" in current or not NAME.fullmatch(args[0]):
                    raise OrdoError(f"line {lineno}: invalid or duplicate ACCIPE input spool")
                current["input_spool"] = args[0]
            elif command == "LIMES":
                if ("limit" in current or not args[0].isdecimal()
                        or not 1 <= int(args[0]) <= MAX_STEPS):
                    raise OrdoError(f"line {lineno}: LIMES requires 1..100000 instructions")
                current["limit"] = int(args[0])
            else:
                raise OrdoError(f"line {lineno}: unknown card {command!r}")
    if current is not None:
        raise OrdoError("unfinished LABOR at end of deck")
    if not jobs:
        raise OrdoError("empty job deck")
    return tuple(jobs)


def _source_path(job: Job, root: Path) -> Path:
    relative = Path(job.source)
    if (relative.is_absolute() or "\\" in job.source or ":" in job.source
            or ".." in relative.parts):
        raise OrdoError("absolute/traversal paths are forbidden")
    allowed = ".trf" if job.mode == "TRANFOR" else (
        ".m36" if job.target == "XXXVI" else ".nvi")
    if relative.suffix != allowed:
        raise OrdoError(f"expected {allowed} input file for {job.target} {job.mode}")
    base = root.resolve(strict=True)
    path = (base / relative).resolve(strict=True)
    if not path.is_relative_to(base) or not path.is_file():
        raise OrdoError("source must be a file inside deck directory")
    if path.stat().st_size > MAX_SOURCE_BYTES:
        raise OrdoError("source exceeds maximum file size")
    return path


def _run_native(job: Job, root: Path, input_record: bytes | None = None) -> Execution:
    path = _source_path(job, root)
    image = None
    build = None
    if job.mode == "TRANFOR":
        from tranfor.vectors import compile_vectors
        build = compile_vectors(path.read_text(encoding="utf-8"))
        image = build.native
    if job.target == "XXXVI":
        from machina_xxxvi.machine import Machine
        from machina_xxxvi.image import load_image
        from machina_xxxvi.floating import F36
        cpu = Machine()
        cpu.load(image.old_words if image is not None else load_image(path))
        if input_record is not None:
            from .device import for_xxxvi
            cpu.mount_input(for_xxxvi(input_record))
        output = cpu.run(job.limit)
        values: dict[str, str] = {}
        if build is not None:
            if output != image.expected_text:
                raise OrdoError("XXXVI output disagrees with source contract")
            for name in build.exposed:
                kind = image.kinds[name]
                word = cpu.memory[image.old_addresses[name]]
                value = word if kind == "NAT15" else F36.decode(word)
                expected = (image.expected_integer[name] if kind == "NAT15"
                            else image.expected_f36[name])
                if value != expected:
                    raise OrdoError(f"XXXVI source variable {name} mismatched")
                values[name] = str(value)
        return Execution(output, cpu.steps, values)

    from machina_nova.cpu import NovaCPU
    from machina_nova.image import read_image
    from machina_xxxvi.floating import F32
    cpu = NovaCPU()
    cpu.load_regions(image.nova_regions if image is not None else read_image(path))
    if input_record is not None:
        from .device import for_nova
        cpu.mount_input(for_nova(input_record))
    output = decode_cvl68(cpu.run(job.limit))
    values = {}
    if build is not None:
        if output != image.expected_text:
            raise OrdoError("Nova output disagrees with source contract")
        for name in build.exposed:
            kind = image.kinds[name]
            word = cpu.memory.read_word32(image.nova_addresses[name])
            value = word if kind == "NAT15" else F32.decode(word)
            expected = (image.expected_integer[name] if kind == "NAT15"
                        else image.expected_f32[name])
            if value != expected:
                raise OrdoError(f"Nova source variable {name} mismatched")
            values[name] = str(value)
    return Execution(output, cpu.steps, values)


def run_deck(deck: str, root: Path,
             executor: Callable[[Job, Path], Execution] | None = None
             ) -> tuple[list[JobResult], Archives]:
    jobs = parse_deck(deck)
    archives = Archives()
    results: list[JobResult] = []
    execute = executor
    read_positions: dict[str, int] = {}
    for job in jobs:
        try:
            record = None
            if job.input_spool is not None:
                index = read_positions.get(job.input_spool, 0)
                available = archives.records.get(job.input_spool, [])
                if index >= len(available):
                    raise OrdoError(f"no unread record in spool {job.input_spool}")
                record = available[index]
            # Preserve existing two-argument mock executors for isolated
            # monitor tests; native mode receives the actual selected record.
            outcome = (_run_native(job, root, record) if execute is None
                       else execute(job, root))
            if not isinstance(outcome, Execution) or not 0 <= outcome.steps <= job.limit:
                raise OrdoError("invalid executor result")
            output_record = encode_cvl68(outcome.text)
            archives.append(job.spool, output_record)
            if job.input_spool is not None:
                read_positions[job.input_spool] = read_positions.get(job.input_spool, 0) + 1
            results.append(JobResult(job.name, job.target, job.mode, "FINIS",
                                     job.spool, outcome.steps, outcome.text, outcome.values))
        except Exception as exc:
            # A failed job is recorded; subsequent jobs still execute.
            results.append(JobResult(job.name, job.target, job.mode, "ERROR",
                                     job.spool, 0, "", {}, f"{type(exc).__name__}: {exc}"))
    return results, archives


def write_results(destination: Path, results: list[JobResult], archives: Archives) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for name in sorted(archives.records):
        (destination / f"{name}.omr").write_bytes(archives.serialize(name))
    report = {
        "format": "Ordo Operum/P0 experimental host batch report",
        "jobs": [asdict(job) for job in results],
        "spools": {
            name: {"records": len(records), "byte_lengths": [len(r) for r in records]}
            for name, records in sorted(archives.records.items())
        },
    }
    (destination / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
