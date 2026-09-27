from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,AIMessageChunk

load_dotenv()

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)

def parse(ai_message: AIMessage)-> str:
    """parser the AI message"""
    return ai_message.content.swapcase()

response = model.invoke("hello")

print(parse(response))


