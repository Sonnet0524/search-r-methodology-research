# SEARCH-R 模板仓库更新通知

**更新时间**: 2026-03-14  
**版本**: v2.1  
**重要程度**: ⚠️ 重要更新

---

## 📢 主要更新内容

### 1. Skills和Tools架构重构

SEARCH-R已完成Skills和Tools的架构重构，实现了清晰的关注点分离：

```
✅ 新架构
skills/                   # 业务能力（4个）
├── literature-review/
├── observation/
├── theory-building/
└── quality-gate/

tools/                    # 底层工具（8个）
├── baidu-search/
├── baidu-scholar-search/
├── baidu-baike-data/
├── paddleocr-async/
├── paddleocr-text-recognition/
├── paddleocr-doc-parsing/
├── file-reading/
└── document-output/
```

### 2. 工具状态透明化

所有工具都标记了清晰的状态：

- ✅ **已测试**（6个）：可直接使用
- ⚠️ **待测试**（2个）：需配置专属URL
- 🚧 **建设中**（2个）：脚本待实现

### 3. API Keys配置完善

新增完整的配置指南：

- `.env.example` - 配置模板
- `API_KEYS_SETUP.md` - 详细获取步骤
- 专属URL获取提醒

---

## ⚠️ 重要：需要采取的行动

### 立即行动

1. **更新Skills引用**
   - 检查所有Skills的SKILL.md
   - 区分Skills和Tools引用
   - 删除web-search引用（已删除）

2. **配置API Keys**
   - 配置BAIDU_API_KEY
   - 如需使用PaddleOCR同步API，配置专属URL

3. **更新opencode.json**
   - Skills列表只包含4个业务能力
   - 不包含Tools

### 可选行动

1. 测试PaddleOCR同步API工具
2. 实现file-reading和document-output脚本

---

## 📋 详细更新文档

所有详细更新文档已同步到：`sync-logs/`

| 文档 | 说明 |
|------|------|
| `sync-logs/REFACTOR_SUMMARY.md` | 重构完整总结 |
| `sync-logs/PROJECT_CHECK_REPORT.md` | 项目检查报告 |
| `sync-logs/SKILLS_TOOLS_UPDATE_SUMMARY.md` | Skills引用更新总结 |
| `sync-logs/README.md` | 同步日志索引 |

---

## 🔑 API Keys配置快速指南

### 必需配置

```bash
# 百度API Key（用于所有百度服务）
BAIDU_API_KEY=your_baidu_api_key_here
```

获取地址：https://aistudio.baidu.com/account/accessToken

### 可选配置（用于PaddleOCR同步API）

```bash
# OCR同步API专属URL
PADDLEOCR_OCR_API_URL=https://your-instance.aistudio-app.com/ocr
PADDLEOCR_DOC_PARSING_API_URL=https://your-instance.aistudio-app.com/layout-parsing
```

获取地址：https://aistudio.baidu.com/paddleocr/task

---

## 🔍 检查清单

### Skills引用更新

- [ ] literature-review/SKILL.md
- [ ] observation/SKILL.md
- [ ] theory-building/SKILL.md
- [ ] quality-gate/SKILL.md

### 配置更新

- [ ] opencode.json - 只保留skills配置
- [ ] .env文件 - 配置API Keys
- [ ] 验证配置 - 运行测试脚本

### 文档更新

- [ ] 更新README说明
- [ ] 同步.env.example模板
- [ ] 更新研究课题配置

---

## 🔗 相关资源

- [SEARCH-R仓库](../SEARCH-R) - 方法论模板仓库
- [同步日志](./sync-logs/README.md) - 详细同步内容
- [API Keys配置指南](../SEARCH-R/API_KEYS_SETUP.md) - 完整配置步骤

---

## 💡 需要帮助？

如果在同步过程中遇到问题：

1. 查看 `sync-logs/` 目录中的详细文档
2. 参考 SEARCH-R 仓库的 `API_KEYS_SETUP.md`
3. 检查 `.env.example` 配置模板

---

**通知者**: Research Agent  
**通知时间**: 2026-03-14
