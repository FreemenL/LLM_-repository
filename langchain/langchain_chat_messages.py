from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


load_dotenv()

llm = ChatOpenAI(model="gpt-5.5")

input_string = "评价一下山西仓江科技"


input_tuple =[
    ("system","你是一个美国人只会说英文"),
    ("user","你好，今天过的怎么养ovo")
]

input_dict = [
    {"role":"system","content":"你是一个韩国人，只会说韩语"},
    {"role":"user","content":"哈喽"}
]

input_message_object = [
    SystemMessage(content="你是一只小狗只会汪汪叫，被踹了会跑"),
    HumanMessage(content="(吹了个口哨)"),
    AIMessage(content="汪汪！"),
    HumanMessage(content="哪来的狗（踹了你一脚）")
]

message_object_response = llm.invoke(input_dict)
print(message_object_response.content)