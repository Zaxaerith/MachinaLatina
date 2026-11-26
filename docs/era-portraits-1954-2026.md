# Era Portraits / 七个时代的典型计算环境
> Phase XXXVII · 2026-11-26. Fictional composite scenarios, DRAFT; not concrete shipped configurations or market statistics. Uses existing names only. Hardware limits, illustrative installations and actual implementation remain distinct.

## 1954 — 科学中心
一台 36 位 XXXVI 研究机、六位 CVL-54 双页终端、字寻址记录；拉丁工程名称和希腊学术字符需要明确移位。典型工作是批量数值计算、终端输入输出和纸带式资料保存。早期 TRANFOR 只是 1957 年候选发展方向，不能提前出现在 1954 年。现代 Python 模拟器仅供研究。
[XXXVI](../specifications/Machina-XXXVI.md) · [CVL-54](../specifications/CVL-54-P0.md)

## 1968 — 商业数据处理
Nova N1 32 位累加器机、24 位字节地址、候选 CVL-68 直接双文字编码，与旧 XXXVI 档案并存。1963 TP1 仍是旧六位字符通信包装，不会变成新字符表。1968 主流八位方向为 CANON，但 RC1 的逐字节映射及后来的学术组合扩充不应被当作当年全部已经冻结。
[N1](../specifications/Machina-Nova-N1.md) · [RC1](../specifications/CVL-68-RC1.md)

## 1985 — 大众微机和科研机分流
家庭学校使用 Minor 候选 8 位机器、48 KiB 初期 RAM 与银行式内存；Media、早期 TABVLA 和 LVDVS 方向并行。科研中心可选择 Sextaria S1 48 位机器、16 个寄存器和 F48 候选数值格式，使用 TRANFOR 传统及新兴 MODVLA/RATIO 语言研究。PARTES I 与 ORDO-N I 的具体保护机制属于较晚的候选年代，不提前移入这幅场景。
[Nova family](../specifications/Nova-family-evolution-study.md) · [S1](../specifications/Sextaria-S1-R1.md) · [RATIO](../specifications/RATIO-I-R1.md)

## 1995 — 图形工作站与桌面
Maior M32 / ORDO-N I 的分页进程与字节文件，Sextaria S2 / PARTES I 的连续区段和同步消息，TABVLA 用户态图形布局与 IMAGO 表面并存。FIGVRA-95 候选可定义固定点屏幕三角形和深度测试；并非完整三维引擎。科研 GIS 需要独立保存 CRS、坐标精度与记录来源。全球 COS 还处于候选制度讨论。
[ORDO-N](../specifications/ORDO-N-I-R1.md) · [PARTES](../specifications/PARTES-I-R1.md) · [FIGVRA](../specifications/FIGVRA-95-R1.md)

## 2005 — 全球网络与 64 位过渡
Magna M64 16 个 64 位寄存器、48 位有效地址范围和可选 M32 执行模式；不是已装配 256 TiB RAM。COS C24/W1、NODVS、LIGAMEN、RETE 和 SERMO 形成候选文献网络。旧 F48 科研档案保存原始字节。RETE 基础规范只有取文档操作，不能独立支撑现代登录、电子商务、代码托管写入。M64 系统保护及 ABI 未完成，桌面迁移只是历史方向。
[Magna](../specifications/Nova-Maior-Magna-R1.md) · [NODVS](../specifications/NODVS-98-R1.md) · [RETE](../specifications/RETE-00-R1.md)

## 2015 — 手机和全球开发者
Mobilis 低功耗设备与 CVSTOS 应用权限，ORDO-N 开放/商业发行版及 PARTES 科研生态并存。STEMMA 保存源码世系，FASCICVLVS 绑定跨目标分发，FORVM CODICVM 代表多机构公共协作平台。应用签名、启动信任、许可证和运行权限相互独立。CVSTOS 的后台预算仅是政策算例，没有实测电池收益。图形处理进入可编程时代，完整 shader/driver 契约还待研究。
[CVSTOS](../specifications/CVSTOS-I-R1.md) · [STEMMA](../specifications/STEMMA-R1.md) · [FASCICVLVS](../specifications/FASCICVLVS-R1.md)

## 2026 — 异构计算与机器智能
通用 Nova 后继、Mobilis 移动设备、图形及矩阵加速器共同工作。MENTIS 候选使用 COS 字符序列建立词表，以明确来源和权限检索 NODVS 文献；M16 输入、F32 累加是一个有限矩阵候选，不是完整训练框架。RATIO 只接受已定义标量 F32/F36 子集，不能把 F48 或矩阵算例标为已经验收。一个科学助手可以生成解释、检索固定文献修订、请求独立计算并记录人工审阅，但尚无真实服务实现。
[MENTIS](de-mente-1965-2026.md) · [evidence](../specifications/MENTIS-evidence-R1.md)

## A shared document through time
原始 CVL 文档的五字节 SALVE（52 41 4B 54 45）在 COS/C24 下成为 15 字节，在 W1 的旧码映射下仍可为五字节，但必须声明不同 profile；两种文件内容身份不能混为一谈。2026 MENTIS 示例词表可将 SALVE 编成一个 token，既不等于五个字符变为一个字符，也不能推导真实语料的压缩比。跨时代保存原始对象、解码声明、版本与来源，才是连续性主线。

See [atlas](technology-atlas-1954-2026.md), [chronology](chronology.md), [history](historia-machinae-latinae-1954-2026.md).
