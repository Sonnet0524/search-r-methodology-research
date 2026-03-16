# SEARCH-R 框架目录重构设计

**版本**: v3.0  
**日期**: 2026-03-16  
**状态**: 设计中

---

## 🎯 设计目标

### 核心原则

1. **职责分离**：agents/ 只放Agent定义，research/ 只放研究内容
2. **课题独立**：每个课题拥有完整的文档体系
3. **统一入口**：research agent层面管理所有课题概览
4. **灵活扩展**：支持单课题和多课题两种模式

---

## 📁 新目录结构

### SEARCH-R 框架模板

```
SEARCH-R/
├── agents/research/              # Agent定义层（只读模板）
│   ├── AGENTS.md                 # Agent核心定义
│   ├── init.md                   # 初始化指南
│   ├── ESSENTIALS.md             # 核心要点速查
│   └── skills/                   # 技能库
│       ├── literature-review/
│       ├── observation/
│       ├── theory-building/
│       └── quality-gate/
│
├── research/                     # 研究内容层（实例化时复制）
│   ├── registry.md               # 课题注册表（所有课题概览）
│   ├── current-topic.md          # 当前激活课题引用
│   │
│   ├── topics/                   # 多课题目录
│   │   ├── [topic-name]/         # 单个课题目录
│   │   │   ├── topic.md          # 课题定义
│   │   │   ├── catch-up.md       # 课题追更文档
│   │   │   ├── session-log.md    # 会话日志
│   │   │   ├── observations/     # 观察笔记
│   │   │   ├── retrievals/       # 检索报告
│   │   │   ├── theory/           # 理论文档
│   │   │   ├── reflections/      # 反思笔记
│   │   │   └── references/       # 参考资料
│   │   │
│   │   └── [another-topic]/      # 另一个课题
│   │       └── ...
│   │
│   └── templates/                # 课题模板
│       ├── topic-template.md
│       └── registry-template.md
│
├── methodology/                  # 方法论体系
│   ├── search-r-cycle.md
│   ├── research-depth.md
│   └── human-role.md
│
├── templates/                    # 文档模板
│   ├── observation-template.md
│   ├── retrieval-template.md
│   ├── theory-template.md
│   └── reflection-template.md
│
├── tools/                        # 工具集
│   └── init-research.sh
│
└── opencode.json                 # 项目配置
```

### 单课题模式实例

```
my-research/                      # 单课题研究项目
├── agents/research/              # Agent定义（从SEARCH-R复制）
│   └── ...
│
├── research/                     # 研究内容
│   ├── registry.md               # 课题注册表（只有一个课题）
│   ├── current-topic.md          # 引用当前课题
│   │
│   ├── topic.md                  # 直接放在research根目录
│   ├── catch-up.md
│   ├── session-log.md
│   ├── observations/
│   ├── retrievals/
│   ├── theory/
│   ├── reflections/
│   └── references/
│
├── methodology/
├── templates/
└── opencode.json
```

### 多课题模式实例

```
my-research/                      # 多课题研究项目
├── agents/research/              # Agent定义
│   └── ...
│
├── research/                     # 研究内容
│   ├── registry.md               # 课题注册表
│   ├── current-topic.md          # 当前激活课题
│   │
│   ├── topics/                   # 课题目录
│   │   ├── agent-memory/         # 课题1
│   │   │   ├── topic.md
│   │   │   ├── catch-up.md
│   │   │   ├── session-log.md
│   │   │   ├── observations/
│   │   │   ├── theory/
│   │   │   └── ...
│   │   │
│   │   └── agent-metacognition/  # 课题2
│   │       ├── topic.md
│   │       ├── catch-up.md
│   │       └── ...
│   │
│   └── templates/
│
├── methodology/
├── templates/
└── opencode.json
```

---

## 🔄 工作流程变更

### 启动流程（新）

```
1. 读取课题注册表
   - 查看 research/registry.md
   - 了解所有课题概览和状态

2. 确认当前课题
   - 查看 research/current-topic.md
   - 确定当前激活的课题路径

3. 读取课题内容
   - 单课题：research/topic.md
   - 多课题：research/topics/[topic-name]/topic.md

4. 继续研究
   - 读取课题的 catch-up.md
   - 读取课题的 session-log.md
   - 开始研究循环
```

### 会话结束流程（新）

```
1. 更新课题进展
   - 更新 research/topics/[topic-name]/topic.md
   - 更新 research/topics/[topic-name]/session-log.md

2. 更新课题注册表
   - 更新 research/registry.md 中的进度概览

3. 生成追更文档
   - 更新 research/topics/[topic-name]/catch-up.md
```

---

## 📋 课题注册表设计

### registry.md 结构

```markdown
---
updated: YYYY-MM-DD
total_topics: N
active_topics: M
---

# 课题注册表

## 📊 课题概览

| 课题名称 | 状态 | 优先级 | 阶段 | 完成度 | 最后更新 |
|---------|------|--------|------|--------|----------|
| Agent记忆系统 | active | high | Survey | 30% | 2026-03-16 |
| Agent元认知 | paused | medium | Explore | 10% | 2026-03-15 |
| Agent协作模式 | planned | low | - | 0% | - |

## 📁 课题路径

- **Agent记忆系统**: `topics/agent-memory/`
- **Agent元认知**: `topics/agent-metacognition/`
- **Agent协作模式**: `topics/agent-collaboration/`

## 🎯 当前焦点

**活跃课题**: Agent记忆系统

**关键问题**:
1. 记忆如何分类？
2. 如何实现记忆压缩？

**下一步**: 完成Survey阶段的资料收集

---

**维护者**: Research Agent
**更新时间**: 2026-03-16
```

### current-topic.md 结构

```markdown
---
topic: Agent记忆系统
path: topics/agent-memory
activated: 2026-03-16
---

# 当前研究课题

**课题名称**: Agent记忆系统

**路径**: `topics/agent-memory/`

**状态**: active

**快速链接**:
- [课题定义](topics/agent-memory/topic.md)
- [追更文档](topics/agent-memory/catch-up.md)
- [会话日志](topics/agent-memory/session-log.md)

---

**激活时间**: 2026-03-16
```

---

## 📝 单课题 vs 多课题模式

### 模式判断

```
判断逻辑：
if (research/topics/ 目录存在 && 包含子目录) {
    使用多课题模式
} else {
    使用单课题模式
}
```

### 模式差异

| 方面 | 单课题模式 | 多课题模式 |
|------|-----------|-----------|
| topic.md位置 | `research/topic.md` | `research/topics/[name]/topic.md` |
| 研究产出 | `research/observations/` | `research/topics/[name]/observations/` |
| catch-up | `research/catch-up.md` | `research/topics/[name]/catch-up.md` |
| registry | 只有一个课题记录 | 包含所有课题概览 |
| 切换课题 | 不需要 | 通过current-topic.md切换 |

---

## 🔧 迁移指南

### 从旧结构迁移

```
旧结构 → 新结构

agents/research/research-topics/[topic].md 
    → research/topics/[topic]/topic.md

agents/research/observations/
    → research/topics/[topic]/observations/

agents/research/session-log.md
    → research/topics/[topic]/session-log.md

agents/research/current-topic.md
    → research/current-topic.md (引用方式变更)
```

### 迁移步骤

1. 创建 `research/` 目录结构
2. 迁移课题配置到 `research/topics/`
3. 迁移研究产出到对应课题目录
4. 创建课题注册表 `research/registry.md`
5. 更新 `research/current-topic.md`
6. 清理 `agents/research/` 中的旧内容

---

## 🎓 设计决策记录

### 决策1：为什么agents/不放输出？

**理由**：
- agents/ 是Agent的"程序定义"，应该只包含定义性文件
- 输出内容属于研究数据，应该放在research/
- 职责分离更清晰，便于版本控制和权限管理

### 决策2：为什么每个topic有自己的catch-up？

**理由**：
- 不同课题的上下文完全不同
- 切换课题时不需要重新生成catch-up
- 每个课题的追更内容独立管理

### 决策3：为什么需要registry？

**理由**：
- 提供课题全局视图
- 便于Research Agent快速了解所有课题状态
- 支持课题优先级管理和进度追踪

---

## 📊 实施计划

### Phase 1: 框架更新
- [ ] 更新 AGENTS.md
- [ ] 更新 init.md
- [ ] 创建 registry-template.md
- [ ] 移动 topic-template.md 到 research/templates/

### Phase 2: 实例迁移
- [ ] 迁移 power-service-research
- [ ] 迁移 agent-team-research
- [ ] 验证新结构可行性

### Phase 3: 文档完善
- [ ] 更新 QUICKSTART.md
- [ ] 更新 README.md
- [ ] 添加迁移指南

---

**设计者**: Research Agent
**设计时间**: 2026-03-16
**状态**: 待评审
