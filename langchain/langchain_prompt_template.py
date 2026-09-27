# 提示词模版
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

chat_prompt_template = ChatPromptTemplate.from_messages(
    messages=[
        ("system","你是一个专业的评论员，善于适应使用刻薄刁钻且有深度的分析去处理问题"),
        ("user","评价一下{product}的优缺点，包含连个方面{aspect1}和{aspect2}")
    ]
)

prompt = chat_prompt_template.invoke(
    {"product":"iphone手机","aspect1":"价格","aspect2":"外观"}
)

print(prompt)
print("=======================")

llm = ChatOpenAI(model="gpt-5.5")
response = llm.invoke(prompt)
print(response.content)