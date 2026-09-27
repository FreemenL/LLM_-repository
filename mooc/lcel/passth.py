from langchain_core.runnables import RunnablePassthrough, RunnableLambda


passthrough = RunnablePassthrough()

def add_extra(input_text):
    return {"name": input_text["name"], "geeting": input_text["geeting"], "extra": "附加信息"}

add_extra_runnable = RunnableLambda(func=add_extra)

# chain = passthrough | add_extra_runnable

# print(chain.invoke({"name": "张三","age": 18}))

print("===" * 20)

runnable_1 = passthrough.assign(geeting=lambda x: f"hello,{x['name']}!")

chain1 = runnable_1 | add_extra_runnable
print(chain1.invoke({"name": "张三","age": 18}))