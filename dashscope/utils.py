
from openai import OpenAI
def chat_with_LLM(message:list):
    client = OpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key='sk-ws-H.PLDDLHR.wrVF.MEQCIBfaZWKUymGwfVneKKWW4DwCCCNHxantSoyehzkXSFjYAiAvSLAKX21-U-P8rIKwZngTcd8GHYXB-OXQLPn_jQhuKw',
    )
    response = client.chat.completions.create(
        model='qwen-max',
        messages=message
    )
    return response.choices[0].message.content