import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key='sk-ws-H.PLDDLHR.wrVF.MEQCIBfaZWKUymGwfVneKKWW4DwCCCNHxantSoyehzkXSFjYAiAvSLAKX21-U-P8rIKwZngTcd8GHYXB-OXQLPn_jQhuKw',
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model= "qwen3.8-max",
    messages=[
        {"role": "system", "content": "你是一个法律专家，可以回答用户的法律咨询问题"},
        {"role": "user", "content": "你是谁？"},
        {"role":"assistant","content":"我是法律专家，请问有什么可以帮你的？"},
        {"role": "user", "content": "我同学欠我100元1年没还怎么办？"},
    ]
)

print(completion.choices[0].message.content)