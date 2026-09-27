import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

responses = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [
        {"role":"user","content":"你好，介绍一下山西仓江科技"}
    ]
)

print(f"{responses.choices[0].message.content}")


