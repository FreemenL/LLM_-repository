# 输出格式化-字符串
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)

prompt = "请用一句话解释量子力学"

response = model.invoke(prompt)


parser_response = parser.invoke(response)

print(parser_response)