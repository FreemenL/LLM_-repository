from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="deepseek-v4", temperature=0.1)

gpt4_model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

branch = RunnableBranch(
    (lambda x: len(x) < 10, llm),
    gpt4_model
)

print(branch.invoke("你是谁？请用比较简单的回复语言进行回答"))