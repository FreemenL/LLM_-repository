from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="glm-5.2",temperature=0)

message = [
    SystemMessage(content="你是知识渊博的专家，知道很多著名书籍相关知识，请简洁的用20个字回答问题"),
    HumanMessage(content="我的身份是学员名字叫小顾"),
    AIMessage(content="欢迎，有什么需要咨询的"),
    HumanMessage(content="三国志的作者是谁?"),
    AIMessage(content="《三国志》的作者是个三国时期的历史学家陈寿"),
    HumanMessage(content="红楼梦呢？")
]

response = model.invoke(message)
print(response.content)

