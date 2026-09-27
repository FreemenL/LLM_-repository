from langchain_core.runnables import RunnableLambda
import random
import time
from datetime import datetime


def add_one(x: int) -> int:
    return x + 1


def double(x: int) -> int:
    start_time = time.time()
    format_time = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
    print(f"开始执行时间：{format_time}")

    r = random.random()

    print(f"随机数：{r}")

    if r > 10:
        print("此代码有异常")
        raise ValueError(f"触发了异常，随机数为{r}")

    return x * 2

pipline = (RunnableLambda(add_one) |
            RunnableLambda(double).with_retry(
                stop_after_attempt=5,
                retry_if_exception_type=(ValueError,),
            )
)

try:
    print(pipline.invoke(2))
except Exception as e:
    print(e)