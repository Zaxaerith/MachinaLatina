# De Revolutione Machinarum Domesticarum (1981–1995)
## 家庭计算机革命：Nova 微机、Sextaria 工作站与双文字桌面

> **DRAFT · 架空技术史提案（2026-11-23）**。文中所有架空厂商、上市日期、争议事件和产品名称均为创作候选，并非真实历史，也未上升为 Machina Latina 的 CANON。本文不包含可执行程序、GUI 模型或已完成的操作系统。

## 从机器字争论到桌面革命

[前一篇研究](de-bello-verborum-et-machinarum-1973-1985.md)留下三种架构：36 位的 XXXVI 科学计算遗产，32 位的 Nova 字节机器，以及尚在研究中的 48 位 Sextaria 高端科学机。

进入 1980 年代，新的问题不是选择唯一字长，而是**哪种计算机能让普通人买得起、读得懂、写得出并打印得好**。古典拉丁语作为通用工程与行政语言，希腊语作为科学与高等教育的重要语言，是本世界已有前提。这将改变人们对于键盘、文档和印刷的要求，却不意味着任何人免费获得高质量图形界面。

### 现实史实参照，非架空事件

- **HIST：** Xerox Alto 自 1973 年起探索位图显示、指针、窗口和网络，1981 年的 Xerox Star 延伸了文档中心的交互思想。参考 [Computer History Museum](https://computerhistory.org/press-releases/xerox-alto/) 与 [IEEE Spectrum](https://spectrum.ieee.org/graphical-user-interface)。
- **HIST：** IBM PC 于 1981 年上市，采用 Intel 8088 处理器。内部计算位宽与外部数据总线可以不同，这启发我们区别 Nova 软件家族与微机的物理字长。参考 [IBM](https://www.ibm.com/history/personal-computer)。
- **HIST：** 1984 年 Macintosh 的 128 KiB 内存说明早期 GUI 要严肃面对存储约束。参考 [Smithsonian](https://americanhistory.si.edu/collections/object/nmah_334371)。
- **HIST：** 1985 年 PostScript、LaserWriter 与 PageMaker 一类技术推动桌面出版；存储字符与排印准确是两个不同难题。参考 [Computer History Museum 档案](https://archive.computerhistory.org/resources/access/text/2012/10/102746510-05-01-acc.pdf)。
- **HIST：** Unicode 第一版的现实出版史可作为 1990 年代文字统一化的比较对象，但不能直接移植到本架空世界。参考 [Unicode Consortium](https://www.unicode.org/history/publicationdates.html)。

## 第一幕：1981—1983 年，Nova 进入家庭

**DRAFT 1981：** Nova 系列的廉价后裔走向学校、办公室与家庭。本项目暂以 **Nova Minor** 称呼这条产品研究路线。最便宜的机器可能采用八位数据通路，或窄外部总线的十六位 CPU，预装 CVL-68 的基本拉丁与希腊字形；它不必运行 Nova-N1 的全部 32 位机器指令。

竞争者主要有两类：一类以字符终端为中心，使用文本屏幕和少量 ROM 字体，成本较低；另一类为了学校、大学和出版市场而购买位图显示器、鼠标、磁盘和字体软件，售价自然更高。

**DRAFT 1982 采购争端：** 某所学校购买一批宣称支持 CVL-68 的低价微机，结果发现机器可以把希腊小写字母写入磁盘，却无法在内置 ROM 中正确显示。采购方因此要求厂商区分四项能力：**字符可存储、字形可显示、文本可编辑、页面可正确打印**。这起故事是为了体现真实的技术约束而编造的事件。

## 第二幕：1984—1987 年，双文字桌面之争

**DRAFT 1984：** 大学与科学出版机构推动一种称作 **TABVLA** 的图形桌面概念。这个名字只是拉丁风格候选词，不是实际历史商标，也不是本仓库已运行的软件。

与单纯图标、窗口和鼠标不同，TABVLA 的核心卖点是：同一份文件可以包含拉丁文说明、希腊学术引用、数学符号及具有重音和气音记号的希腊词汇。

假设的菜单词汇：

| 功能 | 暂定界面词 | 技术任务 |
| --- | --- | --- |
| 桌面 | TABVLA | 文件、程序与操作环境 |
| 窗口 | FENESTRA | 同时显示若干文档 |
| 文档容器 | SCRINIVM | 逻辑文件组织，而非磁盘物理结构 |
| 文本编辑器 | SCRIPTVRA | 保存字符身份和编辑序列 |
| 页面排版 | FORMA | 字体度量、段落、纸面和输出设备 |
| 输入脚本 | LATINA / GRAECA | 输入法状态，不应改变已有文字身份 |

这些名称的语言学适切性仍待古典学者评估。它们是技术世界观的一部分，不等于把现代操作系统菜单逐字翻译成拉丁语。

**技术争议：** CVL-68 已经为拉丁 A 与希腊 Α 分配不同字符身份，但不保证两者字体上不同。希腊文 λόγος 的候选字节序列为 AA AE B8 A2 AE 98：其中 B8 是依附在元音上的附加记号。一个把六个字节分别画成六个等宽格子的终端，会排错文字。文件、编码字节、可编辑字符簇和最终字形必须分离。

**DRAFT 1986：** 大学采购规范将“移动光标是否拆开组合重音”“希腊末尾 sigma 是否按上下文变换”“复制粘贴会否混淆 Latin A 与 Greek Alpha”“打印是否正确叠加气音记号”列为实测项目。高级出版系统因此能够与便宜微机形成差异化竞争。

## 第三幕：1987—1990 年，科学工作站不等于家庭电脑

Sextaria 的商业地位仍是 DRAFT。若科学用户采购它，合理原因应来自更高的数值精度、科研绘图、测绘模型、仪器接口、专业打印与软件库，而不是凭 48 位字长就认为“图像更漂亮”。

家庭 Nova 则依靠成本、第三方应用、维修零件和更大的软件市场获胜。一个廉价 Nova 微机可以打开 Sextaria 制作的科学报告，仍不代表它能运行 Sextaria 的二进制程序或复现其数值结果。

**DRAFT 1989 兼容争端：** 某厂商复刻 TABVLA 的窗口布局，却与原系统的程序 ABI 不兼容。由此产生不同层次的“兼容”定义：

- CVL-68 字节可以互换；
- 文档可以被解析、字体与版式可能不同；
- 应用源代码可重新编译；
- 完整旧程序可直接执行。

只有最后一项才是二进制兼容。市场宣传不能用图形外观偷换它。

## 第四幕：1990—1992 年，八位双文字标准的天花板

1990 年代的全球网络正在使 CVL-68 的局限显现：256 个位置难以容纳世界其他文字、所有古典希腊附加符号和大量数学记号。

**DRAFT 1991：** 学术出版机构推动一种全球通用字符身份注册体系。它可能选择扩展字节、定长宽字符或混合方案；本篇暂不将它命名为 Unicode，也不假定现实中的 Unicode 标准组织和决策照搬到这个世界。

特别值得保留的政治争议是：当拉丁与希腊被视为原生文字时，其他语言是否遭到系统性忽视？这使国际标准化不仅是容量和兼容问题，也是文化权力问题。

## 第五幕：1993—1995 年，究竟什么是“文档”？

两种文档理念发生冲突：

- **文字语义优先**：存储字符身份、结构与引用，交给不同字体和设备排版。
- **页面视觉优先**：保存精确几何、字形摆放和印刷效果，即便可编辑性较差。

科学家要求公式、测量表格和希腊记号在未来仍可被机器理解；出版者要求纸面与屏幕一致；办公室用户则要求便宜、快速、容易交换。这可能孕育至少两种并存的文档规范，而不是直接复制现实世界的 DOC 或 PDF。

到 1995 年，三条技术路线可能共存：Nova 大众桌面、TABVLA 式学术排版环境、Sextaria 科学工作站。**这是一种候选历史结局，不是市场份额已经确定的 CANON。**

## 下一阶段的因果链

进入 1995—2005 年时，标准化矛盾将从“如何把希腊字正确显示在我的桌面”变为“如何让世界上任何文字通过网络、文件与网页被正确解析、搜索和存档”。

这可能是比简单重命名 HTTP、HTML 和 Unicode 更独特的平行互联网发展史。

Related: [Nova PC hardware study](../specifications/Nova-personal-computer-study.md), [CVL desktop typography](../specifications/CVL-desktop-typography-study.md), [1985 architecture war](de-bello-verborum-et-machinarum-1973-1985.md).

## 2026-11-25 Nova family follow-up

[Maior/Magna R1](../specifications/Nova-Maior-Magna-R1.md) and [Nova family evolution](../specifications/Nova-family-evolution-study.md) propose later hardware profiles. These do not alter existing N1/Sextaria specifications, claim native OS compatibility or ratify historical adoption. All new profiles remain DRAFT.

## 2026-11-26 graphics follow-up

[IMAGO](../specifications/IMAGO-86-R1.md), [FIGVRA](../specifications/FIGVRA-95-R1.md) and [LVDVS](../specifications/LVDVS-console-study.md) provide subsequent paper candidates; no CPU ISA or existing numeric format changed. Actual devices, shader ISA, full drivers and accelerator execution remain open.
