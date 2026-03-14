# PaddleOCR Skills 配置指南

## 概述

已成功集成Bobholamovic开发的2个PaddleOCR Skills到SEARCH-R框架。

---

## 📦 已集成的Skills

### 1. paddleocr-doc-parsing（文档解析）

**功能**: 高级文档解析，支持表格、公式、图表、多列布局

**适用场景**:
- 发票、财务报表
- 学术论文（含公式）
- 多列报纸/杂志
- 复杂结构文档

### 2. paddleocr-text-recognition（文本识别）

**功能**: 图像/PDF文字识别

**适用场景**:
- 截图、照片、扫描件
- 发票、收据、表单
- 文档图像

---

## 🔑 API配置（官方免费服务）

### 官方API信息

**✅ PaddleOCR提供官方API服务，限时免费！**

**获取方式**:
1. 访问 https://aistudio.baidu.com/paddleocr/task
2. 注册/登录百度账号
3. 获取API URL和Access Token

### 环境变量设置

在您的环境（`.env`文件或系统环境变量）中设置：

#### 异步API（推荐）

```bash
# 访问令牌（从官网获取）
PADDLEOCR_ACCESS_TOKEN=your_access_token_here

# 异步API URL - 支持大文件（PDF最多1000页）
PADDLEOCR_ASYNC_API_URL=https://paddleocr.aistudio-app.com/api/v2/ocr/jobs

# 可选：超时时间（秒）
PADDLEOCR_OCR_TIMEOUT=120
PADDLEOCR_DOC_PARSING_TIMEOUT=600
```

**注意**: 官方目前主要提供异步API，同步API可能不可用。

#### 支持的模型

异步API支持以下模型：
- `PP-OCRv5` - 文本识别
- `PaddleOCR-VL-1.5` - 文档解析（推荐）
- `PaddleOCR-VL` - 文档解析
- `PP-StructureV3` - 复杂文档解析

---

## 📦 支持的模型

| 模型 | 用途 | 特点 |
|------|------|------|
| **PaddleOCR-VL-1.5** | 文档解析 | 最新版，支持109种语言 |
| **PaddleOCR-VL** | 文档解析 | 支持表格、公式、图表 |
| **PP-OCRv5** | 文本识别 | 支持5种文字类型 |
| **PP-StructureV3** | 复杂文档解析 | 保持文档版式 |

---

## 🚀 使用示例

### 文档解析

```bash
# 从本地文件解析
python skills/paddleocr-doc-parsing/scripts/vl_caller.py \
  --file-path "./document.pdf" \
  --pretty

# 从URL解析
python skills/paddleocr-doc-parsing/scripts/vl_caller.py \
  --file-url "https://example.com/paper.pdf" \
  --pretty
```

### 文本识别

```bash
# 从本地图像识别
python skills/paddleocr-text-recognition/scripts/ocr_caller.py \
  --file-path "./image.jpg" \
  --pretty

# 从URL识别
python skills/paddleocr-text-recognition/scripts/ocr_caller.py \
  --file-url "https://example.com/invoice.jpg" \
  --pretty
```

---

## ⚙️ 依赖安装

```bash
# 安装依赖
pip install httpx python-dotenv requests
```

---

## 🔧 测试配置

运行烟雾测试验证配置：

```bash
# 测试文档解析
python skills/paddleocr-doc-parsing/scripts/smoke_test.py

# 测试文本识别
python skills/paddleocr-text-recognition/scripts/smoke_test.py
```

---

## 🆓 免费额度说明

根据官方信息：
- **MCP调用接口**：限时免费
- **API在线服务**：限时免费

建议尽快注册使用！

---

## 📚 官方资源

- **PaddleOCR官网**: https://aistudio.baidu.com/paddleocr
- **获取Token**: https://aistudio.baidu.com/paddleocr/task
- **API文档**: https://ai.baidu.com/ai-doc/AISTUDIO/Kmfl2ycs0
- **GitHub**: https://github.com/PaddlePaddle/PaddleOCR
- **输出格式说明**: `paddleocr-doc-parsing/references/output_schema.md`

---

## ⚠️ 注意事项

1. **API配额**: 注意API调用次数限制
2. **文件大小**: PDF最多100页（同步）/ 1000页（异步），文件大小限制50MB-200MB
3. **超时设置**: 文档解析建议设置较长超时时间（默认10分钟）
4. **安全性**: 不要在代码中硬编码Token，使用环境变量

---

## 🔄 API类型说明

### 同步API（适合小文件）
- 快速响应
- PDF最多100页
- 适合实时处理

### 异步API（适合大文件）
- 支持大文件（PDF最多1000页）
- 支持URL上传（最大200MB）
- 需要轮询获取结果

---

**来源**: Bobholamovic (Lin Manhui) @ Baidu  
**官方API**: https://aistudio.baidu.com/paddleocr/task  
**集成日期**: 2026-03-13  
**维护者**: SEARCH-R Framework
