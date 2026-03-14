# 百度API测试报告

## 测试时间
2026-03-13

## 环境配置
```bash
# .env 文件（请在自己的环境中配置）
BAIDU_API_KEY=<your_baidu_api_key>
PADDLEOCR_ACCESS_TOKEN=<your_paddleocr_token>
```

---

## 测试结果总览

| API | 状态 | 说明 |
|-----|------|------|
| baidu-search | ✅ 通过 | 网络搜索正常工作 |
| baidu-scholar-search | ✅ 通过 | 学术搜索正常工作（已修复） |
| baidu-baike-data | ✅ 通过 | 百科查询正常工作 |

---

## 详细测试

### 1. baidu-search（百度搜索）✅

**测试命令**:
```bash
python3 skills/baidu-search/scripts/search.py '{"query":"AI","count":2}'
```

**测试结果**:
```json
[
  {
    "id": 1,
    "url": "https://baijiahao.baidu.com/s?id=1859548976874012994",
    "title": "机器狗、烹饪助手……这个展会上AI无处不在",
    "date": "2026-03-13 20:13:48",
    "content": "2026年3月12日,2026中国家电及消费电子博览会在上海开幕...",
    "website": "百家号"
  }
]
```

**状态**: ✅ 成功

---

### 2. baidu-scholar-search（百度学术搜索）✅

**问题**: 最初报错"API error: Success"
**原因**: API返回的code字段是字符串"0"，不是整数0
**修复**: 修改判断条件为 `result["code"] not in ["0", 0]`

**测试命令**:
```bash
python3 skills/baidu-scholar-search/scripts/search.py --keyword "深度学习"
```

**测试结果**:
```json
[
  {
    "title": "深度学习研究进展",
    "publishYear": 2014,
    "publishInfo": {
      "journalName": "计算机应用研究"
    },
    "keyword": "深度学习；神经网络；模型；表示；堆栈；预训练",
    "abstract": "鉴于深度学习的重要性,综述了深度学习的研究进展..."
  }
]
```

**状态**: ✅ 成功

---

### 3. baidu-baike-data（百度百科）✅

**测试命令**:
```bash
python3 skills/baidu-baike-data/scripts/baike.py \
  --search_type=lemmaTitle \
  --search_key="人工智能"
```

**测试结果**:
```json
{
  "lemma_id": 9180,
  "lemma_title": "人工智能",
  "lemma_desc": "智能科学与技术专业术语",
  "url": "https://baike.baidu.com/item/人工智能/9180",
  "abstract_plain": "人工智能（Artificial Intelligence），英文缩写为AI...",
  "card": [
    {
      "name": "中文名",
      "value": ["人工智能"]
    },
    {
      "name": "外文名",
      "value": ["Artificial Intelligence（AI）"]
    },
    {
      "name": "提出时间",
      "value": ["1956年"]
    }
  ]
}
```

**状态**: ✅ 成功

---

## 修复记录

### baidu-scholar-search 修复

**文件**: `skills/baidu-scholar-search/scripts/search.py`

**修改前**:
```python
if "code" in result and result["code"] != 0:
    raise RuntimeError(f"API error: {result.get('message', 'Unknown error')}")
```

**修改后**:
```python
# 检查错误（百度API返回code字段，可能是字符串"0"或整数0）
if "code" in result and result["code"] not in ["0", 0]:
    raise RuntimeError(f"API error: {result.get('message', 'Unknown error')}")
```

---

## 使用示例

### 百度搜索
```bash
# 基本搜索
python3 skills/baidu-search/scripts/search.py '{"query":"人工智能"}'

# 限制结果数量
python3 skills/baidu-search/scripts/search.py '{"query":"AI","count":20}'

# 时间过滤（过去7天）
python3 skills/baidu-search/scripts/search.py '{"query":"最新新闻","freshness":"pw"}'
```

### 百度学术搜索
```bash
# 基本搜索
python3 skills/baidu-scholar-search/scripts/search.py --keyword "机器学习"

# 包含摘要
python3 skills/baidu-scholar-search/scripts/search.py --keyword "深度学习" --abstract

# 分页搜索
python3 skills/baidu-scholar-search/scripts/search.py --keyword "AI" --page 1
```

### 百度百科
```bash
# 按标题查询
python3 skills/baidu-baike-data/scripts/baike.py \
  --search_type=lemmaTitle \
  --search_key="人工智能"

# 查询同名词条列表
python3 skills/baidu-baike-data/scripts/baike.py \
  --search_type=lemmaList \
  --search_key="苹果" \
  --top_k=5
```

---

## 环境变量使用

所有百度API共用同一个环境变量 `BAIDU_API_KEY`:

```bash
# 加载环境变量
export $(cat .env | grep -v '^#' | xargs)

# 或者直接设置
export BAIDU_API_KEY="bce-v3/ALTAK-..."
```

---

## 结论

✅ 所有三个百度API均测试通过
✅ 环境变量配置正确
✅ 可以正常使用

---

**测试人员**: SEARCH-R Framework  
**测试日期**: 2026-03-13
