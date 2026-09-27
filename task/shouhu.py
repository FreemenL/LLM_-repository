# 用进 p1.terminate()的方式结束子进程
import multiprocessing
import time



def chatQQ():
    for i in range(10):
        print("1聊天中")
        time.sleep(1)

def chatQQ2():
    for i in range(10):
        print("2聊天中")
        time.sleep(1)



if __name__ == '__main__':
    print('主进程启动')

    # p1 = multiprocessing.Process(target=chatQQ, name="chatQQ",daemon=True)
    # p2 = multiprocessing.Process(target=chatQQ2, name="chatQQ2",daemon=True)

    p1 = multiprocessing.Process(target=chatQQ, name="chatQQ")
    p2 = multiprocessing.Process(target=chatQQ2, name="chatQQ2")

    p1.start()
    p2.start()



    p1.terminate()
    #
    # p1.join()
    # p2.join()
    #
    # time.sleep(3)
    print('主进程结束')