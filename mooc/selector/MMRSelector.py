# MMR 最大边际相关性样例选择器
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
# from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI


load_dotenv()

examples = [
    {"id":"1","features":','.join(["时尚","运动鞋","跑步"])},
    {"id": "2", "features": ','.join(["休闲", "运动鞋", "篮球"])},
    {"id": "3", "features": ','.join(["商务", "皮鞋", "正装"])},
    {"id": "4", "features": ','.join(["户外", "徒步鞋", "探险"])},
    {"id": "5", "features": ','.join(["时尚", "板鞋", "滑板"])},
    {"id": "6", "features": ','.join(["咖啡厅", "商务餐", "包厢"])},
]
example_prompt = PromptTemplate(
    input_variables=["id","features"],
    template="id={id}\n描述:{features}"
)

embeddings_path = os.environ.get('BAAI/bge-large-zh-v1.5', 'BAAI/bge-large-zh-v1.5')

embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embeddings,
    FAISS,
    k=3
)

dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="查询和描述相似度最高的id，不需要输出其他信息。只需要输出id",
    suffix="关键词为:{word}",
    input_variables=["word"],
)

prompt  = dynamic_prompt.format(word="咖啡")
print(prompt)
llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

response = llm.invoke(prompt)
print(response)