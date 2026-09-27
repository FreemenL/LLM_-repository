from langchain_core.runnables import Runnable
from typing import AsyncIterator, Iterator

class TextTranformer(Runnable):

    def __init__(self, prefix: str = "处理后的文本: "):
        self.prefix = prefix

    def invoke(self, input: str) -> str:
        # 自定义文本处理逻辑
        processed_text = input.upper()  # 转换为大写
        return f"{self.prefix}{processed_text}"

    async def ainvoke(self, input: str) -> str:
        # 异步处理实现
        return self.invoke(input)

    def stream(self, input: str) -> Iterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    async def astream(self, input: str) -> AsyncIterator[str]:
        processed_text = input.upper()
        for char in processed_text:
            yield f"{self.prefix}{char}"

    def batch(self, inputs: list[str]) -> list[str]:
        return [self.invoke(input) for input in inputs]

    async def abatch(self, inputs: list[str]) -> list[str]:
        return [await self.ainvoke(input) for input in inputs]

transformer = TextTranformer(prefix="结果：")
result = transformer.invoke("hello world")

print(result)

print('stream')


for chunk in transformer.stream("hello world"):
    print(chunk)

print("batch:")

results = transformer.batch(["hello", "world"])
print(results)

print("\n异步 调用:")

import asyncio


async def async_test():
    result = await transformer.ainvoke("hello world")
    print(f"ainvoke: {result}")

    async for chunk in transformer.astream("hello world"):
        print(chunk)  # 每次输出一个字符前缀化内容

    abatch_results = await transformer.abatch(["hello", "world"])
    print("\naBatch 结果:")
    print(abatch_results)


asyncio.run(async_test())