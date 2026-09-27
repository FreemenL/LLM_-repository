import time
import multiprocessing

def add(queue):
    for i in range(10):
        queue.put(i)
        print(f"add 添加数据: {i}")
        time.sleep(1)

def show(queue):
    for i in range(10):
        val = queue.get()
        print(f"show 取出数据: {val}")
        time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue(1024)
    p1 = multiprocessing.Process(target=add, args=(queue,))
    p2 = multiprocessing.Process(target=show, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

