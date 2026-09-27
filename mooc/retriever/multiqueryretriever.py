from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_dir =  "../vector-store/chrome_bge"
# Chroma.from_documents(docs, embeddings,collection_name="laogu",persist_directory=persist_dir)
chroma_db = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="liudehua",
    collection_metadata={"hnsw:space": "cosine"}  # 修改为欧氏距离"l2"：欧氏距离（L2 范数）
                                                # "ip"：点积（Inner Product）
                                                # "cosine"：余弦相似度（默认，无需显式指定）
)

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("langchain_classic.retrievers.multi_query").setLevel(logging.INFO)

llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)
retriever = MultiQueryRetriever.from_llm(
    llm=llm,
    retriever=chroma_db.as_retriever(search_kwargs={"k": 2}),
)

query = "刘德华在电影《至尊无上》里是干什么？"
docs = retriever.invoke(query)

for doc in docs:
    print(doc.page_content)
    print("=====")
