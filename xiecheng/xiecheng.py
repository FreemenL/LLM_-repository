# 协程
import asyncio

async def hello(name):
    print(f'hello {name} 开始')
    await asyncio.sleep(0.5)
    print(f'hello {name} 结束')



async def main():
    t1  = asyncio.create_task(hello("zhangsan"))
    t2 = asyncio.create_task(hello("lisi"))
    await t1
    await t2

if __name__ == '__main__':
    asyncio.run(main())