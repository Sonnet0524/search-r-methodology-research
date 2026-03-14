---
name: git-management
description: 仓库Git安全管理技能。确保所有提交和推送都经过敏感信息审查。当需要进行git commit或push操作时触发。
trigger: on_demand
tags: git, 安全, 提交管理, 敏感信息审查
---

# Git 安全管理技能

## 概述

本技能确保SEARCH-R仓库的所有Git操作都符合安全规范，防止敏感信息泄露。

---

## ⛔ 强制规则

### 1. 关键更新必须Commit和Push

以下情况**必须**执行commit和push：
- 新增或修改核心配置文件
- 新增或修改技能(Skills)
- 新增或修改工具(Tools)
- 修复重要bug
- 完成重要功能开发

### 2. 禁止提交的内容

**绝对禁止提交以下内容**：
- `.env` 文件及所有环境变量文件
- 包含API Key、Token、密码的文件
- 包含用户专属URL的文件
- 临时文件、日志文件
- IDE配置文件

### 3. 推送前必须检查

每次push前必须完成：
1. 检查`.gitignore`是否包含敏感文件
2. 扫描暂存区是否有敏感信息
3. 确认没有遗漏的敏感信息

---

## 🔄 工作流程

### 标准Commit流程

```
1. git add <files>
      ↓
2. 安全审查（自动扫描）
      ↓
3. 发现敏感信息？
   ├── 是 → 中止，提示修改
   └── 否 → 继续
      ↓
4. git commit -m "message"
      ↓
5. 记录提交日志
```

### 标准Push流程

```
1. 检查.gitignore
      ↓
2. 扫描所有待推送内容
      ↓
3. 发现敏感信息？
   ├── 是 → 中止，提示修改
   └── 否 → 继续
      ↓
4. git push
      ↓
5. 生成推送简报
```

---

## 📋 使用方法

### 提交更改

```bash
# 方式1：使用脚本（推荐）
python3 tools/git-management/scripts/git_safe.py commit -m "提交说明"

# 方式2：手动执行
python3 tools/git-management/scripts/git_safe.py commit --files "file1.md" "file2.md" -m "提交说明"
```

### 推送更改

```bash
# 推送到远程仓库
python3 tools/git-management/scripts/git_safe.py push

# 推送到指定分支
python3 tools/git-management/scripts/git_safe.py push --branch main
```

### 安全检查

```bash
# 检查当前暂存区
python3 tools/git-management/scripts/git_safe.py check

# 检查指定文件
python3 tools/git-management/scripts/git_safe.py check --files ".env" "config.json"
```

### 查看简报

```bash
# 查看最近一次推送简报
python3 tools/git-management/scripts/git_safe.py report
```

---

## 🔍 敏感信息检测规则

### 检测模式

| 类型 | 正则表达式 | 示例 |
|------|-----------|------|
| **API Key** | `[Aa][Pp][Ii][_\-]?[Kk][Ee][Yy].*=.*['\"]?[\w\-]{20,}` | `API_KEY="sk-xxx"` |
| **Token** | `[Tt][Oo][Kk][Ee][Nn].*=.*['\"]?[\w\-]{20,}` | `TOKEN=abc123...` |
| **密码** | `[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd].*=.*['\"]?.+` | `PASSWORD=secret` |
| **专属URL** | `https?://[a-z0-9\-]+\.(aistudio-app|bce|baidu)\.com` | `https://xxx.aistudio-app.com` |
| **Bearer Token** | `Bearer\s+[\w\-\.]{20,}` | `Bearer xxx.xxx` |
| **Base64 Key** | `[A-Za-z0-9+/]{40,}={0,2}` | 长Base64字符串 |

### 白名单文件

以下文件路径允许包含敏感信息模式（但不应提交）：
- `.env*`
- `*.local`
- `secrets/`
- `credentials/`

---

## 📊 简报格式

```markdown
## Git 推送简报

**推送时间**: 2026-03-14 12:00:00
**分支**: main
**提交数量**: 3

### 提交内容
1. [abc1234] 新增git-management技能
2. [def5678] 更新AGENTS.md
3. [ghi9012] 修复bug

### 安全检查
- ✅ .gitignore检查通过
- ✅ 敏感信息扫描通过
- ✅ 无禁止提交的文件

### 统计
- 新增文件: 5
- 修改文件: 3
- 删除文件: 0
- 总行数变更: +234

### 远程状态
- 远程仓库: origin/main
- 推送状态: 成功
```

---

## ⚠️ 错误处理

### 发现敏感信息时

```
❌ 安全检查失败！

发现以下敏感信息：

文件: .env
行号: 8
类型: Token
内容: PADDLEOCR_ACCESS_TOKEN=de89a11f...

建议操作：
1. 移除敏感信息
2. 将文件添加到.gitignore
3. 重新提交
```

### .gitignore缺失时

```
❌ .gitignore检查失败！

以下敏感文件未被忽略：
- .env
- credentials.json

建议操作：
1. 将上述文件添加到.gitignore
2. 如果已提交，使用git rm --cached移除
```

---

## 📚 参考

- [Git安全最佳实践](references/git-security.md)
- [敏感信息管理](references/sensitive-data.md)

---

**版本**: 1.0  
**创建日期**: 2026-03-14  
**维护者**: SEARCH-R Framework
