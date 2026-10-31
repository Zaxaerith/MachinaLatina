"""Machina XXXVI/P0 reference CPU.

Fictional 1954 architecture: 36-bit word-addressed, ten opcodes, no floats.
"""
from __future__ import annotations

from .cvl54 import Printer, WORD_MASK

ADDRESS_MASK = (1 << 15) - 1
MEMORY_WORDS = 1 << 15
OPCODES = {
    0: "FIN", 1: "LEGE", 2: "PONE", 3: "ADDE", 4: "SVBT",
    5: "SALTA", 6: "SI0", 7: "PONX", 8: "EMIT", 9: "NVM",
}


class MachineFault(RuntimeError):
    """Invalid instruction or bounded execution exhausted."""


def encode_instruction(op: int, adr: int = 0, tag: int = 0,
                       indirect: int = 0, aux: int = 0) -> int:
    """Encode the 12:1:5:3:15 P0 bit-field layout."""
    fields = ((op, 12), (adr, 15), (tag, 3), (indirect, 1), (aux, 5))
    if any(type(n) is not int or not 0 <= n < 1 << bits for n, bits in fields):
        raise ValueError("instruction field out of range")
    return (op << 24) | (indirect << 23) | (aux << 18) | (tag << 15) | adr


class Machine:
    """Determininistic P0 emulator. Raises on reserved instruction encoding."""

    def __init__(self) -> None:
        self.memory = [0] * MEMORY_WORDS
        self.printer = Printer()
        self.pc = 0
        self.a = 0
        self.q = 0  # reserved extension register
        self.x = [0, 0, 0]
        self.halted = False
        self.steps = 0

    @property
    def z(self) -> bool:
        return self.a == 0

    def load(self, words: dict[int, int]) -> None:
        """Set memory words without resetting registers or the terminal."""
        for addr, word in words.items():
            if type(addr) is not int or not 0 <= addr < MEMORY_WORDS:
                raise ValueError(f"word address outside memory: {addr!r}")
            if type(word) is not int or not 0 <= word <= WORD_MASK:
                raise ValueError(f"invalid 36-bit word at address {addr:05o}")
        for addr, word in words.items():
            self.memory[addr] = word

    def step(self) -> tuple[int, str]:
        """Execute one instruction; on an instruction fault do not advance PC."""
        if self.halted:
            raise MachineFault("machine already halted")
        at = self.pc
        word = self.memory[at]
        op = (word >> 24) & 0xFFF
        indirect = (word >> 23) & 1
        aux = (word >> 18) & 0x1F
        tag = (word >> 15) & 7
        adr = word & ADDRESS_MASK
        if op not in OPCODES:
            raise MachineFault(f"unknown opcode {op:04o} at {at:05o}")
        if indirect or aux:
            raise MachineFault(f"reserved I/AUX field at {at:05o}")
        if tag not in (0, 1, 2, 4):
            raise MachineFault(f"reserved index TAG={tag} at {at:05o}")
        if op == 0 and (tag or adr):
            raise MachineFault(f"FIN must be all zero at {at:05o}")
        if op == 9 and tag:
            raise MachineFault(f"NVM cannot use an index at {at:05o}")
        if op == 7 and tag == 0:
            raise MachineFault(f"PONX requires X1, X2 or X3 at {at:05o}")

        next_pc = (at + 1) & ADDRESS_MASK
        ea = (adr + (self.x[{1: 0, 2: 1, 4: 2}[tag]] if tag else 0)) & ADDRESS_MASK
        if op == 0:
            self.halted = True
        elif op == 1:
            self.a = self.memory[ea]
        elif op == 2:
            self.memory[ea] = self.a
        elif op == 3:
            self.a = (self.a + self.memory[ea]) & WORD_MASK
        elif op == 4:
            self.a = (self.a - self.memory[ea]) & WORD_MASK
        elif op == 5:
            next_pc = ea
        elif op == 6:
            if self.z:
                next_pc = ea
        elif op == 7:
            self.x[{1: 0, 2: 1, 4: 2}[tag]] = adr
        elif op == 8:
            # Printer stages all six symbols and commits only on successful parse.
            self.printer.feed_word(self.memory[ea])
        elif op == 9:
            self.a = adr
        self.pc = next_pc
        self.steps += 1
        return at, OPCODES[op]

    def run(self, max_steps: int = 100_000) -> str:
        if type(max_steps) is not int or max_steps < 1:
            raise ValueError("max_steps must be a positive integer")
        count = 0
        while not self.halted:
            if count >= max_steps:
                raise MachineFault(f"step limit {max_steps} reached at {self.pc:05o}")
            self.step()
            count += 1
        return self.printer.text
