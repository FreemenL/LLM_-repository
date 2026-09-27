from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system","你是一个乐于助人的助手"),
    ("user","给我们讲一个关于{topic}的笑话")
])

prompt = prompt_template.invoke({"topic":"猫"})

print(prompt.to_string())
print(prompt.to_messages())
print(prompt.to_json())