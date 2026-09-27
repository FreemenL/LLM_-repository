# 链的并行运行
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

load_dotenv()

english_prompt_template = PromptTemplate.from_template("把这句话翻译成英文:{topic}")

korean_prompt_template = PromptTemplate.from_template("把下面这句话翻译成韩文:{topic}")


llm = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

english_chain = english_prompt_template | llm | parser
korean_chain = korean_prompt_template | llm| parser


map_chain = RunnableParallel(
    english = english_chain,
    korean = korean_chain
) 

responses = map_chain.invoke({"topic":"我爱仓江科技"})

print(responses)



