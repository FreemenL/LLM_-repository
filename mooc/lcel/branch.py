from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

chinese_prompt = ChatPromptTemplate.from_template("解释一下概念：{concept}")

english_prompt = ChatPromptTemplate.from_template("解释一下概念：: {concept},用英文回复，字符串长度不超过20个字")

branch = RunnableBranch(
    (lambda x: x["language"] == "zh", chinese_prompt),
    (lambda x: x["language"] == "en", english_prompt),
    lambda x: "没有语言，抱歉，我无法解释。"
)

chain = branch |  ChatOpenAI(model="deepseek-v4-pro",temperature=0)

print(chain.invoke({"concept": "机器学习", "language": "zh"}))