# langchain中的链式处理
# 搭建了一个Runnable 链，链条里面有几个组件，收尾相连
# 前者的输出是后者的一个输入
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt_template = PromptTemplate(
    template="讲一个关于{topic}的冷笑话",
    input_variables=["topic"]
)

llm = ChatOpenAI(model="gpt-5.5")

parser = StrOutputParser()

chain = prompt_template | llm | parser

response = chain.invoke({"topic":"人工智能"})

print(response)


# 这里的 | 是 LangChain LCEL 里的“管道符”，意思是把多个步骤串起来：
# prompt_template 的输出 -> 传给 llm -> llm 的输出 -> 传给 parser
# 等价于手动写：
#
# formatted_prompt = prompt_template.invoke({"topic": "人工智能"})
# ai_message = llm.invoke(formatted_prompt)
# response = parser.invoke(ai_message)
