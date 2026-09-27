# 多线程运行多任务
import threading
import time

def music():
    print(f"进入music函数的线程名称{threading.current_thread().name}")
    for i in range(10):
        print(f"music{i}")
        time.sleep(0.2)

def coding():
    print(f"进入coding函数的线程名称{threading.current_thread().name}")
    for i in range(10):
        print(f"coding{i}")
        time.sleep(0.2)

if __name__ == '__main__':

    print(f"进入main函数的线程名称{threading.current_thread().name}")

    threading.Thread(target=music,name="music").start()
    threading.Thread(target=coding,name="coding").start()




