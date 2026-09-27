from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

response = llm.invoke("你是谁")

print(response.content)