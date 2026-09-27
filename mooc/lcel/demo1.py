from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


from load_dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

prompt_template = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")

prompt = prompt_template.invoke({"topic":"猫"})

response = llm.invoke(prompt)

print("response",response.content)
