from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


prompt_template = ChatPromptTemplate.from_messages([
     SystemMessagePromptTemplate.from_template("你是{product}的客服助手，你的名字叫{name}，请用简洁的20个字回答问题"),
     HumanMessagePromptTemplate.from_template("hello,你好，我的名字叫{human_name}"),
     AIMessagePromptTemplate.from_template("你好，有什么需要咨询的"),
     HumanMessagePromptTemplate.from_template("{query}")
])

prompt = prompt_template.invoke({
    "product":"langchain",
    "name":"夏江",
    "human_name":"张三",
    "query":"langchain是什么，用来做什么的？"
})

load_dotenv()

model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)
response = model.invoke(prompt)

print(response.content)





