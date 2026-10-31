"""Machina XXXVI/P0: fictional Latin–Greek 36-bit reference simulator.

All code is MIT licensed; CVL/ISA design remains experimental.
"""
from .cvl54 import CharacterFault, Printer, pack_codes, unpack_codes
from .image import load_image, parse_image
from .machine import Machine, MachineFault, encode_instruction

__all__ = [
    "Machine", "MachineFault", "CharacterFault", "Printer",
    "encode_instruction", "pack_codes", "unpack_codes",
    "parse_image", "load_image",
]
