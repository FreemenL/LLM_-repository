# 动态参数
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
).configurable_alternatives(
    ConfigurableField(id="llm"),
    default_key="openai",
    deepseek_chat=ChatDeepSeek(model="deepseek-chat", api_key=os.environ.get("OPENAI_API_KEY"))
)

prompt = PromptTemplate.from_template("给我说一下关于{topic}的笑话").configurable_alternatives(
    ConfigurableField(id="prompt"),
    default_key="joke",
    shi = PromptTemplate.from_template("写一首诗关于：{topic}")
)

chain = prompt | model

print(chain.with_config(configurable={"prompt": "shi", "llm": "deepseek_chat"}).invoke({"topic": "蛇"}).content)