
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever


embeddings_path =  "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_dir = Path(__file__).resolve().parents[1] / "vector-store" / "chrome_bge"

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
cross_encoder_model = HuggingFaceCrossEncoder(model_name=embeddings_path1)

reranker_compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=5)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker_compressor,
    base_retriever=base_retriever
)

query = "刘德华曾经用过什么名字？"

ranker_docs = compression_retriever.invoke(query)

# 10. 输出结果
print(f"查询: {query}")
print("重排序后的结果:")

def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"文档 {i+1}:" + d.page_content for i, d in enumerate(docs)]
        )
    )

pretty_print_docs(ranker_docs)
