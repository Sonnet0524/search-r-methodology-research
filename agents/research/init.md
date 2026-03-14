# Research Agent 初始化指南

> 如何使用SEARCH-R方法论创建和管理研究课题

**版本**: v2.0 | **更新**: 2026-03-13

---

## 🎯 设计理念

### 架构定位

```
SEARCH-R (方法论模板仓库)
├─ 提供方法论体系
├─ 提供文档模板
├─ 提供Agent设计规范
└─ 提供工具和技能库
    ↓ 作为模板
    ↓ 复制使用
研究项目 (具体研究仓库)
├─ 使用SEARCH-R方法论
├─ 管理多个研究课题
└─ 产出具体研究成果
```

### 两种使用场景

```
场景A: 创建新的研究项目
"我想研究 [课题描述]"
→ 创建新项目 → 复制SEARCH-R模板 → 创建第一个课题 → 开始研究

场景B: 在现有项目中添加课题
"我想在当前项目中研究 [新课题]"
→ 创建新课题配置 → 激活课题 → 开始研究
```

---

## 🚀 场景A：创建新的研究项目

### 对话式创建流程

**用户**：我想研究Agent的记忆系统设计

**Research Agent**：
```
好的！我将帮你创建一个新的研究项目。

📋 请提供以下基本信息：

1. **项目名称** (用于目录名，建议用英文):
   示例: agent-memory-system-research
   
2. **项目路径** (项目创建在哪里):
   示例: /Users/sonnet/opencode/
   或直接回车使用默认路径

3. **研究背景** (简短描述，1-2句话即可):
   为什么要研究这个课题？
   
4. **核心问题** (最重要的问题，1-3个):
   你想通过研究解决什么问题？

💡 提示：先提供基本信息即可开始，后续可以逐步完善
```

**用户**：
```
1. agent-memory-research
2. /Users/sonnet/opencode/
3. Agent需要有效的记忆系统来支持长期对话和知识积累
4. 记忆应该分为哪些类型？如何实现记忆的压缩和遗忘？
```

**Research Agent**：
```
✅ 收到信息，正在创建研究项目...

[执行以下操作]

1. 创建项目目录结构
2. 复制SEARCH-R方法论模板
3. 创建opencode.json配置
4. 创建第一个研究课题配置
5. 激活研究课题

✅ 项目创建完成！

📁 项目位置: /Users/sonnet/opencode/agent-memory-research
📄 课题配置: agents/research/research-topics/agent-memory-system.md
🎯 当前状态: 已激活

📊 研究课题概览：
- 研究背景: Agent需要有效的记忆系统...
- 核心问题: 记忆分类、记忆压缩、记忆遗忘
- 当前阶段: Survey (观察调研)
- 下一步: 开始第一次调研

是否现在开始研究？
```

### 自动化步骤

Research Agent会自动完成：

```bash
# 1. 创建项目目录
mkdir -p /Users/sonnet/opencode/agent-memory-research

# 2. 复制SEARCH-R模板文件
# - methodology/
# - templates/
# - agents/research/ (AGENTS.md, skills/)
# - tools/

# 3. 创建opencode.json配置
cat > opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "research-agent": {
      "description": "Research Agent - Agent记忆系统研究",
      "mode": "primary",
      "prompt": "{file:./agents/research/AGENTS.md}",
      "skills": ["literature-review", "observation", "quality-gate", "theory-building"]
    }
  }
}
EOF

# 4. 创建研究课题配置 (使用最小化模板)
# 详见下一节

# 5. 激活研究课题
# 更新 current-topic.md
```

---

## 📝 研究课题配置模板

### 最小化模板（推荐用于快速启动）

```markdown
---
topic: [课题名称]
created: YYYY-MM-DD
status: active
priority: high
---

# [课题名称]

## 📋 研究背景

[为什么要研究？背景是什么？]

## 🎯 核心问题

1. [问题1]
2. [问题2]
3. [问题3]

## 📊 当前进展

### 当前阶段
- 阶段：Survey (观察调研)
- 完成度：0%
- 下一步：[下一步行动]

### 已完成
- [YYYY-MM-DD] 创建研究课题

## 📝 研究记录

### [YYYY-MM-DD] 创建课题
- 研究内容：初始化研究课题
- 下一步：开始Survey阶段
```

### 完整模板

当研究逐步深入时，可以扩展为完整模板。详见：
- [topic-template.md](research-topics/topic-template.md) - 包含所有字段
- [课题配置详解](#课题配置字段说明)

### 何时使用哪个模板？

```
启动阶段 → 最小化模板
├─ 只填写核心信息
├─ 快速开始研究
└─ 后续逐步完善

深入研究 → 完整模板
├─ 补充研究范围
├─ 添加研究计划
├─ 记录风险管理
└─ 设置里程碑
```

---

## 🔄 场景B：在现有项目中添加课题

### 对话式添加流程

**用户**：我想在当前项目中研究Agent的元认知能力

**Research Agent**：
```
好的！我将在当前项目中创建新的研究课题。

📋 当前项目信息：
- 项目：agent-memory-research
- 当前课题：Agent记忆系统设计 (active)

📋 新课题基本信息：

1. **课题名称**: Agent元认知能力研究
   (建议用中文名称，便于理解)

2. **研究背景** (1-2句话):
   为什么要研究这个课题？

3. **核心问题** (1-3个):
   你想解决什么问题？

4. **优先级**: high/medium/low
   (相对于当前课题的优先级)
```

**用户**：
```
2. Agent需要知道自己什么时候不知道，这是质量门控的基础
3. 元认知如何定义？如何评估Agent的元认知水平？
4. medium
```

**Research Agent**：
```
✅ 创建新研究课题...

[创建课题配置文件]
[更新项目课题列表]

✅ 课题创建完成！

📁 课题配置: research-topics/agent-metacognition.md
📊 当前状态: paused (优先级medium)
🎯 当前课题: 仍为"Agent记忆系统设计"

💡 提示：
- 新课题状态为paused，不会干扰当前研究
- 可以随时切换："切换到Agent元认知能力研究"
- 建议完成当前课题的重要节点后再切换

是否需要切换到新课题？
```

---

## 📊 课题配置字段说明

### 必填字段（最小化模板）

| 字段 | 说明 | 示例 |
|------|------|------|
| `topic` | 课题名称 | Agent记忆系统设计 |
| `created` | 创建日期 | 2026-03-13 |
| `status` | 当前状态 | active/paused/completed |
| `priority` | 优先级 | high/medium/low |
| **研究背景** | 为什么研究 | Agent需要有效的记忆系统... |
| **核心问题** | 1-3个关键问题 | 记忆如何分类？如何压缩？ |

### 可选字段（完整模板）

| 字段 | 何时添加 | 说明 |
|------|----------|------|
| **研究目标** | Survey阶段后 | 明确期望产出和成功标准 |
| **研究范围** | 探索阶段时 | 定义包含和不包含的内容 |
| **研究资料** | 检索过程中 | 记录相关文档和参考资料 |
| **研究计划** | 规划阶段时 | 分阶段的任务和产出 |
| **风险挑战** | 发现风险时 | 识别的风险和缓解措施 |
| **里程碑** | 明确节点后 | 关键节点和时间点 |

### 字段填充策略

```
创建时 → 必填字段
├─ 快速启动
└─ 基本方向明确

Survey阶段 → 补充背景
├─ 深化背景理解
└─ 明确研究动机

Explore阶段 → 补充资料
├─ 记录检索结果
└─ 整理参考资料

Analyze阶段 → 补充计划
├─ 制定研究计划
└─ 设置里程碑

持续更新 → 记录进展
├─ 更新当前进展
└─ 记录研究日志
```

---

## 🔄 课题状态管理

### 状态定义

```
active   - 正在进行的研究
paused   - 暂停的研究
completed - 已完成的研究
```

### 状态转换规则

```
创建课题 → paused (初始状态)
paused → active (激活课题)
active → paused (暂停课题)
active → completed (完成课题)
```

### 多课题管理

```
建议策略：
├─ 同时active的课题不超过2个
├─ 高优先级课题优先处理
├─ 定期回顾paused的课题
└─ 完成的课题及时归档

课题切换：
1. 保存当前课题进展
2. 更新当前课题状态为paused
3. 更新新课题状态为active
4. 更新current-topic.md
5. 读取新课题配置继续研究
```

---

## 🛠️ 自动化工具

### init-research.sh 脚本

提供自动化创建工具（可选）：

```bash
# 使用脚本创建新项目
./tools/init-research.sh \
  --name "agent-memory-research" \
  --path "/Users/sonnet/opencode/" \
  --topic "Agent记忆系统设计"

# 脚本会自动：
# 1. 创建项目目录
# 2. 复制SEARCH-R模板
# 3. 创建配置文件
# 4. 初始化课题
```

### Agent引导创建（推荐）

更推荐使用对话式创建：
- Agent会引导你填写信息
- 可以随时调整和完善
- 避免手动操作的错误

---

## 📁 目录结构

### SEARCH-R模板仓库

```
SEARCH-R/
├── methodology/           # 方法论体系
├── templates/             # 文档模板
├── agents/research/       # Agent设计
│   ├── AGENTS.md          # Agent核心定义
│   ├── init.md            # 本文件
│   ├── skills/            # 技能库
│   └── research-topics/
│       └── topic-template.md
└── tools/                 # 工具集
```

### 研究项目仓库

```
research-project/
├── opencode.json          # 项目配置
├── agents/research/
│   ├── AGENTS.md          # Agent定义
│   ├── init.md            # 初始化指南
│   ├── current-topic.md   # 当前课题
│   ├── session-log.md     # 会话日志
│   ├── research-topics/   # 课题库
│   │   ├── topic-1.md
│   │   ├── topic-2.md
│   │   └── ...
│   ├── observations/      # 观察笔记
│   ├── retrievals/        # 检索报告
│   ├── theory/            # 理论文档
│   └── reflections/       # 反思笔记
├── methodology/           # 方法论
├── templates/             # 文档模板
└── docs/                  # 项目文档
```

---

## 🎓 最佳实践

### 创建研究项目

1. **从对话开始** - 让Agent引导你创建
2. **最小化启动** - 只填写必填信息即可开始
3. **后续完善** - 在研究过程中逐步补充细节

### 管理多个课题

1. **限制active数量** - 同时进行不超过2个
2. **明确优先级** - 帮助决策研究顺序
3. **定期回顾** - 每周回顾paused课题
4. **及时归档** - 完成课题移至completed

### 课题文档维护

1. **及时更新进展** - 每次会话后更新
2. **记录关键决策** - 在研究记录中留痕
3. **整理研究资料** - 在研究资料中归档
4. **同步状态变更** - 切换课题时更新状态

---

## 📖 使用示例

### 示例1：快速创建研究项目

```
Human: "我想研究代码自动生成的质量保证方法"

Agent: "好的！请提供：
1. 项目名称: code-generation-qa-research
2. 项目路径: [使用默认]
3. 研究背景: 代码生成工具的输出质量参差不齐，需要系统化的质量保证方法
4. 核心问题: 如何评估生成代码的质量？如何自动化质量检查？

创建中... ✅ 完成！是否开始研究？"

Human: "开始研究"

Agent: "进入Survey阶段..."
```

### 示例2：在项目中添加课题

```
Human: "我想研究代码生成的测试覆盖"

Agent: "好的！当前项目有1个课题，我将创建新课题。
课题名称: 代码生成测试覆盖研究
研究背景: 测试覆盖是代码质量的重要指标
核心问题: 如何为生成的代码自动创建测试？测试覆盖率达到多少合适？
优先级: medium

创建中... ✅ 完成！是否切换到新课题？"

Human: "先完成当前课题"

Agent: "好的，新课题已创建但保持paused状态。
当前课题: 代码生成质量保证 (active)
可随时切换到: 代码生成测试覆盖 (paused)"
```

### 示例3：切换研究课题

```
Human: "切换到代码生成测试覆盖研究"

Agent: "切换课题中...
1. 保存当前课题进展
   - 已完成: 质量评估框架设计
   - 下一步: 实现评估工具
   
2. 激活新课题
   - 课题: 代码生成测试覆盖研究
   - 状态: active
   - 当前进展: Survey阶段
   
3. 更新current-topic.md

✅ 切换完成！
当前课题: 代码生成测试覆盖研究
下一步: 开始调研测试覆盖最佳实践"
```

---

## 🔧 故障排除

### 常见问题

**Q: 课题配置文件太复杂，不知道怎么填？**
A: 使用最小化模板，只填写核心信息即可开始。后续在研究过程中逐步完善。

**Q: 可以同时研究多个课题吗？**
A: 建议同时active的课题不超过2个，避免分散注意力。可以暂停低优先级课题。

**Q: 如何判断课题是否完成？**
A: 参考课题的"成功标准"和"期望产出"。当核心问题得到解答，期望产出已完成，即可标记为completed。

**Q: 暂停的课题会遗忘吗？**
A: 不会。课题配置会保留所有进展和下一步行动。建议每周回顾paused课题，适时恢复研究。

**Q: 如何复用其他课题的成果？**
A: 在课题配置的"相关课题"部分，可以引用其他课题的成果。详见topic-template.md。

---

## 🔗 相关文档

### 核心文档
- [Agent身份和能力](AGENTS.md) - Research Agent核心定义
- [课题模板](research-topics/topic-template.md) - 完整的课题配置模板

### 方法论文档
- [SEARCH-R方法论](../../methodology/search-r-cycle.md) - 完整的7阶段研究循环
- [研究深度定义](../../methodology/research-depth.md) - Level 0-3深度标准
- [Human角色定义](../../methodology/human-role.md) - Human双重角色和参与最小化

### 工具和资源
- [项目初始化脚本](../../tools/init-research.sh) - 自动化创建工具
- [快速开始指南](../../QUICKSTART.md) - 详细的使用教程
- [研究实例](../../research-instances/README.md) - 使用SEARCH-R的研究案例

---

## 📝 版本历史

- **v2.0** (2026-03-13) - 重构优化
  - 明确两种使用场景
  - 提供最小化模板
  - 强调对话式创建
  - 简化流程和步骤
  - 添加使用示例和故障排除

- **v1.1** (2026-03-07) - 多课题管理支持
  - 分离研究主体和研究课题
  - 添加课题切换机制

- **v1.0** (2026-03-07) - 初始版本

---

**维护者**: SEARCH-R Framework  
**更新时间**: 2026-03-13  
**文档类型**: 初始化指南
