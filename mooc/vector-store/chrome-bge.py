from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma


path = "/Users/xiajiang/Desktop/test/mooc/loader/text/"

loader = TextLoader(file_path=path+"example.txt",encoding="utf-8")

documents = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=15,
    chunk_overlap=0,
)

docs = text_splitter.split_documents(documents)
persist_dir = "chrome_bge"

embeddings = HuggingFaceEmbeddings(model_name="/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5")

db = Chroma.from_documents(docs, embeddings,persist_directory=persist_dir)

