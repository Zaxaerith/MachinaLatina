# De Sextaria (1976–2005)
## 六字节之梦：48 位科学计算机的兴衰

> DRAFT · 2026-11-25。机型、年代、采购与市场走向均为架空候选，不是实际销量或测试结果。

## 1976—1980：从 S0 到 S1

S0 是六个八位字符一字的多板科学机概念。S1 候选发展为 16 个通用寄存器、24 位字地址、六槽混合字节指针和固定 48 位指令。多板或位片实现需要额外控制与布线；乘除法可以多周期完成。48 位不提高每字符的裸存储密度，真正的产品理由是 38 位有效数的 F48 科学计算与软件生态。96 MiB 是架构上限，384 KiB 是示意装机规模，不是已存在产品的规格。原架构史中的 B5000 与 CDC 6600 仅为真实字长多样性的参照。

## 1981—1986：科研中心与商业市场分流

Sextaria 可能服务于天文、地球科学、测绘与统计机构；Nova Minor 争取家庭与办公室。两者市场并非排他。TRANFOR 可通过新后端移植，MODVLA 可声明外部记录；不能因此直接运行旧机器码。RATIO 可以在后续版本声明 F48 数值契约，现有 RATIO I 仍限定 F32/F36。

## 1987—1992：S2 科研工作站候选

S2 可考虑虚拟内存、中断、设备控制、图形缓冲与联网。S1 并未规定这些功能。专业地图制图和科研可视化将数值计算、记录和图形设备结合；像素格式独立于 CPU 字长，不能宣称 48 位自然带来 3D 加速。高端 Nova 也可能凭图形外设、工具链和更广泛的软件市场竞争。

## 1993—2005：退出主流的可能路线

通用计算机的规模经济、常见内存组织、工具链与驱动生态逐渐使六字节机器字及双指针模型增加移植成本。高精度也可通过更宽通用处理器、独立协处理器或软件数值库实现。建议 2000 年前后 Sextaria 逐步退出主流新工作站采购，保留旧机维护、F48 档案和 RATIO 科学复算传统。具体退役年份、市场份额和 Nova 64 位后继规格未定；保留小众持续生存的分支。

| 年代 | 候选 |
| --- | --- |
| 1976–1978 | S0 多板试验 |
| 1978–1980 | S1/R1 48 位寄存器机器与 F48 |
| 1987–1992 | S2 科研工作站方向 |
| 1993–2005 | 生态收缩、数值和档案遗产延续 |

参见 [S1](../specifications/Sextaria-S1-R1.md)、[F48](../specifications/Sextaria-F48-R1.md)、[S0](../specifications/Sextaria-S0-study.md)、[早期架构史](de-bello-verborum-et-machinarum-1973-1985.md)。

## 2026-11-25 Nova family follow-up

[Maior/Magna R1](../specifications/Nova-Maior-Magna-R1.md) and [Nova family evolution](../specifications/Nova-family-evolution-study.md) propose later hardware profiles. These do not alter existing N1/Sextaria specifications, claim native OS compatibility or ratify historical adoption. All new profiles remain DRAFT.

## 2026-11-26 PARTES follow-up

[S2 protection](../specifications/Sextaria-S2-PROTECT-R1.md), [PARTES I IPC](../specifications/PARTES-I-R1.md) and [record service](../specifications/PARTES-record-service-R1.md) are subsequent paper candidates. They do not alter existing S1 or ORDO-N contracts or establish implemented drivers, shared memory, or a Nova native IPC ABI.

## 2026-11-26 graphics follow-up

[IMAGO](../specifications/IMAGO-86-R1.md), [FIGVRA](../specifications/FIGVRA-95-R1.md) and [LVDVS](../specifications/LVDVS-console-study.md) provide subsequent paper candidates; no CPU ISA or existing numeric format changed. Actual devices, shader ISA, full drivers and accelerator execution remain open.

## Phase XLIII industry follow-up

[Candidate company register](industry/company-register-1970-2026.md), [industry history](industry/de-industria-1970-2026.md) and [product dossiers](industry/product-dossiers-1981-2026.md) add a fictional commercial layer. Earlier technical family names remain distinct from corporate identities. All proposed affiliations, dates and outcomes are DRAFT; no existing standard or institution is ratified or reassigned.
