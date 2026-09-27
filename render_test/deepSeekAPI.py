# Please install OpenAI SDK first: `pip3 install openai`

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  # 会自动读取当前目录下的 .env 文件

print(os.environ.get('DEEPSEEK_API_KEY_TEST'))
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY_TEST'),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一名温柔可爱的ai助理，名字叫小梅，请以温柔可爱的语气回答用户问题"},
        {"role": "user", "content": "你是谁"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "disabled"}}
)

print(response.choices[0].message.content)