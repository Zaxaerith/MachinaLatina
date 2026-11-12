# Machina XXXVI-R0 — 36-bit Eight-Bit-Text Adapter Study

**Status: DRAFT MEMORY/RECORD PROFILE.** Not part of the 1954 baseline CPU, not a new implemented opcode set.

R0 preserves the [Machina XXXVI/P0](Machina-XXXVI.md) machine word and addresses. A later adapter can store CVL-68 candidate **8-bit bytes** using 4 bytes in the high 32 bits of each 36-bit word, with four low **reserved zero bits**. This is an example of compatibility engineering rather than a claim that 36-bit machines naturally evolve into 32-bit machines.

```text
36-bit retrofit memory word, bit 35 on the left

35                  28 27                  20 19                  12 11                   4 3   0
+---------------------+---------------------+---------------------+---------------------+------+
|      CVL byte 0     |      CVL byte 1     |      CVL byte 2     |      CVL byte 3     | 0000 |
+---------------------+---------------------+---------------------+---------------------+------+
```

**Rules in prototype R0:**

1. `word = int.from_bytes(four_bytes, "big") << 4`. Missing bytes are `0x00` fillers.
2. Each word must fit unsigned 36 bits; the low nibble must equal zero.
3. Store exact **logical length** as external metadata; it is not derivable from zero padding.
4. Reject too many/few words for declared length and nonzero filler trailing bytes.
5. These values form **data records** and not executable P0 instructions.
6. Preserve original packed six-bit archives separately if byte-exact historical restoration is required.
7. No device interrupt, controller timing, tape framing or independent adapter instruction protocol is defined.

**Example:** candidate CVL-68 `SALVE ΛΟΓΟΣ` (11 bytes) becomes three words: `52414B540`, `45208A8E0`, `828E91000` (hex, nine characters per 36-bit word). Its last word carries three data bytes and one trailing filler byte; there are 4 reserved low bits per word.

**Limit:** this is not native character addressing. An old instruction can still only select entire 36-bit memory words. The CPU's 15-bit addressing remains unchanged.

Reference: [Phase VII analysis](../docs/phase-vii-architecture-fork.md).
