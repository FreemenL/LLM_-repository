from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5")
persist_dir = "chrome_bge"

chroma_db = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="langchain",
    collection_metadata={"hnsw:space": "cosine"}
)


query = "怎么理解langchain？"

docs = chroma_db.similarity_search(query, k=2)
 
for doc in docs:
    print(doc.page_content)
    print("=====")

print("==========================")
#
docs_score = chroma_db.similarity_search_with_relevance_scores(query, k=2)
#
for doc, score in docs_score:
    print(f"内容：{doc.page_content}---->相似度分:{score:.2f}")
    print("=====")