from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from openai.resources import responses

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com/v1",
    api_key=os.environ.get("OPENAI_API_KEY"),
    temperature=0,
)

response = llm.invoke("你是谁")

print(response.content)
