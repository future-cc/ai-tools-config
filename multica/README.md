# Multica 配置备份

这是 AI 可读取的 Multica 配置和跨电脑恢复说明，不是 Multica 官方一键导入文件。

## 工作区

- 名称：个人开发工作区
- 当前 Slug：`cordelia-r7rs`（换工作区后可以变化）
- 所有者：Kane Kane
- 当前配置核验日期：2026-10-19

## 文件

- `agents/`：十八个智能体的独立配置（含开发实施小队的 4 个、调研方案小队的 5 个、测试小队的 5 个和缺陷修复小队的 4 个；文件名与 Multica 网页中的名称一致）、模型和完整 System Prompt。
- `squads/`：四个小队的成员、角色和指引，文件名与 Multica 网页中的小队名一致。调研方案小队负责调研和选方案，输出 `HANDOFF.md`，用户回复“交给开发”后，同一任务改派给开发实施小队；开发实施小队以它为输入，由实施架构师做技术设计，再审核和执行（执行时含运行验证），手机 App 完成后，用户回复“交给测试”，同一任务改派给测试小队，测试总管以 `TEST_HANDOFF.md` 为输入。缺陷修复小队独立接单：一个任务修一个 bug，分析根因后经人工批准，先写失败的复现测试再做最小修复，独立审核后汇报；不自动交给其他小队，是否交给测试小队重测由用户决定。
- `kit-scripts/`：maestro-testing-kit 里新增的两个脚本（脱离启动测试和检查状态）的备份，测试执行员依赖它们。
- `workflow.md`：开发实施小队的工作流摘要，便于快速了解流程；具体规则以各智能体指令和小队指引为准。
- `validation-2026-10-flutter-shop.md`：测试小队 + 缺陷修复小队端到端验证总结（发现的 bug、小队表现、环境陷阱、未验证项和待办）。
- `restore-guide.md`：新电脑恢复步骤、安全规则和验证清单。

## 当前模型与运行时

| 智能体 | 模型 | 运行时类型 |
|---|---|---|
| 实施总管 | `claude-sonnet-5-5` | Claude |
| 实施架构师 | `claude-sonnet-5-5` | Claude |
| 实施审核员 | `claude-sonnet-5` | Claude |
| 实施工程师 | `claude-sonnet-5-5` | Claude |
| 方案评审总管 | `claude-sonnet-5-5` | Claude |
| 方案顾问 | `claude-sonnet-5-5` | Claude |
| 方案调研师 | `claude-opus-5-5` | Claude |
| 方案评审员 | `claude-opus-5-5` | Claude |
| 方案文档师 | `claude-sonnet-5-5` | Claude |
| 测试总管 | `claude-sonnet-5-5` | Claude |
| 测试分析师 | `claude-sonnet-5-5` | Claude |
| 测试用例师 | `claude-sonnet-5-5` | Claude |
| 测试执行员 | `claude-sonnet-5-5` | Claude |
| 测试排查员 | `claude-sonnet-5-5` | Claude |
| 修复总管 | `claude-sonnet-5-5` | Claude |
| 修复分析师 | `claude-opus-5-5` | Claude |
| 修复工程师 | `claude-sonnet-5-5` | Claude |
| 修复审核员 | `claude-opus-5-5` | Claude |

已退役的智能体：实施测试员（开发实施小队不再有单独的测试环节，测试由测试小队负责）。已在平台归档（可恢复）。

当前实测设备名为 `MacBook-Pro.local`，不能机械复制到新电脑。恢复时按 Claude 或 OpenCode 运行时类型选择新电脑上的在线实例。

相同模型可用时直接选择；不可用时必须说明缺少的模型、受影响角色、推荐替代模型和能力/价格差异，不得静默使用默认模型。

并发数、Skills、MCP、集成、对话开场建议、小队描述和其他高级设置不属于核心迁移范围。恢复时保持 Multica 默认值即可；不要因为这些可选项缺失而阻塞恢复。若以后某项成为工作流依赖，再单独记录。

已成为工作流依赖、恢复时必须设置的项：

- 实施工程师的并发必须为 `1`，防止多个开发任务同时修改同一仓库（见 `agents/实施工程师.md` 的 `concurrency`）。
- 测试执行员的并发必须为 `1`，一台设备同一时间只能跑一次测试（见 `agents/测试执行员.md` 的 `concurrency`）。
- 测试执行员必须设置 `custom_args`（`--allowedTools` 放行 `exec-launch.py`、`exec-status.sh`、`multica issue wakeup` 等几条命令，加 `--add-dir` 工具包目录），否则无人值守时会因权限提示无人响应而被拦住（见 `agents/测试执行员.md`）。恢复时先把其中的工具包路径换成新电脑的路径，再用 `multica agent update <id> --custom-args '<JSON>'` 设置，并读回核对。
- 修复工程师的并发必须为 `1`，防止多个修复任务同时修改同一仓库（见 `agents/修复工程师.md` 的 `concurrency`）。
- 测试小队 5 个智能体的指令里写死了 maestro-testing-kit 的本机路径 `/Users/future/Documents/workspace/company_otherspace/test_workspace/maestro-testing-kit`。换电脑恢复时，要把指令里的这个路径全部换成新电脑上的路径；路径不存在时，智能体会停下并提醒用户。

## 安全

本目录不保存密码、API Key、Token、Cookie、OAuth 会话或任何 CLI 登录凭证。新电脑必须重新完成认证。
