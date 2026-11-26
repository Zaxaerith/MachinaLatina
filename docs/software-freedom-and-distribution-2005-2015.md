# Libertas Codicum — Source Code Freedom and Software Distribution
## 2005—2015 年的自由软件制度与跨架构分发

> **DRAFT 架空制度史，不是法律咨询或实际许可协议。** LIBERTAS CODICVM 和所有所谓“互惠许可证”都只是命名与治理的候选方案；此仓库既有的真实许可证仍然是文档 CC BY 4.0 和代码 MIT，**没有发生变化**。

## 核心历史动机：为什么开放源代码？

因为 CVL-68、XXXVI、COS、TABVLA 和 NODVS 长期并存，源代码和文档格式不再只是程序员的私人事务：图书馆担心历史文字无法显示，科研机构担心旧算术格式无法重现，用户担心设备停产以后无法修改阅读软件。

这可能催生一场强调**能研究、运行、修改、分享和保留软件**的公众运动。然而若试图使每一份程序都成为可自由复制的代码，也会和专有应用、厂商商业维护以及特殊设备驱动产生冲突。

### 现实史实（只作比较）

- GNU 于 1983 年发起，真实的自由软件基金会于 1985 年成立；[FSF](https://www.fsf.org/history/)。
- GPLv3 于 2007 年 6 月发布；[FSF GPLv3 新闻](https://www.fsf.org/news/gplv3_launched)。
- Git 的历史起点为 2005 年；[Git 官方](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git)。
- Apple 2008 年面向 iPhone 提供 App Store；[Apple](https://www.apple.com/newsroom/2008/07/14iPhone-App-Store-Downloads-Top-10-Million-in-First-Weekend/)。
- Android 平台公开源码的现实重要时刻为 2008 年 10 月；[Google](https://opensource.googleblog.com/2008/10/android-open-source-cell-phone.html)。

不能把真实的许可证文本、项目名称和时间事件直接复制到架空世界。

## 许可证的两种经济思想

| 候选制度 | 适合软件 | 社会诉求 | 技术或治理成本 |
| --- | --- | --- | --- |
| **宽松许可** | 字体转换基础库、COS 字符表、简单读写工具 | 允许商业和自由系统广泛复用 | 下游可封闭改动，回馈并非强制 |
| **互惠许可** | 重要文档引擎、完整系统组件、公共科研工具 | 分发修改版时继续给予相应代码权利 | 需要精确规定衍生作品、分发、例外和合规边界 |

这是制度比较，不是现成的法律文字。**互惠不等于禁止商业用途**；宽松也不等于不存在版权义务。真实 CC BY 4.0 不应无条件用作软件包许可证，而仓库原有代码 MIT 与文档 CC BY 4.0 的选择必须保留。

## 为什么硬件可安装性成为下一场争论？

移动设备和封闭终端即便提供可修改源代码，也可能通过签名启动链拒绝用户安装修改版。与之相对，厂商有保障完整性、移动运营商合规和减少恶意程序的需求。冲突的核心是**用户控制权、设备安全和应用分发权限**，不是一句“开放好，封闭坏”就能解决。

候选的架空许可证协会可能分别讨论：
- 提供源代码是否足以满足使用者自由？
- 固件、通信基带和启动器是否应允许替换？
- 签名密钥由厂商、组织还是用户共同掌握？
- 商店审核是否与源码权利分别治理？

不在本章伪造任何具有法律效力的条款。

## 全球文字如何影响源代码托管？

COS 的文字身份尚未冻结，旧 CVL-68 的 Latin A 和 Greek Α又具有视觉相似问题。因此软件协作平台必须明确源文件编码、目录名字节语义、源文字正规化、提交者身份和包名检查。公开代码但让亚洲或中东开发者始终使用不可读音译包名，也会继承早期拉丁—希腊制度的偏见。

一种合理的分布式协作模型：

1. 保留原始源码字节和明确字符编码说明；
2. 将仓库对象版本与其内容和元数据绑定；
3. 为合法国际包名提供显示与线路表示区分；
4. 让编译器与软件包管理器明确目标 CPU ABI；
5. 将代码审阅、用户信任和签名授权分别处理。

这些要求并不意味着已经开发 Git 一样的 SHA 仓库，或决定哈希算法、文件系统路径与签名格式。

## 可复核构建不等于可复核科学结果

软件包重新构建得到同一二进制文件，是**位级构建可复现性**问题；同一科学程序得到误差允许范围内一致的结果，是**数值可复算性**问题。来自 XXXVI/F36、Nova/F32 和候选 Sextaria 的不同结果可能都符合各自格式的定义。

一个未来的科研包清单应考虑源码身份、构建环境、架构、操作系统 API、字符编码、输入数据来源、算术精度、运算顺序与产物校验。这是研究议题，不是假装已有规范。

See [historical narrative](de-libertate-codicum-et-imperio-systematum-2005-2015.md), [programming languages](programming-ecosystem-2005-2015.md), [COS study](../specifications/COS-universal-character-registry-study.md).

## 2026-11-26 CVSTOS follow-up

[CVSTOS I/R1](../specifications/CVSTOS-I-R1.md) and [distribution/energy policy](../specifications/CVSTOS-distribution-and-energy-R1.md) provide subsequent paper candidates. No existing ISA/OS ABI, license or actual device policy is changed. App signature, runtime capability and boot authority remain distinct.

## 2026-11-26 developer ecosystem follow-up

[STEMMA R1](../specifications/STEMMA-R1.md) and [FASCICVLVS R1](../specifications/FASCICVLVS-R1.md) are subsequent paper candidates for source identity and target-specific package distribution. No real license, trust roots, boot policy or native ABI changed; signature serialization and digest suites remain open.
