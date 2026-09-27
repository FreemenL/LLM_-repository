import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers.util import cos_sim

embedings_path = "/Users/xiajiang/Desktop/huggingface/bge-large-zh-v1.5"

embeddings = HuggingFaceEmbeddings(model_name=embedings_path)

text1 = "猫在垫子上"

text2 = "垫子上有一只猫"

text3 = "中国很伟大"


text1_vector = embeddings.embed_query(text1)
text2_vector = embeddings.embed_query(text2)
text3_vector = embeddings.embed_query(text3)

text1_vector_reshape = np.array(text1_vector).reshape(1, -1)
text2_vector_reshape = np.array(text2_vector).reshape(1, -1)
text3_vector_reshape = np.array(text3_vector).reshape(1, -1)

similarity = cosine_similarity(text1_vector_reshape, text2_vector_reshape)[0][0]

print(similarity)

s = cos_sim(text1_vector_reshape, text2_vector_reshape)
s1 = cos_sim(text1_vector_reshape, text3_vector_reshape)

print(s.item())
print(s1.item())