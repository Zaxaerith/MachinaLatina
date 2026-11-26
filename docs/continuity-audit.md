# Continuity Audit / 设定连续性与技术一致性审计
## Phase XX · 2026-11-23

> **编纂审阅，不是代码验收。** 目的在于防止十九个研究阶段的暂时性主张被累计叙事误写成确定史实。没有运行模拟器、CI 或任何新的测试。这里记录的“通过”只代表文档层面的一致性判断；没有外部实验结果。

## 审计结果摘要

**可维持的已确定世界前提（CANON）**：古典拉丁语作为活语言、希腊学术制度地位、23 字母古典拉丁核心、双文字原生编码需求、1960 年代后期八位直接双文字编码的主流发展方向，和工程经济/历史惯性优先的写作方法。

**高优先级未决事项**：CVL-63 的七位通信模型、CVL-68 的字节映射和附加符号规范、Sextaria-S0 的具体 ISA/F48、全球 COS 编号与传输字节体系、架空厂商与机构的历史连续性、后继操作系统与语言的真实接口。

## 发现与处置

| 编号 | 发现 | 影响 | Phase XX 的处理 |
| --- | --- | --- | --- |
| C01 | [Chronology](chronology.md) 中 1970s 与 1981–1985 条目交错、前十九阶段多次增加重叠年代 | 用户误认为时间线先后或世界史已确定 | 重整为一次连续的 1954—2026 年代表 |
| C02 | README 顶部还把“Phase XV”称为当前重点，后来又增加 XVI—XIX 章节 | 新读者不清楚项目入口 | 首页统一以 Phase XX 通史导读，早期报告原样保存 |
| C03 | 旧文档中把宿主 Python Ordo Operum 的 CAPTA/STAT 指令称作 fictional 1970s device | 读者可能把研究模型误认已出土的历史内核 | 通史和机构索引明确区分“架空原型机提案”和“现实研究代码”；旧技术文档保留原有溯源声明 |
| C04 | **CVL-68 的具体码表 DRAFT**，但叙述频繁把示例字节用作年代确定史实 | 未来标准迁移可能导致冲突 | 将“直接八位主流方向”作为 CANON，而所有 0x41 等分配继续 DRAFT |
| C05 | 1980s Nova Minor/Media/Maior 与 1968 Nova-N1 的兼容能力未定义 | 不适当的 ISA/ABI 连续性推断 | 在硬件世系中注明软件/数据家族，不承诺二进制兼容 |
| C06 | Sextaria 只是一份 48 位科学机研究，没有 F48 或正式 ISA | AI 部分可能出现未经定义的 48 位张量 GPU | 标明仅可保留科学数值/数据传统，不主张物理机器或算法实现连续 |
| C07 | TABVLA、COS、NODVS、ORDO-N、PARTES、CVSTOS 在叙事中逐渐显得像已上市产品 | 虚构名称从 DRAFT 意外升格 CANON | 所有事件、组织、型号和标准正文继续写明 DRAFT，集中建立机构/世系索引 |
| C08 | 代码许可证 CC BY 4.0 / MIT 是现实仓库法律声明，LIBERTAS CODICVM 是架空许可运动 | 作者误把虚构条款说成实际可用许可证 | 始终分开描述，不起草未经要求的虚构法律文件 |
| C09 | 1980 年代多文字 GUI 技术与全球 AI 数据之间出现跳跃 | 文字存储、字形、token 与数学知识被混淆 | 在通史的“文字身份→排版→COS→模型数据”链条中补足层次 |
| C10 | 2026 年的 Nova 后继、矩阵加速器和 AI 工作站没有确切产品型号 | 被误当作当前存在的架空硬件规格 | 仅作为候选系统组合，标注无完成架构或性能数据 |
| C11 | 旧 Roadmap 在多阶段还留有“未来跑 CI”待办 | 与 2026-11-23 文档优先、删除工作流的决定冲突 | 在新路线图声明此类条目为历史归档，不是恢复 CI 的待办 |
| C12 | 语言 MODVLA、SERMO、RATIO 都未开发，但技术世系图容易暗示已运行的语言 | 后续“源代码示例”被误读为现成编译器 | 明确三者为未完成语法/编译器的语言提案 |

## 当前约束不应偷偷改变

**1954 的 XXXVI** 可为六个六位码一字的研究模型，但真实硬件的存储器、控制器和性能未被证明。

**1968 的 Nova** 有现代参考 CPU 实验，可与 XXXVI 运行独立机器码；此前的 GitHub Actions 验证记录是关于现实代码、非架空硬件存在的证据。停止 CI 后不应否认历史验收，也不应再要求新的自动化工作流。

**1976 的 Sextaria** 没有定案的位址、指令或浮点标准；若继续细化，先确定精度需求和物理成本，而非直接把旧六字符分组作为架构合理性的全部依据。

**1990s 的 COS** 是字符身份方案；不能自动把现实 UTF-8、Punycode、Unicode 字节表原样复制过来。

**2015–2026 的 AI** 由数据、训练、加速器和评价共同决定；拉丁语/希腊语的文化地位不会使模型天然更智能。

## 2026-11-23 update: CVL-68/RC1 review candidate

A [complete 256-position RC1 review ledger](../specifications/CVL-68-RC1-ledger.md) and [strict profile](../specifications/CVL-68-RC1.md) have now been proposed without changing earlier byte assignments. The ledger contains 33 controls, 136 glyph slots, 11 combining signs and 76 RESERVED positions. **This resolves the missing complete proposal/strict decoding documentation, not the CANON ratification.** CVL-63, scholarly mark validation, normalization-to-modern-Unicode round-trips and historical committee approval remain open. The original C04 remains a ratification blocker.

## 2026-11-23 update: CVL-63/TP1 transmission recommendation

The separate [TP1 study](../specifications/CVL-63-TP1.md) recommends carrying original six-bit CVL-54/P0 symbols inside seven-bit parity-checked transmission units, **not** defining a third character codebook. The recommendation clarifies the story's preferred 1963 transition but **does not CANON-ratify it**. Seven-bit physical framing, failed-record retransmission, full source code tables and old tape archival handling are still open. See [worked example](cvl63-transport-migration-ledger.md). Continuity item C04 is still a pending ratification issue for CVL-68.

## 优先处理的技术空白（由重要到次要）

1. **CVL-68**：冻结可核查的直接编码与组合规范前，不能保证世界范围的标准互通。
2. **CVL-63**：决定它是独立代码还是线路转换配置，才能使 1954→1968 的过渡史有唯一可比较的工程描述。
3. **Sextaria**：先明确架构目标、数值精度和指针模型，再考虑具体寄存器与 ISA。
4. **COS**：明确字节兼容目标、编号结构和跨世界文字的治理，才能推演互联网服务实际运作。
5. **机构连续性**：决定哪个组织制定哪项规范，以及不同年代的分裂、合并和权力变迁。
6. **Nova 后代**：解释 Nova-N1 与后来的窄数据通路个人机和 64 位服务器究竟有哪些真实 ABI 或仅数据兼容关系。

以上全部仍列为 DRAFT 开放问题。

## 供后续写作直接引用的标准句式

- “**CANON**：本世界的工程师从一开始有希腊—拉丁双文字原生需求。”
- “**DRAFT**：一种可能的 1976 年 48 位 Sextaria 科学机设计。”
- “**HIST**：真实 IBM System/360 说明八位字节和兼容机族在 1960 年代具备历史可行性。”
- “**研究实现**：2026 年在 GitHub 上运行的参考模拟器，只检验一种反事实机器的内部自洽。”

只要不跨越上述证据等级，Machina Latina 就能继续拥有丰富、细节可信的技术史，而不必为每一个草案写 Python 模拟器。

关联：[总通史](historia-machinae-latinae-1954-2026.md)、[机构世系](institutions-and-lineages.md)、[原始决策记录](decisions.md)。

## Phase XXXVII · 2026-11-26 — follow-up audit
> 文档层审阅，基线 9ec3dca91822b6fd9e957e89b3981d8eb87fd0e5。原 Phase XX 发现保留为历史快照。基线 Git tree 有 161 个文件（docs/ 51、specifications/ 59、Python 32 含 tests/ 10），无 .github/workflows/ 文件。未运行测试、模拟器、编译器，未逐条验证所有历史算例。

| ID | Finding | Disposition |
| --- | --- | --- |
| C13 | README 当前入口仍标 Phase XX | 更新为 XXXVII，保留历史阶段章节 |
| C14 | 年表追加条目不再按时间排列 | 保留 68 个事件行并按起始年稳定排序；不消除重叠 |
| C15 | 通史及旧异构研究仍称 F48/ISA 没有提出，S1/F48/S2 已有候选 | 区分早期研究状态与后续纸面规格，仍不定案或宣称实现 |
| C16 | 早期 COS/NODVS 讨论只有概念；Phase XXIV–XXV 有精确候选 | 更新总索引；全球字表与网络信任仍开放 |
| C17 | 2007–2009 三系统概念叙事易被解读为三个 OS 同时诞生 | 明确 ORDO-N I、PARTES I 的较早候选年代及 CVSTOS 移动时代；早期文章不改作伪史 |
| C18 | 原始 CPU/语言实验和后来 R1 纸面规范容易混同 | 图谱和时代画像按实现状态分类，不新跑历史测试 |
| C19 | M32 与 M64 共用编码框架，却缺少 M64 保护/加载器/ABI；PARTES Nova port 无 native IPC ABI | OPEN，不能声称现代 64 位 OS 已具备执行合同 |
| C20 | RETE 只有 FETCH/RESULT，但 FORVM/软件分发/MENTIS 需要认证授权或写入 | OPEN，必须设计目录、安全传输和写协议；禁止把 ID 当认证 |
| C21 | STEMMA 摘要套件、FASCICVLVS 签名序列化均未定义 | OPEN，逻辑身份与前像不能替代验证系统 |
| C22 | RATIO-I 仅 F32/F36 标量，F48 与 M16/F32 矩阵另有候选 | OPEN，不能把后来数值格式或矩阵算例当成 RATIO 已验收的语言功能 |
| C23 | 图形 R1 是有限绘制/光栅化，LVDVS 仅逻辑快照；缺着色器/设备/音频/输入 | OPEN，不能宣称完整图形或游戏系统 |
| C24 | COS 只登记候选范围与少量映射；W1 非自同步；STEMMA/MENTIS 依赖明确 registry | OPEN，完整 repertoire、语言组合、跨平台名称、错误恢复独立研究 |
| C25 | 早期候选组织、许可证与 2026 现代产业画像尚无全面制度依据 | OPEN，不虚构正式厂商、市场份额、法律文本或政治版图 |

## Priority dependency register (not a mandate to implement)
1. Identity/data foundations: CVL/COS ratification and registry, strict migration and text processing; CCL/CSM legitimacy.
2. Host execution foundations: M64 privilege/address model, loaders/procedure ABIs, concurrency, device isolation; distinct native OS adapters.
3. Network/trust: authority resolution and security, immutable identity, mutation and signatures; package and forge transport.
4. Numeric/graphics/AI: F64 and RATIO expansion, device memory/synchronization, full graphics pipeline and model evaluation.

These are engineering dependencies, not scheduled historical events. A future scenario may explicitly assume one or more are solved, but must label the assumption rather than silently claim an existing spec. See [atlas](technology-atlas-1954-2026.md), [era portraits](era-portraits-1954-2026.md). No new CANON decision.
