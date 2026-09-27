# RetryWithErrorOutputParser
from typing import List,Dict
from dotenv import load_dotenv
from langchain_classic.output_parsers import OutputFixingParser, RetryWithErrorOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, field_validator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)

class MovieRecommendation(BaseModel):
   movies: List[Dict] = Field(description="推荐的电影列表")

   @field_validator("movies")
   def check_movies(cls,field):
       required_fields = ["title","year","genre","rating","description"]
       for movie in field:
           for field_name in required_fields:
               if field_name not in movie:
                   raise ValueError(f"电影记录缺少必要的字段:{field_name}")

       return field

parser = PydanticOutputParser(pydantic_object=MovieRecommendation)

fixing_parser = OutputFixingParser.from_llm(
    parser=parser,
    llm=model
)

retry_parser = RetryWithErrorOutputParser.from_llm(
    parser=parser,
    llm=model,
    max_retries=1
)

template = """
    推荐2部{genre}类型的电影，格式如下:
    {{
        "movies":[
            {{
                "title":"电影名称",
                "year":"发型年份",
                "genre":"电影类型",
                "rating":"评分",
                "description":"简短描述"
            }},
             {{
                "title":"电影名称2",
                "year":"发型年份2",
                "genre":"电影类型2",
                "rating":"评分2",
                "description":"简短描述2"
            }}
        ]
    }}
    
请确保每个电影对象包含所有必要字段: title,year,genre,rating,description

{format_instructions}
"""

prompt_template = PromptTemplate(
    template=template,
    input_variables=["genre"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

prompt_value = prompt_template.format_prompt(genre="科幻")

# print(prompt_value)

model_output = """
    [{
     "title":"星际穿越",
     "year":"2014",
     "rating":"8.6",
     "description":"一部关于时空旅行和黑洞的科幻电影",
    },{
     "title":"盗梦空间",
     "year":"2010",
     "rating":"8.8",
     "description":"一部关于梦境和潜意识的电影",
    }]
"""

# try:
#     print("===使用OutputFixingParser")
#     fixed_output = fixing_parser.parse(model_output)
#     print("成功修复输出",fixed_output)
#     for movie in fixed_output["movies"]:
#         print(f"{movie['title']}")
# except Exception as e:
#     print(f"OutputFixingParser 修复失败{e}")

try:
    print("===使用RetryWithErrorOutputParser")
    retry_output = retry_parser.parse_with_prompt(model_output,prompt_value)
    print("成功修复输出",retry_output)
    for movie in retry_output.movies:
        print(f"电影:{movie['title']}")
except Exception as e:
    print(f"RetryWithErrorOutputParser 修复失败{e}")