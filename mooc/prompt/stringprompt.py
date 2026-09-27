from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
prompt_template = PromptTemplate.from_template("给我讲一个关于{topic}的笑话。")
prompt = prompt_template.invoke({"topic":"python"})

model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)
response = model.invoke(prompt)

print(response.content)


