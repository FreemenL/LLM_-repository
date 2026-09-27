# 多线程运行多任务带参数

import threading
import time

def music(num):
    for i in range(num):
        print(f"music{i}")
        time.sleep(0.2)

def coding(num,s_time):
    for i in range(num):
        print(f"coding{i}")
        time.sleep(s_time)

if __name__ == '__main__':
    print(f"进入main函数的线程名称{threading.current_thread().name}")
    # threading.Thread(target=music,name="music",args=(10,)).start()
    # threading.Thread(target=coding,name="coding",args=(5,0.2)).start()





