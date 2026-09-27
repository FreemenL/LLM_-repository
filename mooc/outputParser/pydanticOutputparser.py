# pydanticOutputParser

from typing import List,Optional
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticToolsParser, PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)

class Movie(BaseModel):
    title: str = Field(description="电影标题")
    director: str = Field(description="导演姓名")
    year: int = Field(description="上映年份",ge=1900,le=2023)
    genres: List[str]= Field(description="电影类型列表")
    rating: Optional[float] = Field(description="电影评分，0-10之间",ge=0,le=10)

template = """
    你是一个电影信息提取助手，请从以下文本中提取电影信息，并以JSON的样式返回。
    文本：{text}
    {format_instructions}
"""

parser = PydanticOutputParser(pydantic_object=Movie)

prompt_template = PromptTemplate(
    template=template,
    input_variables=["text"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

movie_text = """
    《泰坦尼克号》是一部由詹姆斯*卡梅隆执导的史诗级浪漫灾难电影，
    这部电影于1997年上映，讲述了穷画家杰克和贵族女子露丝之间的爱情故事，
    它被归类为爱情、灾难和剧情片，获得了评论界和观众的广泛好评，IMDB评分为8.8分。
"""

formatted_prompt = prompt_template.format_prompt(text=movie_text)

res = model.invoke(formatted_prompt)
# print(res)

response = parser.invoke(res)
print(response)