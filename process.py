

import multiprocessing as mp
import os
import time


def task():
    for i in range(10):
        print(f"进程名称{mp.current_process().name},进程ID{os.getpid()}执行任务{i}")
        time.sleep(0.1)

if __name__ == '__main__':
    p1 = mp.Process(target=task ,name='进程a')
    p2 = mp.Process(target=task,name='进程b')

    p1.start()
    p2.start()

    p1.join() # 主进程等待当前进程执行完毕再继续执行
    p2.join() # 主进程等待当前进程执行完毕再继续执行

    print("程序结束")