from multiprocessing import Process, Manager
import os

from process import task

def func(build_list):
    for i in range(10):
        build_list.append(i)
        print(f'{os.getpid()}添加数据{i}',build_list)


if __name__ == '__main__':
    manager = Manager()
    list = manager.list()
    p1 = Process(target=func, args=(list,))
    p2 = Process(target=func, args=(list,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    manager.shutdown()
    print("程序执行完毕")