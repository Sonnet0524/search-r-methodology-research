# Git 安全管理工具

## 概述

确保SEARCH-R仓库的所有Git操作都符合安全规范，防止敏感信息泄露。

---

## 快速使用

### 检查当前状态

```bash
python3 tools/git-management/scripts/git_safe.py check
```

### 安全提交

```bash
# 提交所有更改
python3 tools/git-management/scripts/git_safe.py commit -m "提交说明"

# 提交指定文件
python3 tools/git-management/scripts/git_safe.py commit --files "file1.md" "file2.md" -m "提交说明"
```

### 安全推送

```bash
# 推送到当前分支
python3 tools/git-management/scripts/git_safe.py push

# 推送到指定分支
python3 tools/git-management/scripts/git_safe.py push --branch main
```

---

## 工作流程

```
git add → 安全检查 → commit → 安全检查 → push → 简报
```

### Commit流程

1. 添加文件到暂存区
2. 扫描暂存文件
3. 检测敏感信息
4. 发现敏感信息 → 中止
5. 无敏感信息 → 执行commit

### Push流程

1. 检查.gitignore
2. 扫描待推送内容
3. 检测敏感信息
4. 发现敏感信息 → 中止
5. 无敏感信息 → 执行push
6. 生成推送简报

---

## 敏感信息检测

### 检测类型

- API Key (百度、通用)
- Token (PaddleOCR、BCE等)
- Password
- Secret Key
- 专属URL (aistudio-app.com等)
- Bearer Token

### 禁止提交的文件

- `.env` 及所有环境变量文件
- `credentials/`
- `secrets/`
- `*.pem`, `*.key`
- `id_rsa`

---

## 简报示例

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
- 变更文件: 5
- 总行数变更: +234

### 远程状态
- 远程仓库: origin/main
- 推送状态: 成功
```

---

## 集成到工作流

### 在AGENTS.md中使用

```markdown
## Git管理

每次更新仓库时必须使用git-management工具：

1. 检查: `python3 tools/git-management/scripts/git_safe.py check`
2. 提交: `python3 tools/git-management/scripts/git_safe.py commit -m "说明"`
3. 推送: `python3 tools/git-management/scripts/git_safe.py push`
```

---

**维护者**: SEARCH-R Framework  
**更新时间**: 2026-03-14
