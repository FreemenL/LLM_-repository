from langchain_huggingface import HuggingFaceEmbeddings
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

retriever = chroma_db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={'score_threshold':0.5}
)

docs = retriever.invoke("刘德华哪年出生？请用5个字回答")

for doc in docs:
    print(doc)
    print("=====")