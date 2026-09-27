import os
# 上下问压缩检索
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever

from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_dir = "../vector-store/chrome_bge"

chroma_db = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="liudehua",
    collection_metadata={"hnsw:space": "cosine"}
)
llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

compressor = LLMChainExtractor.from_llm(llm)

retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=chroma_db.as_retriever())

comp_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)

docs = comp_retriever.invoke("刘德华是哪年出生的？")

if not docs:
    print("没有检索到满足相似度阈值的内容")

for doc in docs:
    print(doc)
    print("=====")
