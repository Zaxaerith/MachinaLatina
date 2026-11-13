"""CLI for Ordo Operum/P0 batch jobs and OMR1 archives."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .monitor import Archives, OrdoError, run_deck, write_results
from machina_xxxvi.gateway import decode_cvl68


def main() -> int:
    parser = argparse.ArgumentParser(description="Ordo Operum/P0 fictional batch monitor (host-side)")
    sub = parser.add_subparsers(dest="action", required=True)
    run = sub.add_parser("run", help="execute a fictional job deck")
    run.add_argument("deck", type=Path)
    run.add_argument("--out-dir", required=True, type=Path)
    read = sub.add_parser("inspect", help="show records in an OMR1 spool archive")
    read.add_argument("archive", type=Path)
    args = parser.parse_args()
    try:
        if args.action == "inspect":
            records = Archives.deserialize(args.archive.read_bytes())
            for idx, data in enumerate(records, 1):
                print(f"RECORD {idx} ({len(data)} bytes): {decode_cvl68(data)}")
            return 0
        jobs, archives = run_deck(args.deck.read_text(encoding="utf-8"), args.deck.parent)
        write_results(args.out_dir, jobs, archives)
        for job in jobs:
            print(f"{job.name:<8} {job.target:<5} {job.status:<5} {job.steps:>6} {job.spool}: {job.text or job.error}")
        return 0 if all(job.status == "FINIS" for job in jobs) else 1
    except (OrdoError, OSError, ValueError) as exc:
        parser.exit(2, f"Ordo/P0 error: {exc}\n")


if __name__ == "__main__":
    sys.exit(main())
