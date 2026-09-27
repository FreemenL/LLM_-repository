from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
#加载环境变量
load_dotenv()
#注册一个大模型对象
llm = ChatOpenAI(model="gpt-4o-mini")
#规定输出的数据类型
class Prime(BaseModel):
    prime:list[int]=Field(description="素数")
    count:list[int]=Field(description="小于该素数的数")

json_parser=JsonOutputParser(pydantic_object=Prime)

system_prompt = json_parser.get_format_instructions()
#通过大模型进行调用
response= llm.invoke([
    ("system",system_prompt),
    ("user","任意生成5个1000-100000之间素数,并标出小于该素数的索数个数")
])

output_text=response.content
print(type(output_text))
print(output_text)

print('================')

json_output=json_parser.invoke(response)

print(type(json_output))
print(json_output)