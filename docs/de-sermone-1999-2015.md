# De Sermone (1999–2015)
## 《文献之语：SERMO 从服务器脚本走向网络应用》

> **DRAFT · 2026-11-24.** 所有架空版本、发布日期、语言语法、市场结果均为候选历史，非 CANON。本文只提供纸面语义与算例，不交付解释器或可运行程序。

## 1999—2000：先有图书馆的脚本，没有浏览器脚本

NODVS 把文档拆成带类型与长度的记录，大学图书馆却发现它难以手写。旧 CVL-68 目录与国际 COS 文献也不能通过拼接字节直接交换。因此一类名为 SERMO（拉丁语语词暂定）的脚本首先用于文献筛选、显式转码与生成结构化目录。此时早期 CVL-only 前身不等于 2002—2004 年综合 COS 候选形成的 SERMO I。

与纯文本模板相比，SERMO 选择把标题、段落、引用当作语言级记录，而不是把任意字符串插入可执行标记。图书馆可以先验证文字与引用，再让服务端生成 NODVS 文档。代价是需要学习记录类型、版本号、编译工具和编辑器，普通小网站仍可能选择轻量标记语言。

## 2002—2004：第一代 FORM 文档语言

[候选 SERMO-I/R1](../specifications/SERMO-I-R1.md) 在纸面上定义严格的 TEXTVS/OCTETI 区分、不可变值、checked NAT、REFERENTIA、FORMA 与 OPVS。开发者直接表达文档结构：

    OPVS SALVTATIO(NOMEN: TEXTVS): TEXTVS;
        REDDE "SALVE " + NOMEN;
    FINIS;

    FORMA INDEX(NOMEN: TEXTVS);
        TITVLVS 1 = "SALVE";
        PARAGRAPHVS 2 = SALVTATIO(NOMEN);
        LIGAMEN 3 EX 2 SPATIVM(6, LONGITVDO(NOMEN)) AD REF(1,2,1,0);
    FINIS;

这段候选源码使用古典拉丁核心字符，不需要真实 ASCII 的 J/U/W。标识符初版限制在拉丁核心字符，希腊语、中文等仍可进入字符串；希腊科学标识符是后续可研究的独立扩展。它生成文档，不执行链接，不发布资源。外部主机才有权为生成的内容绑定资源和修订号。

### Paper vector

Use the COS-97 trial registry FFFF and parameter NOMEN = 中文 (020000,020001). The result is sandbox-only.

| Record | Content | W1 bytes | C24 byte count |
| --- | --- | --- | ---: |
| 1 TITVLVS | SALVE | 52 41 4B 54 45 | 15 |
| 2 PARAGRAPHVS | SALVE 中文 | 52 41 4B 54 45 20 D0 00 D0 01 | 24 |
| 3 LIGAMEN | source 2, start 6, count 2, target 1:2:1:0 | fixed 36-byte binary payload | 36 |

Paragraph = eight CIDs, ten W1 octets. The Chinese span begins after six CIDs (SALVE plus space); C24 byte offset 18, W1 byte offset 6. The link's own source span stays 6,2 in both encodings.

NODVS R1 total = 28 header + 3×12 record headers + 5 title + 10 paragraph + 36 link = **115 W1 octets**. C24 total = 28 + 36 + 15 + 24 + 36 = **139 octets**. Excluding outer RETE framing. The source code itself is not transmitted as a NODVS document.

The same form called with an empty NOMEN fails link validation (zero span); a new name changes content and cannot reuse the prior immutable revision. This is a manual calculation, not an execution or conformance result.

## 2005—2008：服务端语言开始脱离单纯模板

候选 SERMO II / MINISTER 出现模块和服务接口，大学档案馆希望脚本能够从旧磁带索引中查询作者，把希腊数学标题与本地地名放到同一网页。厂商则希望做商业目录、搜索和账户界面。语言的关键问题不只是怎样定义函数，而是哪些文件能够读取、查询是否可以写入、请求错误如何表示、用户私密结果能否进入公开缓存。

LIBERTAS CODICVM 的开放档案精神可能促进公共文本转换库与记录编辑器共享，但不能证明任何具体语言工具链已开源。

## 2009—2012：移动互联网带来的第二次语言分裂

低功耗终端不愿为每个网页启动完整服务器脚本运行时。某些厂商可能提供 CLIENS 受限客户端配置，允许用户点击列表、查询资料、更新局部视图；另一些设备只显示服务器生成的静态 NODVS。原有 R1 文档仍是被动的，不会因新语言而自动执行。

候选异步模型采用局部事件循环、显式任务、结果匹配与能力句柄，而不是允许任意字符串变成网络请求或源代码。若用户依次选择两份地图，先发出的请求后返回时，旧结果不得覆盖新选择。这个问题在任何语言文明都存在，不是拉丁语天然带来的特性。

具体设计见 [SERMO III runtime study](../specifications/SERMO-III-runtime-study.md)。没有实际 RETE 安全握手、浏览器 origin、动态提交或脚本分发格式。

## 2013—2015：三大语言传统的协作而非合并

| 语言 | 候选技术角色 | 必须明确的边界 |
| --- | --- | --- |
| MODVLA | 操作系统服务、宿主 API、驱动和模块 | 共享接口不等于共享 ISA、内存布局或 ABI |
| SERMO | 网络资源、文档构造、文本处理与可选客户端事件 | 字符数不等于字节数；引用不等于权限 |
| RATIO | 科学数值、单位及误差契约 | 科研结果的可复算性不等于网页能正确渲染 |

例如地理研究站由 MODVLA 宿主提供文件和设备服务；RATIO 风格的数值服务计算地形统计、声明数值精度；SERMO 将结果组织为 NODVS 页面并提供指向特定版本的 LIGAMEN 引用。实际地图附件格式、单位系统、RATIO 语法及服务 ABI 仍需研究。SERMO 不替代这三层。

未来可有独立的纯函数模块、记录变换、缓存策略和跨平台应用框架；浏览器完整支持 SERMO III 的普及结果仍未确定。轻量文本网页竞争路线保持开放。

## Next research

The next useful design step is MODVLA's early module/interfaces and explicit data-layout tradition, or TABVLA's document layout and application UI ecosystem. Neither needs an interpreter. RATIO deserves a separate numerical-language phase rather than inheriting SERMO's checked NAT semantics.

Related: [SERMO I](../specifications/SERMO-I-R1.md), [SERMO III runtime](../specifications/SERMO-III-runtime-study.md), [earlier language history](programming-ecosystem-2005-2015.md), [NODVS/RETE](nodvs-rete-1998-2005.md).
