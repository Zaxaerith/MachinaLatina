# De Ordine Novo (1970–2026)
## 新秩序：从批处理到通用操作系统
> DRAFT · 2026-11-26。年代、系统、商业竞争与分支均为架空候选，不是已实现内核。

## 1970—1987：批处理与交互
Ordo Operum 的历史构想继承 LABOR 作业、顺序记录与设备状态。现代 P0–P2 是 Python 宿主实验；OMR1 不是历史磁盘格式。1979 年前后候选 Ordo Interactive 逐步增加终端、文件工具和作业控制，但 Minor/Media 早期硬件不必支持保护模式。

## 1988—1995：ORDO-N I
Maior 后继硬件采用候选 PROTECT-R1：独立用户/监督寄存器组、4 KiB 页、两级页表、陷入与定时事件。ORDO-N I 选择单内核、私有进程空间、轮转调度和字节流接口。内核搬运字节而非解释每个字符身份或科研数值。图书馆要求格式元数据及原始档案完整保存，系统厂商则要求普通文件工具简单通用；用户态文档代理和显式容器可以折中。PARTES 保留类型化记录服务的不同路线。

## 1995—2005：ORDO-N II
Magna 64 位迁移使大型数据库、地图和科研应用获得更大地址空间；M32 模式不自动保证系统 ABI 或应用兼容。TABVLA 作为用户态桌面，负责窗口、字体、剪贴板、输入法和出版。旧 CVL 与新 COS 文档共存，NODVS/RETE 由独立软件处理，非内核解析。SERMO 可在后续阶段提供受限客户端交互。M64 内核扩展和 GUI 接口尚未设计。

## 2005—2015：ORDO-N III
依既有 LIBERTAS CODICVM 设定，公共档案与科研机构要求长期维护字符、排版、数值转换工具。候选 ORDO-N LIBER 分支可先从开放用户态库、接口文档、MODVLA 工具链发展，再形成可重建系统发行版。共享接口不代表共享专有代码或驱动。内核来源可为授权开放或独立重实现，未决；真实仓库 MIT/CC BY 4.0 许可不自动适用于虚构系统。商业系统仍可凭设备支持和服务竞争，自由软件亦可收费维护。

## 2015—2026：ORDO-N IV
现代后继系统可能发展多核、虚拟化、网络与独立加速器。必须另定一致性、原子操作、设备隔离和 ABI；MODVLA、RATIO、SERMO 可经显式接口协作。PARTES 和 CVSTOS 不必与 ORDO-N 合并。

| 候选年代 | 系统 | 方向 |
| --- | --- | --- |
| 1970–1978 | Ordo Operum | 批处理前史 |
| 1979–1987 | Ordo Interactive | 终端、文件工具 |
| 1988–1995 | ORDO-N I | 保护进程、字节流 |
| 1995–2005 | ORDO-N II | 64 位、TABVLA、网络 |
| 2005–2015 | ORDO-N III | 商业与开放发行版 |
| 2015–2026 | ORDO-N IV | 多核与异构 |

本阶段仅完成 [M32 保护扩展](../specifications/Nova-M32-PROTECT-R1.md)与[早期系统调用候选](../specifications/ORDO-N-I-R1.md)的纸面设计。不交付内核、持久磁盘格式、加载器、驱动、M64 或完整 GUI。参阅[原三系统研究](../specifications/operating-system-families-2005-2015.md)、[自由软件史](de-libertate-codicum-et-imperio-systematum-2005-2015.md)。

## 2026-11-26 PARTES follow-up

[S2 protection](../specifications/Sextaria-S2-PROTECT-R1.md), [PARTES I IPC](../specifications/PARTES-I-R1.md) and [record service](../specifications/PARTES-record-service-R1.md) are subsequent paper candidates. They do not alter existing S1 or ORDO-N contracts or establish implemented drivers, shared memory, or a Nova native IPC ABI.
