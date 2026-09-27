import threading
# 创建一个互斥锁
my_lock = threading.Lock()
import time
g_list = 0
def write_data():
    my_lock.acquire() # 获得锁并将锁至于关闭状态
    global g_list
    for item in range(10000000):
        g_list+=1
    print(f"write_data 结束{g_list}")
    my_lock.release() # 释放锁


def write_data2():
    my_lock.acquire()  # 获得锁并将锁至于关闭状态
    global g_list
    for item in range(10000000):
        g_list += 1
    print(f"write_data2 结束{g_list}")
    my_lock.release()  # 释放锁

if __name__ == '__main__':
    threading.Thread(target=write_data).start()
    threading.Thread(target=write_data2).start()

    # time.sleep(5)
    print(f"main{g_list}")