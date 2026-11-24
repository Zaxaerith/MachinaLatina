# De Codice Omnium Scripturarum (1997–2005)
## 全球文字标准的第一次工程妥协

> **DRAFT · 架空史与纸面算例，2026-11-24。** COS-97/R1、C24、W1、年代和实施争论是建议，不是已经发生的历史或程序交付。

## 1997—2005 候选发展

1997 年的 CSM 原则性建议把字符身份和字节格式分开。1998—1999 年的候选技术工作组讨论 16/24/32 位空间。档案与科研团体支持 24 位，考虑 Sextaria 的 48 位打包和 Nova 的 32 位处理能力；廉价 Nova 终端厂商反对固定三字节的磁盘成本。此时 24 位仍是抽象编号，非 CPU 字长命令。

2000—2001 年的候选妥协形成 C24 三字节固定宽度以及 W1 一至四字节格式。CCL 的老 CVL 字节获得显式一字节映射；国际文字获得额外短码银行。1990 年代的国际文字工作者可以反对旧文字享受最短格式，或争论两字节银行如何分配。固定编号和短码银行是不同的权衡，不能声称全球治理已经公平。

2002—2003 年的候选网络事故来自错误的字节扫描：W1 的第二字节可恰好等于标点或 NUL，老网页解析器却把它当作控制或分隔符。修正方向是逐符号解码、显式长度与独立记录校验，而不是在全球字符登记层假装已解决全部网络安全。2004—2005 年可以出现 C24/W1 共存的互操作建议，NODVS 网络仍须独立定义头部、记录与域名。旧 CVL 档案继续保留原始文件。

## Worked examples

For the old mixed record SALVE ΛΟΓΟΣ (11 assigned graphic bytes):

    CVL-68/RC1-L: 52 41 4B 54 45 20 8A 8E 82 8E 91
    COS identities: 010052 010041 01004B 010054 010045 010020
                    01008A 01008E 010082 01008E 010091
    COS/W1:         52 41 4B 54 45 20 8A 8E 82 8E 91
    COS/C24:        01 00 52 01 00 41 01 00 4B 01 00 54
                    01 00 45 01 00 20 01 00 8A 01 00 8E
                    01 00 82 01 00 8E 01 00 91

W1 = 11 bytes, C24 = 33 bytes. This is exact for a valid source sequence without normalization. It is not a claim that all legacy binary files or private extensions are compatible.

For the trial string AΑ中文, using sandbox assignments from the proposed registry document:

    CIDs: 010041 010080 020000 020001
    W1:   41 80 D0 00 D0 01
    C24:  01 00 41 01 00 80 02 00 00 02 00 01

W1 = 6 bytes, C24 = 12 bytes. D0 00 is one identity, not a NUL delimiter. These trial Han assignments have no CANON status.

## Boundary and malformed vectors

| Input W1 | Classification | Explanation |
| --- | --- | --- |
| D0 00 | structurally valid | 020000, trial 中 |
| EF FF | structurally valid | last two-byte bank ID 021FFF |
| F0 00 00 | structurally valid | 030000, trial 人 |
| F0 FF FF | structurally valid | last three-byte bank ID 03FFFF |
| F1 04 00 01 | structurally valid | 040001, trial digamma |
| F1 FF FF FE | structurally valid | max usable position; not assigned |
| F1 01 00 41 | reject | noncanonical; direct 41 exists |
| F1 02 00 00 | reject | noncanonical; D0 00 exists |
| F1 03 00 00 | reject | noncanonical; F0 00 00 exists |
| F1 01 00 58 | reject | permanently invalid legacy hole |
| F1 00 00 00 | reject | invalid sentinel |
| F1 FF FF FF | reject | invalid sentinel |
| D0 | reject | incomplete two-byte symbol |
| F0 00 | reject | incomplete three-byte symbol |
| F2 | reject | undefined leading byte |
| 00 | reject | unmapped device-control byte at boundary |

A syntactically valid numeric ID does not imply an assigned character in a declared registry release. Fixtures are illustrative and not a complete conformance suite. No converter or CI is committed.

## A small editorial erratum from earlier CVL-68/RC1

The old example used ἇ with smooth-breathing BB. In modern Greek transcription ἆ (alpha + smooth breathing + perispomeni) is the correct label for A0 BB BA; ἇ is rough breathing and should be A0 BC BA. Correct the example, not the source byte assignments. This is a documentation correction, not full philological review or COS normalization.

## Why the historical debate matters

W1 prioritizes installed bilingual systems and relatively compact international text, while C24 provides fixed-offset access and a uniform three-byte cost. W1 sacrifices self-synchronization and delimiter transparency; a later network generation may reasonably choose a competing stream codec. The costs of non-Latin/Greek languages, future registry placement, and how to protect poorly represented communities remain institutional conflicts inherited from CCL and CSM.

Related: [COS-97/R1](../specifications/COS-97-R1.md), [migration ledger](../specifications/COS-97-CVL-mapping.md), [CCL→CSM](de-potestate-scripturarum-1985-2005.md). Real historical comparisons: [Unicode encoding model](https://www.unicode.org/reports/tr17/), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629).
