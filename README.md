# SEARCH-R Methodology Research

> 研究SEARCH-R方法论体系，探索如何利用LLM和Research Agent辅助人类开展研究探索

---

## 🌐 仓库生态系统

本项目是SEARCH-R生态系统的一部分，以下是完整的仓库关系：

### 架构层级

```
┌─────────────────────────────────────────────────────────────────┐
│                        L0: 方法论框架层                           │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │  SEARCH-R                                                    │ │
│  │  📍 https://github.com/Sonnet0524/SEARCH-R                   │ │
│  │  🎯 方法论框架模板仓库                                         │ │
│  │  📦 提供：方法论定义、模板、Skills、Tools                      │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              ↓ 提供方法论支撑                      │
├─────────────────────────────────────────────────────────────────┤
│                        L1: 研究课题层                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  search-r-methodology-research (本仓库)                    │   │
│  │  📍 https://github.com/Sonnet0524/search-r-methodology-research │
│  │  🎯 研究SEARCH-R方法论本身                                   │   │
│  │  📦 产出：方法论优化、理论文档、最佳实践                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              ↕ 方法论迭代反馈                     │
│  ┌──────────────────┐ ┌──────────────────┐ ┌─────────────────┐  │
│  │ agent-team-      │ │ harness-         │ │ sgcc-quality-   │  │
│  │ research         │ │ engineering-     │ │ service-        │  │
│  │ research         │ │ research         │ │ research        │  │
│  │                  │ │                  │ │                 │  │
│  │ Agent协作研究    │ │ Harness工程研究  │ │ 国网优质服务研究 │  │
│  └──────────────────┘ └──────────────────┘ └─────────────────┘  │
│                                                                  │
│  ┌──────────────────┐                                           │
│  │ openclaw-research│                                           │
│  │                 │                                           │
│  │ OpenClaw技术研究 │                                           │
│  └──────────────────┘                                           │
└─────────────────────────────────────────────────────────────────┘
```

### 仓库详细说明

| 仓库 | 层级 | 定位 | 用途 |
|------|:----:|------|------|
| **[SEARCH-R](https://github.com/Sonnet0524/SEARCH-R)** | L0 | 方法论框架模板 | 提供方法论定义、模板、Skills、Tools |
| **[search-r-methodology-research](https://github.com/Sonnet0524/search-r-methodology-research)** | L1 | 方法论研究 | 研究SEARCH-R方法论本身，产出优化建议 |
| **[agent-team-research](https://github.com/Sonnet0524/agent-team-research)** | L1 | 领域研究 | 使用SEARCH-R研究Agent协作模式 |
| **[harness-engineering-research](https://github.com/Sonnet0524/harness-engineering-research)** | L1 | 领域研究 | 使用SEARCH-R研究评估方法论 |
| **[sgcc-quality-service-research](https://github.com/Sonnet0524/sgcc-quality-service-research)** | L1 | 领域研究 | 使用SEARCH-R研究国网优质服务举措 |
| **[openclaw-research](https://github.com/Sonnet0524/openclaw-research)** | L1 | 技术研究 | 使用SEARCH-R研究OpenClaw技术 |

### 数据流向

```
SEARCH-R (L0)
    │
    ├─── 方法论定义 ──→ 所有L1研究课题
    │
    ├─── 文档模板 ────→ 所有L1研究课题
    │
    ├─── Skills库 ────→ 所有L1研究课题
    │
    └─── Tools库 ─────→ 所有L1研究课题
    
search-r-methodology-research (L1)
    │
    └─── 方法论优化 ──→ SEARCH-R (L0)
    
其他L1研究课题
    │
    └─── 实践反馈 ────→ search-r-methodology-research
```

---

## 📋 项目概述

本研究课题使用SEARCH-R方法论来研究SEARCH-R方法论本身，形成方法论的自举和迭代优化。

**研究目标**：
- 建立完整的SEARCH-R方法论体系
- 设计高效的Research Agent架构
- 建立研究质量保障机制
- 形成可复用的研究框架

**研究深度**：Level 0-2（第一性原理到设计原则）

**研究周期**：长期持续研究

---

## 📁 项目结构

```
search-r-methodology-research/
├── README.md                    # 项目说明（本文件）
├── research/                    # 研究目录
│   ├── topic.md                 # 课题定义
│   ├── current-topic.md         # 当前研究焦点
│   ├── session-log.md           # 会话日志
│   ├── research-topics/         # 研究课题库
│   ├── observations/            # 观察笔记
│   ├── retrievals/              # 检索报告
│   ├── theory/                  # 理论文档
│   └── reflections/             # 反思笔记
├── methodology/                 # 方法论定义（同步自SEARCH-R）
│   ├── search-r-cycle.md        # 研究循环
│   ├── research-depth.md        # 深度标准
│   └── human-role.md            # 角色定义
├── skills/                      # 研究技能
├── tools/                       # 底层工具
├── templates/                   # 文档模板
└── sync-logs/                   # 同步日志
```

---

## 🎯 研究内容

### 核心研究问题

1. **SEARCH-R研究循环的本质是什么？**
   - 循环的理论基础
   - 循环的设计原则
   - 循环的适用边界

2. **如何设计Research Agent？**
   - Agent架构设计
   - 核心能力定义
   - 记忆系统设计

3. **如何保证研究质量？**
   - 质量门控机制
   - 元认知意识
   - Human参与最小化

4. **如何文档化研究过程？**
   - 文档标准体系
   - 模板设计
   - 可追溯性保障

### 已完成的研究

#### 理论成果

- [元认知意识实现方案](research/theory/2026-03-07-metacognition-implementation.md)
- [记忆压缩机制研究](research/theory/2026-03-07-memory-compression-deep-dive.md)
- [质量门控与Agent定义](research/theory/2026-03-07-quality-gate-and-agent-definition.md)

#### 方法论反思

- [Research Agent方法论设计反思](research/reflections/2026-03-07.md)
- [质量门控深度Review反思](research/reflections/2026-03-07-quality-gate-review.md)

#### 竞品分析

- [Karpathy autoresearch项目分析](research/observations/2026-03-11-karpathy-autoresearch-analysis.md)

---

## 📊 研究进展

- **当前阶段**：持续完善
- **完成度**：85%
- **状态**：方法论框架已建立，持续优化中

### 里程碑

- [x] **2026-03-07**: 完成核心理论构建
- [x] **2026-03-08**: 完成文档迁移和整理
- [x] **2026-03-09**: 明确方法论研究定位
- [x] **2026-03-11**: 完成Karpathy autoresearch分析
- [x] **2026-03-14**: 创建methodology核心文档
- [ ] **持续**: 收集各课题实践经验并优化

---

## 🔗 相关资源

### 方法论框架

- [SEARCH-R方法论框架](https://github.com/Sonnet0524/SEARCH-R) - 方法论模板仓库
- [SEARCH-R循环定义](methodology/search-r-cycle.md)
- [研究深度定义](methodology/research-depth.md)
- [Human角色定义](methodology/human-role.md)

### 使用SEARCH-R的研究课题

| 课题 | 研究方向 | 状态 |
|------|---------|:----:|
| [agent-team-research](https://github.com/Sonnet0524/agent-team-research) | Agent协作模式 | Active |
| [harness-engineering-research](https://github.com/Sonnet0524/harness-engineering-research) | 评估方法论 | Active |
| [sgcc-quality-service-research](https://github.com/Sonnet0524/sgcc-quality-service-research) | 国网优质服务 | Active |
| [openclaw-research](https://github.com/Sonnet0524/openclaw-research) | OpenClaw技术 | Active |

---

## 🚀 快速开始

### 对于研究者

1. 阅读 [课题定义](research/topic.md) 了解研究目标
2. 查看 [当前进展](research/current-topic.md) 了解最新状态
3. 阅读 [会话日志](research/session-log.md) 了解研究历程
4. 参考 [理论成果](research/theory/) 深入理解方法论

### 对于使用者

1. 参考 [SEARCH-R模板](https://github.com/Sonnet0524/SEARCH-R) 创建自己的研究课题
2. 使用SEARCH-R方法论开展研究
3. 反馈实践经验，帮助优化方法论

---

## 🔄 同步机制

本仓库与SEARCH-R模板仓库保持同步：

```
SEARCH-R模板仓库                    研究仓库
├── methodology/      ─────同步────→ methodology/
├── skills/           ─────同步────→ skills/
├── tools/            ─────同步────→ tools/
└── templates/        ─────同步────→ templates/

研究仓库                              SEARCH-R模板仓库
└── 方法论优化建议    ─────反馈────→ 方法论迭代
```

同步日志记录在 [sync-logs/](sync-logs/) 目录。

---

## 📝 研究记录

详细研究记录见 [会话日志](research/session-log.md)

---

## 🤝 贡献

本课题是方法论研究，欢迎：
- 提出方法论改进建议
- 分享使用SEARCH-R的实践经验
- 参与方法论讨论和Review

---

## 📄 许可证

本项目采用 AGPL-3.0 许可证

---

**维护者**: Research Agent  
**创建时间**: 2026-03-11  
**课题类型**: 方法论研究  
**研究状态**: Active
