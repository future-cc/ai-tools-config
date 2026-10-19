# AI 辅助工具配置中心

用于保存可迁移的 AI 辅助工具配置、模型选择原则和恢复说明。

## 目录

- `multica/`：Multica 智能体、小队、模型和工作流配置。
- `codex/`：Codex 配置预留目录。
- `opencode/`：OpenCode 配置预留目录。
- `claude-code/`：Claude Code 配置。`skills/quick-fix/` 是快修简单 App 缺陷的 skill（`/quick-fix`），不满足快修条件时整理成交给 Multica 缺陷修复小队的任务描述；使用前链接或复制到 `~/.claude/skills/quick-fix/`。
- `cursor/`：Cursor 配置预留目录。
- `shared/`：多个 AI 工具共用的原则和模板。
  - `shared/skills/`：通用 skill（`SKILL.md` 格式，Claude Code、Codex 等支持该格式的工具都可用）。
    - `figma-restore-init/`：Figma 还原 skill 的生成器。在项目根目录运行，识别当前工具并确定技能目录，原样复制固定的还原工作流（`workflow.md`），扫描项目并向用户确认后，生成项目级 `figma-restore/` skill。
    - 安装：整个目录用 `ln -s` 链接到对应工具的用户级技能目录（以便读到同目录的 `workflow.md` 和 `template/`），例如 Claude Code 为 `~/.claude/skills/figma-restore-init`；Codex 为 `~/.agents/skills/figma-restore-init`（以 Codex 当前文档为准）。

## 安全规则

这里不保存密码、API Key、Token、Cookie、登录会话或其他凭证。恢复到新电脑时，需要在新电脑上重新完成各工具的登录和认证。

## 恢复原则

1. 先读取本文件。
2. 再读取目标工具对应的子目录。
3. 如果存在相同模型，直接选择相同模型。
4. 如果模型不可用，按照配置中的角色、用途和备选模型选择，并明确告诉用户，不得静默替换。
5. 恢复后检查模型、智能体、成员、指引和工作流版本。

Multica 配置入口是 `multica/README.md`。恢复 AI 应先读取入口文件，再按需读取单个智能体配置，不要一次加载全部提示词。
