import time
import multiprocessing
import os
def chatQQ(name):
    print(multiprocessing.parent_process().name)
    for i in range(10):
        print(f"和{name}聊qq")
        time.sleep(0.1)

def chatWX(name):
    print(multiprocessing.parent_process().name)
    for i in range(10):
        print(f"和{name}聊WX")
        time.sleep(0.2)


def chatSoul(name):
    print(multiprocessing.parent_process().name)
    for i in range(10):
        print(f"和{name}聊WX")
        time.sleep(0.3)



# chatQQ()
# chatWX()
# chatSoul()

if __name__ == '__main__':
    print(multiprocessing.current_process().name,os.getpid())
    multiprocessing.Process(target=chatQQ, name="chatQQ",args=("夏江",)).start()
    multiprocessing.Process(target=chatWX, name="chatWX",args=("芳菲",)).start()
    multiprocessing.Process(target=chatSoul, name="chatSoul",args=("大菲",)).start()

