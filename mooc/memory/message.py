# 消息占位符 - 解决记忆的问题
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个乐于助人的助手，尽你所能回答所有问题。回答简洁，20个字"),
        MessagesPlaceholder(variable_name="message"),
        ("user","{question}")
    ]
)
chain = prompt_template|llm
response= chain.invoke(
    {
        "message":[
            HumanMessage(content="你好，我是夏江，将这句话从汉语翻译成英语：我喜欢编程"),
            AIMessage(content="I Love programming")
        ],
        "question":"你知道我是谁吗？"
    }
)

print(response)

