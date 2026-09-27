# ensemble 聚合检索器
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
  
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
load_dotenv()

sample_text = """
人工智能(AI)是计算机科学的一个分支，致力于创造能够模拟人类智能的系统。
人工智能的历史可以追溯到20世纪50年代，当时科学家们开始探索让计算机执行需要人类智能的任务。

人工智能主要分为弱人工智能和强人工智能。弱人工智能专注于特定任务，如语音识别、图像识别或下棋。
而强人工智能则具有通用智能，能够理解、学习并应用知识解决各种问题。

机器学习是人工智能的一个重要子领域，它使计算机能够从数据中学习而无需明确编程。
深度学习作为机器学习的一个分支，使用神经网络，特别是深度神经网络，来模拟人脑的学习方式。

自然语言处理(NLP)是人工智能的另一个重要领域，它使计算机能够理解、解释和生成人类语言。
计算机视觉则专注于使计算机能够从数字图像或视频中获取高层次的理解。

人工智能在医疗保健、金融、交通、教育和娱乐等多个领域都有广泛应用。
例如，在医疗保健中，AI可用于疾病诊断和药物研发；在交通领域，自动驾驶汽车是AI的一个重要应用。

然而，人工智能也带来了一些挑战和伦理问题，如工作岗位自动化、隐私问题、算法偏见和安全风险。
确保AI系统的透明度、问责制和公平性是当前AI研究的重要方向。

未来，人工智能有望继续发展，与其他技术如物联网、大数据和云计算相结合，创造更智能的系统和解决方案。
随着计算能力的提升和数据的增长，AI的潜力几乎是无限的。
"""

def get_docs(retriever_type)-> list[Document]:
    # 创建文档对象
    document_vector = Document(page_content=sample_text, metadata={"retriever": retriever_type})

    # 将文档放入列表中
    documents_vector = [document_vector]

    # 分割文档
    text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=5)
    return text_splitter.split_documents(documents_vector)

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

vectorstore = FAISS.from_documents(get_docs("vector_retriever"), embeddings)
vector_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

llm = ChatOpenAI(model="deepseek-v4-pro", temperature=0)
compressor = LLMChainExtractor.from_llm(llm)

vector_compression_retriever = ContextualCompressionRetriever(
    base_retriever=vector_retriever,
    base_compressor=compressor
)

bm25_retriever = BM25Retriever.from_documents(get_docs("bm25_retriever"))
bm25_retriever.k = 2

ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_compression_retriever, bm25_retriever],
    weights=[0.6, 0.4]
)

docs = ensemble_retriever.invoke("人工智能的主要应用领域有哪些？")
print(f"检索到 {len(docs)} 个相关文档:")
for i, doc in enumerate(docs):
    print(f"\n文档 {i+1}:")
    print(doc.page_content.strip()[:300] + "..." if len(doc.page_content) > 300 else doc.page_content.strip())
    print(f"元数据: {doc.metadata}")
    print("-------------------------")
