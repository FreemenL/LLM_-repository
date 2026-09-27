from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)

print(model.invoke("三国志的作者是谁").content)







