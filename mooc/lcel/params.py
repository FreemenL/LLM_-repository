from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
).configurable_fields(
    temperature=ConfigurableField(
        id="llm_temperature" ,
        name="llm 温度",
        description="llm 温度",
    )
)

prompt = PromptTemplate.from_template("给一个大于 {x} 的随机数")

chain = prompt | model

print(chain.with_config(configurable={"llm_temperature": 1}).invoke({"x": 5}))