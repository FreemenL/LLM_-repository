# 线程间共享资源
import threading

my_list = []

def write_date():
    print(f"开始写入{my_list}")
    for i in range(5):
        my_list.append(i)
    print(f"写入完毕{my_list}")


def read_date():
    print(f"读取数据{my_list}")


if __name__ == '__main__':

    threading.Thread(target=write_date).start()
    threading.Thread(target=read_date).start()

    print(f"主线程数据-{my_list}")