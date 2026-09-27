from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
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

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

persist_directory = "../vector-store/chroma_db_9"  # 数据库存储的目录

vectorstore = Chroma.from_documents(docs, embeddings, persist_directory = persist_directory)

question = "请帮我推荐一些科幻类的电影"

filter_condition = {
    "$and": [
        {"genre": "科幻"},
        {"rating": {"$gt": 8.0}},
    ]
}

retriever = vectorstore.as_retriever(search_kwargs={"filter":filter_condition,"k": 3})

docs = retriever.invoke(question)

print(docs)