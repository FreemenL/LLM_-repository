from  langchain_huggingface import HuggingFaceEmbeddings

embeddings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"

embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

# vector = embeddings.embed_query("你好，中国")
#
# print(len(vector))

texts = [
    "你好，中国",
    "你好，美国",
    "你好，日本"
]

vectors = embeddings.embed_documents(texts)

for i, vector in enumerate(vectors):
    print(i, len(vector),vector)