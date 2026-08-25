# AI Product Teardown

> 当前版本：v2.1.0

一套基于真实界面、操作截图和可观察状态，对 **AI 产品行为与产品架构** 进行证据化逆向拆解的 Codex Skill。

它回答的核心问题是：用户如何使用这个 AI 产品，界面中出现了哪些 Agent，它们接收什么、判断什么、调用什么能力、产出什么，聊天、任务、画布和资产如何流转，以及怎样构建一个功能上相近的产品系统。

它主要拆解：

- 用户旅程与体验问题
- Agent 清单及 I/O 契约
- 单 Agent 功能等价 System Prompt
- 工具、全局上下文与资产数据流
- As-Is / To-Be 产品架构
- Mermaid 状态图、ER 图、时序图和产品全景图
- 在具备安全浏览器或桌面控制能力时，自主采集、回读校验、去重并登记产品截图

## 它不拆解什么

- **不是书籍拆解工具**：不会提炼书籍章节、作者框架或读书笔记。
- **不是源码反编译工具**：不会绕过访问控制、获取后台源码或把不可见技术栈写成事实。
- **不是 Prompt 窃取工具**：不会声称读取官方私有 System Prompt 或隐藏思维链。
- **不是普通市场调研工具**：只有宣传页、媒体报道或竞品列表时，证据不足以完成产品行为拆解。
- **不是账号或凭据提取工具**：不会读取或输出 Cookie、Token、密码、鉴权头和浏览器私有存储。

## 适用产品

最适合具有 AI 对话、Agent、生成工作流或智能任务编排的产品，例如 AI 助手、研究工具、AI 写作与设计、图片/音频/视频生成、多 Agent 工作台，以及带 AI 决策或审核环节的垂直 SaaS。

普通 SaaS 也可以分析用户旅程和界面状态；如果产品没有 Agent、模型调用或生成流程，Agent 契约和功能等价 Prompt 模式可能不适用。

## 核心原则

- 默认只读，不触发生成、重新生成、发布、删除、购买、充值或资产覆盖。
- 区分 `【已确认】`、`【合理推断】`、`【建议设计】` 和 `【未知】`。
- Agent 声称“已完成”不等于资产或任务状态已经完成。
- Agent 的口头计划不等于工具已经调用。
- 同时核验聊天、画布、任务状态、历史版本和实际资产。
- 不声称读取隐藏思维链、官方 System Prompt 或不可见后端实现。

## 使用方式

将本仓库放入支持 Skills 的工作目录或个人 Skills 目录，然后调用：

```text
使用 $ai-product-teardown，以只读、证据可追溯的方式拆解这个 AI 产品。
```

可指定五种工作模式：

| 模式 | 主要回答 | 典型交付物 |
|---|---|---|
| 用户旅程 | 用户做了什么、看到了什么、在哪里决策或受阻 | 证据表、三泳道旅程、分支流程、体验问题 |
| Agent 契约 | 哪些 Agent 出现，它们如何输入、判断、调用、输出和交接 | Agent 清单、I/O 契约、工具表、上下文数据流 |
| 功能等价 Prompt | 如何让另一个 Agent 表现出相近的可观察行为 | 状态机、System Prompt、规则追溯表、最小测试集 |
| 产品架构 | 产品功能、Agent、工具、模型、数据、资产和治理如何协同 | 分层架构、ER 图、时序图、As-Is / To-Be、风险清单 |
| 完整拆解 | 如何形成端到端、可追溯的产品模型 | 上述交付物的分阶段组合与汇总报告 |

只执行用户请求的模式，不会因为选择了用户旅程就自动继续还原 Prompt 或架构。

## 自主截图与证据采集

当环境中存在安全的浏览器或桌面控制能力时，本 Skill 可以在授权边界内浏览已有页面、等待状态稳定、截图、回读校验、去重，并用稳定截图 ID 生成截图清单。

自主截图不等于自主执行产品任务。默认不会发送消息、提交表单、触发生成或重新生成、改变已保存配置、发布、删除、覆盖、购买、充值或重试付费任务。遇到登录、验证码、设备批准或不可靠的桌面自动化时，会请求用户接管。

如果用户已经提供截图，则直接校验和整理截图，不再操作目标产品；没有可用控制能力时，也不会用宣传页替代真实操作证据。

## 典型交付结构

实际文件根据用户请求裁剪，不会创建无内容的占位报告：

```text
teardown/
├── 00-scope-and-evidence.md
├── 01-journey.md
├── 02-agent-contracts.md
├── 03-<agent>-functional-prompt.md
├── 04-product-architecture.md
├── evidence/
│   ├── ledger.md
│   ├── screenshot-manifest.csv
│   └── screenshots/
└── delivery-manifest.md
```

需要可视化交付时，也可以生成独立 HTML、Mermaid 状态图、用户旅程图、ER 图、时序图和产品全景架构图。

## 目录

```text
ai-product-teardown/
├── LICENSE
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── analysis-modes.md
│   ├── architecture-framework.md
│   ├── evidence-and-observation.md
│   ├── screenshot-acquisition.md
│   ├── html-delivery.md
│   ├── report-and-visualization.md
│   └── staged-execution-sop.md
└── assets/
    └── report-template.html
```

## 主要文件

- [`SKILL.md`](SKILL.md)：Skill 入口、模式路由、证据边界和质量标准。
- [`evidence-and-observation.md`](references/evidence-and-observation.md)：证据账本、跨页面核验和截图规范。
- [`screenshot-acquisition.md`](references/screenshot-acquisition.md)：Web、小程序和桌面产品的安全自主截图、状态校验、去重和清单协议。
- [`analysis-modes.md`](references/analysis-modes.md)：四类拆解任务的固定交付契约。
- [`architecture-framework.md`](references/architecture-framework.md)：产品分层、上下文、知识、模型和实体架构模板。
- [`html-delivery.md`](references/html-delivery.md)：HTML 与 Mermaid 交付、渲染和检查要求。
- [`report-and-visualization.md`](references/report-and-visualization.md)：答案优先的轻量报告结构、最小有效可视化与交付检查。
- [`staged-execution-sop.md`](references/staged-execution-sop.md)：分阶段拆解、多交付物交接、验收门和版本变更控制。
- [`report-template.html`](assets/report-template.html)：可复用的响应式 HTML 报告模板。

## 能力边界

本 Skill 用于行为和产品架构分析，不用于恢复目标产品的私有提示词、隐藏思维链、账号凭据或未经公开的后台源码。功能性工具名和语义化数据字段必须明确标记为推导设计，不得冒充目标产品的官方实现。

## 开源许可

本项目采用 [MIT License](LICENSE)。你可以使用、复制、修改和分发本项目，但必须保留许可证和版权声明。

公开提交前请遵守 [Security Policy](SECURITY.md)，不要上传 Cookie、Token、密码、私有聊天、客户素材、未脱敏截图或其他敏感证据。
