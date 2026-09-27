# retriever 目录文件说明

本文档说明 `/Users/xiajiang/Desktop/test/mooc/retriever` 目录下各个 Python 文件的主要用途。这个目录整体是在演示 LangChain 中不同类型的 Retriever 用法，包括基础向量检索、相似度阈值检索、多查询检索、上下文压缩、混合检索、自查询检索、长上下文重排和 reranker 重排序。

## 目录整体主题

这个目录的核心内容是“检索增强生成（RAG）中的检索阶段”。代码大多围绕以下组件展开：

- `HuggingFaceEmbeddings`：使用本地 `/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5` 向量模型生成文本向量。
- `Chroma` / `FAISS` / `InMemoryVectorStore`：不同的向量数据库或内存向量存储。
- `as_retriever()`：把向量库包装成 LangChain 的检索器。
- `ChatOpenAI(model="deepseek-v4-pro")`：用于多查询改写、自查询解析、LLM 文档压缩等场景。
- `ContextualCompressionRetriever`：先检索，再按问题压缩或重排结果。
- `EnsembleRetriever`：组合多个检索器的结果。
- `CrossEncoder` / `CrossEncoderReranker`：使用 reranker 模型对初检结果重新排序。

## 文件说明

### `base.py`

演示最基础的 Chroma 向量检索流程。

主要流程：

1. 使用 `TextLoader` 读取 `loader/text/刘德华.txt`。
2. 使用 `CharacterTextSplitter` 按换行分割文档，`chunk_size=100`，无重叠。
3. 使用本地 `bge-large-zh-v1.5` 生成 embedding。
4. 连接到 Chroma 持久化目录 `../vector-store/chrome_bge`，集合名是 `liudehuaq`。
5. 把 Chroma 转为 retriever。
6. 查询“刘德华的曾用名是什么？”并打印检索到的文档片段。

这个文件主要讲的是：如何从文本加载、切分、向量化，并通过 Chroma 做基础相似度检索。

### `04-retriver-score.py`

演示带相似度分数阈值的检索。

主要流程：

1. 加载本地 embedding 模型。
2. 连接 Chroma 持久化目录 `../vector-store/chrome_bge`，集合名是 `liudehua`。
3. 使用 `as_retriever(search_type="similarity_score_threshold")`。
4. 设置 `score_threshold=0.5`，只返回相似度达到阈值的文档。
5. 查询“刘德华哪年出生？请用5个字回答”。

这个文件主要讲的是：如何通过相似度阈值过滤低相关文档，避免检索结果中混入太弱的匹配内容。

### `05-ensembleRetriever.py`

演示 `EnsembleRetriever` 聚合多个向量检索器。

主要流程：

1. 准备两组关于苹果、橘子的短文本。
2. 分别构建两个 Chroma 向量库，持久化到 `chroma_db_1` 和 `chroma_db_2`。
3. 每个 Chroma 都转成 retriever，且各自只返回 `k=1` 条结果。
4. 使用 `EnsembleRetriever` 把两个 retriever 合并，权重都是 `0.5`。
5. 查询“谁喜欢橘子？”。

这个文件主要讲的是：如何把多个来源或多个索引的检索结果合并起来，形成一个统一检索器。

### `06-ensembleRetriever.py`

演示更复杂的混合检索：向量检索 + LLM 上下文压缩 + BM25 关键词检索 + 集成排序。

主要流程：

1. 准备一段关于人工智能的长文本。
2. 用 `CharacterTextSplitter` 把文本切成小块。
3. 构建 FAISS 向量检索器，返回 `k=2`。
4. 使用 `LLMChainExtractor` 创建 LLM 文档压缩器。
5. 使用 `ContextualCompressionRetriever` 包装向量检索器，使其返回和问题更直接相关的内容。
6. 同一批文档再创建 BM25 检索器，返回 `k=2`。
7. 使用 `EnsembleRetriever` 按 `0.6` 和 `0.4` 权重组合压缩后的向量检索与 BM25 检索。
8. 查询“人工智能的主要应用领域有哪些？”。

这个文件主要讲的是：如何把语义检索和关键词检索结合起来，并用 LLM 对向量检索结果做上下文压缩，提高检索结果的可用性。

### `07-longcontextReorder.py`

演示长上下文重排 `LongContextReorder`。

主要流程：

1. 准备一批关于篮球、凯尔特人队、歌曲、电影、游戏等短文本。
2. 使用 `InMemoryVectorStore` 构建内存向量库。
3. 查询“你能告诉我关于凯尔特人队的哪些信息？”，取前 `k=5` 条。
4. 使用 `LongContextReorder` 对检索结果重新排序。
5. 把重排后的文档塞进 `create_stuff_documents_chain`，让 LLM 基于上下文回答问题。

这个文件主要讲的是：当检索结果较多、上下文较长时，如何调整文档顺序，减少模型忽略中间内容的问题。

### `08-selfretriever.py`

演示手动 metadata filter 检索。

主要流程：

1. 构造一批电影简介文档，每条文档带有 `year`、`rating`、`genre`、`director` 等元数据。
2. 使用 Chroma 建立向量库，持久化到 `../vector-store/chroma_db_9`。
3. 手动构造过滤条件：
   - `genre` 等于 `科幻`
   - `rating` 大于 `8.0`
4. 通过 `as_retriever(search_kwargs={"filter": filter_condition, "k": 3})` 执行带过滤条件的检索。
5. 查询“请帮我推荐一些科幻类的电影”。

这个文件主要讲的是：如何在向量相似度检索之外，再使用结构化元数据条件过滤文档。

### `09-selfretriever.py`

演示真正的 Self Query Retriever：让 LLM 从自然语言问题中自动提取检索条件。

主要流程：

1. 构造一批带元数据的电影文档。
2. 使用 Chroma 建立向量库，集合名为 `movie_self_query_demo`。
3. 定义 `metadata_field_info`，告诉 LLM 支持哪些元数据字段：
   - `genre`
   - `year`
   - `director`
   - `rating`
4. 使用 `SelfQueryRetriever.from_llm()` 创建自查询检索器。
5. 使用 `ChromaTranslator()` 把 LLM 生成的结构化查询翻译成 Chroma 可执行的过滤条件。
6. 查询“给我推荐一个1971年之后但2005年之前的电影都是关于禁区的，最好是惊悚的”。

这个文件主要讲的是：如何让用户用自然语言表达筛选条件，由 LLM 自动转成向量数据库支持的 metadata filter。

### `10-rankerRetriever.py`

演示手写一个 reranker retriever。

主要流程：

1. 连接已有 Chroma 向量库 `../vector-store/chrome_bge`，集合名是 `liudehuaq`。
2. 基础检索器先取 `k=5` 条候选文档。
3. 加载本地 reranker 模型 `/Users/xiajiang/Desktop/huggingface/bge-reranker-base`。
4. 自定义 `RerankerRetriever`，继承 `BaseRetriever`。
5. 在 `_get_relevant_documents()` 中先调用基础检索器，再调用 `rerank_docs()` 重排序。
6. `rerank_docs()` 把 query 和每个候选文档组成文本对，用 `CrossEncoder.predict()` 打分。
7. 按 reranker 分数从高到低排序，并把分数写入 `doc.metadata["score"]`。
8. 查询“刘德华曾经用过什么名字？”。

这个文件主要讲的是：如何自己封装一个“先召回、再重排”的 Retriever。

### `11-rankerRetriever.py`

演示使用 LangChain 内置的 reranker 压缩器完成重排序。

主要流程：

1. 连接已有 Chroma 向量库 `../vector-store/chrome_bge`，集合名是 `liudehuaq`。
2. 基础检索器先取 `k=5` 条候选文档。
3. 加载本地 `bge-reranker-base`，通过 `HuggingFaceCrossEncoder` 包装。
4. 使用 `CrossEncoderReranker(model=cross_encoder_model, top_n=5)` 创建 reranker compressor。
5. 使用 `ContextualCompressionRetriever` 把基础检索器和 reranker compressor 组合起来。
6. 查询“刘德华曾经用过什么名字？”并输出重排序后的结果。

这个文件主要讲的是：不用手写 `BaseRetriever`，直接使用 LangChain 的 `CrossEncoderReranker` 和 `ContextualCompressionRetriever` 来实现重排序。

### `contextcompressionRetriever.py`

演示 LLM 上下文压缩检索。

主要流程：

1. 连接 Chroma 向量库 `../vector-store/chrome_bge`，集合名是 `liudehua`。
2. 创建 `ChatOpenAI(model="deepseek-v4-pro")`。
3. 使用 `LLMChainExtractor.from_llm(llm)` 创建基于 LLM 的文档内容抽取器。
4. 使用 `ContextualCompressionRetriever` 包装 Chroma retriever。
5. 代码里又把已经压缩过的 retriever 再包了一层 `ContextualCompressionRetriever`。
6. 查询“刘德华是哪年出生的？”。

这个文件主要讲的是：先检索相关文档，再让 LLM 从文档中抽取和问题直接相关的片段，减少传给最终回答模型的无关上下文。

### `multiqueryretriever.py`

演示 `MultiQueryRetriever` 多查询改写检索。

主要流程：

1. 连接 Chroma 向量库 `../vector-store/chrome_bge`，集合名是 `liudehua`。
2. 打开 `langchain_classic.retrievers.multi_query` 的 INFO 日志，便于观察 LLM 生成了哪些改写查询。
3. 使用 `ChatOpenAI(model="deepseek-v4-pro")`。
4. 通过 `MultiQueryRetriever.from_llm()` 包装基础 Chroma retriever。
5. 基础 retriever 每个改写查询取 `k=2` 条。
6. 查询“刘德华在电影《至尊无上》里是干什么？”。

这个文件主要讲的是：让 LLM 从一个用户问题生成多个不同表述的检索 query，从多个语义角度召回文档，提高召回率。

## 学习顺序建议

建议按下面顺序阅读：

1. `base.py`：先理解基础向量检索。
2. `04-retriver-score.py`：理解相似度阈值过滤。
3. `multiqueryretriever.py`：理解用 LLM 改写多个 query 提高召回。
4. `contextcompressionRetriever.py`：理解检索后压缩。
5. `05-ensembleRetriever.py`：理解多个检索器如何聚合。
6. `06-ensembleRetriever.py`：理解 BM25、向量检索、压缩检索的混合使用。
7. `08-selfretriever.py`：理解手动 metadata filter。
8. `09-selfretriever.py`：理解 LLM 自动生成 metadata filter。
9. `07-longcontextReorder.py`：理解长上下文下的文档重排。
10. `10-rankerRetriever.py`：理解手写 reranker retriever。
11. `11-rankerRetriever.py`：理解 LangChain 内置 reranker 方案。

## 主要技术点对照

| 技术点 | 对应文件 |
| --- | --- |
| 基础 Chroma 向量检索 | `base.py` |
| 相似度阈值检索 | `04-retriver-score.py` |
| 多查询改写检索 | `multiqueryretriever.py` |
| LLM 上下文压缩 | `contextcompressionRetriever.py`, `06-ensembleRetriever.py` |
| 聚合检索器 | `05-ensembleRetriever.py`, `06-ensembleRetriever.py` |
| BM25 关键词检索 | `06-ensembleRetriever.py` |
| 长上下文重排 | `07-longcontextReorder.py` |
| 手动 metadata filter | `08-selfretriever.py` |
| Self Query Retriever | `09-selfretriever.py` |
| 手写 reranker | `10-rankerRetriever.py` |
| LangChain 内置 reranker | `11-rankerRetriever.py` |

## 注意事项

- 多数脚本依赖本地 Hugging Face 模型路径：
  - `/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5`
  - `/Users/xiajiang/Desktop/huggingface/bge-reranker-base`
- 使用 `ChatOpenAI(model="deepseek-v4-pro")` 的脚本需要 `.env` 中配置可用的 API Key 和相关 OpenAI 兼容接口环境变量。
- 多个脚本依赖已有的 Chroma 持久化目录，例如 `../vector-store/chrome_bge`。
- `base.py` 中创建集合名是 `liudehuaq`，部分文件使用 `liudehua`，运行前需要确认对应集合中确实已有数据。
- `contextcompressionRetriever.py` 中连续包了两层 `ContextualCompressionRetriever`，从教学角度可以看到压缩器可组合，但实际项目里通常一层就够。
