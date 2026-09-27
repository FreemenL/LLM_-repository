import asyncio
import os

from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个助手,用20个字以内回答",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ]
)

chain = prompt | model


def get_session_history(session_id: str):
    return SQLChatMessageHistory(session_id=session_id, connection="sqlite:///history.db")


chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

config = {"configurable": {"session_id": "a2"}}

# r1 = chain_with_history.invoke(
#     {"input": "我是张三,请问中国有多大？"},
#     config=config
# )


r2 = chain_with_history.invoke(
    {"input": "你知道我的 名字叫什么吗？"},
    config=config
)

print(r2)