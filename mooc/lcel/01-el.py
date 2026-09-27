import asyncio

from langchain_core.runnables import RunnableLambda


def add_one(x:int)->int:
    return x + 1

async def add_one_async(x:int)->int:
    return x + 2

runnable_add_one = RunnableLambda(func=add_one,afunc=add_one_async)

print(runnable_add_one.invoke(1))
print(runnable_add_one.batch([1,2,3]))

async def main():
    print(await runnable_add_one.ainvoke(4))

asyncio.run(main())


