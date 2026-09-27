from langchain_core.messages import AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt_template = ChatPromptTemplate([
    ("system","你是一个乐于助人的助手，在回答用户问题时，需要带上用的名字"),
    ("user","我是{name}"),
    MessagesPlaceholder("msgs"),
])

s = prompt_template.invoke({
    "msgs":[
        AIMessage(content="你好有什么需要咨询的？"),
        HumanMessage(content="三国志的作者是谁？")
    ],
    "name":"张三"
})


model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)
response = model.invoke(s)

print(response.content)


