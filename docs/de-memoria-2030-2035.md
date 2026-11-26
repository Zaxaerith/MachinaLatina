# De Memoria (2030–2035)
## 《内存之治：从处理器中心走向异构数据中心》
> FUTURE SCENARIO / DRAFT · 2026-11-26. Beyond the 1954–2026 comparison period. Dates, names, physical configurations and market paths are conditional, not real predictions or CANON.

## 2030–2031：Nova Memoria
MENTIS 任务服务与本地模型推动内存容量和数据移动成本进入消费者视野。候选 Nova Memoria 不是新统一指令集，而是 Nova CPU、FIGVRA 图形设备、MATRICES 及可选科学协处理器围绕内存控制器的体系。可采用分片封装、堆叠内存与大容量主存；封装良率、散热、供电和成本可能阻止普及。地址相同不等于物理共享或一致性。先提出有界缓冲区所有权交接，保留不同 OS 的实现边界。
## 2032：近内存计算
栅格过滤、数据扫描、部分归约可以在内存控制器附近执行，减少结果以外的数据跨互连传输。存内计算更激进，模拟精度、耐久性和制造仍是变量。不能假设任意程序自动加速。保留 CPU 与普通加速器，按任务选择策略。
## 2033：Sextaria 的第二次生命
F48 档案、TRANFOR 数值传统、PARTES 记录服务和 RATIO 的验证理念可能激励精度优先的独立科学计算子系统。不是复活旧 48 位 CPU。提出 F64/R0 的显式 52 位有效数与有限算术；保留旧 F48 交换格式。实际是否采用专用硬件取决于竞争与成本；软件实现或通用 GPU 可替代。RATIO-I 不自动支持 F48/F64 或矩阵语言。
## 2034–2035：个人 AI 工作站
候选两类配置仅用于比较：一台 64 GiB 统一资源池的桌面，另一台 128 GiB 主机 RAM 加独立 32 GiB 加速器存储的工作站。第一种可减少部分复制、但 CPU/GPU/模型争用容量带宽；第二种能提供独立设备资源、但大模型并不能仅凭容量相加就直接驻留设备。没有指定价格、频率、实际内存带宽、功耗或吞吐。CVSTOS Mobilis 仍受温度与能耗约束，普通 ORDO-N PC 仍可运行传统软件，PARTES 科学服务需要显式设备契约。MENTIS 只规划任务，不能绕过资源权限。
## 分叉
主路线为分层内存与显式设备资源交换；全系统硬件一致性是一条更复杂的后续路线；传统独立显存加速卡因成本和升级性继续竞争。冯·诺依曼式存储程序主机仍然存在，异构数据流及近内存单元只是逐步改变计算职责，不宣称 2035 年终结传统体系。

| Candidate year | Direction |
| --- | --- |
| 2030 | unified resource management |
| 2031 | Nova Memoria modular platform |
| 2032 | near-memory computation |
| 2033 | Sextaria precision service and F64/R0 proposal |
| 2034–2035 | personal heterogeneous workstations |

[Memoria R1](../specifications/Nova-Memoria-R1.md) and [scientific engine](../specifications/Sextaria-scientific-engine-study.md) are bounded paper proposals. C19–C25 remain open; no full M64 MMU, cache consistency, device IOMMU, actual chiplet packaging, measured bandwidth or numerical implementation. Next scenario: 2035–2040 scientific world models and digital twins, with model resolution, observation uncertainty and update costs explicitly bounded. No code or CI.
