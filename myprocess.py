
import multiprocessing as mp
import time
import os



class MyProcess(mp.Process):

    def __init__(self,name:str):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            pid = os.getpid()
            name = mp.current_process().name
            print(f"进程名称{name}进程id{pid},执行任务{i}")
            time.sleep(0.2)


if __name__ == '__main__':
    p1 = MyProcess("**********进程a**********")
    p2 = MyProcess('进程b')

    # p1.run()
    # p2.run()


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("进程结束")