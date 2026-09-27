# 输出格式化-json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)

template = """
    你是一个助手，需要返回用户信息的JSON格式数据
    {format_instructions}
    
    请返回一个包含以下字段的JSON对象
    - name: 用户的姓名
    - age: 用户的年龄
    - hobbies:  用户的爱好列表
    - favorite_colors: 用户最喜欢的颜色
    
    用户信息: {text}
"""

parser = JsonOutputParser()

prompt_template = PromptTemplate(
    template=template,
    input_variables=["text","format_instructions"]
)

prompt = prompt_template.format_prompt(text="用户叫张三，今年25岁，喜欢阅读、游泳和编程，最喜欢的颜色是蓝色",format_instructions="")

res = model.invoke(prompt)

response = parser.invoke(res)
print(type(response))
print(response)