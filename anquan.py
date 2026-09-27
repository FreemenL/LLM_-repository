# 进程安全，互斥锁
import threading as td
import time

tickets = 10
lock = td.Lock()

def buy_ticket():
    global tickets
    while True :
        time.sleep(1)
        lock.acquire()
        if tickets == 0 :
            lock.release()
            break
        tickets -= 1
        print(f"{td.current_thread().name}抢到了第{10-tickets}张票，还剩{tickets}张票")
        lock.release()
    print("票卖完了")


if __name__ =='__main__':
    t1 = td.Thread(target=buy_ticket, name="张三",args=())
    t2 = td.Thread(target=buy_ticket, name="里斯",args=())
    t3 = td.Thread(target=buy_ticket, name="王五",args=())


    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()



print("程序结束")
