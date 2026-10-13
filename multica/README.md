# Multica 配置备份

这是 AI 可读取的 Multica 配置和跨电脑恢复说明，不是 Multica 官方一键导入文件。

## 工作区

- 名称：个人开发工作区
- 当前 Slug：`cordelia-r7rs`（换工作区后可以变化）
- 所有者：Kane Kane
- 当前配置核验日期：2026-10-13

## 文件

- `agents/`：六个智能体的独立配置、模型和完整 System Prompt。
- `squad.md`：个人开发工作流总队的成员、角色和指引。
- `workflow.md`：完整工作流规范，作为流程唯一真相来源。
- `restore-guide.md`：新电脑恢复步骤、安全规则和验证清单。

## 当前模型与运行时

| 智能体 | 模型 | 运行时类型 |
|---|---|---|
| 工作流总管 | `opencode-go/glm-5.3-flash` | OpenCode |
| 调研与可行性分析师 | `claude-sonnet-5-5` | Claude |
| Codex 规划师 | `claude-sonnet-5-5` | Claude |
| 方案与实现审核员 | `opencode-go/gpt-6-luna` | OpenCode |
| OpenCode 执行工程师 | `opencode-go/glm-5.3-flash` | OpenCode |
| 通用测试员 | `opencode-go/glm-5.3-flash` | OpenCode |

当前实测设备名为 `MacBook-Pro.local`，不能机械复制到新电脑。恢复时按 Claude 或 OpenCode 运行时类型选择新电脑上的在线实例。

相同模型可用时直接选择；不可用时必须说明缺少的模型、受影响角色、推荐替代模型和能力/价格差异，不得静默使用默认模型。

并发数、Skills、MCP、集成、对话开场建议、小队描述和其他高级设置不属于核心迁移范围。恢复时保持 Multica 默认值即可；不要因为这些可选项缺失而阻塞恢复。若以后某项成为工作流依赖，再单独记录。

## 安全

本目录不保存密码、API Key、Token、Cookie、OAuth 会话或任何 CLI 登录凭证。新电脑必须重新完成认证。
