---
name: figma-restore
description: 按 Figma 设计稿还原或修改本项目的 UI：先分析出逻辑对照表和差异清单，用户确认后只改清单内的内容，按项目的适配方式、token 和组件实现，最后多尺寸截图校验。用户给出 Figma 链接或 node-id 要求还原、实现、按新 UI 修改页面时使用。
argument-hint: "<Figma 链接或 node-id> <要还原或修改的页面>"
---

# Figma 还原：{{PROJECT_NAME}}

任务：$ARGUMENTS

（不支持 `$ARGUMENTS` 替换的工具里，以用户调用本 skill 时给出的 Figma 链接和页面为任务。）

先完整阅读同目录的 `workflow.md`，严格按其中的三个阶段执行。下面是本项目的信息，`workflow.md` 里提到“见 SKILL.md”的内容都在这里。

> 本文件由 `figma-restore-init` 于 {{GENERATED_DATE}} 生成。项目变化（换组件库、改主题、换电脑）后重新运行 `figma-restore-init` 更新。标记为“待确认”的条目，使用前先问用户。

## 1. 技术栈

- 平台 / 框架：{{FRAMEWORK}}
- 语言：{{LANGUAGE}}
- UI 组件库：{{UI_LIBRARY}}
- 样式方案：{{STYLING}}
- 状态管理：{{STATE_MANAGEMENT}}

## 2. 尺寸与适配

- 设计稿基准宽度：{{DESIGN_BASE_WIDTH}}
- 适配方式：{{ADAPT_METHOD}}
- 换算规则：{{CONVERSION_RULE}}
- 校验用的尺寸：{{VERIFY_SIZES}}

### 折叠屏

- 是否支持：{{FOLDABLE_SUPPORT}}
- 支持的形态与校验宽度：{{FOLDABLE_FORMS}}
- 内屏默认布局策略：{{FOLDABLE_LAYOUT}}
- 铰链 / 半折叠姿态：{{FOLDABLE_HINGE}}
- 校验方式：{{FOLDABLE_VERIFY}}

## 3. Token 对照表

按“值”把设计稿数值匹配到项目写法。阶段二只能用这里的写法；完全一致的直接用，不一致或找不到的在阶段一列出归并建议，让用户确认。

- token / 主题文件位置：{{TOKEN_FILES}}

### 颜色
| 值 | 项目写法 | 用途 |
|---|---|---|
{{COLOR_ROWS}}

### 字体
| 字号 / 字重 / 行高 | 项目写法 |
|---|---|
{{TYPOGRAPHY_ROWS}}

### 间距与圆角
| 值 | 项目写法 |
|---|---|
{{SPACING_ROWS}}

### 阴影
| 值 | 项目写法 |
|---|---|
{{SHADOW_ROWS}}

## 4. 可复用组件

| 组件 | 路径 | 用途 / 备注 |
|---|---|---|
{{COMPONENT_ROWS}}

## 5. 资源

- 图片目录：{{IMAGE_DIR}}
- 图标目录与格式：{{ICON_DIR}}
- 图标使用方式：{{ICON_USAGE}}

## 6. 本机环境

- Figma MCP：{{FIGMA_MCP}}
- 运行与截图方式：{{RUN_AND_SCREENSHOT}}
- 静态分析与测试命令（生成时已实际运行确认）：{{CHECK_COMMANDS}}
- 版本管理：{{VCS}}

## 7. 项目特有规则

{{PROJECT_RULES}}
