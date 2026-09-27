


from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

path = "/Users/xiajiang/Desktop/test/mooc/loader/text/"

loader = TextLoader(file_path= path + "刘德华.txt",encoding="utf-8")

documents = loader.load()


text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=0
)

docs = text_splitter.split_documents(documents)

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_dir =  "../vector-store/chrome_bge"
# # Chroma.from_documents(docs, embeddings,collection_name="laogu",persist_directory=persist_dir)
chroma_db = Chroma(
    persist_directory=persist_dir,
    embedding_function=embeddings,
    collection_name="liudehuaq",
    collection_metadata={"hnsw:space": "cosine"}  # 修改为欧氏距离"l2"：欧氏距离（L2 范数）
                                                # "ip"：点积（Inner Product）
                                             # "cosine"：余弦相似度（默认，无需显式指定）
)
# chroma_db.add_documents(docs)

retriever = chroma_db.as_retriever()

docs = retriever.invoke("刘德华的曾用名是什么？")

for doc in docs:
    print(doc.page_content)
    print("=====")

