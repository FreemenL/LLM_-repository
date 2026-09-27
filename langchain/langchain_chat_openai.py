from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

response=llm.invoke("介绍一下尚硅谷")

print(response.content)