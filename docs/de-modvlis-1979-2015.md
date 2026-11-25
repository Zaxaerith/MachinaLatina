# De Modvlis (1979–2015)
## 《模块之争：MODVLA 与跨架构系统软件》

> DRAFT · 架空技术史，2026-11-25。所有版本、年代和商业结局都是候选，非 CANON。下文是文档与手工算例，并没有开发语言编译器。

## 1979—1981：三种机器、一份模块接口

旧 XXXVI 的 36 位机器字、Nova 的 32 位字节寻址和 Sextaria 的 48 位科学机提案，使“将内存结构直接写入磁带”成为危险的行业惯例。一份在某台机器上可读取的记录，可能在另一台机器上发生字段错位。更宽的机器字也不意味着更宽的逻辑计数值必须出现在每个文件里。

候选 MODVLA I 因此把模块分为 INTERFACIES（接口）、CORPVS（实现），并把 RECORDVM 逻辑记录与 EXTERNA 外部表示分别声明。早期语法应能在声明的 CVL-68 源码编码中表达，不要求尚未诞生的 COS。历史语言名称和具体版本仍可修订。

现实 1970 年代的 Mesa 和 Modula-2 提供模块化系统语言的时代参照，1987 年 XDR 提供外部数据表示的稍晚参照；它们不是本世界的直接祖先。参见 [Mesa 历史](https://softwarepreservation.computerhistory.org/mesa/)、[Wirth](https://people.inf.ethz.ch/wirth/Articles/Modula-Oberon-June.pdf)、[RFC 1014](https://www.rfc-editor.org/rfc/rfc1014)。

## 1982—1985：为什么同一份数据不等于同一个程序？

设想科研档案模块定义测量记录 IDENTITAS (16 bits), NOTA (8 bits), NVMERVS (24 bits)。其外部格式固定六八位单元，依次为 12 34 A5 01 02 03。XXXVI 可将三个值分别放入三个原生机器字；Nova 可以采用八字节对齐结构；Sextaria 候选编译器可用三个原生字，或将外部记录压入一个 48 位字。不同内存表示经过显式编码后才形成相同的六字节记录。

这并不证明 1954 P0 已拥有编译器调用约定、1968 N1 已有系统栈、1976 S0 已有 ISA。需要后继机器和工具链才能实现。准确的纸面规范见 [MODVLA-I/R1](../specifications/MODVLA-I-R1.md) 及 [布局研究](../specifications/MODVLA-layout-and-abi-study.md)。

## 1986—1995：系统语言的第一次分叉

**DRAFT MODVLA II** 可能从模块化记录处理扩展到文件、设备和本机地址。大众 Nova 厂商希望低开销直接操作设备；科学机构要求显式记录格式、数值单位和转换诊断。编译器可同时提供可移植类型和明确标为目标特定的 VERBVM、硬件入口等能力，而非把所有设备寄存器假装成跨平台对象。

**DRAFT MODVLA III** 可能出现模块接口版本、独立编译对象及链接器的 ABI 检查。共享源码可降低移植成本，却仍需要不同机器的代码生成器、启动代码、系统服务适配器和设备驱动。厂商可能将自己的 ABI 扩展视为竞争优势，并不必然接受开放二进制格式。

## 1995—2005：从磁带接口到文献网络

COS 的出现迫使语言再次区分字节、六位/八位旧字符码与全球抽象字符身份。MODVLA 的后续版本可以增加 CID24 逻辑类型及显式解码服务；这不是 1979 年已经存在的类型。SERMO 从 NODVS 的文档构造需求发展起来，可调用由 MODVLA 实现的宿主服务，但不能把服务权限当作任意数值引用。NODVS/RETE 的八位网络记录也不要求 MODVLA 的本机数据结构与协议字节直接一致。

## 2005—2015：三类操作系统如何共享语言而非共享内核

| 系统候选 | MODVLA 适配方向 | 仍不兼容的事项 |
| --- | --- | --- |
| ORDO-N | 进程、字节流、文件描述服务 | 本机程序装载、设备驱动、系统调用 |
| PARTES | 类型化消息、记录服务、科学数据 | IPC、资源权限及其内核实现 |
| CVSTOS | 受限设备服务与不透明资源句柄 | 启动链、低功耗 ISA、应用权限模型 |

一个共同的模块接口不意味着这三种系统使用相同内核、机器码或服务 ABI。后世自由软件运动可以以源码可移植性和公开接口为目标，而非假设旧 36 位程序永久二进制兼容。

## Candidate lineage

| Date | Proposed edition | Development |
| --- | --- | --- |
| 1979–1985 | I | logical types, separate interface/body, explicit external records |
| 1986–1992 | II | candidate local references, device-specific native modules, I/O |
| 1993–2000 | III | separate compilation, interface revisions, target ABI tags |
| 2001–2015 | IV | COS and network services, OS adapters, service-handle discipline |

Only the small I/R1 paper subset and illustrative layout rules are described concretely. II–IV remain historical directions, not grammars or toolchains. No full memory management, calling convention, interrupt handling, concurrency or native linking has been settled.

**Next:** give RATIO a genuine scientific-language identity through numeric formats, rounding, physical units and error contracts; or proceed to the three OS families' early kernel and service interfaces. No CI needed for documentary research.
