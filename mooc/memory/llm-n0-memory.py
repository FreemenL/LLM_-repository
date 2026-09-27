from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

# response = llm.invoke("你是谁")
#
# print(response.content)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个乐于助人的助手，尽你所能回答所有问题。回答简洁，20个字"),
        ("user","{question}")
    ]
)

chain = prompt_template|llm
response= chain.invoke({"question":"你好我叫夏江，金庸是谁"})

print(response)

response= chain.invoke({"question":"你好，你知道我叫什么名字吗？"})

print(response)

