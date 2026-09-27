from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

texts = [
    "篮球是一项很棒的运动。",
    "《Fly me to the moon》是我最喜欢的歌曲之一。",
    "凯尔特人队是我最喜欢的球队。",
    "这是一篇关于波士顿凯尔特人队的文档。",
    "我特别喜欢去看电影。",
    "波士顿凯尔特人队以20分的优势赢得了比赛。",
    "这只是一个随机文本。",
    "《艾尔登法环》是过去15年中最好的游戏之一。",
    "L·科内特是凯尔特人队最好的球员之一。",
    "拉里·伯德是一位标志性的NBA球员。"
]

retriever = InMemoryVectorStore.from_texts(texts, embedding=embeddings).as_retriever(
    search_kwargs={"k": 5}
)

query = "你能告诉我关于凯尔特人队的哪些信息？"

docs = retriever.invoke(query)
for doc in docs:
    print(f"- {doc}")

print("=" * 50)
from langchain_community.document_transformers import LongContextReorder

reorder = LongContextReorder()
reordered_docs = reorder.transform_documents(docs)

for doc in reordered_docs:
    print(f"-> {doc.page_content}")

print("=" * 50)

from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="deepseek-v4-pro", temperature=0)

prompt_template = """
Given these texts:
-----
{context}
-----
Please answer the following question:
{query}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "query"],
)

# Create and invoke the chain:
chain = create_stuff_documents_chain(llm, prompt)
response = chain.invoke({"context": reordered_docs, "query": query})
print(response)