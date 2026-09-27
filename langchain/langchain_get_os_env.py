# 从env读取url和apikey
from dotenv import load_dotenv
import os

load_dotenv()
baseURL = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")


print(baseURL)
print(api_key)
