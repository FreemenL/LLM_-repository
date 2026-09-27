
import threading   as td
import time


def run():
    for i in range(10):
        print(f"线程名称{td.current_thread().name}打印数据{i}")
        time.sleep(0.1)


if __name__ == '__main__':
    t1 = td.Thread(target=run,name="线程a")
    t2 = td.Thread(target=run,name="线程b")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序结束")