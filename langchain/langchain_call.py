from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

load_dotenv()

llm= init_chat_model(
    model_provider="openai",
    model="gpt-4o-mini",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
response= llm.invoke("你好")
print(response)