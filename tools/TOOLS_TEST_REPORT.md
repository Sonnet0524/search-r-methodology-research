# 工具测试报告

## 测试时间
2026-03-13

---

## 测试结果总览

| 工具 | 状态 | 说明 |
|------|:----:|------|
| baidu-search | ✅ 通过 | 百度AI搜索正常 |
| baidu-scholar-search | ✅ 通过 | 百度学术搜索正常 |
| baidu-baike-data | ✅ 通过 | 百度百科 词条查询正常 |
| paddleocr-async | ✅ 通过 | PaddleOCR异步API正常 |
| paddleocr-text-recognition | ✅ 通过 | PaddleOCR同步API正常 |
| paddleocr-doc-parsing | ⚠️ 需指定文件类型 | 同步API可用，需指定file-type |
| file-reading | 🚧 设计中 | 无脚本实现 |
| document-output | 🚧 设计中 | 无脚本实现 |

---

## 关键发现

### 同步API vs 异步API

| 特性 | 同步API | 异步API |
|------|---------|---------|
| **URL来源** | 用户专属任务页面 | 公共URL |
| **响应方式** | 直接返回结果 | 返回jobId，需轮询 |
| **超时风险** | 较高（大文件） | 低 |
| **适用场景** | 小文件、快速响应 | 大文件、批量处理 |

### API URL配置

**重要**: 同步API需要用户专属URL，需从以下页面获取：
https://aistudio.baidu.com/paddleocr/task

---

## 详细测试

### 1. paddleocr-text-recognition ✅

**测试命令**:
```bash
python3 tools/paddleocr-text-recognition/scripts/ocr_caller.py \
  --file-path "/tmp/test_ocr.png" --stdout --pretty
```

**结果**: 
```
状态: ✅ 成功
识别文字: HelloPaddleOCR API Test
```

---

### 2. paddleocr-doc-parsing ⚠️

**测试命令**:
```bash
python3 tools/paddleocr-doc-parsing/scripts/vl_caller.py \
  --file-path "document.pdf" --file-type 0 --stdout --pretty
```

**注意事项**:
- 需要指定 `--file-type` 参数（0=PDF, 1=图像）
- 超时时间默认600秒，大文件可能需要更长

---

## 可用工具（6个）

| 工具 | 功能 | API类型 |
|------|------|---------|
| baidu-search | 网络搜索 | - |
| baidu-scholar-search | 学术搜索 | - |
| baidu-baike-data | 百科查询 | - |
| paddleocr-async | OCR/文档解析 | 异步 |
| paddleocr-text-recognition | OCR识别 | 同步 |
| paddleocr-doc-parsing | 文档解析 | 同步 |

---

## 环境变量配置

```bash
# .env 文件（已在.gitignore中，不会被提交）

# 百度API Key
BAIDU_API_KEY=bce-v3/ALTAK-...

# PaddleOCR Token
PADDLEOCR_ACCESS_TOKEN=de89a11f...

# PaddleOCR 同步API（用户专属URL，需从任务页面获取）
PADDLEOCR_OCR_API_URL=https://xxx.aistudio-app.com/ocr
PADDLEOCR_DOC_PARSING_API_URL=https://xxx.aistudio-app.com/layout-parsing

# PaddleOCR 异步API（公共URL）
PADDLEOCR_ASYNC_API_URL=https://paddleocr.aistudio-app.com/api/v2/ocr/jobs
```

---

**测试人员**: SEARCH-R Framework  
**测试日期**: 2026-03-13
