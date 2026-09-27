import os
from pathlib import Path

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains.query_constructor.schema import AttributeInfo
from langchain_classic.retrievers.self_query.base import SelfQueryRetriever
from langchain_community.query_constructors.chroma import ChromaTranslator
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(
        page_content="一群科学家带回恐龙，混乱爆发",
        metadata={"year": 1993, "rating": 7.7, "genre": "科幻"},
    ),
    Document(
        page_content="里奥·迪卡普里奥迷失在梦中，在梦中迷失在梦里，在梦里迷失在。。。",
        metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},
    ),
    Document(
        page_content="一位心理学家/侦探在梦中的一系列梦中迷失了方向，《盗梦空间》再次使用了这个想法",
        metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6, "genre": "科幻"},
    ),
    Document(
        page_content="一群正常体型的女人非常健康，有些男人对她们很渴望",
        metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},
    ),
    Document(
        page_content="玩具活了过来，玩得很开心",
        metadata={"year": 1995, "genre": "动画","rating": 9.0,},
    ),
    Document(
        page_content="三个人走进禁区，三个人走出禁区",
        metadata={
            "year": 1979,
            "director": "Andrei Tarkovsky",
            "genre": "惊悚",
            "rating": 9.9,
        },
    ),
]
doc_ids = [f"movie-{i}" for i in range(len(docs))]

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_directory = Path(__file__).resolve().parents[1] / "vector-store" / "chroma_db_11"
collection_name = "movie_self_query_demo"

vectorstore = Chroma.from_documents(
    docs,
    embeddings=embeddings,
    ids=doc_ids,
    collection_name=collection_name,
    persist_directory=str(persist_directory),
)

metadata_field_info = [
    AttributeInfo(
        name="genre",
        description="电影的类型。[“科幻”、“喜剧”、“戏剧”、“惊悚”、“浪漫”、“动作”、“动画”]之一",
        type="string",
    ),
    AttributeInfo(
        name="year",
        description="电影上映的那一年",
        type="integer",
    ),
    AttributeInfo(
        name="director",
        description="电影导演的名字",
        type="string",
    ),
    AttributeInfo(
        name="rating", description="电影的评分为1-10", type="float"
    ),
]


retriever = SelfQueryRetriever.from_llm(
    llm= ChatOpenAI(model="deepseek-v4-pro", temperature=0),
    vectorstore=vectorstore,
    document_contents="电影的简介",
    metadata_field_info=metadata_field_info,
    structured_query_translator=ChromaTranslator(),
)

question = "给我推荐一个1971年之后但2005年之前的电影都是关于禁区的，最好是惊悚的"

docs = retriever.invoke(question)

for doc in docs:
    print(doc)
    print("==============")
