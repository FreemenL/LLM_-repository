from threading import Thread
import time




class MyThread(Thread):
    def __init__(self,name:str):
        super().__init__()
        self.name=name

    def run(self):
        for i in range(10):
            print(f"线程名称{self.name},打印数据{i}")
            time.sleep(1)


if __name__ == '__main__':
    t1 = MyThread("线程a")
    t2 = MyThread("线程b")


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序结束")