# 部分提示词模版
from langchain_core.prompts import PromptTemplate
from datetime import datetime

def get_datetime():
    now = datetime.now()
    return now.strftime("%Y/%m/%d")

prompt_template = PromptTemplate(
    template="给我讲一个发生在{date}的有关{who}的新闻",
    input_variables=["who","date"],
)

partial_prompt_template1 = prompt_template.partial(date=get_datetime)

partial_prompt_template2 = prompt_template.partial(date="2021/02/11")

print(partial_prompt_template1.format(who="张三"))
print(partial_prompt_template2.format(who="张三"))
