# Catch-Up 文档

## 📍 当前位置
- **阶段**: Reflect（反思迭代）
- **进度**: 90%
- **会话日期**: 2026-03-16

---

## 🎯 本次会话核心内容

### 发现的问题

**问题现象**：power-service-research启动时找不到topic文件

**问题根源**：SEARCH-R框架存在目录结构设计缺陷

| 问题 | 描述 |
|------|------|
| 两套目录 | `agents/research/` 和 `research/` 同时存放研究内容 |
| 引用错误 | `current-topic.md` 引用空的模板文件，实际内容在别处 |
| 职责混乱 | agents/ 目录既放Agent定义，又放研究产出 |

### 解决方案

**新的设计原则**：
1. `agents/` 只放Agent定义（AGENTS.md, skills/, init.md）
2. `research/` 放所有研究内容
3. 每个课题拥有完整的文档体系
4. 通过registry.md管理所有课题概览

**两种模式**：
- **单课题模式**：`research/topic.md` + 研究产出目录
- **多课题模式**：`research/topics/[name]/` 每个课题完整独立

---

## 📝 本次会话完成的工作

### 框架更新

| 文件 | 操作 | 说明 |
|------|------|------|
| `agents/research/AGENTS.md` | 更新 | v2.0，新增目录结构说明 |
| `agents/research/init.md` | 重写 | v3.0，完整初始化指南 |
| `research/templates/registry-template.md` | 新建 | 课题注册表模板 |
| `research/templates/topic-template.md` | 移动 | 从agents/移动到research/ |
| `research/theory/2026-03-16-directory-restructure-design.md` | 新建 | 设计文档 |

### 实例迁移

**power-service-research** 已迁移到新结构：
- ✅ `research/registry.md` - 课题注册表
- ✅ `research/current-topic.md` - 当前课题引用
- ✅ `research/topic.md` - 课题定义（已存在）
- ✅ `research/catch-up.md` - 追更文档（已存在）
- ✅ `research/observations/` - 观察笔记（已存在）
- ✅ `research/theory/` - 理论文档（已存在）

---

## 📁 新的目录结构

### 单课题模式
```
research/
├── registry.md           # 课题注册表
├── current-topic.md      # 当前课题引用
├── topic.md              # 课题定义
├── catch-up.md           # 追更文档
├── session-log.md        # 会话日志
├── observations/         # 观察笔记
├── theory/               # 理论文档
└── reflections/          # 反思笔记
```

### 多课题模式
```
research/
├── registry.md           # 所有课题概览
├── current-topic.md      # 当前激活课题
└── topics/
    ├── topic-1/          # 完整文档体系
    │   ├── topic.md
    │   ├── catch-up.md
    │   └── ...
    └── topic-2/
        └── ...
```

---

## 🚀 新的启动流程

```
1. 读取课题注册表
   └→ research/registry.md（了解所有课题概览）

2. 确认当前课题
   └→ research/current-topic.md（确定课题路径）

3. 读取课题内容
   └→ research/topic.md（单课题）
   └→ research/topics/[name]/topic.md（多课题）

4. 快速恢复上下文
   └→ catch-up.md
```

---

## ⏭️ 下一步行动

### 立即执行
1. **推送更新**：将SEARCH-R框架更新推送到远程仓库
2. **验证迁移**：在power-service-research中测试新结构

### 后续任务
1. **迁移其他实例**：
   - agent-team-research
   - sgcc-quality-service-research
   - 其他研究项目

2. **更新文档**：
   - QUICKSTART.md
   - README.md

3. **实践验证**：
   - 跟踪新结构的使用效果
   - 收集改进建议

---

## 💾 关键上下文

### 设计决策

**决策1：为什么agents/不放输出？**
- agents/ 是Agent的"程序定义"，应该只包含定义性文件
- 输出内容属于研究数据，应该放在research/
- 职责分离更清晰，便于版本控制和权限管理

**决策2：为什么每个topic有自己的catch-up？**
- 不同课题的上下文完全不同
- 切换课题时不需要重新生成catch-up
- 每个课题的追更内容独立管理

**决策3：为什么需要registry？**
- 提供课题全局视图
- 便于Research Agent快速了解所有课题状态
- 支持课题优先级管理和进度追踪

### 模式判断逻辑

```
if (research/topics/ 目录存在 && 包含子目录) {
    使用多课题模式
} else {
    使用单课题模式
}
```

---

## 📊 进度更新

| 阶段 | 之前 | 现在 | 变化 |
|------|------|------|------|
| 完成度 | 85% | 90% | +5% |
| 核心产出 | Skills/Tools分离 | 目录结构重构 | 新增 |

---

**更新时间**: 2026-03-16  
**更新者**: Research Agent
