import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

responses = client.responses.create(
    model="gpt-5.2",
    input="长治市市委书记现任人",
    tools=[
        {"type":"web_search"}
    ]
)

print(f"{responses.output_text}")


