# MODVLA, SERMO and RATIO — Programming Ecosystems, 2005–2015
## 三类编程语言为何走向不同的社会功能

> **DRAFT 历史推演，没有编译器、源码语法标准或正式运行时。** 现有 TRANFOR/P0/P1/P2 的现代实验性 Python 后端不意味着 MODVLA、SERMO 或 RATIO 已经存在。不要把它们写成拉丁版 C、Python 或 Rust。

## 树枝是如何从 TRANFOR 长出来的？

1950 年代实验性 TRANFOR 的特长是科学公式、有限数值运算以及逐步舍入。1970 年代的硬件分歧为大型程序和记录格式带来困难，推动了 MODVLA、RATIO 等架空语言思路。1990 年代 COS/NODVS 的多文字文档网络则给 SERMO 提供了脚本语言动机。

到 2005—2015 年，我们建议形成三套彼此互通而不完全合并的开发传统：

| 语言 | 主要用途 | 候选的设计特征 | 不应偷换成 |
| --- | --- | --- | --- |
| **MODVLA** | 操作系统、驱动抽象、记录服务 | 显式模块接口、字节/字符/记录类型、跨平台 ABI 描述 | C、Modula 或 Rust 的拉丁拼写 |
| **SERMO** | NODVS 应用、网络、文本转换 | 以 COS 字符身份为中心的文本对象和带类型文档节点 | JavaScript 或 Python 改关键字 |
| **RATIO** | 科学计算、数值审计、可复现研究 | 精度和误差契约、数学单位、编译目标与数据来源声明 | 一套现代 Rust borrow checker |

## 2026-11-25 MODVLA follow-up

[MODVLA-I/R1](../specifications/MODVLA-I-R1.md), [layout and ABI study](../specifications/MODVLA-layout-and-abi-study.md), and [language history](de-modvlis-1979-2015.md) distinguish interface, native layout and external record encoding. Later reference/handle semantics and OS adapters remain design studies, not implemented toolchains.

## MODVLA：模块不是“放在文件里的函数集合”

当两个系统的字节顺序、浮点格式、数据指针和调用约定可能不同，MODVLA 模块首先需要描述“什么是接口”。

一个接口可分别声明**抽象文本**、**原始字节**和**结构化数值记录**。允许一个文件被多个架构读取，并不代表内存中的字段布局可以直接共享。若想以一个共同源码调用 ORDO-N 和 PARTES 的系统功能，必须以模块适配器或目标 ABI 描述消除差异。

研究议题包括可选安全引用、序列化的显式长度、文件编码标签、可读错误类型、操作系统服务能力；不要求所有功能在 1980 年代一次性发明。

## 2026-11-24 SERMO follow-up

The [SERMO-I/R1 paper subset](../specifications/SERMO-I-R1.md) now proposes a concrete core syntax and type semantics; the [later runtime study](../specifications/SERMO-III-runtime-study.md) proposes optional client/server execution profiles. The older statement that no formal syntax had been proposed describes the original study; no interpreter, complete language or runtime has been implemented. See [history](de-sermone-1999-2015.md).

## SERMO：为什么 NODVS 使它与 JavaScript 不同？

如果网页先以内容类型和结构化节点为核心，那么 SERMO 早期可能更擅长解析、查询和转换学术文献及数据记录，而不一定先服务于浏览器动画。

它天然需要：
- COS 文字身份与原始字节的分别表示；
- 标注来源/编码的输入对象；
- 结构化的节点遍历和 LIGAMEN 链接；
- 明确的错误处理与不可解码文本保留；
- 服务器端沙箱及权限范围。

到 2010 年代，浏览器客户端是否也获得 SERMO 运行时仍未决定。假如移动端资源紧张，系统可能更倾向服务器端脚本和带权限的轻量客户端，而不是所有网页都默认执行同等强大的代码。

## RATIO：科学可复算性而非字节相同

RATIO 可以规定数值算法的舍入顺序、误差上界、单位约束和输入数据版本。若一个数值模型在 F36 和 F32 上得到不同中间结果，不能简单写成“错误”，而应给出允许范围与研究理由。

到 2015 年，即使科学机器的硬件迁移到通用 64 位处理器，这套数值契约仍可以通过库、编译器注解或实验清单发挥作用。语言是否仍保持独立，或成为 TRANFOR/MODVLA 的扩展，也是开放问题。

## 自由软件推动了哪些共同工具？

候选的公共开发工具至少需要：
- 源文件编码标记与 Unicode 类全球文字身份登记的显式映射（但不直接使用现实 Unicode 码位）；
- 源码与文档的内容身份；
- 目标 ISA / OS API / ABI 明确声明；
- 包管理中的合法多文字名称与同形异码警告；
- 编译与科学结果的不同级别可复现性声明。

**语法设计不得超前于社会需求。** 没有必要为三门尚未决定的语言伪造几百行其实无法执行的示例，再在下一阶段宣布实现成功。

See [2005–2015 narrative](de-libertate-codicum-et-imperio-systematum-2005-2015.md), [language roots 1974–1985](programming-languages-1974-1985.md), [OS families](../specifications/operating-system-families-2005-2015.md).
