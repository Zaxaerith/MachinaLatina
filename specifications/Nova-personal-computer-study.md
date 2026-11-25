# Nova Personal Computers, 1981–1995
## 微处理器经济、软件家族与兼容性分层

> **DRAFT；仅为文档研究。** 现有 Nova-N1 是一套实验性的 32 位固定指令、24 位字节地址 CPU。本文不宣称 1981 年的廉价家用微处理器能够低成本地直接实现全部 Nova-N1 指令。

## 1. 三种不同的兼容性

| 等级 | 兼容目标 | 不能暗示 |
| --- | --- | --- |
| DATA | 读取 CVL-68 字节、文档和具有标记的数值记录 | 同样的 CPU 指令 |
| SOURCE | TRANFOR 或未来 MODVLA 的共同子集可编译 | 相同系统调用和文件布局 |
| BINARY | 对象文件、调用约定、系统 ABI 与 ISA 一致 | 仅靠文本兼容即可获得 |

“Nova 兼容”不是足够精确的标签。廉价 8 位机器可能拥有 CVL-68 标准键盘，却与研究机构 32 位 Nova-N1 程序二进制不兼容。

## 2. 候选硬件层次

| 架空家族 | 拟议时代 | 候选实现 | 主要需求 |
| --- | --- | --- | --- |
| Nova Minor | 1981–1984 | 八位数据通路、分段/银行式扩展寻址 | 廉价终端、教育、文本编辑 |
| Nova Media | 1984–1989 | 十六位数据通路，8/16 位外部总线 | 图形、文件系统、办公 |
| Nova Maior | 1988–1995 | 32 位程序员模型，实际 ISA 待定义 | 商业服务器和高端桌面 |

年代、型号和指标均为设计情景而非发布记录。对于 Nova Maior，保留或重写 N1 固定四字节指令尚有权衡；更紧凑的指令可能降低内存成本，但损失直接兼容。

## 3. 真实的图形存储成本

基础位图帧缓冲大小（未计窗口备份、字体、程序和磁盘缓存）：

- 320×200，1 bit/pixel = 8,000 字节；
- 640×480，1 bit/pixel = 38,400 字节；
- 640×480，4 bit/pixel = 153,600 字节；
- 256 个字形、每字形 8×16 单色位图，若每编码值一份 = 4,096 字节。

最后一个数仅计算字形像素，不包括希腊附加符号的正确组合位置、字体度量、可缩放轮廓和未知字形。复杂希腊文的正确绘制不能靠“256 个字节就是 256 个字符格”来解决。

## 4. 字符、磁盘和固件的边界

存储字节兼容不等于显示能力相同。需要分别讨论：键盘扫描码与语言输入状态、CVL-68 字符身份、屏幕字符簇、字体绘制、磁盘文件记录、打印机页面指令。

没有理由仅凭 CVL-68 是八位就推断 CPU 必须有八位 ALU，也没有理由凭 48 位字就断言 Sextaria 文本存储密度高于 Nova。

## 5. 可能出现的兼容诉讼（纯虚构案例）

一款低价微机拥有同样的 TABVLA 式图标，但无法运行已有 TABVLA 可执行程序。它或许能打开文字语义相同的文件，却无法保持页面排版。这场冲突可能推动协会把“界面行为、文档互换、源代码、二进制”的合规等级分开审核。

## 6. 未决技术问题

具体微机 ISA、引导 ROM、操作系统 API、磁盘格式、可执行文件加载、语言字体 ROM 和 1995 年前的网络接口仍未确定，不在本章偷偷确认为标准。尤其不允许把真实 IBM PC 或 Macintosh 的指令集直接换个名字。

See [Phase XVI narrative](../docs/de-revolutione-machinarum-domesticarum-1981-1995.md), [existing Nova N1 profile](Machina-Nova-N1.md), [Sextaria study](Sextaria-S0-study.md).

## 2026-11-25 Nova family follow-up

[Maior/Magna R1](Nova-Maior-Magna-R1.md) and [Nova family evolution](Nova-family-evolution-study.md) propose later hardware profiles. These do not alter existing N1/Sextaria specifications, claim native OS compatibility or ratify historical adoption. All new profiles remain DRAFT.
