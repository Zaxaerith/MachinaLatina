"""Machina Nova-N1: fictional byte-addressed 1968 CPU reference interpreter.

Independent ISA: one 32-bit instruction = 8-bit opcode + 24-bit operand.
Uses the Phase VII Nova-N0 experimental byte memory, not the XXXVI ISA.
"""
from __future__ import annotations

from machina_xxxvi.archlab import NovaMemory, DEFAULT_NOVA_INSTALLED_BYTES
from machina_xxxvi.floating import F32

ADDRESS_MAX = (1 << 24) - 1
WORD_MASK = (1 << 32) - 1
OPCODES = {
    0x00: "FIN", 0x10: "LEGB", 0x11: "LEGW", 0x12: "PONB",
    0x13: "PONW", 0x20: "ADDE", 0x21: "SVBT", 0x30: "SALTA",
    0x31: "SI0", 0x40: "NVM", 0x41: "ADI", 0x50: "EMIT",
    0x60: "FLEG", 0x61: "FADD", 0x62: "FSVB", 0x63: "FPON",
    0x64: "FMVL", 0x65: "FDIV",
}
MNEMONICS = {name: code for code, name in OPCODES.items()}


class NovaFault(RuntimeError):
    """An unsupported instruction or invalid memory/PC access."""


def encode_instruction(opcode: int, operand: int = 0) -> bytes:
    """Encode exactly four bytes: [opcode, operand_hi, mid, low]."""
    if type(opcode) is not int or opcode not in OPCODES:
        raise ValueError("invalid Nova-N1 opcode")
    if type(operand) is not int or not 0 <= operand <= ADDRESS_MAX:
        raise ValueError("Nova-N1 operand exceeds 24 bits")
    if opcode == 0 and operand:
        raise ValueError("FIN operand must be zero")
    return bytes((opcode, (operand >> 16) & 0xFF, (operand >> 8) & 0xFF, operand & 0xFF))


def decode_instruction(word: bytes) -> tuple[int, int]:
    if not isinstance(word, bytes) or len(word) != 4:
        raise ValueError("Nova-N1 instruction is four bytes")
    opcode, a, b, c = word
    if opcode not in OPCODES or (opcode == 0 and (a or b or c)):
        raise NovaFault(f"invalid Nova-N1 instruction 0x{int.from_bytes(word, 'big'):08X}")
    return opcode, (a << 16) | (b << 8) | c


class NovaCPU:
    """Plausible accumulator-style 1968 CPU; output is uninterpreted bytes."""

    def __init__(self, installed_bytes: int = DEFAULT_NOVA_INSTALLED_BYTES):
        self.memory = NovaMemory(installed_bytes)
        self.pc = 0                    # 24-bit *byte* address
        self.a = 0                     # 32-bit unsigned accumulator
        self.halted = False
        self.steps = 0
        self.output = bytearray()      # raw CVL-68 *candidate* bytes

    @property
    def z(self) -> bool:
        return self.a == 0

    def load_regions(self, regions: dict[int, bytes]) -> None:
        """Atomically stage sparse code+data segments; reject overlaps."""
        ranges: list[tuple[int, int, bytes]] = []
        for addr, payload in regions.items():
            if type(addr) is not int or addr < 0 or addr > ADDRESS_MAX:
                raise ValueError("invalid 24-bit image address")
            if not isinstance(payload, bytes) or not payload:
                raise ValueError("each image region must contain bytes")
            if len(payload) > len(self.memory.data) - addr:
                raise ValueError("image region outside installed memory")
            ranges.append((addr, addr + len(payload), payload))
        ranges.sort()
        if any(a[1] > b[0] for a, b in zip(ranges, ranges[1:])):
            raise ValueError("overlapping Nova memory regions")
        for start, _, payload in ranges:
            self.memory.load(start, payload)

    def step(self) -> tuple[int, str]:
        if self.halted:
            raise NovaFault("Nova-N1 already halted")
        at = self.pc
        if at % 4:
            raise NovaFault(f"unaligned PC 0x{at:06X}")
        try:
            op, operand = decode_instruction(self.memory.read_bytes(at, 4))
            next_pc = (at + 4) & ADDRESS_MAX
            next_a = self.a
            output_byte = None
            if op == 0x10:      # LEGB
                next_a = self.memory.read_byte(operand)
            elif op == 0x11:    # LEGW
                next_a = self.memory.read_word32(operand)
            elif op == 0x12:    # PONB
                self.memory._range(operand, 1)
            elif op == 0x13:    # PONW
                self.memory._range(operand, 4)
                if operand % 4:
                    raise ValueError("unaligned PONW")
            elif op == 0x20:    # ADDE aligned word
                next_a = (self.a + self.memory.read_word32(operand)) & WORD_MASK
            elif op == 0x21:    # SVBT aligned word
                next_a = (self.a - self.memory.read_word32(operand)) & WORD_MASK
            elif op in (0x30, 0x31):
                if op == 0x30 or self.z:
                    if operand % 4:
                        raise ValueError("unaligned branch target")
                    self.memory._range(operand, 4)
                    next_pc = operand
            elif op == 0x40:
                next_a = operand
            elif op == 0x41:
                next_a = (self.a + operand) & WORD_MASK
            elif op == 0x50:
                output_byte = self.memory.read_byte(operand)
            elif op == 0x60:
                word = self.memory.read_word32(operand)
                F32.decode(word)
                next_a = word
            elif op == 0x61:
                next_a = F32.add(self.a, self.memory.read_word32(operand))
            elif op == 0x62:
                next_a = F32.subtract(self.a, self.memory.read_word32(operand))
            elif op == 0x64:
                next_a = F32.multiply(self.a, self.memory.read_word32(operand))
            elif op == 0x65:
                next_a = F32.divide(self.a, self.memory.read_word32(operand))
            elif op == 0x63:
                self.memory._range(operand, 4)
                if operand % 4:
                    raise ValueError("unaligned FPON")
                F32.decode(self.a)
        except ValueError as exc:
            raise NovaFault(f"Nova-N1 fault at PC=0x{at:06X}: {exc}") from exc
        # Commit after validations. Instruction faults leave A/PC/output unchanged.
        if op == 0x12:
            self.memory.write_byte(operand, self.a & 0xFF)
        elif op == 0x13:
            self.memory.write_word32(operand, self.a)
        elif op == 0x63:
            self.memory.write_word32(operand, self.a)
        if output_byte is not None:
            self.output.append(output_byte)
        if op == 0:
            self.halted = True
        self.a = next_a
        self.pc = next_pc
        self.steps += 1
        return at, OPCODES[op]

    def run(self, max_steps: int = 100_000) -> bytes:
        if type(max_steps) is not int or max_steps < 1:
            raise ValueError("max_steps must be a positive integer")
        count = 0
        while not self.halted:
            if count >= max_steps:
                raise NovaFault(f"step limit {max_steps} at 0x{self.pc:06X}")
            self.step()
            count += 1
        return bytes(self.output)
