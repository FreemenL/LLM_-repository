from multiprocessing import Pool
import time
import os



def task(task_name):
    print(f"进程池执行任务{task_name},进程id{os.getpid()}正在执行")
    time.sleep(0.1)
    print(f"进程池执行任务{task_name},进程id{os.getpid()}执行完毕")

if __name__ == '__main__':
    pool = Pool(3)

    for  i in range(10):
        pool.apply(func=task, args=(i,))
        # pool.apply_async(func=task, args=(i,))   

    pool.close()

    pool.join()

    print("程序结束")