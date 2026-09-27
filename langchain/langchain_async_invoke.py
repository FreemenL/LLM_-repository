import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

async def async_invoke():
        llm = ChatOpenAI(model="gpt-4o-mini")
        responses = await llm.ainvoke("你好")
        print(responses.content)


if __name__ == '__main__':
    asyncio.run(async_invoke())