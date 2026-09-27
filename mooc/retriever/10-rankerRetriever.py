
import os
from pathlib import Path
from typing import Callable, List

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from sentence_transformers import CrossEncoder

from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from pydantic import Field

os.environ["TOKENIZERS_PARALLELISM"] = "false"

embeddings_path =  "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_dir = Path(__file__).resolve().parents[1] / "vector-store" / "chrome_bge"
# Chroma.from_documents(docs, embeddings,collection_name="laogu",persist_directory=persist_dir)
vectorstore = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="liudehuaq",
    collection_metadata={"hnsw:space": "cosine"}  # 修改为欧氏距离"l2"：欧氏距离（L2 范数）
    # "ip"：点积（Inner Product）
    # "cosine"：余弦相似度（默认，无需显式指定）
)

base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

embeddings_path1 = "/Users/xiajiang/Desktop/huggingface/bge-reranker-base"
reranker_model = CrossEncoder(model_name_or_path=embeddings_path1)


class RerankerRetriever(BaseRetriever):
    base_retriever: BaseRetriever = Field(..., description="基础检索器")
    reranker_fn: Callable = Field(..., description="reranker模型，排序函数")

    def _get_relevant_documents(self, query: str) -> List[Document]:
        initial_docs = self.base_retriever.invoke(query)
        reranked_docs = self.reranker_fn(query, initial_docs)
        return reranked_docs


def rerank_docs(query, docs):
    # 准备查询-文档对
    query_doc_pairs = [(query, doc.page_content) for doc in docs]

    print(f"没有重排序前的文档:")
    for i, (q, content) in enumerate(query_doc_pairs):
        print(f"文档 {i + 1} 的内容: {content}")

    # 计算相关性分数
    scores = reranker_model.predict(query_doc_pairs)
    # 将分数与文档关联并排序
    print(f"利用排序模型 计算文档的相关性分数:")
    doc_score_pairs = list(zip(docs, scores))
    for i, (doc, score) in enumerate(doc_score_pairs):
        print(f"文档 {i + 1} 的相关性分数: {score}")
        doc.metadata["score"] = score

    for doc in docs:
        print(f"文档 {doc.metadata['score']} 的内容: {doc.page_content}")

    sorted_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    # 返回排序后的文档
    return [doc for doc, _ in sorted_pairs]


reranker_retriever = RerankerRetriever(base_retriever=base_retriever, reranker_fn=rerank_docs)

query = "刘德华曾经用过什么名字？"
ranker_docs = reranker_retriever.invoke(query)

# 打印结果
print("问题:", query)
print("\n使用的文档（经过重排序）:")


def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"文档 {i + 1}:" + d.page_content for i, d in enumerate(docs)]
        )
    )


pretty_print_docs(ranker_docs)
