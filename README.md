# AI Product Teardown

一套基于真实页面证据的 AI 产品逆向拆解 Skill，用于系统化产出：

- 用户旅程与体验问题
- Agent 清单及 I/O 契约
- 单 Agent 功能等价 System Prompt
- 工具、全局上下文与资产数据流
- As-Is / To-Be 产品架构
- Mermaid 状态图、ER 图、时序图和产品全景图

## 核心原则

- 默认只读，不触发生成、重新生成、发布、删除、购买、充值或资产覆盖。
- 区分 `【已确认】`、`【合理推断】`、`【建议设计】` 和 `【未知】`。
- Agent 声称“已完成”不等于资产或任务状态已经完成。
- Agent 的口头计划不等于工具已经调用。
- 同时核验聊天、画布、任务状态、历史版本和实际资产。
- 不声称读取隐藏思维链、官方 System Prompt 或不可见后端实现。

## 安装

Codex 会从个人目录或项目目录发现独立 Skill。安装后不会改动本仓库内容，后续也可以通过普通的 `git pull` 更新。

### 安装到个人目录

适合希望在所有项目中使用本 Skill 的用户：

```bash
git clone https://github.com/w93139/ai-product-teardown.git "$HOME/.agents/skills/ai-product-teardown"
```

### 安装到当前项目

在目标 Git 仓库根目录执行：

```bash
git clone https://github.com/w93139/ai-product-teardown.git .agents/skills/ai-product-teardown
```

也可以在 Codex 中调用 `$skill-installer`，让它从本仓库地址安装。Codex 通常会自动发现新增或更新的 Skill；如果没有出现，请重启 Codex。目录约定参见 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/codex/build-skills)。

## 使用方式

安装完成后，在 Codex 中输入 `$` 选择本 Skill，或直接调用：

```text
使用 $ai-product-teardown，以只读、证据可追溯的方式拆解这个 AI 产品。
```

可指定五种工作模式：

1. 用户旅程
2. Agent 契约
3. 单 Agent 功能等价 Prompt
4. 完整产品架构
5. 分阶段完整拆解

如需更新个人安装：

```bash
git -C "$HOME/.agents/skills/ai-product-teardown" pull --ff-only
```

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
│   ├── html-delivery.md
│   └── report-and-visualization.md
└── assets/
    └── report-template.html
```

## 主要文件

- [`SKILL.md`](SKILL.md)：Skill 入口、模式路由、证据边界和质量标准。
- [`evidence-and-observation.md`](references/evidence-and-observation.md)：证据账本、跨页面核验和截图规范。
- [`analysis-modes.md`](references/analysis-modes.md)：四类拆解任务的固定交付契约。
- [`architecture-framework.md`](references/architecture-framework.md)：产品分层、上下文、知识、模型和实体架构模板。
- [`html-delivery.md`](references/html-delivery.md)：HTML 与 Mermaid 交付、渲染和检查要求。
- [`report-and-visualization.md`](references/report-and-visualization.md)：答案优先的轻量报告结构、最小有效可视化与交付检查。
- [`report-template.html`](assets/report-template.html)：可复用的响应式 HTML 报告模板。

## 说明

本 Skill 用于行为和产品架构分析，不用于恢复目标产品的私有提示词、隐藏思维链、账号凭据或未经公开的后台源码。功能性工具名和语义化数据字段必须明确标记为推导设计，不得冒充目标产品的官方实现。

## 开源许可

本项目采用 [MIT License](LICENSE)。你可以使用、复制、修改和分发本项目，但必须保留许可证和版权声明。

公开提交前请遵守 [Security Policy](SECURITY.md)，不要上传 Cookie、Token、密码、私有聊天、客户素材、未脱敏截图或其他敏感证据。
