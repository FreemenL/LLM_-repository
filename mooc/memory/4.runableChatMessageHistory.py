# RunnableWithMessageHistory  实现llm 的 memory
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableWithMessageHistory
load_dotenv()

llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个助手，擅长能力{ability},用20个字以内回答，如果不知道的话，请回答不知道",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{input}")
    ]
)

chain = prompt_template | llm

store= {}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chat_with_history  = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

r1 = chat_with_history.invoke(
    {"ability":"数学","input":"请问什么是勾股定理？"},
    config={"configurable":{"session_id":"a1"}}
)

print(r1)

r1 = chat_with_history.invoke(
    {"ability":"数学","input":"我刚才的问题是什么？"},
    config={"configurable":{"session_id":"a1"}}
)

print(r1)


r1 = chat_with_history.invoke(
    {"ability":"数学","input":"我刚才的问题是什么？"},
    config={"configurable":{"session_id":"b2"}}
)

print(r1)