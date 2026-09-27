from langchain_core.runnables import RunnableLambda


result = RunnableLambda(lambda x:x+1) | RunnableLambda(lambda x: x*2)

print(result.invoke(2))
