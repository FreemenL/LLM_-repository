from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)
response = model.invoke("2🐦9是什么？")

print(response)