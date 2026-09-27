import threading as td
from concurrent.futures import ThreadPoolExecutor
import time



def task():
    print(f"线程名称:{td.current_thread().name}开始执行任务")
    time.sleep(1)
    print(f"线程名称:{td.current_thread().name}任务执行完毕")

if __name__ == '__main__':
     with ThreadPoolExecutor(max_workers=2) as pool:
        for i in range(10):
            pool.submit(task)


print("程序执行结束")
