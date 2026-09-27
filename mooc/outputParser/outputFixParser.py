# outputFixingParser

from typing import List,Optional
from dotenv import load_dotenv
from langchain_classic.output_parsers import OutputFixingParser
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser
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
    name: str = Field(description="电影名称")
    director: str = Field(description="导演姓名")
    year: int = Field(description="上映年份",ge=1900,le=2023)

parser = PydanticOutputParser(pydantic_object=Movie)

# bad_output = '{"name":"卧虎藏龙","director":"李安"}'
# bad_output = '{"name":"卧虎藏龙","fare":"89.89"}'
bad_output = '{"director":"冯小刚"}'


try:
    parser.parse(bad_output)
except OutputParserException as e:
    print('错误',e)

print("=======开始修复======")

fix_parser = OutputFixingParser.from_llm(parser=parser,llm=model)
# print(fix_parser.invoke(bad_output))
fixed_point =fix_parser.parse(bad_output)
print(fixed_point)
print(type(fixed_point))

