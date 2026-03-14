# ClawHub 百度Skills研究报告

## 概述

本报告研究了ClawHub上的三个百度官方Skills，分析其功能、API接口和集成可行性。

---

## 📦 研究的Skills

### 1. baidu-search（百度搜索）✅
**ClawHub链接**: https://clawhub.ai/ide-rea/baidu-search
**下载量**: 36,000+（全球第一）

#### 功能
- 网络实时搜索
- 支持时效性过滤（pd/pw/pm/py）
- 支持时间范围过滤（YYYY-MM-DDtoYYYY-MM-DD）
- 返回结果数量控制（1-50条）

#### API
```
Endpoint: https://qianfan.baidubce.com/v2/ai_search/web_search
Method: POST
Auth: Bearer Token
```

#### 测试结果
✅ **测试成功** - 使用现有`BAIDU_AISEARCH_TOKEN`可正常调用

#### 参数
| 参数 | 类型 | 必需 | 默认 | 说明 |
|------|------|------|------|------|
| query | str | ✅ | - | 搜索关键词 |
| count | int | ❌ | 10 | 返回结果数（1-50） |
| freshness | str | ❌ | null | 时间过滤 |

#### Freshness格式
- `pd` - 过去24小时
- `pw` - 过去7天
- `pm` - 过去31天
- `py` - 过去365天
- `YYYY-MM-DDtoYYYY-MM-DD` - 自定义时间范围

#### 示例
```bash
export BAIDU_API_KEY="your_token"

python3 skills/baidu-search/scripts/search.py '{"query":"人工智能","count":10}'
```

---

### 2. baidu-scholar-search（百度学术搜索）🔬
**ClawHub链接**: https://clawhub.ai/ide-rea/baidu-scholar-search-skill

#### 功能
- 学术文献搜索（中英文）
- 支持期刊、会议、学位论文
- 可选返回摘要
- 分页支持

#### API
```
Endpoint: https://qianfan.baidubce.com/v2/tools/baidu_scholar/search
Method: GET
Auth: Bearer Token
```

#### 参数
| 参数 | 类型 | 必需 | 默认 | 说明 |
|------|------|------|------|------|
| wd | str | ✅ | - | 搜索关键词 |
| pageNum | int | ❌ | 0 | 页码（从0开始） |
| enable_abstract | bool | ❌ | false | 是否返回摘要 |

#### 返回字段
- `title` - 论文标题
- `abstract` - 摘要（需启用）
- `keyword` - 关键词
- `paperId` - 论文ID
- `publishYear` - 发表年份
- `url` - 百度学术链接

#### 特点
- **默认不返回摘要** - 快速响应
- **可选返回摘要** - 详细信息
- **支持中英文** - 双语搜索

#### 使用场景
- 快速浏览：不返回摘要
- 深入了解：返回摘要

#### 示例
```bash
export BAIDU_API_KEY="your_token"

python3 skills/baidu-scholar-search/scripts/search.py --keyword "机器学习" --page 0
```

---

### 3. baidu-baike-data（百度百科数据）📖
**ClawHub链接**: https://clawhub.ai/ide-rea/baidu-baike-data

#### 功能
- 查询百科词条
- 支持同名词条列表
- 支持词条ID查询
- 返回结构化数据

#### API
```
Base URL: https://appbuilder.baidu.com/v2/baike
Method: GET
Auth: Bearer Token
```

#### 三种查询方式

##### 1. 按标题查询
```bash
python3 scripts/baike.py --search_type=lemmaTitle --search_key="人工智能"
```

##### 2. 查询同名词条列表
```bash
python3 scripts/baike.py --search_type=lemmaList --search_key="苹果" --top_k=5
```

##### 3. 按词条ID查询
```bash
python3 scripts/baike.py --search_type=lemmaId --search_key="12345"
```

#### 返回字段
- 基本信息字段
- 结构化数据
- 已排除大字段（summary, abstract_html等）

#### 使用场景
- 直接查询：明确名词
- 同名词处理：多义项词条

---

## 🔑 环境变量配置

三个Skills共用同一个环境变量：`BAIDU_API_KEY`

### 获取方式
1. 访问百度千帆平台
2. 获取API Key
3. 设置环境变量

```bash
export BAIDU_API_KEY="your_baidu_api_key"
```

### 兼容性
✅ 可复用现有的 `BAIDU_AISEARCH_TOKEN`

---

## 📊 对比分析

| 特性 | baidu-search | baidu-scholar-search | baidu-baike-data |
|------|-------------|---------------------|-----------------|
| **用途** | 网络搜索 | 学术文献搜索 | 百科词条查询 |
| **数据源** | 全网网页 | 学术数据库 | 百度百科 |
| **时效性** | 实时 | 历史文献 | 相对稳定 |
| **深度** | 广度优先 | 深度优先 | 权威定义 |
| **速度** | 快 | 中等（带摘要慢） | 快 |
| **测试状态** | ✅ 通过 | ⚠️ 待验证 | ⚠️ 待验证 |

---

## 🔗 联动优势

三个Skills可以无缝协同：

```
用户问题
    ↓
baidu-baike-data (概念定义)
    ↓
baidu-scholar-search (学术支撑)
    ↓
baidu-search (最新动态)
```

**示例工作流**：
1. 先用百科获取基础概念
2. 再用学术搜索找论文支撑
3. 最后用网络搜索找最新进展

---

## 💡 集成建议

### 优先级
1. **baidu-search** - ✅ 已测试通过，优先集成
2. **baidu-scholar-search** - 研究课题必备
3. **baidu-baike-data** - 辅助工具

### 配置统一
建议统一使用 `BAIDU_API_KEY` 环境变量。

### 使用场景
- **一般搜索** → baidu-search
- **学术研究** → baidu-scholar-search
- **概念查询** → baidu-baike-data

---

## 📝 总结

1. **baidu-search** ✅
   - 全球下载量第一
   - 测试通过
   - 可立即使用

2. **baidu-scholar-search** 🔬
   - 学术研究利器
   - 支持中英文
   - 需要配置测试

3. **baidu-baike-data** 📖
   - 权威定义来源
   - 多义项处理
   - 需要配置测试

---

**研究日期**: 2026-03-13  
**研究方法**: ClawHub官方Skills分析  
**维护者**: SEARCH-R Framework
