"""Exact-rational reference for two fictional pre-universal floating formats.

Not IEEE 754. Zero is canonical; subnormals, infinities, NaN, negative zero
and overflow/underflow gradual behavior are deliberately unspecified/trapped.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


class FloatFault(ValueError):
    """Invalid representation, exponent overflow or unsupported underflow."""


@dataclass(frozen=True)
class FloatFormat:
    name: str
    bits: int
    exponent_bits: int
    fraction_bits: int
    bias: int

    def __post_init__(self):
        if self.bits != 1 + self.exponent_bits + self.fraction_bits:
            raise ValueError("sign + exponent + stored fraction must sum to word bits")

    def _two_power(self, exponent: int) -> Fraction:
        return Fraction(1 << exponent, 1) if exponent >= 0 else Fraction(1, 1 << -exponent)

    def _floor_log2(self, value: Fraction) -> int:
        if value <= 0:
            raise ValueError("expected positive number")
        tentative = value.numerator.bit_length() - value.denominator.bit_length()
        if value < self._two_power(tentative):
            tentative -= 1
        return tentative

    def encode(self, value: Fraction | int) -> int:
        value = Fraction(value)
        if not value:
            return 0
        sign = int(value < 0)
        value = abs(value)
        exp_unbiased = self._floor_log2(value) + 1
        biased = exp_unbiased + self.bias
        max_exp = (1 << self.exponent_bits) - 1
        if biased <= 0:
            raise FloatFault(f"{self.name}: exponent underflow (subnormals unavailable)")
        if biased >= max_exp:
            raise FloatFault(f"{self.name}: exponent overflow")
        exact_m = value / self._two_power(exp_unbiased - self.fraction_bits)
        quotient, rem = divmod(exact_m.numerator, exact_m.denominator)
        # ties to even; no host hardware float operation affects result.
        if 2 * rem > exact_m.denominator or (2 * rem == exact_m.denominator and quotient % 2):
            quotient += 1
        if quotient == 1 << self.fraction_bits:
            quotient = 1 << (self.fraction_bits - 1)
            biased += 1
        if biased >= max_exp:
            raise FloatFault(f"{self.name}: exponent overflow after rounding")
        if quotient < 1 << (self.fraction_bits - 1):
            raise AssertionError("normalized mantissa too small")
        return ((sign << (self.bits - 1)) | (biased << self.fraction_bits) | quotient)

    def decode(self, word: int) -> Fraction:
        if type(word) is not int or not 0 <= word < (1 << self.bits):
            raise FloatFault(f"{self.name}: invalid {self.bits}-bit word")
        if word == 0:
            return Fraction(0)
        sign = (word >> (self.bits - 1)) & 1
        exponent = (word >> self.fraction_bits) & ((1 << self.exponent_bits) - 1)
        fraction = word & ((1 << self.fraction_bits) - 1)
        if exponent in (0, (1 << self.exponent_bits) - 1):
            raise FloatFault(f"{self.name}: exponent field reserved")
        if fraction < 1 << (self.fraction_bits - 1):
            raise FloatFault(f"{self.name}: unnormalized or invalid mantissa")
        result = Fraction(fraction) * self._two_power(exponent - self.bias - self.fraction_bits)
        return -result if sign else result

    def add(self, left: int, right: int) -> int:
        return self.encode(self.decode(left) + self.decode(right))

    def subtract(self, left: int, right: int) -> int:
        return self.encode(self.decode(left) - self.decode(right))


# Fractional binary significand with an EXPLICIT leading 1 bit in the fraction.
# Normal: 1/2 <= mantissa / 2**fraction_bits < 1.
# The exponent is base-2 and biased; neither format is IEEE 754.
F36 = FloatFormat("XXXVI-F36", 36, 8, 27, 128)
F32 = FloatFormat("Nova-F32", 32, 7, 24, 64)
