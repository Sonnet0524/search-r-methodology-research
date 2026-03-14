# Skills - 研究技能库

本目录包含Research Agent可用的研究技能，遵循Skills v2.0标准。

## 核心原则

1. **Context Window is a Public Good** - 每个token都要有价值
2. **Progressive Disclosure** - 渐进式加载
3. **Skills可调用Tools** - 协作关系

## 目录结构

```
project/                      # 项目根目录
├── skills/                   # 技能（业务能力）
│   ├── literature-review/    # 文献检索
│   ├── observation/          # 观察记录
│   ├── theory-building/      # 理论构建
│   └── quality-gate/         # 质量门控
│
└── tools/                    # 工具（底层能力）
    ├── baidu-search/         # 百度搜索
    ├── baidu-scholar-search/ # 百度学术
    ├── baidu-baike-data/     # 百度百科
    ├── paddleocr-doc-parsing/    # PaddleOCR文档解析
    ├── paddleocr-text-recognition/ # PaddleOCR文本识别
    ├── paddleocr-async/      # PaddleOCR异步API
    ├── file-reading/         # 文件读取
    └── document-output/      # 文档输出
```

## 技能分类

| 类型 | 说明 | 技能 |
|------|------|------|
| **tool** | 底层工具，可执行脚本 | baidu-search, baidu-scholar-search, baidu-baike-data, paddleocr-doc-parsing, paddleocr-text-recognition, paddleocr-async, file-reading, document-output |
| **ability** | 业务能力，方法论指导 | literature-review, observation, theory-building, quality-gate |

## 技能列表

### Tools（底层工具）

| 工具 | 触发条件 | 用途 |
|------|---------|------|
| [baidu-search](../tools/baidu-search/SKILL.md) | "百度搜索"、"全网搜索" | 百度AI搜索（全球下载量第一） |
| [baidu-scholar-search](../tools/baidu-scholar-search/SKILL.md) | "学术搜索"、"论文搜索" | 百度学术文献检索 |
| [baidu-baike-data](../tools/baidu-baike-data/SKILL.md) | "百科查询"、"词条解释" | 百度百科 词条查询 |
| [paddleocr-doc-parsing](../tools/paddleocr-doc-parsing/SKILL.md) | "解析文档"、"提取表格/公式" | 高级文档解析（表格、公式、图表） |
| [paddleocr-text-recognition](../tools/paddleocr-text-recognition/SKILL.md) | "识别文字"、"OCR"、"提取文字" | 图像/PDF文字识别 |
| [paddleocr-async](../tools/paddleocr-async/SKILL.md) | "异步OCR"、"大文件识别" | PaddleOCR异步API调用 |
| [file-reading](../tools/file-reading/SKILL.md) | "读取"、"解析"文件 | 读取PDF/Word/Excel等 |
| [document-output](../tools/document-output/SKILL.md) | "生成报告"、"输出文档" | 生成格式化文档 |

### Abilities（业务能力）

| 技能 | 触发条件 | 用途 |
|------|---------|------|
| [literature-review](literature-review/SKILL.md) | "检索文献"、"调研研究" | 文献检索与分析 |
| [observation](observation/SKILL.md) | "观察"、"记录发现" | 系统化观察记录 |
| [theory-building](theory-building/SKILL.md) | "构建理论"、"建立模型" | 理论构建与验证 |
| [quality-gate](quality-gate/SKILL.md) | 研究结论需验证时 | 质量评估与介入决策 |

## Skills vs Tools

```
Skills (Markdown文档)
    ↓ 指导/调用
Tools (Python实现)
    ↓ 执行
外部API / 文件系统
```

- **Skills**: 给LLM看的指令文档
- **Tools**: 实际执行的代码
- Skills可以调用Tools

## SKILL.md规范

```yaml
---
name: skill-name
description: 功能描述 + 触发条件。Use when user asks to "trigger1", "trigger2".
trigger: on_demand
tags: tag1, tag2
---
```

**要求**:
- Frontmatter仅4个字段
- description包含触发条件
- Body < 200行

## Scripts规范

```python
# scripts/api.py
# - 每个文件 < 80行
# - 只依赖Python标准库
# - API Key从环境变量读取
```

## 使用方法

### 1. Tool类型技能
```python
# 调用baidu-search
from tools.baidu_search.scripts.search import search

result = search(query="关键词", count=10)
```

### 2. Ability类型技能
```markdown
# 按SKILL.md中的方法指导执行
1. 阅读SKILL.md理解方法论
2. 按Execution Flow执行
3. 使用Usage Patterns参考
4. 输出符合Output Format
```

## 相关资源

- [SEARCH-R循环](../methodology/search-r-cycle.md)
- [研究深度定义](../methodology/research-depth.md)
- [文档模板库](../templates/)

---

**版本**: v2.3  
**更新时间**: 2026-03-14  
**维护者**: SEARCH-R Framework
